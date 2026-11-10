import {search, validateIndex} from './search-core.js';
const input=document.querySelector('#search');
const status=document.querySelector('#search-status');
const retry=document.querySelector('#retry-search');
const clear=document.querySelector('#clear-search');
const browse=document.querySelector('#browse');
const results=document.querySelector('#search-results');
const grid=document.querySelector('#result-grid');
const count=document.querySelector('#result-count');
const empty=document.querySelector('#empty-results');
const originals=new Map([...document.querySelectorAll('[data-entry]')].map(e=>[e.dataset.entry,e]));
let index=null, loading=false;
async function initialize() {
  if(loading || index) return;
  loading=true; input.disabled=true; retry.hidden=true;
  status.textContent='Loading search…';
  const controller=new AbortController();
  const timeout=setTimeout(()=>controller.abort(),15000);
  try {
    const response=await fetch('/search-index.json',{signal:controller.signal});
    if(!response.ok) throw new Error('Index request failed');
    const candidate=validateIndex(await response.json());
    if(candidate.some(e=>!originals.has(e.id))) throw new Error('Index does not match page');
    index=candidate; input.disabled=false; status.textContent='Search ready. Try a title, an acronym, or another name.';
  } catch {
    status.textContent='Search is unavailable. You can still browse the categories.';
    retry.hidden=false;
  } finally {clearTimeout(timeout);loading=false;}
}
function update() {
  const query=input.value.trim();
  clear.hidden=!input.value;
  if(!query) {browse.hidden=false;results.hidden=true;grid.replaceChildren();return;}
  const matches=search(index,query);
  browse.hidden=true;results.hidden=false;
  count.textContent=`${matches.length} ${matches.length===1?'result':'results'} for “${query}”`;
  empty.hidden=matches.length>0;
  const fragment=document.createDocumentFragment();
  for(const match of matches) {
    const card=originals.get(match.id).cloneNode(true);
    card.removeAttribute('data-entry');
    if(match.explanation) {const p=document.createElement('p');p.className='match-note';p.textContent=match.explanation;card.append(p);}
    fragment.append(card);
  }
  grid.replaceChildren(fragment);
}
input.addEventListener('input',update);
input.addEventListener('keydown',e=>{if(e.key==='Escape'){input.value='';update();}});
clear.addEventListener('click',()=>{input.value='';update();input.focus();});
retry.addEventListener('click',initialize);
document.querySelectorAll('[data-browse-link]').forEach(a=>a.addEventListener('click',()=>{if(index){input.value='';update();}}));
if(document.readyState==='complete') initialize();
else window.addEventListener('load',initialize,{once:true});
