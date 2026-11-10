"""One-time import of the editorial outline; run explicitly to refresh records."""
from pathlib import Path
import re,json,unicodedata
ROOT=Path(__file__).resolve().parents[1]
s=(ROOT/'content/site-outline.md').read_text()
def slug(t):
 t=unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode().lower()
 return re.sub('[^a-z0-9]+','-',t).strip('-')
entries=[];category='';section=0
for line in s.splitlines():
 if line.startswith('## '):
  m=re.match(r'## (\d+)\.',line);section=int(m[1]) if m else 0
 if section==6 and line.startswith('### '): category=line[4:]
 if not re.match(r'\| [TSD]\d{3} \|',line):continue
 cells=[x.strip() for x in line.split('|')[1:-1]]
 id,title=cells[:2]
 if id.startswith('D'):kind='D';desc,example,evidence=cells[2:];cat='Social dynamics'
 else:kind,desc,example,evidence=cells[2:];cat='Systems and institutions' if id.startswith('S') else category
 codes=re.findall(r'\[([^]]+)\]\(#source-',evidence)
 entries.append(dict(id=id,title=title,slug=slug(title),kind=kind,category=cat,description=desc,example=example,sources=codes,published=bool(codes),adaptation='Adaptation:' in evidence,aliases=[],terms=[]))
# Preserve the deeper page outlines already authored in the base document.
seed={}
for title,body in re.findall(r'### ([^\n]+?) — `/technologies/[^`]+`\n(.*?)(?=\n### |\n## |\Z)',s,re.S):
 fields=dict(re.findall(r'- \*\*([^*]+):\*\* (.*)',body))
 seed[title.lower()]=fields
for e in entries:
 if e['title'].lower() in seed:e['outline']=seed[e['title'].lower()]
sources={}
for code,body in re.findall(r'<a id="source-([^"]+)"></a>\n(.*?)(?=\n<a id=|\n### |\n## |\Z)',s,re.S):
 sources[code.upper()]={'text':body.strip(),'links':[{'title':a,'url':b} for a,b in re.findall(r'\[([^]]+)\]\((https?://[^)]+)\)',body)]}
assert len(entries)==412 and len({e['slug'] for e in entries})==412
(ROOT/'content/catalog.json').write_text(json.dumps(entries,indent=2,ensure_ascii=False)+'\n')
(ROOT/'content/sources.json').write_text(json.dumps(sources,indent=2,ensure_ascii=False)+'\n')
print(f'Imported {len(entries)} entries, {sum(e["published"] for e in entries)} with source trails; {len(sources)} sources.')
# Keep the later research, aliases, scenarios, and scale placements on reimport.
if (ROOT/'research/remaining-entries.json').exists():
 import runpy
 runpy.run_path(str(ROOT/'scripts/apply_research.py'),run_name='__main__')
