from pathlib import Path
from string import Template
from html import escape
from urllib.parse import urlsplit
import json,re,shutil,os
from cases import load_cases,render_cases
from editorial_drafts import load_drafts,NOTICE
from concept_links import load_relations,validate_article
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'dist'
origin=os.environ.get('SITE_URL',json.loads((ROOT/'config.json').read_text())['origin']).rstrip('/')
if urlsplit(origin).scheme not in ('http','https') or not urlsplit(origin).netloc:raise ValueError('SITE_URL must be an absolute HTTP(S) origin')
records=json.loads((ROOT/'content/catalog.json').read_text());editorial=json.loads((ROOT/'content/editorial.json').read_text());sources=json.loads((ROOT/'content/sources.json').read_text())
drafts=load_drafts(records,complete=True)
entries=[e for e in records if e['published']]
for e in entries:
 e.update(editorial.get(e['title'],{}));e['url']=('/dynamics/' if e['kind']=='D' else '/technologies/')+e['slug']+'/'
for e in entries:
 if e['id'] in drafts:e['description']=drafts[e['id']]['description']
scale_data=json.loads((ROOT/'content/scales.json').read_text())
scales=scale_data['groups']
scale_lookup={group['id']:group for group in scales}
placements={}
for group in scales:
 for entry_id in group['entries']:
  if entry_id in placements:raise ValueError(f'Duplicate primary scale: {entry_id}')
  placements[entry_id]=group['id']
assert set(placements)=={e['id'] for e in entries}, 'Assign each published entry exactly one primary scale'
for e in entries:
 e['scale']=placements[e['id']]
 e['other_scales']=scale_data['also'].get(e['id'],[])
 assert all(scale in scale_lookup and scale!=e['scale'] for scale in e['other_scales'])
lookup={e['title']:e for e in entries}
cases=load_cases(entries)
relations=load_relations(entries)
by_id={e["id"]:e for e in entries}
by_url={e["url"]:e for e in entries}
assert len({e['url'] for e in entries})==len(entries)
base=Template((ROOT/'templates/base.html').read_text())
if OUT.exists():shutil.rmtree(OUT)
OUT.mkdir();shutil.copytree(ROOT/'assets',OUT/'assets')
paths=[]
def esc(t):return escape(str(t),quote=True)
def slug(t):return re.sub('[^a-z0-9]+','-',t.lower()).strip('-')
def md(t):
 t=esc(t)
 t=re.sub(r'\[([^]]+)\]\((https?://[^)]+)\)',r'<a href="\2">\1</a>',t)
 t=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',t)
 t=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<em>\1</em>',t)
 t=re.sub(r'`([^`]+)`',r'<code>\1</code>',t)
 return t
kindnames={'P':'Practice','F':'Organizational form','S':'System / domain','D':'Social dynamic'}
categories=['Learning and knowledge','Belonging and relationships','Decisions and authority','Collaboration and production','Resources and ownership','Recognition and succession','Systems and institutions','Social dynamics']
shortnames=['Learning','Belonging','Decisions','Collaboration','Resources','Succession','Systems','Dynamics']
symbols=['<path d="M5 6h8c3 0 4 2 4 2s1-2 4-2h8v23h-8c-3 0-4 2-4 2s-1-2-4-2H5zM17 8v23"/>','<circle cx="12" cy="14" r="8"/><circle cx="24" cy="14" r="8"/><path d="M6 29c2-5 6-7 12-7s10 2 12 7"/>','<circle cx="18" cy="18" r="12"/><path d="M10 18h16M18 10v16"/>','<rect x="4" y="4" width="11" height="11"/><rect x="21" y="4" width="11" height="11"/><rect x="4" y="21" width="11" height="11"/><path d="M21 26h11M26 21v11"/>','<ellipse cx="18" cy="9" rx="12" ry="5"/><path d="M6 9v16c0 7 24 7 24 0V9M6 17c0 7 24 7 24 0"/>','<path d="M7 28V10h9v18M20 28V5h9v23M3 28h30"/>','<path d="M4 14l14-9 14 9M6 15h24M9 17v12m9-12v12m9-12v12M4 30h28"/>','<circle cx="8" cy="18" r="4"/><circle cx="27" cy="8" r="4"/><circle cx="27" cy="28" r="4"/><path d="M12 16l11-6M12 20l11 6"/>']
def symbol(cat):return '<svg class="card-symbol" viewBox="0 0 36 36" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true">'+symbols[categories.index(cat)]+'</svg>'
def page(path,title,description,body,search=False):
 target=OUT/(path.lstrip('/')+'index.html' if path.endswith('/') else path.lstrip('/'))
 target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(base.substitute(title=esc(title+' — Social Tech Toolkit' if title!='Social Tech Toolkit' else title),description=esc(description),canonical=esc(origin+path),scripts='<script type="module" src="/assets/search.js"></script>' if search else '',content=body))
 if path!='/404.html':paths.append(path)
