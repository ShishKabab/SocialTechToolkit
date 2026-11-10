"""Validate editorially chosen relationships; never infer links from keywords."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json

ROOT=Path(__file__).resolve().parents[1]
BATCHES=['learning-community','governance-work','resources-succession','systems-dynamics','reviewed']

def entry_url(entry):
    return ('/dynamics/' if entry['kind']=='D' else '/technologies/')+entry['slug']+'/'

def load_relations(entries):
    ids={e['id'] for e in entries}
    result={}
    for batch in BATCHES:
        data=json.loads((ROOT/'research/editorial'/(batch+'-relations.json')).read_text())
        assert not result.keys() & data.keys(),('Duplicate relationship records',batch)
        result.update(data)
    assert result.keys()==ids,('Relationship coverage',sorted(ids-result.keys()),sorted(result.keys()-ids))
    for source,links in result.items():
        targets=[link['id'] for link in links]
        assert len(targets)>=2 and len(targets)==len(set(targets)),source
        assert set(targets)<=ids and source not in targets,source
        assert all(link['reason'].strip() for link in links),source
    return result

class ArticleLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.in_anchor=False
    def handle_starttag(self,tag,attrs):
        if tag=='a':
            assert not self.in_anchor,'Nested article links'
            self.in_anchor=True
            self.links.append(dict(attrs)['href'])
    def handle_endtag(self,tag):
        if tag=='a':
            assert self.in_anchor,'Unmatched closing link'
            self.in_anchor=False

def validate_article(entry,html,relations,by_url):
    parsed=ArticleLinks();parsed.feed(html)
    assert not parsed.in_anchor,(entry['id'],'Unclosed link')
    body_targets=set()
    for href in parsed.links:
        path=urlsplit(href).path
        if href.startswith(('/technologies/','/dynamics/')):
            assert path in by_url,(entry['id'],'Unknown concept link',href)
            target=by_url[path]['id']
            assert target!=entry['id'],(entry['id'],'Self link')
            body_targets.add(target)
    assert body_targets,(entry['id'],'No concepts linked in the explanation')
    related_targets={link['id'] for link in relations[entry['id']]}
    assert body_targets<=related_targets,(entry['id'],'Body links missing from Explore alongside',sorted(body_targets-related_targets))
    return body_targets
