"""Render explicitly authored public cases. Never import research dossiers here."""
from pathlib import Path
from html import escape
import json,re
from editorial_drafts import NOTICE,Fragment
ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/'content/cases'
LABELS={'success':'Bounded success','mixed':'Mixed outcomes','failure':'Failure on the stated objective','uncertain':'Outcome evidence uncertain'}
PUBLIC_FIELDS={'id','title','question','period','location','scale','technology_ids','summary','outcome','outcome_summary','editorial_status','sections'}
def validate_case(c,ids):
    assert set(c)==PUBLIC_FIELDS,(c.get('id'),'Unexpected or missing public case field')
    assert c['editorial_status']=='needs-guidance',(c['id'],'Case requires editorial guidance')
    assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',c['id'])
    assert c['outcome'] in LABELS
    assert c['scale'] in ['societies','movements','institutions','communities','groups','everyday']
    assert c['technology_ids'] and set(c['technology_ids'])<=ids,c['id']
    assert c['sections'],c['id']
    section_ids=[]
    for section in c['sections']:
        assert set(section)=={'id','title','html'},c['id']
        assert re.fullmatch('[a-z][a-z0-9-]*',section['id'])
        section_ids.append(section['id'])
        fragment=Fragment();fragment.feed(re.sub(r'</?h3>', '', section['html'].replace(' class="source-list"', '')))
    assert len(section_ids)==len(set(section_ids)),c['id']
def load_cases(entries):
    cases=json.loads((DIR/'articles.json').read_text())
    assert len(cases)==len({c['id'] for c in cases})
    for c in cases:validate_case(c,{e['id'] for e in entries})
    return cases

def inline(s):
    s=escape(str(s),quote=True)
    s=re.sub(r'\[([^]]+)\]\((https?://[^)]+)\)',r'<a href="\2">\1</a>',s)
    return re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
def markdown_blocks(text):
    # Small renderer for the checked-in evidence guide; no runtime dependencies.
    out=[]
    for block in text.strip().split('\n\n'):
        ls=block.splitlines()
        if ls[0].startswith('# '):out.append('<h1>'+inline(ls[0][2:])+'</h1>')
        elif ls[0].startswith('### '):out.append('<h3>'+inline(ls[0][4:])+'</h3>')
        elif ls[0].startswith('## '):out.append('<h2>'+inline(ls[0][3:])+'</h2>')
        elif ls[0].startswith('|'):
            rows=[x for x in ls if not re.match(r'^\|[\s|:-]+$',x)]
            out.append('<div style="overflow-x:auto"><table class="guide-table"><thead><tr>'+''.join('<th>'+inline(x.strip())+'</th>' for x in rows[0].strip('|').split('|'))+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(x.strip())+'</td>' for x in r.strip('|').split('|'))+'</tr>' for r in rows[1:])+'</tbody></table></div>')
        elif ls[0].startswith('- ') or re.match(r'^\d+\. ',ls[0]):
            tag='ul' if ls[0].startswith('- ') else 'ol'
            out.append('<'+tag+'>'+''.join('<li>'+inline(re.sub(r'^(?:- |\d+\. )','',x))+'</li>' for x in ls)+'</'+tag+'>')
        else:out.append('<p>'+inline(' '.join(ls))+'</p>')
    return '\n'.join(out)

def render_cases(page,entries,scales,cases):
    byid={e['id']:e for e in entries}
    e=escape
    notice='<p class="editorial-notice" data-editorial-status="needs-guidance">'+NOTICE+'</p>'
    for c in cases:
        sections=[(s['id'],e(s['title']),s['html']) for s in c['sections']]
        links=''.join('<a class="tag" href="'+byid[i]['url']+'">'+e(byid[i]['title'])+'</a>' for i in c['technology_ids'])
        body='<main id="main"><div class="crumb"><a href="/cases/">Real cases</a> / '+e(c['location'])+'</div><header class="article-header"><div class="eyebrow">Case study · '+e(c['period'])+'</div><h1>'+e(c['title'])+'</h1><p class="lead">'+e(c['question'])+'</p><p>'+e(c['summary'])+'</p>'+notice+'<div class="article-tags">'+links+'</div></header><div class="article-layout"><article class="article-body">'+''.join('<section id="'+sid+'"><h2>'+title+'</h2>'+html+'</section>' for sid,title,html in sections)+'</article><aside class="sidebar" aria-label="On this page"><div class="sidebar-inner"><h2>On this page</h2>'+''.join('<a href="#'+sid+'">'+title+'</a>' for sid,title,_ in sections)+'<hr><a href="/cases/"> All cases</a></div></aside></div></main>'
        page('/cases/'+c['id']+'/',c['title'],c['question'],body)
    intro='<main id="main" class="source-page"><div class="eyebrow">Social technologies in the wild</div><h1>What happened when<br>people tried it?</h1><p class="lead">'+str(len(cases))+' real cases, from friendship and mutual support to the institutions that govern millions.</p><p>A prize can produce a winning prototype without a working service. A cooperative can protect its members while one of its businesses fails. The interesting part is understanding what worked, for whom, and why.</p><p>These AI-assisted case studies need further editorial guidance. They explore outcomes, possible explanations, and unanswered questions. The outcome label refers to the question in that case—not a verdict on the whole organization.</p><p><a href="/cases/evidence/">How to read the evidence</a></p>'
    intro+='<nav class="category-nav" aria-label="Cases by scale">'+''.join('<a href="#'+s['id']+'">'+e(s['label'])+'</a>' for s in scales if any(c['scale']==s['id'] for c in cases))+'</nav>'
    for s in scales:
        group=sorted([c for c in cases if c['scale']==s['id']],key=lambda c:c['title'].lower())
        if not group:continue
        intro+='<section id="'+s['id']+'"><h2>'+e(s['title'])+'</h2>'
        for c in group:intro+='<article class="source-entry"><div class="eyebrow">'+e(LABELS[c['outcome']])+'</div><h3><a href="/cases/'+c['id']+'/">'+e(c['title'])+'</a></h3><p>'+e(c['question'])+'</p><p>'+e(c['outcome_summary'])+'</p></article>'
        intro+='</section>'
    page('/cases/','Real cases','What worked, what failed, and what remains uncertain: social technologies in real organizations and societies.',intro+'</main>')
    page('/cases/evidence/','How to learn from these cases','How to learn from these cases','<main id="main" class="source-page"><div class="crumb"><a href="/cases/">Real cases</a></div><article class="article-body">'+markdown_blocks((DIR/'evidence-guide.md').read_text())+'</article></main>')
