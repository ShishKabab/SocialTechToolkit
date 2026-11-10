export const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
const words = value => normalize(value).split(' ').filter(Boolean);
// Optimal string alignment distance includes adjacent transpositions.
export function distance(a, b) {
  const d = Array.from({length: a.length + 1}, () => Array(b.length + 1).fill(0));
  for(let i=0;i<=a.length;i++) d[i][0]=i;
  for(let j=0;j<=b.length;j++) d[0][j]=j;
  for(let i=1;i<=a.length;i++) for(let j=1;j<=b.length;j++) {
    d[i][j]=Math.min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+(a[i-1]===b[j-1]?0:1));
    if(i>1&&j>1&&a[i-1]===b[j-2]&&a[i-2]===b[j-1]) d[i][j]=Math.min(d[i][j],d[i-2][j-2]+1);
  }
  return d[a.length][b.length];
}
function matchesTokens(query, field, fuzzy=false) {
  const tokens = words(field);
  return query.every(q => tokens.some(t => {
    if(t===q || t.startsWith(q)) return true;
    const limit=q.length<=3?0:q.length<=7?1:2;
    return fuzzy && limit>0 && Math.abs(t.length-q.length)<=limit && distance(q,t)<=limit;
  }));
}
export function validateIndex(data) {
  if(!Array.isArray(data) || !data.length) throw new Error('Empty search index');
  const ids=new Set();
  for(const e of data) {
    if(!e || typeof e.id!=='string' || ids.has(e.id) || typeof e.title!=='string' || !e.title || typeof e.url!=='string' || !e.url.startsWith('/') || e.url.startsWith('//') || typeof e.kind!=='string' || typeof e.category!=='string' || !Array.isArray(e.aliases) || !Array.isArray(e.terms) || ![...e.aliases,...e.terms].every(x=>typeof x==='string')) throw new Error('Invalid search record');
    ids.add(e.id);
  }
  return data;
}
export function search(index, value) {
  const q=normalize(value), tokens=words(q);
  if(!q) return [];
  return index.flatMap(e=>{
    let rank=Infinity, explanation='';
    if(normalize(e.title)===q) rank=0;
    else if(e.aliases.some(a=>normalize(a)===q)) {rank=1;explanation='Also known as '+e.aliases.find(a=>normalize(a)===q);}
    else if(matchesTokens(tokens,e.title)) rank=2;
    else if(e.aliases.some(a=>matchesTokens(tokens,a))) {rank=3;explanation='Also known as '+e.aliases.find(a=>matchesTokens(tokens,a));}
    else if(e.terms.some(t=>matchesTokens(tokens,t))) {rank=4;explanation='Related to '+e.terms.find(t=>matchesTokens(tokens,t));}
    else if(matchesTokens(tokens,e.title,true)) rank=5;
    else if(e.aliases.some(a=>matchesTokens(tokens,a,true))) rank=6;
    return Number.isFinite(rank)?[{...e,rank,explanation}]:[];
  }).sort((a,b)=>a.rank-b.rank||a.title.localeCompare(b.title));
}
