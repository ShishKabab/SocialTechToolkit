from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set();self.dupes=[];self.search_disabled=False;self.titles=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:
   if a['id'] in self.ids:self.dupes.append(a['id'])
   self.ids.add(a['id'])
  for key in ('href','src'):
   if key in a:self.links.append(a[key])
  if tag=='input' and a.get('id')=='search':self.search_disabled='disabled' in a
  if tag=='title':self.titles+=1
pages={}
for f in D.rglob('*.html'):
 p=Page();p.feed(f.read_text());assert not p.dupes,(f,p.dupes);assert p.titles>=1,f;pages[f.resolve()]=p
for f,p in pages.items():
 for href in p.links:
  u=urlsplit(href)
  if u.scheme or u.netloc:continue
  path=unquote(u.path)
  target=(D/path.lstrip('/')) if path.startswith('/') else (f.parent/path) if path else f
  if target.is_dir():target=target/'index.html'
  assert target.exists(),(f,href)
  if u.fragment and target.suffix=='.html':assert unquote(u.fragment) in pages[target.resolve()].ids,(f,href,'missing anchor')
index=json.loads((D/'search-index.json').read_text());assert len(index)==len({x['id'] for x in index})
catalog=json.loads((ROOT/'content/catalog.json').read_text())
from editorial_drafts import load_drafts,NOTICE
drafts=load_drafts(catalog,complete=True)
from concept_links import load_relations,validate_article,ArticleLinks,entry_url
published=[e for e in catalog if e['published']]
relations=load_relations(published)
by_url={entry_url(e):e for e in published}
concept_links=0
for entry in index:
 html=(D/entry['url'].strip('/')/'index.html').read_text()
 expected=1 if entry['id'] in drafts else 0
 assert html.count('data-editorial-status="needs-guidance"')==expected,(entry['id'],'draft notice')
 if expected:assert NOTICE in html,entry['id']
 assert '/sources/' not in html,(entry['id'],'obsolete sources directory')
 body=html.split('<article class="article-body">',1)[1].split('<section id="related">',1)[0]
 concept_links+=len(validate_article(entry,body,relations,by_url))
 related_html=html.split('<section id="related">',1)[1].split('</section>',1)[0]
 related=ArticleLinks();related.feed(related_html)
 assert {by_url[u]['id'] for u in related.links}=={r['id'] for r in relations[entry['id']]},(entry['id'],'Rendered related links differ from editorial choices')
home=(D/'index.html').read_text()
assert 'class="development-notice"' in home and 'developed with AI' in home
assert {x['id'] for x in index}=={e['id'] for e in catalog if e['published']}
research_file=ROOT/'research/remaining-entries.json'
if research_file.exists():
 research=json.loads(research_file.read_text())
 baseline=json.loads((ROOT/'research/baseline.json').read_text())
 assert len(research)==len({r['id'] for r in research})==len(baseline)
 assert {r['id'] for r in research}=={e['id'] for e in baseline}
 assert {r['id'] for r in research}<={x['id'] for x in index}
 for e in catalog:
  if e['id'] in {r['id'] for r in research}:
   assert e.get('research',{}).get('finding') and e['research'].get('limitation') and e['research'].get('scenario'),e['id']
assert pages[(D/'index.html').resolve()].search_disabled
for e in index:assert (D/e['url'].strip('/')/'index.html').exists(),e['url']
from cases import load_cases
cases=load_cases(catalog)
assert not (D/'case-catalog.json').exists(),'Internal research export published'
assert not (D/'cases/backlog').exists(),'Internal research backlog published'
for c in cases:
 case_html=(D/'cases'/c['id']/'index.html').read_text()
 assert case_html.count('data-editorial-status="needs-guidance"')==1,c['id']
 assert NOTICE in case_html,c['id']
 assert 'Reading alongside Great Founder Theory' not in case_html,c['id']
 assert 'No dedicated theory connection assessed' not in case_html,c['id']
# Check public assets as well as HTML: a clean page must not link to a raw dump.
for f in D.rglob('*'):
 if f.is_file() and f.suffix in {'.html','.json','.js','.xml','.txt'}:
  content=f.read_text()
  for marker in ('editorial_research_notes','gft_reference','prior_research_gaps','source_ids','research_note','Download the research data'):
   assert marker not in content,(f,'Internal research field published',marker)
urls=ET.parse(D/'sitemap.xml').getroot();assert len(urls)==len(index)+len(cases)+4
assert len(pages)==len(index)+len(cases)+5
print(f'PASS: {len(pages)} HTML pages; {len(drafts)+len(cases)} draft notices; local links and fragments, unique IDs, index destinations, sitemap coverage, homepage notice, and initially disabled search checked.')
print(f'PASS: {len(relations)} curated relationship lists; {concept_links} distinct inline concept connections; all are represented in Explore alongside.')
