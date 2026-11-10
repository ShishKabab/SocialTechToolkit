"""Load separately maintained, explicitly provisional editorial drafts."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json,re
ROOT=Path(__file__).resolve().parents[1]
DRAFTS=ROOT/'research/editorial'
NOTICE='AI-assisted draft — this page needs further editorial guidance.'
class Fragment(HTMLParser):
 def __init__(self):super().__init__();self.text=[];self.links=[]
 def handle_starttag(self,tag,attrs):
  assert tag in {'p','a','strong','em','ul','ol','li','table','thead','tbody','tr','th','td','br','blockquote','small','code'},tag
  for k,v in attrs:
   assert k in {'href','title','scope'},(tag,k)
   if k=='href':
    assert v.startswith(('/', '#','https://','http://')),v
    assert not v.startswith('//'),v
    self.links.append(v)
 def handle_data(self,data):self.text.append(data)
def load_drafts(records,complete=False):
 manifest=json.loads((DRAFTS/'manifest.json').read_text())
 expected=set(manifest['expected_ids']);lookup={e['id']:e for e in records};result={}
 for batch in manifest['batches']:
  p=DRAFTS/(batch+'.json')
  if not p.exists():continue
  for d in json.loads(p.read_text()):
   assert d['id'] in expected and d['id'] not in result,d['id']
   assert d['title']==lookup[d['id']]['title'],d['id']
   assert d['description'] and d['opening_html'] and d['sources'],d['id']
   ids=[x['id'] for x in d['sections']]
   assert len(ids)==len(set(ids)) and not set(ids)&{'related','real-cases','sources'},d['id']
   for sid in ids:assert re.fullmatch('[a-z][a-z0-9-]*',sid),(d['id'],sid)
   for x in d['sections']:
    assert x['title'] not in {'How it works','In practice','Conditions & tradeoffs','When to use it'},d['id']
   f=Fragment();f.feed(d['opening_html']+''.join(x['html'] for x in d['sections']))
   assert len(' '.join(f.text).split())>=140,(d['id'],'underdeveloped')
   assert any(urlsplit(u).scheme in ('http','https') for u in f.links),(d['id'],'no inline sources')
   for src in d['sources']:
    assert urlsplit(src['url']).scheme in ('http','https'),d['id']
    assert src['title'] and src['access'] and src['note'],d['id']
   result[d['id']]=d
 if complete:assert set(result)==expected,('Missing editorial drafts',sorted(expected-set(result)))
 assert not {d['title'] for d in result.values()}&set(manifest['protected_titles'])
 return result