def link(title):
 e=lookup.get(title)
 return '<a href="'+e['url']+'">'+esc(title)+'</a>' if e else esc(title)
def card(e):
 ex=e.get('outline',{}).get('Card examples','')
 # A concrete scenario rather than invented named case studies.
 footer=ex or e['example']
 return f'''<article class="card" data-entry="{e['id']}"><div class="card-top">{symbol(e['category'])}<span class="kind">{kindnames[e['kind']]}</span></div><h4><a href="{e['url']}">{esc(e['title'])}</a></h4><p>{esc(e['description'])}</p><span class="card-purpose">{esc(e['category'])}</span><div class="card-bottom"><span>{esc(footer)}</span></div></article>'''
art='<aside class="scale-map" aria-label="From society to everyday life"><div class="eyebrow">The same world, at every scale</div><ol>'+''.join(f'<li><a data-browse-link href="#{group["id"]}"><span class="scale-orbit orbit-{n}" aria-hidden="true"><i></i><i></i><i></i></span><span><strong>{esc(group["label"])}</strong><small>{esc(group["prompt"])}</small></span></a></li>' for n,group in enumerate(scales))+'</ol><p>From millions of people to you and the person next to you.</p></aside>'
sections=''
for n,group in enumerate(scales):
 featured=group['featured']
 group_entries=sorted([e for e in entries if e['scale']==group['id']],key=lambda e:(featured.index(e['id']) if e['id'] in featured else len(featured),e['title'].lower()))
 sections+=f'<section class="catalog-group" id="{group["id"]}" aria-labelledby="heading-{n}"><div class="scale-heading"><div><div class="eyebrow">{n+1:02} / {esc(group["kicker"])}</div><h3 id="heading-{n}">{esc(group["title"])}</h3><p>{esc(group["description"])}</p></div><span class="subtle">{len(group_entries)} entries</span></div><div class="cards">'+''.join(card(e) for e in group_entries)+'</div></section>'
alphabetical='<details class="alphabetical"><summary>Browse all titles A–Z</summary><div class="alphabetical-list">'+''.join(f'<a href="{e["url"]}">{esc(e["title"])}</a>' for e in sorted(entries,key=lambda e:e['title'].lower()))+'</div></details>'
nav=''.join(f'<a data-browse-link href="#{group["id"]}">{esc(group["label"])}</a>' for group in scales)
personal_picks=(ROOT/'content/home-personal-picks.html').read_text()
home=f'''<main id="main"><aside class="development-notice" aria-label="Project status"><strong>A project in development.</strong> This site is being developed with AI. Its content and structure will change over time, and parts may need significant editorial guidance.</aside><section class="hero hero-scales"><div><div class="eyebrow">Social technologies, from the everyday to the extraordinary</div><h1>See what makes<br>the world work.<br><em>Find ways to change it.</em></h1><p class="hero-question">How do strangers become friends? How does an idea become a movement? How do millions of people cooperate without ever meeting?</p><p class="hero-copy">Social technologies are the arrangements behind all of this: the invitations, habits, rules, and institutions that organize our lives. They shape everything from who you spend Friday night with to who holds power in society.</p><p class="hero-copy">These arrangements came from people designing ways to organize—or trying things and discovering what worked. We can invent new ones, improve those we inherit, and put them to use ourselves: to make friends, build an organization, or change society.</p><p class="hero-copy">Once you start noticing them, ordinary life looks different. The ways we live and work together become things we can understand and help shape.</p></div>{art}</section>
{personal_picks}
<section class="explore" id="explore" aria-labelledby="explore-title"><div class="section-top"><h2 id="explore-title">From the big picture to your everyday</h2><span class="subtle page-counter">{len(entries)} entries · Six scales</span></div><p class="explore-intro">Start with the world you want to understand—or the part of it you want to change. Many of these ideas work at several scales.</p><label class="eyebrow" for="search" style="margin-bottom:12px">Search social technologies</label><div class="search-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="10" cy="10" r="6.5"/><path d="m15 15 6 6"/></svg><input id="search" type="search" disabled placeholder="Try mentorship, BDFL, or shared ownership…" autocomplete="off" spellcheck="false" aria-describedby="search-status"><button id="clear-search" type="button" hidden>Clear</button></div><div class="search-status"><span id="search-status" role="status" aria-live="polite">Search will load after the page finishes loading.</span> <button id="retry-search" type="button" hidden>Retry search</button></div><noscript><p class="note">Search requires JavaScript. All entries remain available in the categories below.</p></noscript><nav class="category-nav" aria-label="Browse by scale">{nav}</nav><div id="search-results" hidden><h3 class="results-heading" id="result-count" aria-live="polite"></h3><div id="result-grid" class="cards"></div><p class="empty" id="empty-results" hidden>No matching technologies. Try another term or browse the categories.</p></div><div id="browse">{alphabetical}{sections}</div></section>
<section class="about" aria-labelledby="about-title"><div><div class="eyebrow">A different way of seeing</div><h2 id="about-title">Someone figured this out.<br>You can, too.</h2></div><div><p>A regular invitation can become a circle of friends. A shared set of rules can keep a project going for decades. People have been figuring out how to live and work together for a very long time.</p><p>This toolkit brings some of those ideas into view. Explore how they work, where they fall short, and what becomes possible when you try them in your own life.</p><a href="/guide/">Read the introduction</a></div></section></main>'''
page('/','Social Tech Toolkit','A field guide to social technologies: practical ways to learn, belong, decide, collaborate, share resources, and carry knowledge forward.',home,True)
questions={
 'Learning and knowledge':['What capability or understanding should participants develop?','Where do learners receive feedback, and how will you recognize independent capability?'],
 'Belonging and relationships':['Who can join, and what makes participating easier or harder?','Who does the ongoing work of hosting, maintenance, and repair?'],
 'Decisions and authority':['Who is eligible, who actually participates, and who holds decision authority?','How can a decision be challenged, reviewed, or changed?'],
 'Collaboration and production':['Who owns the work and how are dependencies made visible?','What happens when participation changes or a key contributor leaves?'],
 'Resources and ownership':['Who contributes, who benefits, and who has the power to change the arrangement?','How are maintenance, shortages, and disagreements handled?'],
 'Recognition and succession':['What contributions or capabilities are being recognized?','Can responsibility transfer along with the knowledge needed to exercise it?'],
 'Systems and institutions':['Which component practices carry the system, and which assumptions depend on context?','Who participates, who holds authority, and who is excluded?'],
 'Social dynamics':['What observations support this interpretation rather than another explanation?','Which relationships, incentives, or participation patterns would you examine next?']}
for e in entries:
 outline=e.get('outline',{});custom=editorial.get(e['title'],{});research=e.get('research',{})
 draft=drafts.get(e['id'])
 sections=[]
 opening=''
 if draft:
  opening='<div class="draft-opening">'+draft['opening_html']+'</div>'
  sections.extend((x['id'],x['title'],x['html']) for x in draft['sections'])
 else:
  intro=outline.get('What to explain',e['description'])
  sections.append(('what-it-is',custom.get('intro_title','What it is'),f'<p>{md(intro)}</p>'))
  for extra in custom.get('sections',[]):
   sections.append((extra['id'],extra['title'],(ROOT/'content'/extra['file']).read_text()))
 validate_article(e,opening+''.join(body for _,_,body in sections),relations,by_url)
 rel=[by_id[r['id']] for r in relations[e['id']]]
 case_matches=[c for c in cases if e['id'] in c['technology_ids']]
 if case_matches:sections.append(('real-cases','Real cases','<ul>'+''.join('<li><a href="/cases/'+c['id']+'/">'+esc(c['title'])+'</a> — '+esc(c['question'])+'</li>' for c in case_matches)+'</ul>'))
 sections.append(('related','Explore alongside','<div class="related-links">'+''.join(f'<a href="{r["url"]}">{esc(r["title"])}</a>' for r in rel)+'</div>'))
 linked_urls=set(re.findall(r'href="([^"]+)"',opening+''.join(body for _,_,body in sections)))
 citations=[]
 seen_urls=set(linked_urls)
 page_sources=[{'links':[x]} for x in draft['sources']] if draft else [sources[code] for code in e['sources']]
 for src in page_sources:
  for item in src['links']:
   if esc(item['url']) not in seen_urls:
    citations.append('<li><a href="'+esc(item['url'])+'">'+esc(item['title'])+'</a></li>')
    seen_urls.add(esc(item['url']))
  if not src['links']:
   text=re.sub(r'^\*\*[A-Z0-9-]+\s*[—–-]\s*','**',src['text'])
   citations.append('<li>'+md(text)+'</li>')
 if citations:
  sourcebody='<ul class="source-list">'+''.join(citations)+'</ul>'
  sections.append(('sources','Sources',sourcebody))
 toc=''.join(f'<a href="#{id}">{esc(title)}</a>' for id,title,_ in sections)
 article=opening+''.join(f'<section id="{id}"><h2>{esc(title)}</h2>{body}</section>' for id,title,body in sections)
 draft_notice='<p class="editorial-notice" data-editorial-status="needs-guidance">'+NOTICE+'</p>' if draft else ''
 body=f'''<main id="main"><div class="crumb"><a href="/">Toolkit</a> / <a href="/#{e['scale']}">{esc(scale_lookup[e['scale']]['label'])}</a></div><header class="article-header"><div class="eyebrow">{kindnames[e['kind']]} · {e['id']}</div><h1>{esc(e['title'])}</h1><p class="lead">{esc(e['description'])}</p>{draft_notice}<div class="article-tags"><span class="tag">{esc(e['category'])}</span>{"".join('<a class="tag" href="/#'+scale+'">'+esc(scale_lookup[scale]["label"])+'</a>' for scale in [e["scale"],*e["other_scales"]])}<span class="tag">{'Needs editorial guidance' if draft else 'Editorial adaptation' if e['adaptation'] else 'Source-based overview'}</span></div></header><div class="article-layout"><article class="article-body">{article}</article><aside class="sidebar" aria-label="On this page"><div class="sidebar-inner"><h2>On this page</h2>{toc}<hr><a href="/#explore"> Back to the toolkit</a><p class="subtle">A starting point for understanding.<br>A prompt for better questions.</p></div></aside></div></main>'''
 page(e['url'],e['title'],e['description'],body)
guide='''<main id="main"><div class="crumb"><a href="/">Toolkit</a> / The idea</div><header class="article-header"><div class="eyebrow">An introduction</div><h1>The ways we organize<br>shape what we can do.</h1><p class="lead">Social technologies are repeatable ways of organizing relationships and actions. Some fit into a meeting. Others hold an institution together.</p></header><div class="article-layout"><article class="article-body"><section id="everyday"><h2>Already part of everyday life</h2><p>A library depends on more than books and a building. Membership, lending procedures, trained librarians, and shared expectations make it usable. A community depends on more than people being nearby: invitations, recurring gatherings, agreements, and practical care help relationships develop.</p><p>These arrangements shape who gets to participate, what people can expect, how resources move, and which knowledge survives. Their effects can be useful, harmful, or unevenly distributed.</p></section><section id="scope"><h2>What makes something a social technology?</h2><p>A promise, a rule, or a recurring invitation can change what people are able to do together. That is the thread connecting the ideas here: reusable arrangements for coordinating action, sharing knowledge, cooperating, and exercising authority.</p><p>The revealing question is what the arrangement makes possible. A magazine’s <a href="/technologies/subscriptions/">subscriptions</a>, for example, can turn scattered purchases into commitments that help fund the next issue. The interesting part is how readers can sustain continuing work—and how the terms of their commitment affect what the publisher can plan.</p><p>Some arrangements deserve an explanation of their own; others make more sense as parts of a larger one. An everyday practice can be as revealing as a political system when it shows us a way people achieve something together.</p></section><section id="different-kinds"><h2>Not all tools are the same kind</h2><table class="guide-table"><thead><tr><th>Kind</th><th>What it describes</th><th>Example</th></tr></thead><tbody><tr><td>Practice</td><td>A repeatable method or rule</td><td>Lightning talks</td></tr><tr><td>Organizational form</td><td>A durable arrangement of people and responsibilities</td><td>Worker cooperatives</td></tr><tr><td>System / domain</td><td>A larger bundle of arrangements</td><td>Democracy</td></tr><tr><td>Social dynamic</td><td>A phenomenon to recognize and investigate</td><td>Informal authority</td></tr></tbody></table><p>Browse from society-wide arrangements down to everyday interactions. The purpose labels help you see whether an idea concerns learning, belonging, decisions, work, resources, or succession. A community can combine an apprenticeship, a steering council, a shared wiki, and recurring meals. These solve different problems and can support one another.</p></section><section id="lenses"><h2>Look at rules—and relationships</h2><p><a href="https://samoburja.com/gft/"><em>Great Founder Theory</em></a> emphasizes the people and capabilities that create and maintain institutions. <a href="https://extitutions.org/about">Extitutional theory</a> offers a complementary lens: participation, relationships, and mutual recognition can coordinate people beyond what their formal roles explain.</p><p>A chart can tell you who holds office. It may not tell you whom people trust, who brings newcomers into the group, or whose judgment resolves uncertainty. Both kinds of observation matter.</p></section></article><aside class="sidebar"><div class="sidebar-inner"><h2>In this introduction</h2><a href="#everyday">Everyday arrangements</a><a href="#scope">What belongs here?</a><a href="#different-kinds">Kinds of technology</a><a href="#lenses">Rules and relationships</a></div></aside></div></main>'''
page('/guide/','The idea behind the toolkit','Understand social technologies, how they shape society, and how to choose useful ways to organize together.',guide)
page('/404.html','Page not found','Find your way back to the Social Tech Toolkit.', '<main id="main" class="source-page"><div class="eyebrow">A small detour</div><h1>This page isn’t here.</h1><p class="lead">Browse the toolkit to find a social technology, or search by another name.</p><a class="hero-link" href="/">Return to the toolkit</a></main>')
# Curated aliases and discovery terms; related concepts are not asserted to be synonyms.
metadata={
 'Worker cooperatives':(['Worker co-ops','Worker coops'],['shared ownership','worker ownership']),
 'Consumer cooperatives':(['Consumer co-ops'],['shared ownership','customer ownership']),
 'Housing cooperatives':(['Housing co-ops'],['shared ownership','community housing']),
 'Producer cooperatives':(['Producer co-ops'],['shared ownership']),
 'Multistakeholder cooperatives':(['Multi-stakeholder cooperatives'],['shared ownership']),
 'Sortition':(['Selection by lot'],['civic lottery','random selection']),
 'Assemblies':(['Assembly'],['collective deliberation']),
 'Open-source collaboration':(['Open source','OSS collaboration'],['shared software','open development']),
 'Community land trusts':(['CLT','Community land trust'],['shared ownership','community land']),
 'Autonomous microenterprise units':(['Micro-enterprises','Microenterprises'],['Haier','distributed entrepreneurship']),
 'Time banking':(['Timebanking','Time bank'],['time credits','service exchange']),
 'Markets':(['Market','Market coordination'],['trade','exchange','prices','collective intelligence','price signals','distributed knowledge','supply and demand','externalities','market failures','purchasing power']),
 'Merit-based selection':(['Merit selection'],['meritocracy']),
 'Extitutional theory':(['Extitutions'],['relationships','mutual recognition']),
 'Steering councils':(['Steering council'],['project governance','Python']),
 'Participatory budgeting':(['PB'],['community budget','public spending']),
 'Recurring open gatherings':(['Stoop coffee','Neighborhood coffee'],['meet neighbors','community building','regular meetups']),
 'Succession planning':(['Leadership succession'],['founder transition','handover']),
 'Apprenticeship':(['Apprenticeships'],['learning by doing','craft training','supervised practice','mentorship'])}
for e in entries:
 if e['title'] in metadata:e['aliases'],e['terms']=metadata[e['title']]
index=[{k:e[k] for k in ['id','title','url','kind','category','scale','other_scales','aliases','terms']} for e in entries]
(OUT/'search-index.json').write_text(json.dumps(index,ensure_ascii=False,separators=(',',':')))
render_cases(page,entries,scales,cases)
(OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+esc(origin+p)+'</loc></url>' for p in paths)+'</urlset>\n')
(OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+origin+'/sitemap.xml\n')
(OUT/'_headers').write_text('/assets/*\n  Cache-Control: public, max-age=3600\n/search-index.json\n  Cache-Control: no-cache\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n')
print(f'Built {len(entries)} entry pages, {len(cases)} case studies, case index, evidence guide, overview, guide, 404, and sitemap. Index: {(OUT/"search-index.json").stat().st_size:,} bytes.')
