# Social Tech Toolkit — website content outline

Working site name: **Social Tech Toolkit**. The original requested domain was `socialtechtookit.com`; `socialtechtoolkit.com` is the corrected spelling used in this outline. Domain choice remains unconfirmed.

Purpose: help readers recognize the social technologies around them, understand how they work, and choose useful ways to coordinate people.

Foundational source: Samo Burja, *Great Founder Theory*, 2020 manuscript. Page references below use the printed page numbers. The site will paraphrase and explain the source in original language, clearly attribute its theoretical claims, and distinguish those claims from the site's practical applications. It should work for readers who have never read the manuscript.

## 1. Homepage — `/`

### Header

- Site name: **Social Tech Toolkit**.
- Navigation: **Explore technologies** (anchor to the grid), **About this toolkit** (anchor to the source note).
- No account, onboarding, or separate application interface.

### Introduction

**Heading:** “See what makes the world work. Find ways to change it.”

**Homepage introduction:**

How do strangers become friends? How does an idea become a movement? How do millions of people cooperate without ever meeting?

Social technologies are the arrangements behind all of this: the invitations, habits, rules, and institutions that organize our lives. They shape everything from who you spend Friday night with to who holds power in society.

Once you start noticing them, ordinary life looks different. You can understand what holds a community together, why an organization gets stuck, or how a movement gathers strength—and use those ideas to make something happen yourself.

**The lens behind the toolkit:** Samo Burja argues that effective institutions depend on people who design, maintain, and adapt these arrangements. Preserving their outward forms is not enough to preserve their usefulness. Present this as the manuscript's perspective, rather than an uncontested theory of history.

**Invitation:** “Explore the tools that make cooperation possible—and the conditions that make them work.” Link to the grid.

Keep this introduction short: approximately 150–200 words in the finished site.

### Technology grid

**Heading:** “Explore social technologies.”

Use a responsive grid grouped by the six scales below, with an alphabetical index and anchor links. Keep purpose and kind as secondary labels. The original 20 outlines below are the foundation; section 6 expands the inventory. Publish cards only when their full pages are ready. Separate broad systems and social dynamics from practical methods. Add client-side title search above the grid, as specified below. Each card contains:

1. **Title** — the technology's familiar name.
2. **Short description** — one sentence explaining its coordination function.
3. **Examples** — two or three recognizable instances.
4. **Link** — “Explore [technology]” leading to its full page.

The title, description, and examples specified in section 3 seed the initial card content. The inventory in section 6 supplies additional page briefs, not finished articles. Keep card content available directly in HTML.

### Overview search

Place a clearly labeled **Search social technologies** field above the grid. Placeholder: “Try mentorship, BDFL, or shared ownership”. Search published entries across technologies, systems, and dynamics; keep each result's kind and purpose visible.

- **Search fields:** titles, curated aliases (including acronyms and spelling variants), and curated discovery terms. Do not search full article bodies in the first version.
- **Normalization:** ignore case, accents, and punctuation differences; normalize whitespace and hyphenation. Match words regardless of their order. Preserve meaningful short acronyms.
- **Fuzzy matching:** tolerate small spelling errors in titles and aliases. Start conservatively: exact or prefix matching for tokens of three characters or fewer, one edit for four-to-seven-character tokens, and up to two edits for longer tokens. Include adjacent-letter transpositions. Tune these defaults against representative queries before release.
- **Synonym discovery:** store entry-specific search terms at build time. Distinguish genuine alternate names from related concepts: “shared ownership” can discover several ownership arrangements without implying they are equivalent. Do not automatically expand synonyms transitively.
- **Ranking:** exact title first, then exact alias, title word/prefix matches, curated discovery-term matches, and finally fuzzy matches. Prefer complete query coverage over partial matches; use alphabetical order to break ties. Avoid unrelated results based on a single common word in a multiword query.
- **Results:** while searching, show one ranked grid using the existing cards. When an alias or discovery term supplies the match, optionally show a short explanation such as “Also known as …” or “Related to …”. An empty or cleared query restores the categorized overview.
- **Feedback:** display the result count and a clear-search control. For no matches, show “No matching technologies. Try another term or browse the categories.” Never replace the user's query silently.
- **Loading:** render the search input visibly disabled in the initial HTML. Start fetching the index in the background only after the browser's `window.load` event, without blocking browsing. If the search module starts after that event, check `document.readyState === "complete"` and begin then. Do not preload or fetch the index earlier. Keep the input disabled until the index has been fetched, parsed, validated, and the matcher initialized; then enable it without moving focus.
- **Loading feedback and failure:** show “Search will load after the page finishes loading”, then “Loading search…” while preparing the index. Announce “Search ready” on success. If fetching or initialization fails, keep search disabled and show “Search is unavailable. You can still browse the categories.” Provide a retry button that repeats initialization, with duplicate attempts prevented while loading. With JavaScript disabled, explain that search requires JavaScript and categorized browsing remains available.
- **Accessibility:** use a native labeled search input with the actual `disabled` attribute, ordinary linked cards, and polite announcements for loading status and result counts. Associate the status with the input using `aria-describedby`. Keep keyboard focus in the input during result updates; hidden cards must leave the tab order. If JavaScript fails or is disabled, the full categorized HTML overview remains usable.

Search metadata examples (editorial starting points, not an exhaustive synonym dictionary):

| Entry | Aliases / alternate names | Discovery terms |
| --- | --- | --- |
| Mentorship | Mentoring | Mentor, guidance |
| Lightning talks | Lightning talk | Short presentations, five-minute talks |
| BDFL governance | BDFL, benevolent dictator for life | Founder-led governance |
| Sortition | Selection by lot | Civic lottery, random selection |
| Worker cooperatives | Worker co-ops, worker coops | Shared ownership, worker ownership |
| Assemblies | Assembly | Collective deliberation |
| Consensus process | Consensus decision-making | Group agreement |
| Consent decision-making | Consent-based decisions | Objections, safe enough to try |

Keep consensus and consent separate. Likewise, meritocracy and aristocracy must not become synonyms. Typo tolerance helps find a term; it does not erase conceptual distinctions.

Acceptance examples for implementation: `mentroship` finds Mentorship; `BDFL` finds BDFL governance; `short presentations` finds Lightning talks; `shared ownership` finds relevant ownership entries; `consent` ranks Consent decision-making above Consensus process; clearing a query restores every published card. Check keyboard navigation, no-result feedback, and the no-JavaScript overview as well. Under a throttled connection, verify that the index request starts only after `window.load`, browsing remains usable throughout, and search stays disabled until initialization completes. Also check initialization after an already-fired load event, failed requests, invalid index data, and successful retry.

### About this toolkit / footer

- Explain that this is an independent educational guide drawing on *Great Founder Theory*, extitutional theory, practitioner accounts, and research collections; it is not an official publication of those authors.
- Attribute and link to the author's manuscript page: `https://samoburja.com/gft/`.
- Explain that practical scenarios are illustrative applications, not historical claims from the source or guarantees of success.
- Brief reading guidance: ask what problem an arrangement solves, what it depends on, and how to tell whether it still works.
- Include an accessible text link back to the technology grid.

The general introduction (“The idea”) explains social technologies, their effects, and the institutional and relational lenses. Keep democracy-specific comparisons on the Democracy page. Omit the method-selection advice section (“Start with a situation, not a favorite method”) from the introduction.

## 2. Shared technology-page outline

Route pattern: `/technologies/<slug>/`.

Target length: approximately 500–800 words per finished page, with plain-language definitions and concrete examples. Shorter pages are preferable when the mechanism is simple.

### Navigation and title

- Breadcrumb: **Home → [Technology]**.
- Page title and the same one-sentence description used on its card.

### What it is

- Define the technology in everyday language.
- Identify the coordination problem it addresses.
- Clarify important boundaries: for example, a credential signals competence but does not itself create competence.

### How it works

- Explain the mechanism in three or four steps: participants, shared expectations, incentives or authority, and resulting behavior.
- Describe the conditions that make the mechanism usable.
- Identify what requires human judgment, even when procedures are standardized.

### Examples in practice

- Expand the card's examples into two or three short explanations.
- Explain what each example coordinates, rather than merely naming an institution.
- Label historical examples, contemporary illustrations, and hypothetical scenarios distinctly.

### What makes it work—and how it fails

- Describe signs of actual functionality, such as reliable outcomes or successful knowledge transfer.
- Explain characteristic failure modes: empty imitation, capture, misleading signals, rigidity, or misplaced incentives.
- Include the relevant tradeoffs and limits. A social technology can coordinate effectively while serving harmful ends; effectiveness alone is not endorsement.

### Related technologies and source

- Link to two or three complementary or contrasting technology pages.
- Cite sources relevant to this entry; include chapter and printed pages when drawing on the manuscript.
- Use the source register in section 9 and add entry-specific evidence. Distinguish research, practitioner experience, historical description, and editorial hypotheses. Include complementary technologies and the social dynamics that could undermine the mechanism.

### When to use it — final content section

- End every technology page with two concrete situations where the mechanism could help.
- For each situation, explain **the problem**, **a possible use**, and **what to look for afterward**.
- Include a brief boundary where useful: when another approach is more suitable, or where the example is for understanding an institution rather than creating one personally.
- Treat family relationships and clinical practices with their actual purposes and obligations in view; avoid presenting them as generic organizational tactics.

The original outlines below specify the content unique to each seed page. The expanded inventory in section 6 supplies additional briefs; systems and dynamics use the adaptations in section 5. Their final bullets supply the closing “When to use it” section.

## 3. Individual technology-page outlines

### Adoption — `/technologies/adoption/`

- **Card description:** Recognized family membership creates lasting relationships, responsibilities, and continuity beyond biological ties.
- **Card examples:** Child adoption; Roman adult adoption; Japanese family-business succession.
- **What to explain:** How social recognition and formal status establish family roles and expectations. Distinguish child welfare from historical uses of adult adoption for succession.
- **Examples to expand:** Burja's account of Roman adoptive succession; his discussion of Japanese family businesses. Avoid implying either model transfers directly to other societies.
- **Conditions and failures:** Legitimate recognition, sustained obligations, and the difference between transferring a position and transferring the ability to fulfill it.
- **Related:** Marriage, Dynasties, Law.
- **Source:** “Social Technology,” pp. 29–30; “How Roman Emperors Handled the Succession Problem,” pp. 82–88.
- **When to use it:** Understand how adoptive families acquire recognized roles and obligations; analyze why a historical succession mechanism could transfer personal ties as well as formal authority. These are explanatory cases, not personal adoption advice.

### Awards and honors — `/technologies/awards-and-honors/`

- **Card description:** Public recognition directs attention and prestige toward achievements a community values.
- **Card examples:** Scientific awards; civic honors; teaching awards.
- **What to explain:** How award-givers, recipients, and audiences jointly establish prestige. Distinguish recognition of past achievement from a financial prize offered for a future result.
- **Examples to expand:** The Nobel Prize as described by Burja; a hypothetical community teaching award.
- **Conditions and failures:** Credible judgment, meaningful achievement, and an audience that respects the honor; risks of favoritism, prestige inflation, and rewarding appearances.
- **Related:** Education, Marketing, Credentials.
- **Source:** “Social Technology,” p. 29; “Honors Fuel Achievement,” pp. 40–46.
- **When to use it:** Recognize valuable maintenance work that rarely gets attention; make excellent mentoring visible across an organization. Look for changes in what participants actually value and practice.

### Bureaucracy — `/technologies/bureaucracy/`

- **Card description:** Defined roles and procedures make recurring work repeatable across many people.
- **Card examples:** Permit processing; expense approvals; routine service requests.
- **What to explain:** Burja's account of bureaucracy as a way to extend a capable person's reach when suitable delegates are scarce. Distinguish following a procedure from exercising delegated judgment.
- **Examples to expand:** A predictable application process; an internal workflow with a clear exception path.
- **Conditions and failures:** A well-understood task, maintainable procedures, and someone able to revise them; risks of abandoned processes and procedural compliance replacing results.
- **Related:** Government, Law, Strategy.
- **Source:** “How to Use Bureaucracies,” pp. 103–110.
- **When to use it:** Process frequent, similar requests consistently; make recurring administrative work dependable as a team grows. Check completion quality, delays, and whether exceptions reach someone who can resolve them.

### Cities — `/technologies/cities/`

- **Card description:** Concentrating people and shared services makes exchange, specialization, and cooperation easier.
- **Card examples:** Market towns; university cities; industrial districts.
- **What to explain:** The city as a durable arrangement of proximity, shared infrastructure, labor markets, and social expectations—not merely a collection of buildings.
- **Examples to expand:** Burja's discussion of cities outlasting particular regimes; a hypothetical district where complementary trades cluster.
- **Conditions and failures:** Accessible shared services and useful connections; crowding, exclusion, and physical proximity without meaningful exchange.
- **Related:** Government, Social norms, Marketing.
- **Source:** “Social Technology,” p. 27.
- **When to use it:** Assess whether co-locating complementary organizations would improve collaboration; understand why a shared workshop or market district could support specialization. Test whether proximity leads to actual exchange.

### Credentials — `/technologies/credentials/`

- **Card description:** Recognized qualifications help people assess expertise without evaluating every skill themselves.
- **Card examples:** Degrees; trade certifications; professional licenses.
- **What to explain:** The relationship between an issuer, an assessment, a holder, and the people relying on the signal. Distinguish training, demonstrated competence, and permission to practice.
- **Examples to expand:** A degree used in hiring; a practical skills certification.
- **Conditions and failures:** Trustworthy assessment and a meaningful link to performance; risks of credential inflation, exclusion, and test preparation replacing mastery.
- **Related:** Education, Healthcare, Law.
- **Source:** “Social Technology,” p. 27; “On the Loss and Preservation of Knowledge,” pp. 50–58.
- **When to use it:** Help unfamiliar collaborators identify qualified specialists; certify completion of a genuinely assessed training program. Check whether holders can perform the work the credential promises.

### Diplomacy — `/technologies/diplomacy/`

- **Card description:** Representation, protocol, and negotiation let independent groups coordinate across differences.
- **Card examples:** Embassies; diplomatic visits; negotiated agreements.
- **What to explain:** How recognized representatives and shared protocols make communication possible without requiring identical cultures or interests.
- **Examples to expand:** Diplomatic protocol in the manuscript; an explicitly analogous partnership between independent organizations.
- **Conditions and failures:** Representatives with real authority, reliable channels, and credible commitments; ceremonial agreement without implementation.
- **Related:** Government, Ritual, Strategy.
- **Source:** “Social Technology,” p. 26.
- **When to use it:** Establish a dependable point of contact between independent organizations; negotiate a shared project where neither side can direct the other. Look for fewer misunderstandings and commitments that are honored.

### Dynasties — `/technologies/dynasties/`

- **Card description:** Family continuity can carry relationships, resources, and institutional knowledge across generations.
- **Card examples:** Family businesses; royal houses; political families.
- **What to explain:** Why informal trust and relationships may transfer through families alongside formal positions. Separate this mechanism from an endorsement of hereditary power.
- **Examples to expand:** Family-business succession; Burja's historical account of the Khama family in Botswana, explicitly situated in the manuscript's period.
- **Conditions and failures:** Preparation, ability, and accepted succession; risks of entitlement, exclusion, family conflict, and incompetent heirs.
- **Related:** Adoption, Marriage, Education.
- **Source:** “Social Technology,” p. 30; “What Botswana Can Teach Us About Political Stability,” pp. 89–96.
- **When to use it:** Analyze continuity in a family-run organization; identify which relationships a succession plan must preserve. Evaluate both successor capability and actual authority, rather than family connection alone.

### Education — `/technologies/education/`

- **Card description:** Deliberate teaching passes on the knowledge and abilities needed for shared work.
- **Card examples:** Schools; apprenticeships; workplace training.
- **What to explain:** How instruction, practice, feedback, and assessment transfer capabilities. Emphasize the difference between repeating explanations and being able to act on them.
- **Examples to expand:** A master teaching a craft; a new employee learning how to handle unfamiliar cases.
- **Conditions and failures:** Skilled teachers, meaningful practice, and ways to detect misunderstanding; risks of teaching to the test and losing tacit knowledge.
- **Related:** Credentials, Bureaucracy, Dynasties.
- **Source:** “Social Technology,” p. 27; “On the Loss and Preservation of Knowledge,” pp. 50–58; “Intellectual Dark Matter,” pp. 59–67.
- **When to use it:** Prepare a successor before an experienced practitioner leaves; train a growing team without reducing its work to memorized scripts. Check performance on new problems and the ability to teach others.

### Government — `/technologies/government/`

- **Card description:** Recognized authority organizes collective decisions, shared services, and enforcement.
- **Card examples:** Municipal administration; public infrastructure; national government.
- **What to explain:** How authority, resources, legitimacy, and administration enable collective action. Distinguish formal office from the practical ability to govern.
- **Examples to expand:** Maintaining shared infrastructure; coordinating services across a jurisdiction.
- **Conditions and failures:** Effective execution and accepted authority; institutional capture, fragmented responsibilities, and formal mandates without capacity.
- **Related:** Law, Bureaucracy, Political theory.
- **Source:** “Social Technology,” p. 25; “Functional Institutions Are the Exception,” pp. 97–102.
- **When to use it:** Understand which public institution can address a shared infrastructure problem; assess why collective rules need both a decision-maker and an implementation process. Use delivery of the public function as the test.

### Healthcare — `/technologies/healthcare/`

- **Card description:** Specialized roles and institutions coordinate the work of maintaining and restoring health.
- **Card examples:** Clinics; hospitals; referral systems.
- **What to explain:** How people rely on organized expertise, defined responsibilities, and handoffs rather than each household supplying all care itself.
- **Examples to expand:** Coordination between a clinic and a specialist; the organizational roles surrounding a hospital visit.
- **Conditions and failures:** Appropriate expertise, continuity, and clear responsibilities; fragmented care and administrative activity that loses sight of its purpose.
- **Related:** Credentials, Education, Bureaucracy.
- **Source:** “Social Technology,” pp. 27–28.
- **When to use it:** Map who is responsible at each stage of a care pathway; understand where institutional handoffs need improvement. Keep applications about coordination, not diagnosis or treatment.

### Ideology — `/technologies/ideology/`

- **Card description:** Shared beliefs and interpretations help groups align priorities and behavior.
- **Card examples:** Religious worldviews; political movements; organizational missions.
- **What to explain:** How beliefs shape what people regard as legitimate, desirable, and worth doing. Distinguish the coordinating effect of a belief from whether it is true.
- **Examples to expand:** The manuscript's discussion of religious commitments shaping literacy; a hypothetical mission guiding a team's decisions.
- **Conditions and failures:** Shared understanding and connection to actual practice; dogmatism, slogans without consequences, and beliefs insulated from correction.
- **Related:** Social norms, Ritual, Political theory.
- **Source:** “Social Technology,” p. 26.
- **When to use it:** Articulate the purpose of a voluntary association; examine why groups with similar resources choose different priorities. Look for consistent decisions and room to recognize contrary evidence.

### Law — `/technologies/law/`

- **Card description:** Recognized rules define obligations and provide ways to resolve disputes.
- **Card examples:** Contracts; property rules; dispute procedures.
- **What to explain:** How rules, interpretation, and enforcement work together. Written rules alone do not ensure compliance, and enforcement arrangements differ across societies.
- **Examples to expand:** A contract establishing responsibilities; Burja's comparison of centralized and distributed enforcement.
- **Conditions and failures:** Legibility, credible enforcement, and workable remedies; inaccessible procedures, selective enforcement, and rules disconnected from practice.
- **Related:** Government, Diplomacy, Social norms.
- **Source:** “Social Technology,” pp. 25–26.
- **When to use it:** Understand why a collaboration needs explicit obligations and a dispute process; diagnose why an existing rule fails to settle recurring disagreements. Keep scenarios educational rather than jurisdiction-specific legal advice.

### Marketing — `/technologies/marketing/`

- **Card description:** Communication helps people discover an offering and understand how it fits their lives.
- **Card examples:** Product demonstrations; public information campaigns; service launches.
- **What to explain:** How awareness, explanation, and adoption connect a useful offering to a sustainable audience. Describe Burja's argument that adoption often requires new social practices as well as inventions.
- **Examples to expand:** Teaching people what a new service does; the manuscript's discussion of mass adoption of technologies.
- **Conditions and failures:** A real offering, intelligible benefits, and workable adoption; empty promotion, manipulation, and claims that outrun delivery.
- **Related:** Awards and honors, Social norms, Strategy.
- **Source:** “Social Technology,” p. 29; “How Social Engineering Drives Technology,” pp. 31–39.
- **When to use it:** Introduce an unfamiliar tool with concrete demonstrations; help the intended audience find an underused service. Assess successful use and retention, not attention alone.

### Marriage — `/technologies/marriage/`

- **Card description:** A recognized partnership establishes shared expectations and enduring responsibilities.
- **Card examples:** Spousal roles; household commitments; kinship relationships.
- **What to explain:** How marriage connects personal relationships to a wider structure of recognition, responsibilities, family, and property. Note that its forms and meanings vary.
- **Examples to expand:** Shared household expectations; marriage's role in connecting families in Burja's account.
- **Conditions and failures:** Consent, compatible expectations, and sustained commitments; coercion, unequal burdens, and conflicting assumptions about roles.
- **Related:** Adoption, Law, Social norms.
- **Source:** “Social Technology,” p. 29; discussion of marriage and succession, pp. 87–88.
- **When to use it:** Understand how private relationships become publicly recognized commitments; examine how family expectations shape household cooperation. These examples explain the institution rather than recommend marriage as a strategy.

### Political theory — `/technologies/political-theory/`

- **Card description:** Models of authority and cooperation guide the design and reform of governing institutions.
- **Card examples:** Constitutional design; theories of representation; institutional reform.
- **What to explain:** Burja's view of political theory as engineering knowledge for governance, and its additional role as ideology. Distinguish an explanation of power from a justification of it.
- **Examples to expand:** Designing decision rights; the manuscript's comparison of Confucian and Legalist approaches.
- **Conditions and failures:** Explicit assumptions, attention to actual behavior, and revision in response to results; elegant theories with no workable implementation.
- **Related:** Government, Ideology, Strategy.
- **Source:** “Social Technology,” p. 25; “How Late Zhou China Reverse-Engineered a Civilization,” pp. 174–182.
- **When to use it:** Design governance for a new association; investigate why formal decision rights differ from actual influence in an existing institution. Test whether the model explains behavior and helps resolve concrete problems.

### Psychotherapy — `/technologies/psychotherapy/`

- **Card description:** A structured therapeutic relationship organizes professional support for psychological difficulties.
- **Card examples:** Recurring therapy sessions; agreed therapeutic goals; a defined practitioner–client relationship.
- **What to explain:** The social arrangement of roles, continuity, expectations, and professional boundaries. Keep the discussion separate from claims about the effectiveness of particular treatments.
- **Examples to expand:** Burja's description of the therapeutic setting; his comparison with traditions of spiritual guidance, without treating them as clinically equivalent.
- **Conditions and failures:** Appropriate professional competence and clear boundaries; role confusion and institutional incentives that diverge from the purpose of care.
- **Related:** Healthcare, Credentials, Social norms.
- **Source:** “Social Technology,” pp. 28–29.
- **When to use it:** Understand why a dedicated professional relationship differs from informal conversation; examine how an organization can make qualified support easier to access. No self-treatment or amateur therapy instructions.

### Ritual — `/technologies/ritual/`

- **Card description:** Repeated, shared actions make transitions, commitments, and collective meaning recognizable.
- **Card examples:** Graduation ceremonies; civic commemorations; welcoming ceremonies.
- **What to explain:** How a repeatable sequence gives participants a shared interpretation of an event. Distinguish meaningful ritual from repetition with no social function.
- **Examples to expand:** Marking entry into a community; the Confucian emphasis on rites discussed by Burja.
- **Conditions and failures:** Understood meaning and credible participation; empty performance, compulsory conformity, and rituals disconnected from lived practice.
- **Related:** Social norms, Awards and honors, Ideology.
- **Source:** “Social Technology,” p. 28; “How Late Zhou China Reverse-Engineered a Civilization,” pp. 174–182.
- **When to use it:** Welcome newcomers into a voluntary community; mark a handover of responsibility. Look for clearer roles and shared understanding after the event.

### Sacrifice — `/technologies/sacrifice/`

- **Card description:** Giving up something valued can make collective commitments visible and meaningful.
- **Card examples:** Historical religious offerings; communal contributions; voluntary commitments of time.
- **What to explain:** Burja's discussion of sacrifice as a historical coordination mechanism, including its violent forms. Clearly label modern, nonviolent analogies as the site's interpretation.
- **Examples to expand:** The historical role of offerings; a hypothetical group whose members voluntarily contribute time to a shared undertaking.
- **Conditions and failures:** Shared meaning and freely accepted, proportionate costs; coercion, scapegoating, waste, and mistaking suffering for achievement.
- **Related:** Ritual, Ideology, Social norms.
- **Source:** “Social Technology,” p. 28.
- **When to use it:** Understand what a historical offering communicated to its community; consider a modest, voluntary contribution that makes commitment to a shared project tangible. Evaluate the public benefit, not the size of the cost imposed.

### Social norms — `/technologies/social-norms/`

- **Card description:** Shared expectations make everyday behavior predictable without spelling out every interaction.
- **Card examples:** Queueing; meeting etiquette; professional conduct.
- **What to explain:** How people learn expectations, recognize deviations, and reinforce behavior through ordinary social responses. Contrast informal norms with explicit law and procedures.
- **Examples to expand:** Taking turns; a team clarifying how and when to respond to colleagues.
- **Conditions and failures:** Understandable expectations and consistent practice; hidden rules, exclusion of newcomers, and norms that suppress useful disagreement.
- **Related:** Law, Ritual, Education.
- **Source:** “Social Technology,” pp. 21–26; “Functional Institutions Are the Exception,” pp. 100–102.
- **When to use it:** Reduce recurring friction in a shared space; help a new team establish dependable communication habits. Check whether misunderstandings decline and newcomers can learn the expectations.

### Strategy — `/technologies/strategy/`

- **Card description:** Shared reasoning connects actions and resources to a chosen goal.
- **Card examples:** Project plans; organizational priorities; contingency planning.
- **What to explain:** How goals, constraints, sequences, and feedback guide coordinated action. Distinguish a working strategy from a persuasive plan that no one can execute.
- **Examples to expand:** Coordinating teams around a shared objective; adapting a plan when assumptions change.
- **Conditions and failures:** Accurate models, sufficient authority, and feedback; prestige-driven goals, rigid plans, and internal competition that consumes the effort needed for the mission.
- **Related:** Political theory, Bureaucracy, Education.
- **Source:** “Social Technology,” pp. 26–27; “Competition for Power,” pp. 111–117; “Empire Theory,” pp. 118–145.
- **When to use it:** Align several teams working toward one outcome; choose what to stop doing when resources become constrained. Evaluate progress toward the goal and the ability to revise the plan.

## 4. Minimal publishing structure

This is a content outline, not an implementation commitment. The first website needs only:

- One homepage template and one reusable technology-page template.
- One content record per technology: title, slug, short description, examples, section content, related-page slugs, source references, aliases, and discovery terms.
- Build-time generation of ordinary HTML pages and `sitemap.xml` from that content list.
- Shared CSS for readable typography and a responsive grid.
- One small client-side search module on the overview, with a separate compact JSON index generated from published content and fetched in the background after `window.load`: stable ID, title, aliases, discovery terms, kind, primary purpose, and URL. Reuse the existing rendered cards for results.
- Keep matching in the browser. At this catalog size, a bounded edit-distance matcher and curated metadata are sufficient as an initial design; no search service or application framework is required. Measure responsiveness against the complete index before choosing any dependency.
- Generate the index and HTML from the same content records so titles, links, and publication status cannot drift. Search only published entries with real destination pages; research candidates stay out of both the index and sitemap.
- Static hosting, with the production domain configured once and used consistently for canonical URLs and the sitemap.

Initial sitemap: `/` plus whichever technology pages have completed editorial review. The 20 routes above remain the original seed set; unpublished inventory entries do not enter the sitemap. No separate category, search, or about pages are needed for this version.

Before publishing the finished content, verify historical details against the manuscript and supporting sources, keep period-specific examples dated, and check every technology link and source link. The local PDF itself is not part of the planned public assets.


## 5. Expanded catalog: organization and editorial rules

Research expansion: 5 November 2026. This inventory incorporates the original manuscript, the concepts discussed subsequently, extitutional theory, Supernuclear, Digital Grove, and additional method collections. It is a collection of page candidates, not a claim that all entries are equally supported or ready to prescribe.

### Primary browsing: from society to everyday life

The homepage should communicate that social technologies shape life at every scale, and that understanding them opens up practical ways to change things. Use this progression:

| Scale | Section heading | Invitation |
| --- | --- | --- |
| Societies | The big picture: What moves societies | Who gets a say? What gets built? Where does the money go? The arrangements that organize millions of lives also shape what a society can become. |
| Movements | Making waves: How change spreads | One person has an idea. A few people start organizing. Eventually, the rules can change. Explore how people build a shared voice and turn it into influence. |
| Institutions | Built to last: More than one person's big idea | A good idea needs people who can carry it forward. How do you build an organization that works, shares responsibility, and survives its founders? |
| Communities | Finding your people: How strangers become us | Friendship often starts with something surprisingly practical: a reason to show up, a place to gather, and someone who keeps inviting you. |
| Groups | Getting our act together: From “we should” to actually doing it | The group chat has plenty of ideas. Now someone has to decide, coordinate, and do the work. These are ways to turn good intentions into things that happen. |
| Between people | The everyday: Where it starts: between people | An introduction, a shared meal, a little help at the right moment. Even the smallest interactions have patterns you can notice, learn, and make part of your life. |

Give each published entry a primary location so the overview has no duplicate cards. Record other relevant scales and link them from its page: assemblies, for instance, can matter in a group, a community, or a society. These are editorial starting points, not rigid boundaries or a claim that larger scale is more important. Lead each group with recognizable examples, then list the rest alphabetically. Keep the A–Z index and search across all entries.

### Secondary labels: the problem you are trying to solve

| Primary purpose | Reader's question |
| --- | --- |
| Learning and knowledge | How do we learn, teach, and remember? |
| Belonging and relationships | How do people meet, trust one another, and stay connected? |
| Decisions and authority | Who decides, how, and with what accountability? |
| Collaboration and production | How do we organize and complete shared work? |
| Resources and ownership | How do we allocate, exchange, finance, and steward resources? |
| Recognition and succession | How do we recognize contributions and transfer responsibility? |

Retain one primary purpose and optional secondary purposes as descriptive labels beneath the scale-based navigation. These are aids to understanding, not claims that each technology has only one function. An open-source community can combine a BDFL, mentorship, contributor recognition, public proposals, and lightning talks.

### Identify what kind of thing each entry is

- **P — Practice:** a repeatable protocol, format, rule, or mechanism. Includes selection principles and meeting formats; detailed subtypes can be tags.
- **F — Organizational form:** a durable arrangement of participants, responsibilities, and relationships.
- **S — System or domain:** a large bundle of arrangements, or a field containing many technologies. These are orientation pages linking to specific mechanisms.
- **D — Social dynamic:** a phenomenon to understand and respond to. These belong in a companion section, not in a list of practices to install.

A decision forum, participant selection method, and decision rule are distinct. An assembly might recruit by sortition, hear expert evidence, deliberate in small groups, and decide by a supermajority. Markets are exchange mechanisms; capitalism is a broader economic system. Microenterprises can be independent businesses or autonomous units within an organization. Extitutional theory is a lens on relationships and participation, not a synonym for a leaderless organization.

### Democracy: participation, scale, and authority

Do not classify democracy using only a direct-versus-representative distinction. That distinction concerns who makes decisions; it does not describe who is eligible, who attends, how participants deliberate, or how many people can interact. Direct decision-making does not require every eligible citizen to cast a vote. [UK Parliament's explanation](https://www.parliament.uk/site-information/glossary/referendum/)

Add **assembly democracy** as an orientation page: members exercise collective authority through a convened assembly. Distinguish this governance arrangement from **Assemblies**, the existing forum entry—an assembly may merely advise someone else. Assembly democracy can involve direct decision-making, but is not a synonym for all direct democracy.

Use these dimensions on democracy and governance pages:

| Dimension | What the page must specify |
| --- | --- |
| Eligibility | Who is entitled to participate, and who is excluded? Distinguish citizenship, membership, age, and any status or property requirements. |
| Actual participation | Who turns up or votes? Distinguish open attendance among eligible members, selection by lot, election, and appointment. |
| Scale | How large is the eligible population, the attending body, and the discussion group? These can differ substantially. |
| Interaction | Do participants meet face to face, discuss in smaller groups, deliberate asynchronously, or only cast ballots? |
| Authority | Does the body recommend, make binding decisions, delegate, or oversee implementation? |
| Decision rule | How are proposals accepted: majority, supermajority, consensus, consent, or another specified rule? |
| Agenda and accountability | Who can propose issues, prepare the agenda, challenge decisions, and review officeholders? |

Illustrative comparison, with implementation-specific details to be filled in on each page:

| Arrangement | Who participates? | How it operates | Important distinction |
| --- | --- | --- | --- |
| Member assembly with binding authority | Eligible members who attend, subject to its rules | Discussion and decisions in a convened body | Open eligibility does not imply universal attendance or equal influence. |
| Mass referendum | Eligible voters who cast ballots | Votes are aggregated across a large electorate | Direct decision-making does not require a shared deliberative meeting. |
| Elected legislature | Representatives selected by voters | Representatives deliberate and decide | Voters authorize officeholders rather than deciding each issue themselves. |
| Citizens' assembly selected by lot | A selected subset, often recruited for broad representation | Structured deliberation, usually followed by recommendations or a defined decision | This is a selected body, not an assembly open to every eligible person's attendance; authority varies. |

**Athenian democracy is a historical case, not a third category mutually exclusive with direct and representative democracy.** The eligible political community was restricted to adult male citizens; women, enslaved people, and resident foreigners were excluded. Within that citizen body, poorer men could participate: do not describe the assembly as simply a wealthy-class institution. Actual attendees were a subset of eligible citizens. The assembly also operated alongside a council, courts, allotted offices, and some elected offices; explain changes across periods rather than presenting one timeless constitution. [Parliament historical overview](https://researchbriefings.files.parliament.uk/documents/RP14-25/RP14-25.pdf), [scholarship on Athenian participation](https://www.cambridge.org/core/books/democracy-and-participation-in-athens/087DFD98C944977C46BD9416AED9BA3E/listing), [research on election and lot](https://www.ascsa.edu.gr/uploads/media/hesperia/25068022.pdf)

The user's scale distinction should remain visible: a convened subset can interact differently from a mass electorate. Do not infer that Athens was a small, intimate discussion circle merely because only part of the population attended; its institutions involved thousands of citizens. Verify period-specific attendance figures before using numbers on the full page. Likewise, do not attribute assembly size solely to class restrictions: distinguish eligibility, actual attendance, practical participation costs, and institutional arrangements.

**Page outline additions:**

- **Assembly democracy:** explain membership, convening, agenda control, deliberation, binding authority, quorum, and implementation. Compare a member association's assembly with a referendum and an elected board. Discuss attendance burden, unequal speaking influence, agenda control, and scaling. End with when an assembly can help a community make shared decisions and when delegation or smaller deliberative groups may help.
- **Direct democracy:** explain direct decisions on issues through assemblies or ballots. Separate eligibility, turnout, proposal rights, voting rules, and deliberation. End with situations where members should retain decision authority over specified matters; distinguish binding votes from consultation.
- **Representative democracy:** explain selection, mandate, discretion, term, oversight, and removal. Compare decisions made by elected representatives with decisions reserved to members. End with situations requiring sustained attention or coordination beyond what all members can provide personally.
- **Athenian democracy (case study only):** present a dated historical account of how its institutions combined, who was excluded, and how participation worked. Link to assembly democracy, sortition, elected offices, rotation, and accountability. End with when this case helps analyze institutional design; avoid presenting the historical system as a ready-made prescription.

**Search metadata:** use “assembly-based democracy” as an alias for Assembly democracy, “indirect democracy” for Representative democracy, and “democracy in ancient Athens” for Athenian democracy. Treat “direct democracy”, “Athenian democracy”, and “citizens' assembly” as related discovery terms where appropriate, not interchangeable synonyms.

### Evidence labels in the inventory

- **Source code** (for example `S3` or `SN-D`): the named source supports the core mechanism. It does not establish effectiveness in every setting. Examples in the table are illustrative unless explicitly named as documented cases.
- **`~CODE`**: editorial adaptation or inference inspired by that source; the source does not name or validate this exact pattern.
- **`C`**: candidate based on general knowledge, still requiring entry-specific research. Do not publish it as a verified recommendation.
- Definitions and hypothetical use cases are deliberately brief. A citation to a method collection is a discovery trail; the full page should cite the individual method and explain its limits.

For all entries, use the shared page outline in section 2. The final column before evidence seeds the final **When to use it** section; expand it into a problem, an application, and an observable result. For systems, this becomes **When this lens is useful**; for dynamics, **When to look for it and how to respond**. Description is not endorsement, especially for hereditary, coercive, or exclusionary arrangements.

### Additional fields for a full page

Record: primary purpose; secondary purposes; kind; group scale; duration; who is eligible; how actual participants are selected or attend; eligible population and attending-body scale; deliberation format; who can decide; entry and exit rights; setup effort; maintenance burden; prerequisites; failure modes; complementary technologies; evidence strength; and source dates. Ask who bears costs and who can challenge an outcome. Describe cultural and historical context rather than treating every practice as interchangeable across societies.

## 6. Expanded technology inventory

**Inventory size:** 338 technology entries, 34 system/domain orientation entries, and 32 social-dynamic entries: **404 entries total**. Counts include explicitly labeled umbrella concepts, not 404 interchangeable interventions.

| Purpose | Technology entries |
| --- | ---: |
| Learning and knowledge | 54 |
| Belonging and relationships | 54 |
| Decisions and authority | 71 |
| Collaboration and production | 56 |
| Resources and ownership | 65 |
| Recognition and succession | 38 |


Each row is a distinct page candidate. Umbrella entries are marked S and should link down to their component practices. Do not sum umbrella pages and component pages as independent interventions. Stable IDs support later editing; they are not rankings.

### Learning and knowledge

| ID | Technology | Kind | Coordination mechanism | Example / when to consider it | Evidence |
| --- | --- | --- | --- | --- | --- |
| T001 | Mentorship | P | An experienced person supports another's development over time. | Help a new maintainer grow into responsibility. | [NIH-M](#source-nih-m) |
| T002 | Apprenticeship | F | Learn a craft through supervised participation in real work. | Train someone where written instructions omit important judgment. | [GFT](#source-gft), [ILO-A](#source-ilo-a) |
| T003 | Peer learning circles | F | Peers meet repeatedly to work through shared learning goals. | Study a difficult subject without a permanent teacher. | [R-T003](#source-r-t003) |
| T004 | Communities of practice | F | Practitioners sustain shared learning around a common domain. | Connect isolated people doing similar work. | [COP](#source-cop) |
| T005 | Study groups | F | Members jointly read, discuss, and solve problems. | Maintain momentum through a course or reading program. | [R-T005](#source-r-t005) |
| T006 | Journal clubs | P | A group critically examines research papers together. | Build shared standards for interpreting evidence. | [R-T006](#source-r-t006) |
| T007 | Socratic seminars | P | Participants examine claims through disciplined questioning. | Explore assumptions behind a disputed idea. | [R-T007](#source-r-t007) |
| T008 | Teach-back | P | Learners explain material in their own words. | Find misunderstandings after an explanation. | Adaptation: [R-T008](#source-r-t008) |
| T009 | Peer instruction | P | Learners discuss conceptual questions and reconsider answers. | Expose reasoning differences in a classroom. | [R-T009](#source-r-t009) |
| T010 | Deliberate practice with feedback | P | Repeat targeted tasks with feedback on specific weaknesses. | Improve a clearly defined component of a skill. | [R-T010](#source-r-t010) |
| T011 | Job shadowing | P | Observe an experienced person's work in context. | Reveal everyday decisions before assuming a role. | [R-T011](#source-r-t011) |
| T012 | Job rotation | P | Move people through different responsibilities. | Develop cross-functional understanding and backup capacity. | [R-T012](#source-r-t012) |
| T013 | Cross-training | P | Teach several people to perform critical tasks. | Reduce dependence on a single specialist. | Adaptation: [R-T013](#source-r-t013) |
| T014 | Office hours | P | Reserve recurring times for accessible advice. | Make expert help available without constant interruption. | Adaptation: [R-T014](#source-r-t014) |
| T015 | Ask-me-anything sessions | P | Participants question someone with relevant experience. | Surface concerns hidden by a prepared presentation. | [R-T015](#source-r-t015) |
| T016 | Lightning talks | P | Short presentations expose a group to many interests. | Discover fellow residents' skills. | [SN-L](#source-sn-l) |
| T017 | Show-and-tell sessions | P | People demonstrate work and explain choices. | Share progress through concrete artifacts. | [R-T017](#source-r-t017) |
| T018 | Workshops | P | Participants learn through facilitated hands-on activity. | Practice a method together before using it independently. | [R-T018](#source-r-t018) |
| T019 | Train-the-trainer | P | Prepare participants to teach the next cohort. | Expand teaching capacity beyond the original instructor. | [R-T019](#source-r-t019) |
| T020 | Learning cohorts | F | Participants progress together through a defined learning period. | Provide peer support during intensive study. | [R-T020](#source-r-t020) |
| T021 | Reading salons | P | Conversation around selected texts connects ideas and people. | Build an intellectual community across specialties. | Adaptation: [R-T021](#source-r-t021) |
| T022 | Oral history | P | Record participants' accounts of events and practices. | Preserve experience before long-standing members leave. | [R-T022](#source-r-t022) |
| T023 | Storytelling | P | Narratives communicate situations, choices, and consequences. | Transmit practical judgment through memorable cases. | [R-T023](#source-r-t023) |
| T024 | Case-method discussion | P | Participants analyze a concrete situation before comparing judgments. | Practice decisions under incomplete information. | [R-T024](#source-r-t024) |
| T025 | Simulation exercises | P | Rehearse coordinated responses in a constructed scenario. | Prepare a team for unusual disruptions. | Adaptation: [R-T025](#source-r-t025) |
| T026 | After-action reviews | P | Compare intended and actual events to identify lessons. | Learn from a completed operation while memories are fresh. | Adaptation: [R-T026](#source-r-t026) |
| T027 | Retrospectives | P | Review collaboration and agree on improvements. | Adjust a team's recurring work. | [S3](#source-s3) |
| T028 | Peer review of work | P | Others inspect an artifact and provide substantive criticism. | Improve a draft before release. | [R-T028](#source-r-t028) |
| T029 | Replication | P | Repeat a study with new observations to examine whether its findings recur. | Check whether a finding survives a different team. | [R-T029](#source-r-t029) |
| T030 | Preregistration | P | Record intended questions and analyses before observing outcomes. | Distinguish planned tests from exploratory interpretation. | [R-T030](#source-r-t030) |
| T031 | Open notebooks | P | Expose ongoing methods and observations for others to inspect. | Let collaborators follow how a result emerged. | [R-T031](#source-r-t031) |
| T032 | Community wikis | P | Members maintain shared reference material. | Reduce repeated onboarding questions. | [SN-W](#source-sn-w) |
| T033 | Institutional archives | F | Preserve records with provenance and retrieval practices. | Recover decisions and obligations after personnel change. | [ARC](#source-arc) |
| T034 | Decision logs | P | Record decisions and rationale. | Explain why a policy exists. | [S3](#source-s3) |
| T035 | Knowledge maps | P | Map expertise, documents, and unanswered questions. | Find who can answer an unfamiliar problem. | [R-T035](#source-r-t035) |
| T036 | Expert directories | P | Maintain searchable accounts of people's skills and interests. | Route requests to relevant people. | [R-T036](#source-r-t036) |
| T037 | Open educational resources | P | Share learning materials under permissions enabling reuse. | Let teachers adapt materials to local needs. | [R-T037](#source-r-t037) |
| T038 | Translation networks | F | Coordinate people who translate and review shared materials. | Make knowledge accessible across language communities. | [R-T038](#source-r-t038) |
| T039 | Libraries | F | Organize shared collections and access to them. | Provide durable access beyond individual ownership. | [R-T039](#source-r-t039) |
| T040 | 1-2-4-All | P | Move from individual reflection to pairs, fours, and plenary. | Broaden participation in idea generation. | [LS](#source-ls) |
| T041 | Troika Consulting | P | Three participants alternate receiving and offering help. | Explore a challenge with peers. | [LS](#source-ls) |
| T042 | Appreciative Interviews | P | Interview partners about successful experiences. | Discover existing strengths. | [LS](#source-ls) |
| T043 | What, So What, Now What | P | Separate observations, interpretations, and next actions. | Reflect after an event. | [LS](#source-ls) |
| T044 | Fishbowl discussion | P | A small visible conversation is observed by a larger group. | Let others learn from practitioner dialogue. | [R-T044](#source-r-t044) |
| T045 | World Café | P | Rotate small-table conversations and share emerging insights. | Explore a common question across a large gathering. | [WC](#source-wc) |
| T046 | Open Space Technology | P | Participants propose sessions and choose where to contribute. | Convene around a shared concern without a fixed agenda. | [OS](#source-os) |
| T047 | Unconferences | P | Attendees help determine the event's sessions. | Match discussion topics to participants' actual interests. | [R-T047](#source-r-t047) |
| T048 | Delphi process | P | Experts respond through successive rounds with summarized feedback. | Explore judgments without requiring simultaneous discussion. | [R-T048](#source-r-t048) |
| T049 | Red teams | P | Assign a group to challenge plans or assumptions. | Expose weaknesses before committing resources. | Adaptation: [R-T049](#source-r-t049) |
| T050 | Premortems | P | Imagine a plan has failed and identify plausible causes. | Surface reservations before execution. | [R-T050](#source-r-t050) |
| T307 | Citizen science | P | Participants contribute observations or analysis to a research project. | Expand inquiry while defining data quality and participant roles. | [R-T307](#source-r-t307) |
| T308 | Participatory mapping | P | Participants collectively represent places, resources, or relationships. | Make local knowledge visible in planning. | [R-T308](#source-r-t308) |
| T309 | Deliberative polling | P | Compare opinions before and after structured informed deliberation. | Study how judgments change with information and discussion. | [R-T309](#source-r-t309) |
| T310 | Knowledge fairs | P | Participants offer demonstrations and exchange expertise across stations. | Discover capabilities across a large community. | [R-T310](#source-r-t310) |


### Belonging and relationships

| ID | Technology | Kind | Coordination mechanism | Example / when to consider it | Evidence |
| --- | --- | --- | --- | --- | --- |
| T051 | Recurring open gatherings | P | Meet at a predictable time with low entry requirements. | Make casual neighborhood encounters repeatable. | [SN-S](#source-sn-s) |
| T052 | Shared meals | P | Eating together creates recurring opportunities for interaction. | Connect people whose daily activities rarely overlap. | Adaptation: [BSC](#source-bsc) |
| T053 | Potlucks | P | Participants contribute food to a shared meal. | Distribute hosting effort and invite participation. | [R-T053](#source-r-t053) |
| T054 | Residential retreats | P | Participants share a place for sustained interaction. | Develop relationships beyond scheduled sessions. | [BSC](#source-bsc) |
| T055 | Protected unstructured time | P | Leave room for participant-led interaction. | Let conference conversations continue. | Adaptation: [BSC](#source-bsc) |
| T056 | Shared journeys | P | Travel together creates extended informal contact. | Help a cohort meet before an event. | Adaptation: [BSC](#source-bsc) |
| T057 | Hospitality hosting | P | A host welcomes and introduces guests. | Help unfamiliar participants enter a gathering. | [R-T057](#source-r-t057) |
| T058 | Buddy systems | P | Pair newcomers with someone who can orient them. | Reduce the social cost of asking basic questions. | [R-T058](#source-r-t058) |
| T059 | Cohort onboarding | P | Introduce newcomers together through a shared orientation. | Balance growth with teaching capacity. | Adaptation: [BSC](#source-bsc) |
| T060 | Membership curation | P | Use explicit criteria to select participants. | Assemble a focused working retreat; examine exclusion effects. | [BSC](#source-bsc) |
| T061 | Trial membership | P | Use a defined mutual evaluation period before commitment. | Test expectations in a shared living arrangement. | [R-T061](#source-r-t061) |
| T062 | Introductions by a connector | P | Someone identifies relevant common interests between people. | Help strangers begin a useful conversation. | [R-T062](#source-r-t062) |
| T063 | Check-in rounds | P | Invite each person to share their current state. | Begin a meeting with awareness of participants. | [S3](#source-s3) |
| T064 | Listening pairs | P | Partners alternate speaking and attentive listening. | Provide space for concerns outside a large meeting. | [R-T064](#source-r-t064) |
| T065 | Mutual aid networks | F | People organize reciprocal support around shared needs. | Coordinate neighborhood help during disruption. | [R-T065](#source-r-t065) |
| T066 | Care circles | F | A small group shares ongoing support responsibilities. | Prevent support from falling on one person. | Adaptation: [R-T066](#source-r-t066) |
| T067 | Meal trains | P | Schedule contributions of prepared meals. | Support a household during a demanding period. | [R-T067](#source-r-t067) |
| T068 | Childcare exchanges | P | Participants arrange reciprocal care with clear responsibilities. | Coordinate support among trusted households. | [R-T068](#source-r-t068) |
| T069 | Neighborhood associations | F | Residents organize around local concerns and relationships. | Maintain recurring coordination across households. | [R-T069](#source-r-t069) |
| T070 | Coliving households | F | Residents combine private living with shared spaces and practices. | Support everyday companionship and shared responsibilities. | [SN-D](#source-sn-d) |
| T071 | Cohousing communities | F | Households retain homes while jointly organizing common facilities. | Combine privacy with intentional community. | [CLT](#source-clt) |
| T072 | Third places | F | Accessible social settings support repeated informal encounters. | Create a gathering point outside home and work. | [R-T072](#source-r-t072) |
| T073 | Clubs | F | Members sustain activities around a shared interest. | Provide continuity beyond a one-off event. | [R-T073](#source-r-t073) |
| T074 | Affinity groups | F | People organize around a shared experience or concern. | Offer focused peer support within a larger organization. | [R-T074](#source-r-t074) |
| T075 | Alumni networks | F | Former participants maintain relationships after a shared experience. | Keep expertise and support accessible after departure. | [R-T075](#source-r-t075) |
| T076 | Festival cycles | P | Recurring collective celebrations renew relationships and identity. | Bring dispersed participants together periodically. | [R-T076](#source-r-t076) |
| T077 | Rites of passage | P | Mark recognized transitions in social role or status. | Acknowledge a cohort completing an apprenticeship. | [R-T077](#source-r-t077) |
| T078 | Welcoming ceremonies | P | Publicly recognize newcomers and introduce shared commitments. | Make entry into a group visible. | Adaptation: [R-T078](#source-r-t078) |
| T079 | Farewell rituals | P | Mark departures and acknowledge relationships and contributions. | End participation without silently losing institutional memory. | [R-T079](#source-r-t079) |
| T080 | Commemorations | P | Collectively recall events and people. | Transmit a group's history across generations. | Adaptation: [R-T080](#source-r-t080) |
| T081 | Shared symbols | P | Use recognizable signs to express collective identity. | Help a dispersed community recognize its affiliation. | [R-T081](#source-r-t081) |
| T082 | Origin stories | P | Tell how a group began and what problems shaped it. | Explain inherited priorities while permitting correction. | [R-T082](#source-r-t082) |
| T083 | Community agreements | P | Participants articulate expectations for interacting. | Clarify norms before predictable friction occurs. | [R-T083](#source-r-t083) |
| T084 | Codes of conduct | P | State behavioral boundaries and reporting processes. | Make participation expectations explicit at events. | [R-T084](#source-r-t084) |
| T085 | Principle-based norms | P | Use shared principles to guide contextual judgment. | Handle situations too varied for detailed rules. | [SN-P](#source-sn-p) |
| T086 | Mediation | P | A third party helps disputants seek an agreement. | Address a conflict that direct conversation has stalled. | [R-T086](#source-r-t086) |
| T087 | Restorative conferences | P | Prepared, voluntary dialogue addresses harm and responsibilities. | Consider repair where participants can engage safely. | [RJC](#source-rjc) |
| T088 | Conflict coaching | P | Help a participant prepare for a difficult conversation. | Clarify needs and choices before escalation. | [R-T088](#source-r-t088) |
| T089 | Repair conversations | P | Acknowledge an interaction's effects and negotiate changes. | Restore cooperation after a manageable breach. | Adaptation: [R-T089](#source-r-t089) |
| T090 | Community moderation | P | Designated participants apply discussion boundaries. | Keep a shared forum usable as participation grows. | [R-T090](#source-r-t090) |
| T091 | Guest policies | P | Define how visitors enter and use shared spaces. | Resolve recurring ambiguity in a household. | [R-T091](#source-r-t091) |
| T092 | Chore rotations | P | Rotate recurring maintenance responsibilities. | Distribute necessary but unattractive work. | [R-T092](#source-r-t092) |
| T093 | Notice-and-claim protocols | P | Announce an item before removing or reallocating it. | Clear abandoned shared-space belongings. | [SN-C](#source-sn-c) |
| T094 | Shared-space labeling | P | Make storage locations and expectations visible. | Reduce repeated household coordination. | [SN-C](#source-sn-c) |
| T095 | Participation stipends | P | Compensate time or expenses incurred by participants. | Make attendance possible beyond those with spare resources. | [R-T095](#source-r-t095) |
| T096 | Accessibility arrangements | P | Provide agreed supports for participation. | Include people excluded by the default meeting setup. | [R-T096](#source-r-t096) |
| T097 | Confidentiality agreements | P | Agree what information may be shared and with whom. | Support candid discussion of sensitive organizational issues. | [R-T097](#source-r-t097) |
| T098 | Cross-community exchanges | P | Arrange visits or joint activities between groups. | Build relationships beyond a familiar social circle. | Adaptation: [R-T098](#source-r-t098) |
| T099 | Peer support groups | F | People with related experiences support one another. | Reduce isolation without assuming professional treatment. | [R-T099](#source-r-t099) |
| T100 | Rotating hosts | P | Share responsibility for convening recurring gatherings. | Sustain a group beyond its original organizer. | Adaptation: [SN-S](#source-sn-s) |
| T311 | Congregations | F | People sustain recurring shared religious practice and mutual obligations. | Understand community through worship, care, and governance. | [R-T311](#source-r-t311) |
| T312 | Pilgrimage | P | A meaningful journey organizes shared commitment and encounter. | Study religious or cultural participation in its own tradition. | [R-T312](#source-r-t312) |
| T313 | Mutual-benefit societies | F | Members organize continuing support and benefits for one another. | Study collective care predating or supplementing public provision. | [R-T313](#source-r-t313) |
| T314 | Community sponsorship of newcomers | P | A group commits resources and relationships to welcoming new arrivals. | Coordinate practical integration beyond a one-time welcome. | [R-T314](#source-r-t314) |


### Decisions and authority

| ID | Technology | Kind | Coordination mechanism | Example / when to consider it | Evidence |
| --- | --- | --- | --- | --- | --- |
| T101 | Assemblies | F | A convened body deliberates on shared matters. | Bring members together for consequential choices. | [OECD](#source-oecd) |
| T102 | Citizens' assemblies | F | A broadly representative recruited group deliberates on public issues. | Examine a complex policy question in depth. | [OECD](#source-oecd) |
| T103 | Citizens' juries | P | A smaller deliberative panel hears evidence and forms recommendations. | Review a bounded public question. | [OECD](#source-oecd) |
| T104 | Town halls | P | An open meeting gathers questions and discussion. | Hear concerns; distinguish consultation from binding decisions. | [R-T104](#source-r-t104) |
| T105 | Public consultations | P | Invite input before an authority decides. | Collect affected people's knowledge about a proposal. | [OECD](#source-oecd) |
| T106 | Petitions | P | Aggregate support for a request to an authority. | Demonstrate demand for reconsidering a decision. | [R-T106](#source-r-t106) |
| T107 | Referendums | P | Eligible voters decide a specified question directly. | Resolve an issue assigned to the electorate. | Adaptation: [R-T107](#source-r-t107) |
| T108 | Sortition | P | Select participants by lottery, sometimes with stratification. | Reduce dependence on self-selection or campaigning. | [OECD](#source-oecd) |
| T109 | Elections | P | Participants select officeholders through a defined ballot process. | Authorize representatives for a term. | Adaptation: [R-T109](#source-r-t109) |
| T110 | Appointment | P | An authorized person or body chooses a role holder. | Fill a responsibility requiring specific judgment. | Adaptation: [R-T110](#source-r-t110) |
| T111 | Nomination with reasons | P | Explain role nominations before selection. | Make selection criteria discussable. | [S3](#source-s3) |
| T112 | Term limits | P | Limit how long someone may retain an office. | Create predictable leadership turnover. | Adaptation: [R-T112](#source-r-t112) |
| T113 | Rotating chairmanship | P | Rotate responsibility for chairing meetings. | Spread facilitation experience and reduce dependence. | Adaptation: [R-T113](#source-r-t113) |
| T114 | Recall procedures | P | Provide a defined route to remove a representative. | Respond to lost confidence before a term expires. | Adaptation: [R-T114](#source-r-t114) |
| T115 | Delegated authority | P | Give another person specified decision rights. | Move decisions closer to relevant expertise. | [R-T115](#source-r-t115) |
| T116 | Subsidiarity | P | Assign decisions to the lowest competent level. | Avoid escalating choices that local groups can handle. | Adaptation: [R-T116](#source-r-t116) |
| T117 | Single accountable decision maker | P | One named person decides within a stated remit. | Avoid unclear ownership for a time-sensitive choice. | [SN-D](#source-sn-d) |
| T118 | Advice process | P | A decision maker consults affected people and relevant experts. | Combine initiative with informed input. | [ADV](#source-adv) |
| T119 | Majority voting | P | Adopt an option exceeding half of the relevant votes. | Resolve a binary question under agreed voting rules. | [R-T119](#source-r-t119) |
| T120 | Plurality voting | P | The option receiving the most votes wins. | Choose among candidates without requiring a majority. | Adaptation: [R-T120](#source-r-t120) |
| T121 | Supermajority voting | P | Require a specified threshold greater than half. | Raise the bar for consequential changes. | Adaptation: [R-T121](#source-r-t121) |
| T122 | Unanimity | P | Require every eligible decision maker's agreement. | Give each party a veto over a shared commitment. | Adaptation: [R-T122](#source-r-t122) |
| T123 | Consensus process | P | Seek an agreement participants can support or accept under explicit rules. | Work through concerns before committing collectively. | [SEEDS](#source-seeds) |
| T124 | Consent decision-making | P | Test proposals for reasoned objections. | Try a revisable policy. | [S3](#source-s3) |
| T125 | Rough consensus | P | Address substantive objections without equating agreement to a vote tally. | Resolve technical proposals through reasoned discussion. | [IETF](#source-ietf) |
| T126 | Fist-to-five checks | P | Participants signal degrees of support with their hands. | Locate reservations before deciding; specify binding rules separately. | [SN-D](#source-sn-d) |
| T127 | Approval voting | P | Voters mark every acceptable candidate; the highest total wins. | Choose among several acceptable alternatives. | [R-T127](#source-r-t127) |
| T128 | Ranked-choice voting | P | Voters rank options; a specified counting rule determines outcomes. | Capture preferences beyond a single first choice. | Adaptation: [R-T128](#source-r-t128) |
| T129 | Score voting | P | Voters rate options on a defined scale. | Compare degrees of support with explicit tally rules. | Adaptation: [R-T129](#source-r-t129) |
| T130 | Dot voting | P | Participants allocate limited marks across options. | Prioritize discussion topics; avoid treating it as full deliberation. | [R-T130](#source-r-t130) |
| T131 | Quadratic voting | P | Additional voting intensity costs progressively more credits. | Explore preference intensity; design identity and budget rules carefully. | [R-T131](#source-r-t131) |
| T132 | Liquid democracy | P | Participants vote directly or delegate revocable voting authority. | Allow issue-specific representation. | Adaptation: [R-T132](#source-r-t132) |
| T133 | Proxy voting | P | Authorize another person to cast a vote under stated rules. | Represent an absent member. | Adaptation: [R-T133](#source-r-t133) |
| T134 | Delegation poker | P | Discuss and compare desired levels of delegated authority. | Clarify how much autonomy a team has. | [R-T134](#source-r-t134) |
| T135 | Decision thresholds by impact | P | Match required participation to consequences and reversibility. | Separate minor purchases from membership decisions. | [SN-D](#source-sn-d) |
| T136 | Doocracy | P | People take initiative within understood boundaries. | Complete low-risk reversible work without repeated approval. | [SN-P](#source-sn-p) |
| T137 | BDFL governance | F | A recognized leader retains final authority over project direction. | Understand founder-led coordination and its succession problem. | [OSS](#source-oss) |
| T138 | Steering councils | F | A small group holds defined governance responsibilities. | Distribute project leadership beyond one founder. | [PY](#source-py) |
| T139 | Boards of trustees | F | A governing body stewards an organization's purpose and assets. | Separate enduring oversight from daily management. | [R-T139](#source-r-t139) |
| T140 | Worker councils | F | Workers select representatives for collective workplace participation. | Create recurring representation within an enterprise. | Adaptation: [R-T140](#source-r-t140) |
| T141 | Circles with domains | F | A team governs a defined responsibility. | Clarify the scope of self-management. | [S3](#source-s3) |
| T142 | Double linking | P | Connect groups through representation in both directions. | Coordinate adjacent governance domains. | [S3](#source-s3) |
| T143 | Federations | F | Autonomous member bodies coordinate through shared arrangements. | Act jointly while retaining local control. | Adaptation: [R-T143](#source-r-t143) |
| T144 | Confederations | F | Members retain substantial autonomy under limited shared authority. | Coordinate independent organizations around narrow commitments. | Adaptation: [R-T144](#source-r-t144) |
| T145 | Separation of powers | P | Allocate governing functions to different bodies. | Reduce concentrated control through mutual constraints. | Adaptation: [R-T145](#source-r-t145) |
| T146 | Constitutions and charters | P | Define basic purposes, rights, offices, and amendment rules. | Make foundational governance commitments explicit. | Adaptation: [R-T146](#source-r-t146) |
| T147 | Bylaws | P | Codify internal governance procedures. | Maintain organizational continuity. | [S3](#source-s3) |
| T148 | Quorum rules | P | Require minimum participation for valid decisions. | Prevent a tiny attendance from committing everyone. | [R-T148](#source-r-t148) |
| T149 | Agenda-setting procedures | P | Specify how issues reach a decision forum. | Make control of discussion visible and contestable. | [R-T149](#source-r-t149) |
| T150 | Speaking queues | P | Maintain an explicit order for contributions. | Reduce competition for attention in a meeting. | [R-T150](#source-r-t150) |
| T151 | Facilitated rounds | P | Offer each participant a turn. | Hear voices beyond frequent speakers. | [S3](#source-s3) |
| T152 | Anonymous ballots | P | Separate voter identity from recorded choice. | Reduce interpersonal pressure on a sensitive decision. | [R-T152](#source-r-t152) |
| T153 | Conflict-of-interest disclosure | P | Reveal interests relevant to a decision. | Let others evaluate potential bias. | [R-T153](#source-r-t153) |
| T154 | Recusal | P | A decision maker steps aside from a particular matter. | Address a specific conflict of interest. | Adaptation: [R-T154](#source-r-t154) |
| T155 | Appeals procedures | P | Permit review by another authority under defined grounds. | Correct decisions without relying on personal influence. | Adaptation: [R-T155](#source-r-t155) |
| T156 | Ombuds offices | F | Provide an independent channel for concerns and navigation. | Surface problems outside ordinary reporting lines. | [R-T156](#source-r-t156) |
| T157 | Sunset clauses | P | Expire a rule unless it is deliberately renewed. | Prevent temporary measures from persisting automatically. | Adaptation: [R-T157](#source-r-t157) |
| T158 | Policy review dates | P | Schedule reconsideration of agreements. | Adapt rules as circumstances change. | [S3](#source-s3) |
| T159 | Public decision records | P | Make decisions and reasons accessible to affected people. | Support accountability beyond meeting attendees. | Adaptation: [R-T159](#source-r-t159) |
| T160 | Emergency authority with limits | P | Predefine temporary decision powers and their expiry. | Coordinate urgent responses while preserving later review. | Adaptation: [R-T160](#source-r-t160) |
| T315 | Collective bargaining | P | Worker and employer representatives negotiate shared employment conditions. | Create agreements beyond individual negotiations. | [ILO](#source-ilo) |
| T316 | Trade unions | F | Workers organize representation and collective interests. | Maintain a continuing basis for workplace voice. | [ILO](#source-ilo) |
| T317 | Arbitration | P | Parties submit a dispute to a designated decision maker. | Resolve a defined dispute through an agreed process. | [R-T317](#source-r-t317) |
| T318 | Courts | F | Authorized bodies hear disputes and apply recognized law. | Understand adjudication, remedies, and procedural protections. | Adaptation: [R-T318](#source-r-t318) |
| T319 | Jury trials | P | Selected lay participants assess specified questions within a trial. | Distinguish legal adjudication from a citizens' policy jury. | Adaptation: [R-T319](#source-r-t319) |
| T320 | Parliamentary procedure | P | Rules organize motions, debate, amendments, and votes. | Handle competing proposals in a formal assembly. | [R-T320](#source-r-t320) |
| T321 | Spokescouncils | F | Small groups coordinate through selected spokespeople with defined mandates. | Coordinate many groups while retaining local deliberation. | [R-T321](#source-r-t321) |
| T322 | Whistleblowing channels | P | Provide routes for reporting wrongdoing outside implicated authority. | Surface concerns that normal reporting relationships suppress. | Adaptation: [R-T322](#source-r-t322) |
| T323 | Freedom-of-information processes | P | Define rights and procedures for requesting public records. | Make official activity more inspectable. | [R-T323](#source-r-t323) |
| T324 | Social audits | P | Community participants examine records and actual delivery together. | Compare public commitments with lived implementation. | [R-T324](#source-r-t324) |
| T325 | Independent audits | P | An external evaluator examines records or practices against criteria. | Add scrutiny beyond self-reporting. | Adaptation: [R-T325](#source-r-t325) |


### Collaboration and production

| ID | Technology | Kind | Coordination mechanism | Example / when to consider it | Evidence |
| --- | --- | --- | --- | --- | --- |
| T161 | Open-source collaboration | F | Combine reusable licensed code with contribution and maintenance processes. | Let independent contributors improve a shared tool. | [OSI](#source-osi) |
| T162 | Commons-based peer production | F | Participants contribute to a shared resource without one employment hierarchy. | Understand collaborative knowledge projects. | [R-T162](#source-r-t162) |
| T163 | Project teams | F | Assign a group responsibility for a defined outcome. | Coordinate work with an identifiable completion condition. | [R-T163](#source-r-t163) |
| T164 | Working groups | F | Convene participants around a bounded issue or responsibility. | Develop a proposal across existing teams. | [R-T164](#source-r-t164) |
| T165 | Task forces | F | Temporarily concentrate people on an urgent objective. | Address an exceptional problem with dedicated capacity. | Adaptation: [R-T165](#source-r-t165) |
| T166 | Cross-functional teams | F | Combine different specialties within one working unit. | Reduce repeated handoffs across departments. | [R-T166](#source-r-t166) |
| T167 | Autonomous microenterprise units | F | Small internal units hold business responsibilities within a larger enterprise. | Study Haier's approach to distributed entrepreneurship. | [HAIER](#source-haier) |
| T168 | Independent microenterprises | F | Very small businesses organize production and exchange. | Provide local services with a small operating unit. | Adaptation: [R-T168](#source-r-t168) |
| T169 | Guilds across teams | F | Practitioners coordinate standards and learning across delivery teams. | Keep a specialty connected without centralizing all work. | Adaptation: [R-T169](#source-r-t169) |
| T170 | Hackathons | P | Time-bound gatherings concentrate collaborative making. | Prototype ideas and identify potential collaborators. | [R-T170](#source-r-t170) |
| T171 | Sprints | P | Commit to a short work cycle followed by review. | Deliver progress in manageable increments. | Adaptation: [R-T171](#source-r-t171) |
| T172 | Work parties | P | Convene people to complete a shared physical task. | Maintain a garden or improve a common space. | [R-T172](#source-r-t172) |
| T173 | Barn-raising | P | Community members pool labor for a substantial construction effort. | Understand reciprocal labor beyond individual household capacity. | Adaptation: [R-T173](#source-r-t173) |
| T174 | Pair work | P | Two people work together on the same task. | Share judgment and catch misunderstandings early. | Adaptation: [R-T174](#source-r-t174) |
| T175 | Mob or ensemble work | P | A group collaborates on one task with rotating active roles. | Combine expertise on a difficult shared problem. | Adaptation: [R-T175](#source-r-t175) |
| T176 | Shared task boards | P | Make pending work, ownership, and progress visible. | Coordinate distributed contributions. | [R-T176](#source-r-t176) |
| T177 | Pull systems | P | Take new work when capacity becomes available. | Limit overload. | [S3](#source-s3) |
| T178 | Work-in-progress limits | P | Cap concurrent tasks at a chosen stage. | Expose bottlenecks and encourage completion. | [R-T178](#source-r-t178) |
| T179 | Issue triage | P | Sort incoming requests by relevance, urgency, and ownership. | Keep a public project backlog usable. | Adaptation: [R-T179](#source-r-t179) |
| T180 | Request-for-comments processes | P | Circulate written proposals before adopting changes. | Gather review from people who cannot meet together. | [R-T180](#source-r-t180) |
| T181 | Design reviews | P | Review a proposed solution before committing to implementation. | Catch incompatible assumptions across specialties. | Adaptation: [R-T181](#source-r-t181) |
| T182 | Contribution guidelines | P | Explain how to submit, review, and accept work. | Reduce newcomer guesswork in a shared project. | Adaptation: [OSS](#source-oss) |
| T183 | Maintainer delegation | P | Assign responsibility for reviewing and integrating contributions. | Scale work beyond one central reviewer. | [OSS](#source-oss) |
| T184 | Forking | P | Create an independently governed derivative of a shared project. | Allow divergent directions where licensing permits. | Adaptation: [OSI](#source-osi) |
| T185 | Release governance | P | Specify who can authorize and coordinate a release. | Make publication responsibilities predictable. | [R-T185](#source-r-t185) |
| T186 | Standards bodies | F | Participants negotiate shared technical or procedural specifications. | Enable interoperability across independent organizations. | [R-T186](#source-r-t186) |
| T187 | Protocols and interfaces | P | Agree how separate actors exchange requests and results. | Coordinate without sharing every internal process. | Adaptation: [R-T187](#source-r-t187) |
| T188 | Standard operating procedures | P | Document repeatable operations and escalation points. | Make routine work transferable. | [R-T188](#source-r-t188) |
| T189 | Checklists | P | Prompt verification of specified steps or conditions. | Reduce omissions in repeatable workflows. | Adaptation: [R-T189](#source-r-t189) |
| T190 | Handoff protocols | P | Transfer responsibility with explicit context and acknowledgment. | Preserve continuity between shifts or teams. | Adaptation: [R-T190](#source-r-t190) |
| T191 | Responsibility matrices | P | State who acts, approves, advises, and is informed. | Resolve overlapping expectations in a project. | [R-T191](#source-r-t191) |
| T192 | Service-level agreements | P | Define expected service, measurement, and response obligations. | Coordinate between teams providing and consuming a service. | [R-T192](#source-r-t192) |
| T193 | Rotating duty rosters | P | Allocate recurring coverage through a schedule. | Maintain support while sharing undesirable shifts. | Adaptation: [R-T193](#source-r-t193) |
| T194 | Incident command | F | Temporarily organize response around explicit command and coordination roles. | Manage a complex disruption. | Adaptation: [R-T194](#source-r-t194) |
| T195 | Blameless postmortems | P | Examine contributing conditions without defaulting to individual blame. | Learn from failure while retaining responsibility for improvements. | [R-T195](#source-r-t195) |
| T196 | Communities of contribution | F | Participants organize around maintaining a shared artifact or cause. | Connect occasional help to durable stewardship. | [R-T196](#source-r-t196) |
| T197 | Volunteer matching | P | Match available skills and time to specified needs. | Turn willingness to help into concrete commitments. | [R-T197](#source-r-t197) |
| T198 | Time-boxed commitments | P | Agree on bounded periods of responsibility. | Let volunteers contribute without indefinite obligations. | Adaptation: [R-T198](#source-r-t198) |
| T199 | Public pledges | P | Make a commitment visible to an audience. | Coordinate expectations around a future contribution. | Adaptation: [R-T199](#source-r-t199) |
| T200 | Accountability partners | P | Peers periodically check progress on agreed commitments. | Sustain work that otherwise receives little feedback. | Adaptation: [R-T200](#source-r-t200) |
| T201 | Coworking sessions | P | People work alongside one another at an agreed time. | Create social support for independent tasks. | [R-T201](#source-r-t201) |
| T202 | Distributed campaigns | F | Independent local actors coordinate around shared objectives and materials. | Adapt collective action to different local contexts. | [R-T202](#source-r-t202) |
| T203 | Coalitions | F | Separate organizations cooperate on a shared objective. | Combine capabilities without requiring a merger. | [R-T203](#source-r-t203) |
| T204 | Collective impact partnerships | F | Organizations align goals, measures, and ongoing coordination. | Study sustained cooperation across service providers. | Adaptation: [R-T204](#source-r-t204) |
| T205 | Boundary-spanning roles | P | Assign someone to connect groups with different vocabularies or priorities. | Reduce misunderstandings across organizational interfaces. | Adaptation: [R-T205](#source-r-t205) |
| T206 | Minimum specifications | P | Specify only essential constraints. | Leave room for local methods. | [LS](#source-ls) |
| T207 | 15% Solutions | P | Identify actions within existing discretion. | Start without waiting for additional authority. | [LS](#source-ls) |
| T208 | Discovery-and-Action Dialogue | P | Explore obstacles and locally successful behaviors. | Find practical responses within a group. | [LS](#source-ls) |
| T209 | What I Need From You | P | Exchange concrete requests across groups. | Clarify dependencies. | [LS](#source-ls) |
| T210 | Purpose-to-Practice | P | Connect purpose with participants and working arrangements. | Design a shared initiative. | [LS](#source-ls) |
| T326 | Strikes | P | Workers collectively withhold labor around stated demands. | Understand bargaining power and collective coordination. | Adaptation: [R-T326](#source-r-t326) |
| T327 | Boycotts | P | Participants coordinate refusal to purchase or cooperate. | Express pressure through organized nonparticipation. | [R-T327](#source-r-t327) |
| T328 | Citizen journalism | P | Community participants gather and publish public-interest reporting. | Document issues overlooked by established media. | [R-T328](#source-r-t328) |
| T329 | Monastic orders | F | Religious communities organize life through shared rules and commitments. | Study durable collective practice in its historical tradition. | Adaptation: [R-T329](#source-r-t329) |
| T330 | Joint ventures | F | Separate organizations establish a shared undertaking. | Combine resources while retaining distinct parent organizations. | Adaptation: [R-T330](#source-r-t330) |
| T331 | Franchising | F | Independent operators use a shared brand and operating arrangement. | Study replication through contractual standards and support. | [R-T331](#source-r-t331) |


### Resources and ownership

| ID | Technology | Kind | Coordination mechanism | Example / when to consider it | Evidence |
| --- | --- | --- | --- | --- | --- |
| T211 | Markets | P | Prices and exchange coordinate supply, demand, and allocation. | Compare decentralized allocation with negotiated or planned alternatives. | [ECON](#source-econ) |
| T340 | Private ownership | P | Assign recognized rights over resources to people or private organizations. | Distinguish use, control, exclusion, and transfer. | [PRIVATE-OWNERSHIP](#source-private-ownership) |
| T341 | Intellectual property | S | Assign rights over inventions, creative expression, and other intangible assets, shaping who may use them and on what terms. | A designer can share a drawing while retaining rights over how it is reproduced. | [R-T341](#source-r-t341) |
| T342 | Patents | P | Offer time-limited exclusion rights over qualifying inventions in exchange for disclosure, creating one possible route to recovering development costs. | A new water-pump mechanism can be disclosed while its owner negotiates manufacturing licenses. | [R-T342](#source-r-t342) |
| T343 | Copyright | P | Give creators and other rightsholders control over specified uses of original expression, while leaving underlying ideas outside that protection. | A publisher needs permission to reproduce an illustrated guide, but its subject is not thereby owned. | [R-T343](#source-r-t343) |
| T344 | Trade secrets | P | Preserve an advantage through valuable confidential knowledge and arrangements that limit its unauthorized acquisition or disclosure. | A manufacturer can sell finished goods without revealing its internal production process. | [R-T344](#source-r-t344) |
| T345 | Advance market commitments | P | Make future demand more credible by committing funding toward purchases of products that meet specified requirements. | A buyer commits funds for an affordable vaccine meeting agreed criteria, encouraging investment in supply. | [R-T345](#source-r-t345) |
| T346 | Commissioned research and development | P | Pay a team to investigate or develop a solution, assigning development risks, payments, and rights through an agreement. | A transport operator pays for prototypes and testing of a more durable component. | [R-T346](#source-r-t346) |
| T347 | Patent buyouts | P | Compensate a patent holder for releasing rights so others can use an invention more freely. | A public fund purchases rights to a useful invention and releases them for wider manufacture. | [R-T347](#source-r-t347) |
| T348 | Earning from complementary capabilities | P | Earn from the production, implementation, or service that makes an invention useful, even when others can reproduce the idea. | A workshop shares a design but sells reliable manufacture, installation, and maintenance. | [R-T348](#source-r-t348) |
| T212 | Auctions | P | Allocate goods or contracts through structured bidding. | Discover offers when demand or value is uncertain. | [R-T212](#source-r-t212) |
| T213 | Double auctions | P | Buyers and sellers both submit offers under matching rules. | Organize repeated exchange across many participants. | [R-T213](#source-r-t213) |
| T214 | Barter | P | Exchange goods or services directly. | Trade without a common monetary payment. | [R-T214](#source-r-t214) |
| T215 | Mutual credit | P | Track reciprocal credits and obligations within a network. | Support exchange without requiring each trade to balance bilaterally. | [R-T215](#source-r-t215) |
| T216 | Time banking | P | Account for service exchanges using time credits. | Coordinate reciprocal practical help. | [TIME](#source-time) |
| T217 | Local currencies | P | Use a means of exchange within a defined community. | Study efforts to retain exchange within a network. | [R-T217](#source-r-t217) |
| T218 | Gift economies | S | Giving and reciprocal obligations organize circulation. | Understand exchange that is not priced transaction by transaction. | [R-T218](#source-r-t218) |
| T219 | Reciprocal labor exchanges | P | Participants return labor across different tasks or occasions. | Coordinate seasonal work among households. | [R-T219](#source-r-t219) |
| T220 | Rotating savings groups | F | Members contribute regularly and take turns receiving the pooled sum. | Understand collective saving with scheduled access. | [R-T220](#source-r-t220) |
| T221 | Credit unions | F | Members jointly own a financial cooperative. | Study member-governed provision of financial services. | [R-T221](#source-r-t221) |
| T222 | Mutual insurance | F | Members pool risks through an insurer organized for their benefit. | Understand collective coverage of uncertain losses. | [R-T222](#source-r-t222) |
| T223 | Emergency mutual-aid funds | P | Pool contributions for agreed urgent needs. | Respond to hardship beyond individual reserves. | [R-T223](#source-r-t223) |
| T224 | Crowdfunding | P | Raise contributions from many supporters for a defined project. | Test support for a proposed public artifact. | [R-T224](#source-r-t224) |
| T225 | Crowdlending | P | Multiple lenders finance borrowers through coordinated arrangements. | Compare distributed lending with a single financier. | [R-T225](#source-r-t225) |
| T226 | Subscriptions | P | Participants pay periodically for continuing access or support. | Fund recurring work with predictable contributions. | [R-T226](#source-r-t226) |
| T227 | Membership dues | P | Members contribute under shared funding rules. | Cover a club's recurring collective costs. | [R-T227](#source-r-t227) |
| T228 | Patronage | P | A supporter funds another's ongoing work or institution. | Sustain work that lacks direct paying customers. | [R-T228](#source-r-t228) |
| T229 | Grants | P | Allocate funds toward specified purposes through selection processes. | Support work whose benefits are not easily sold. | [R-T229](#source-r-t229) |
| T230 | Prize competitions | P | Offer a reward for achieving a defined result. | Attract multiple approaches to a bounded challenge. | [R-T230](#source-r-t230) |
| T231 | Bounties | P | Attach a reward to completion of a specified task. | Recruit help for a concrete missing contribution. | [R-T231](#source-r-t231) |
| T232 | Participatory budgeting | P | Community members help decide allocation of a budget. | Give residents authority over part of public spending. | [PB](#source-pb) |
| T233 | Quadratic funding | P | Use a matching formula that rewards breadth of financial support. | Explore funding of shared goods; examine identity manipulation risks. | [R-T233](#source-r-t233) |
| T234 | Matching grants | P | Release funding conditional on another contribution. | Encourage co-funding of a shared project. | [R-T234](#source-r-t234) |
| T235 | Endowments | F | Steward assets to support an institution over time. | Reduce dependence on a single annual fundraising cycle. | [R-T235](#source-r-t235) |
| T236 | Pooled procurement | P | Combine purchasing needs across participants. | Negotiate supply for a group of small buyers. | [R-T236](#source-r-t236) |
| T237 | Buying clubs | F | Members jointly arrange repeated purchases. | Access goods through coordinated demand. | [R-T237](#source-r-t237) |
| T238 | Tool libraries | F | Maintain tools for shared borrowing. | Provide occasional access without individual ownership. | [R-T238](#source-r-t238) |
| T239 | Resource booking systems | P | Agree how scarce shared resources are reserved and released. | Coordinate use of a workshop or common room. | [R-T239](#source-r-t239) |
| T240 | Queues | P | Allocate service in an agreed sequence. | Make access predictable when capacity is limited. | [R-T240](#source-r-t240) |
| T241 | Allocation lotteries | P | Randomly distribute a scarce benefit among eligible applicants. | Avoid discretionary favoritism where claims are comparable. | [R-T241](#source-r-t241) |
| T242 | Needs-based allocation | P | Prioritize resources according to explicit assessments of need. | Distribute limited support across unequal circumstances. | [R-T242](#source-r-t242) |
| T243 | Rationing | P | Limit individual access under defined allocation rules. | Manage a shortage without unrestricted first arrival. | [R-T243](#source-r-t243) |
| T244 | Tradable quotas | P | Set aggregate limits and permit transfer of allocated shares. | Study coordination under a collectively imposed resource cap. | [R-T244](#source-r-t244) |
| T245 | Commons governance | F | Users collectively maintain rules for a shared resource. | Study sustainable use beyond simple state-versus-market categories. | [OST](#source-ost) |
| T246 | Resource boundaries | P | Identify the resource and legitimate users. | Clarify who participates in commons governance. | [R-T246](#source-r-t246) |
| T247 | User participation in rulemaking | P | Affected users help revise operational rules. | Adapt management to local conditions. | [R-T247](#source-r-t247) |
| T248 | Community monitoring | P | Users or accountable monitors observe compliance. | Make shared commitments observable. | [R-T248](#source-r-t248) |
| T249 | Graduated sanctions | P | Responses escalate with severity or repetition. | Address breaches without treating every case identically. | [R-T249](#source-r-t249) |
| T250 | Community land trusts | F | Community organizations steward land for lasting local benefit. | Maintain assets beyond short-term individual resale incentives. | [CLT](#source-clt) |
| T251 | Worker cooperatives | F | Workers jointly own and democratically govern an enterprise. | Align work and ownership. | [ICA](#source-ica) |
| T252 | Consumer cooperatives | F | Customers jointly own and govern a provider. | Organize provision around member needs. | [ICA](#source-ica) |
| T253 | Producer cooperatives | F | Producers jointly organize shared services or market access. | Coordinate distribution among small producers. | [ICA](#source-ica) |
| T254 | Housing cooperatives | F | Members collectively organize housing ownership or provision. | Share residential governance. | [ICA](#source-ica) |
| T255 | Multistakeholder cooperatives | F | Different stakeholder groups share an enterprise's governance. | Balance member interests. | Adaptation: [ICA](#source-ica) |
| T256 | Employee ownership | F | Employees hold ownership interests under a defined arrangement. | Compare ownership participation with worker control. | [R-T256](#source-r-t256) |
| T257 | Steward ownership | F | Ownership arrangements protect purpose and responsible control. | Study alternatives to unrestricted investor control. | [R-T257](#source-r-t257) |
| T258 | Revenue sharing | P | Distribute defined shares of revenue among participants. | Coordinate collaborators with different contributions. | [R-T258](#source-r-t258) |
| T259 | Profit sharing | P | Distribute part of surplus according to an agreed formula. | Connect compensation to collective results. | [R-T259](#source-r-t259) |
| T260 | Transparent compensation formulas | P | Publish the criteria used to determine pay. | Make compensation reasoning open to scrutiny. | [R-T260](#source-r-t260) |
| T261 | Rent allocation formulas | P | Agree how room differences and shared costs affect rent. | Reduce recurring bargaining in a shared household. | [R-T261](#source-r-t261) |
| T262 | Fiscal sponsorship | F | An established organization administers support for an aligned project. | Explore support for a project without a separate organization. | [R-T262](#source-r-t262) |
| T263 | Community-supported agriculture | F | Members commit to a farm's production through advance participation. | Share aspects of production risk and seasonal supply. | [R-T263](#source-r-t263) |
| T264 | Repair cafés | P | Volunteers help people repair belongings at organized gatherings. | Share skills and extend the use of goods. | [R-T264](#source-r-t264) |
| T265 | Swap events | P | Convene people to exchange reusable items. | Redistribute goods that participants no longer need. | [R-T265](#source-r-t265) |
| T266 | Escrow | P | A third party holds assets pending agreed conditions. | Coordinate exchange when performance occurs at different times. | [R-T266](#source-r-t266) |
| T267 | Contracts | P | Specify commitments and remedies between parties. | Clarify responsibilities for a joint undertaking. | [R-T267](#source-r-t267) |
| T268 | Open licensing | P | Grant advance permissions for specified forms of reuse. | Allow collaboration without negotiating each permission separately. | [OSI](#source-osi) |
| T269 | Copyleft | P | Condition redistribution on preserving specified licensing freedoms. | Maintain downstream sharing obligations. | [R-T269](#source-r-t269) |
| T270 | Public provisioning | F | Public bodies organize access to goods or services. | Compare collective provision with individual purchasing. | [R-T270](#source-r-t270) |
| T332 | Taxation | P | Public authorities collect resources under defined rules. | Understand how collective functions are financed. | [R-T332](#source-r-t332) |
| T333 | Double-entry accounting | P | Maintain linked records of transactions within a balancing system. | Make organizational resource flows inspectable. | [R-T333](#source-r-t333) |
| T334 | Public asset registers | P | Record assets, stewardship responsibilities, and relevant rights. | Clarify what an institution holds and who maintains it. | [R-T334](#source-r-t334) |
| T335 | Assurance contracts | P | Contributions take effect only if specified participation conditions are met. | Coordinate a project requiring a minimum funding threshold. | [R-T335](#source-r-t335) |
| T336 | Risk-sharing pools | P | Agree how uncertain costs are distributed among participants. | Compare collective exposure with isolated individual risk. | [R-T336](#source-r-t336) |


### Recognition and succession

| ID | Technology | Kind | Coordination mechanism | Example / when to consider it | Evidence |
| --- | --- | --- | --- | --- | --- |
| T271 | Credentials | P | Recognized attestations communicate qualifications. | Help strangers assess claimed competence. | [GFT](#source-gft) |
| T272 | Certification | P | Assess conformity with defined requirements and attest results. | Make a specific standard legible across organizations. | [R-T272](#source-r-t272) |
| T273 | Accreditation | P | Evaluate organizations or programs against recognized criteria. | Support trust in institutions that train or assess others. | [R-T273](#source-r-t273) |
| T274 | Professional licensing | P | Authorize practice through a public regulatory arrangement. | Understand entry controls and public accountability. | [R-T274](#source-r-t274) |
| T275 | Portfolios | P | Present examples of completed work. | Evaluate demonstrated capability beyond formal credentials. | [R-T275](#source-r-t275) |
| T276 | References | P | People with direct experience offer testimony about someone. | Add context to a selection decision. | [R-T276](#source-r-t276) |
| T277 | Reputation systems | P | Aggregate assessments of past interactions. | Help unfamiliar participants evaluate prospective partners. | [R-T277](#source-r-t277) |
| T278 | Contribution records | P | Document work, maintenance, and support that people provide. | Recognize contributions otherwise overlooked. | [R-T278](#source-r-t278) |
| T279 | Awards | P | Publicly recognize selected achievements. | Direct attention to work a community values. | [GFT](#source-gft) |
| T280 | Peer nominations | P | Invite participants to identify others' contributions. | Surface valuable work beyond managers' visibility. | [R-T280](#source-r-t280) |
| T281 | Public appreciation | P | Make specific contributions visible and acknowledged. | Recognize everyday maintenance in shared living. | [SN-C](#source-sn-c) |
| T282 | Contributor credits | P | Attribute work to its contributors. | Preserve recognition in a collective artifact. | [R-T282](#source-r-t282) |
| T283 | Authorship conventions | P | Agree what contribution qualifies for authorship and ordering. | Reduce ambiguity around credit before publication. | [R-T283](#source-r-t283) |
| T284 | Merit-based selection | P | Select using explicit evidence relevant to the responsibility. | Choose a maintainer through demonstrated work; scrutinize criteria. | [R-T284](#source-r-t284) |
| T285 | Seniority rules | P | Assign priority according to length of participation or service. | Make advancement or allocation predictable. | [R-T285](#source-r-t285) |
| T286 | Competitive examinations | P | Use a common assessment to compare applicants. | Select at scale under published criteria. | [R-T286](#source-r-t286) |
| T287 | Work-sample assessments | P | Evaluate performance on a relevant task. | Assess practical capability for a specific role. | [R-T287](#source-r-t287) |
| T288 | Auditions | P | Observe candidates performing representative work. | Select performers or contributors through demonstration. | [R-T288](#source-r-t288) |
| T289 | Trial projects | P | Use a bounded collaboration before a longer commitment. | Test working compatibility and capability. | [R-T289](#source-r-t289) |
| T290 | Blind review | P | Conceal specified identity information during evaluation. | Reduce some identity cues in initial assessment. | [R-T290](#source-r-t290) |
| T291 | Peer promotion | P | Existing participants evaluate readiness for greater responsibility. | Expand a project's trusted contributor group. | Adaptation: [OSS](#source-oss) |
| T292 | Sponsorship for advancement | P | An established member advocates for someone's opportunities. | Connect demonstrated ability to access and responsibility. | [R-T292](#source-r-t292) |
| T293 | Succession planning | P | Identify and prepare people to assume critical responsibilities. | Reduce disruption when a founder leaves. | [GFT](#source-gft) |
| T294 | Deputy roles | P | Give a second person substantive responsibility alongside a role holder. | Build continuity and an informed substitute. | [R-T294](#source-r-t294) |
| T295 | Overlapping handovers | P | Incoming and outgoing role holders work together temporarily. | Transfer judgment as well as documents. | [R-T295](#source-r-t295) |
| T296 | Graduated responsibility | P | Increase authority as capability is demonstrated. | Develop successors without transferring everything at once. | [R-T296](#source-r-t296) |
| T297 | Leadership pipelines | F | Connect development experiences to progressively demanding roles. | Prepare future leaders across generations. | [R-T297](#source-r-t297) |
| T298 | Founder transition agreements | P | Specify the founder's future authority and transfer of control. | Avoid ambiguity after operational leadership changes. | [R-T298](#source-r-t298) |
| T299 | Emeritus roles | P | Retain optional advisory affiliation after active responsibility ends. | Preserve knowledge without blocking new leadership. | [R-T299](#source-r-t299) |
| T300 | Exit interviews | P | Ask departing participants about their experience and unfinished work. | Detect issues missed by routine feedback. | [R-T300](#source-r-t300) |
| T301 | Institutional memory interviews | P | Capture a role holder's reasoning and relationships before departure. | Transfer context absent from formal procedures. | [R-T301](#source-r-t301) |
| T302 | Backup ownership | P | Assign an informed alternate for important responsibilities. | Maintain continuity during absence. | [R-T302](#source-r-t302) |
| T303 | Stewardship terms | P | Assign responsibility for a defined period with review. | Renew commitment without making positions permanent. | [R-T303](#source-r-t303) |
| T304 | Knowledge succession demonstrations | P | Have successors perform critical work before handover. | Check that competence transferred alongside authority. | Adaptation: [GFT](#source-gft) |
| T305 | Lineage recognition | P | Trace teaching or authority through acknowledged predecessors. | Understand continuity claims in craft or religious traditions. | [R-T305](#source-r-t305) |
| T306 | Oaths of office | P | Publicly affirm obligations attached to a role. | Mark accountability when assuming authority. | [R-T306](#source-r-t306) |
| T337 | Peer juries for awards | P | A selected panel evaluates submissions against stated criteria. | Distribute recognition using deliberated judgments. | [R-T337](#source-r-t337) |
| T338 | Recallable stewardship | P | Grant stewardship with an explicit community removal process. | Combine continuing responsibility with contestable authority. | [R-T338](#source-r-t338) |


## 7. Systems, domains, and historical arrangements

These orientation pages explain bundles and connect them to actionable components. The original 20 page outlines remain useful, but broad domains such as healthcare should not appear to be interchangeable with a meeting technique. The table preserves the remaining original concepts and adds the larger systems discussed later.

| ID | Concept | Kind | What the page should distinguish | Illustrative context / components | Evidence |
| --- | --- | --- | --- | --- | --- |
| S001 | Capitalism | S | Private capital, employment, investment, and markets are related but distinct. | Compare ownership and allocation arrangements. | [ECON](#source-econ) |
| S002 | Socialism | S | A contested family of social-ownership arrangements, not one operational recipe. | Compare cooperative, public, and planned forms; further research required. | [R-S002](#source-r-s002) |
| S003 | Economic planning | S | Allocation through plans can coexist with markets. | Compare centralized planning and participatory planning variants. | [R-S003](#source-r-s003) |
| S004 | Democracy | S | Participation, representation, rights, and decision rules vary independently. | Link assemblies, elections, sortition, and accountability. | [DEM](#source-dem), [ATH](#source-ath) |
| S005 | Aristocracy | S | Rule by a privileged elite; historical forms often involve hereditary status. | Examine inherited authority and exclusion; not a recommendation. | [ARIST](#source-arist) |
| S006 | Meritocracy | S | An ideal or legitimating account of rule by merit, distinct from a particular selection procedure. | Ask who defines merit and who has opportunities to demonstrate it. | [MERIT](#source-merit) |
| S007 | Technocracy | S | Authority grounded in claimed technical expertise. | Compare expert advice with expert control. | [R-S007](#source-r-s007) |
| S008 | Monarchy | S | Authority vested in a monarch under varying succession and constitutional rules. | Connect hereditary succession, appointment, and checks on authority. | [R-S008](#source-r-s008) |
| S009 | Dynasties | F | Durable family transmission of authority, assets, or position. | Distinguish competence succession from inheritance. | [GFT](#source-gft) |
| S010 | Bureaucracy | F | Offices, procedures, records, and delegated responsibilities. | Explain continuity and scale alongside rigidity. | [GFT](#source-gft) |
| S011 | Government | S | Institutions exercising public authority. | Link taxation, law, administration, representation, and services. | [GFT](#source-gft) |
| S012 | Law | S | Recognized rules, interpretation, enforcement, and remedies. | Distinguish legislation, precedent, adjudication, and informal norms. | [GFT](#source-gft) |
| S013 | Diplomacy | S | Practices for managing relations between political actors. | Link envoys, negotiation, treaties, and confidence-building measures. | [GFT](#source-gft) |
| S014 | Political theory | S | Ideas used to analyze or justify collective authority. | Explain theories as intellectual tools rather than executable procedures. | [GFT](#source-gft) |
| S015 | Ideology | S | Shared interpretive and normative frameworks. | Examine coordination, legitimacy, and suppressed disagreement. | [GFT](#source-gft) |
| S016 | Strategy | S | Connecting aims, resources, actions, and feedback. | Link scenario exercises, priorities, and adaptation. | [GFT](#source-gft) |
| S017 | Education | S | Arrangements for transmitting and developing knowledge and capability. | Link apprenticeship, schools, mentorship, and peer learning. | [GFT](#source-gft) |
| S018 | Cities | S | Dense settlements combining many physical and social arrangements. | Link markets, public services, neighborhood groups, and governance. | [GFT](#source-gft) |
| S019 | Healthcare | S | Coordinated prevention, treatment, care, and supporting institutions. | Explain professional roles and care coordination, not clinical instructions. | [GFT](#source-gft) |
| S020 | Psychotherapy | S | Professional therapeutic practices, with distinct methods and evidence. | Explain the organized therapeutic relationship, not a general management tactic. | [GFT](#source-gft) |
| S021 | Marriage | F | Socially and legally recognized relationships with culturally variable obligations. | Explain kinship, care, property, and recognition in context. | [GFT](#source-gft) |
| S022 | Adoption | F | Arrangements establishing recognized parent-child relationships. | Center family relationships and obligations rather than organizational analogy. | [GFT](#source-gft) |
| S023 | Ritual | S | Patterned symbolic action organizing attention, meaning, and belonging. | Link welcoming, mourning, commemoration, and transitions. | [GFT](#source-gft) |
| S024 | Sacrifice | S | Historically varied practices involving relinquishment, offering, or costly commitment. | Distinguish religious meanings from analytical signaling accounts. | [GFT](#source-gft) |
| S025 | Marketing | S | Practices shaping attention, understanding, and exchange. | Link audience research, positioning, distribution, and reputation. | [GFT](#source-gft) |
| S026 | Social norms | S | Shared expectations maintained through social responses. | Link onboarding, conventions, sanctions, and norm change. | [GFT](#source-gft) |
| S027 | Sociocracy | S | A governance family combining consent, circles, selection, and linking. | Compare a complete system with adopting individual practices. | [S3](#source-s3) |
| S028 | Polycentric governance | S | Multiple decision centers with overlapping or nested responsibilities. | Compare resource governance across local and wider levels. | [R-S028](#source-r-s028) |
| S029 | Open-source ecosystems | S | Licenses, maintainers, users, contributors, funders, and governance interact. | Distinguish permission to reuse from power to decide. | [OSI](#source-osi), [OSS](#source-oss) |
| S030 | Extitutional theory | S | A relational analytical lens, not an organizational template. | Study participation and mutual recognition alongside formal roles. | [EXT](#source-ext) |
| S031 | Assembly democracy | S | Members exercise collective authority through a convened assembly; distinguish eligibility from attendance and a binding body from an advisory forum. | Compare a member assembly, a mass referendum, and an elected legislature. | Adaptation: [DEM](#source-dem), [ATH](#source-ath) |
| S032 | Direct democracy | S | Eligible participants decide issues themselves; universal turnout and face-to-face discussion are not requirements. | Compare assembly decisions and referendums; specify proposal rights and voting rules. | [DEM](#source-dem) |
| S033 | Representative democracy | S | Elected representatives exercise decision authority on behalf of constituents. | Examine mandates, discretion, oversight, and decisions reserved to voters. | [DEM](#source-dem) |

## 8. Social dynamics: companion reading

These are diagnostic concepts. They can inform design but should not be framed as guaranteed effects of a technique. Entries marked C are a research backlog. Related theories are not automatically claims made by extitutional theory.

| ID | Dynamic | What to notice | Design question or response | Evidence |
| --- | --- | --- | --- | --- |
| D001 | Participation-based alignment | Repeated participation shapes coordination beyond formal office. | What interactions actually hold this group together? | [EXT](#source-ext) |
| D002 | Mutual recognition | People respond to one another's perceived contributions and standing. | Whose contributions become visible? | [EXT](#source-ext) |
| D003 | Informal authority | Influence can differ from the organizational chart. | Map whom people consult and follow. | [FREEMAN](#source-freeman) |
| D004 | Cliques and informal exclusion | Friendship networks can control access without accountability. | Make information and selection routes accessible. | [FREEMAN](#source-freeman) |
| D005 | Economic embeddedness | Exchange occurs inside ongoing social relationships. | Which ties make agreements credible or constrain access? | [EMBED](#source-embed) |
| D006 | Weak-tie bridges | Some acquaintances connect otherwise separated social circles. | Are opportunities circulating beyond close friends? | [TIES](#source-ties) |
| D007 | Learning through participation | People develop practice by engaging with practitioners. | Can newcomers do meaningful work with support? | [COP](#source-cop) |
| D008 | Core and peripheral participation | Participation intensity varies across members and time. | Can occasional contributors remain welcome? | [COP](#source-cop) |
| D009 | Stigmergic coordination | Shared artifacts provide cues that guide subsequent contributions. | What work can participants discover without asking a manager? | [STIG](#source-stig) |
| D010 | Growth outrunning onboarding | New participation can exceed a group's ability to teach its practices. | Expand orientation capacity and observe newcomer experience. | Adaptation: [BSC](#source-bsc) |
| D011 | Tacit knowledge dependence | Essential judgment may remain with particular practitioners. | Can successors perform the work, not just repeat rules? | [GFT](#source-gft) |
| D012 | Institutional imitation | Visible forms persist without the capability that made them useful. | Check actual outputs and adaptation. | [GFT](#source-gft) |
| D013 | Founder dependence | Coordination relies heavily on a particular person's relationships and judgment. | Transfer skills, relationships, and authority deliberately. | [GFT](#source-gft) |
| D014 | Homophily | Similar people may form ties more readily. | Does apparent shared interest conceal restricted access? | [R-D014](#source-r-d014) |
| D015 | Reciprocity | Help can create expectations of future return. | Are those expectations understood and sustainable? | [R-D015](#source-r-d015) |
| D016 | Trust formation and repair | Reliability, interpretation, and vulnerability affect willingness to cooperate. | What would demonstrate changed behavior after a breach? | [R-D016](#source-r-d016) |
| D017 | Free riding | Some benefit without contributing to maintenance. | Distinguish unwillingness from inability and unclear expectations. | [R-D017](#source-r-d017) |
| D018 | Social loafing | Individual effort may decline when contributions are difficult to identify. | Make responsibilities intelligible without excessive surveillance. | [R-D018](#source-r-d018) |
| D019 | Volunteer burnout | Sustained overload and unsupportive conditions can exhaust volunteers and drive them away. | Bound commitments, distribute responsibility, and enable succession. | [R-D019](#source-r-d019) |
| D020 | Status hierarchies | Prestige shapes whose speech and work receive attention. | Are evaluations tracking relevant contributions? | [R-D020](#source-r-d020) |
| D021 | Preference falsification | Public agreement can conceal private disagreement. | Offer credible channels for dissent. | [R-D021](#source-r-d021) |
| D022 | Pluralistic ignorance | People can misread one another's private beliefs from public behavior. | Test assumptions about what others support. | [R-D022](#source-r-d022) |
| D023 | Group polarization | Discussion can shift participants toward more extreme positions. | Include substantive disagreement and examine information sources. | [R-D023](#source-r-d023) |
| D024 | Groupthink | Pressure for cohesion may suppress critical examination. | Assign challenge roles and separate proposals from commitments. | [R-D024](#source-r-d024) |
| D025 | Goal displacement | Procedures or proxy measures become objectives themselves. | Compare measured success with the original purpose. | [R-D025](#source-r-d025) |
| D026 | Metric gaming | Rewards attached to indicators encourage strategic reporting or behavior. | Examine what the indicator leaves out. | [R-D026](#source-r-d026) |
| D027 | Capture | A subset redirects governance toward its own interests. | Inspect entry, oversight, appeals, and concentrated benefits. | [R-D027](#source-r-d027) |
| D028 | Principal-agent problems | Delegates and delegators have differing incentives or information. | Clarify discretion, reporting, and accountability. | [R-D028](#source-r-d028) |
| D029 | Path dependence | Earlier choices constrain later possibilities. | Identify switching costs before adding another dependency. | [R-D029](#source-r-d029) |
| D030 | Norm drift | Expectations change through repeated behavior and shifting membership. | Compare stated norms with actual practice. | Adaptation: [R-D030](#source-r-d030) |
| D031 | Network brokerage | Intermediaries connect groups that otherwise interact little. | Who controls access, interpretation, and introductions? | [R-D031](#source-r-d031) |
| D032 | Boundary maintenance | Communities negotiate membership and acceptable participation. | Can boundaries protect purpose without insulating power? | [R-D032](#source-r-d032) |

## 9. Research sources and provenance

Codes link inventory entries to research trails. A source may describe a practice without testing its effectiveness. The candidate label C intentionally leaves gaps visible rather than attaching loosely related citations. Access levels are recorded explicitly. Entries supported only by abstracts or search excerpts remain introductory; deeper claims require full-text review.

<a id="source-gft"></a>
**GFT — Samo Burja, Great Founder Theory (2020 manuscript).** User-supplied PDF, read as extracted text. Original page outlines retain chapter and page references. [Author's manuscript page](https://samoburja.com/gft/). Theory and historical argument; illustrative applications here are editorial.

<a id="source-ext"></a>
**EXT — Extitutional theory.** [Project's explanation](https://extitutions.org/about); [Schingler and De Filippi's introduction](https://medium.com/berkman-klein-center/an-introduction-to-extitutional-theory-e74b5a49ea53); [De Filippi and Santolini paper abstract](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4001721). The full paper was not accessible in this research pass; claims here are limited to the introduction and abstract. Do not portray extitutions as inherently egalitarian or as the opposite of institutions.

<a id="source-sn-d"></a>
**SN-D — Supernuclear, [Group Decision Making in Coliving](https://supernuclear.substack.com/p/group-decision-making-in-coliving).** Practitioner comparison of authority and agreement requirements. Detailed definitions of decision rules need their own references.

<a id="source-sn-p"></a>
**SN-P — Supernuclear, [Rules vs. Principles](https://supernuclear.substack.com/p/rules-vs-principles).** Practitioner discussion of principles, initiative, and shared living.

<a id="source-sn-s"></a>
**SN-S — Supernuclear, [Stoop Coffee](https://supernuclear.substack.com/p/stoop-coffee-how-a-simple-idea-transformed).** A recurring neighborhood gathering and relationship-building account.

<a id="source-sn-c"></a>
**SN-C — Supernuclear, [11 Strategies for Keeping Your Coliving Space Clean](https://supernuclear.substack.com/p/11-strategies-for-keeping-your-coliving).** Household experiments concerning objects, chores, and recognition.

<a id="source-sn-w"></a>
**SN-W — Supernuclear, [Why It's Worth Having a Community Wiki](https://supernuclear.substack.com/p/why-its-worth-having-a-community).** Documentation and onboarding practices; distinguish public information from private resident records.

<a id="source-sn-l"></a>
**SN-L — Supernuclear, [How to Host Lightning Talks](https://supernuclear.substack.com/p/how-to-host-lightning-talks).** Practical hosting account.

<a id="source-bsc"></a>
**BSC — Ryan Fleury, [The Magic of the Better Software Conference](https://www.dgtlgrove.com/p/the-magic-of-the-better-software), January 2026.** First-person account of a 2025 event. The inventory abstracts event-design possibilities; the article does not establish a universal law of inevitable institutional decline.

<a id="source-cop"></a>
**COP — Wenger-Trayner, [Introduction to communities of practice](https://www.wenger-trayner.com/wp-content/uploads/2022/01/07-Brief-introduction-to-communities-of-practice.pdf), and [forms of participation](https://blogarchive.wenger-trayner.com/2011/12/29/slide-forms-of-participation/).** Conceptual resources on shared practice and varying involvement.

<a id="source-s3"></a>
**S3 — [Sociocracy 3.0 pattern index](https://patterns.sociocracy30.org/pattern-index.html).** Practitioner collection. Links to individual patterns are the next source layer for page drafting; preserve distinctions between consent, voting, and consensus. Pattern names and brief summaries here are discovery aids, not a reproduction of the guide.

<a id="source-ls"></a>
**LS — [Liberating Structures menu](https://www.liberatingstructures.com/ls-menu-1).** Named facilitation methods. Consult the individual protocols for steps, timing, and attribution before publishing instructions. The live menu includes additions beyond the original repertoire.

<a id="source-wc"></a>
**WC — [The World Café method](https://theworldcafe.com/key-concepts-resources/world-cafe-method/).** Originating community's description of rotating small-group dialogue and shared harvesting.

<a id="source-os"></a>
**OS — Open Space World, [brief user's guide](https://openspaceworld.org/wp2/hho/papers/brief-users-guide-open-space-technology/).** Participant-generated agendas and freedom to move between sessions.

<a id="source-adv"></a>
**ADV — Reinventing Organizations Wiki, [decision making](https://reinventingorganizationswiki.com/en/theory/decision-making/).** Practitioner description of the advice process. Using the process does not require accepting the site's broader developmental theory.

<a id="source-ietf"></a>
**IETF — [RFC 7282: On Consensus and Humming in the IETF](https://datatracker.ietf.org/doc/html/rfc7282).** Explains why rough consensus concerns substantive issues rather than simple vote counting.

<a id="source-oss"></a>
**OSS — [Open Source Guides: Leadership and Governance](https://opensource.guide/leadership-and-governance/).** Contributor roles and governance models. Roles and actual powers vary by project.

<a id="source-osi"></a>
**OSI — [Open Source Definition](https://opensource.org/osd).** Primary definition of software licensing requirements. Open-source licensing alone does not entail participatory project governance. Open licensing beyond software needs domain-specific references.

<a id="source-py"></a>
**PY — [Python PEP 13](https://peps.python.org/pep-0013/).** Primary governance specification. Python is a steering-council example; its BDFL era is historical.

<a id="source-oecd"></a>
**OECD — [Innovative Citizen Participation and New Democratic Institutions](https://www.oecd.org/en/publications/2020/06/innovative-citizen-participation-and-new-democratic-institutions_11aa2baf.html), and [Guidelines for Citizen Participation Processes](https://doi.org/10.1787/f765caf6-en).** Comparative models and participation guidance. Recruitment, authority, and decision rules must be specified separately.

<a id="source-pb"></a>
**PB — [Participatory Budgeting Project](https://www.participatorybudgeting.org/), with its [implementation handbook](https://pbhandbook.participatorybudgeting.org/).** Practitioner resources on community involvement in public budget allocation.

<a id="source-econ"></a>
**ECON — IMF, [What Is Capitalism?](https://www.imf.org/en/publications/fandd/issues/series/back-to-basics/capitalism).** Introductory economic account, useful for separating markets from the wider system. Broader comparisons require additional perspectives.

<a id="source-haier"></a>
**HAIER — London Business School, [The Haier Cases (C)](https://publishing.london.edu/cases/the-haier-cases-c/).** Published case overview concerning Haier's internal microenterprises. Only the public overview was used, not the full teaching case; avoid unsupported performance claims.

<a id="source-ica"></a>
**ICA — International Cooperative Alliance, [cooperative identity, values and principles](https://www.ica.coop/en/cooperatives/cooperative-identity/).** Supports the shared ownership and democratic-control baseline. Individual cooperative forms need more detailed case sources.

<a id="source-ost"></a>
**OST — Elinor Ostrom, [Nobel lecture landing page](https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/lecture/) and [interview on commons research](https://www.nobelprize.org/prizes/economic-sciences/2009/ostrom/164465-ostrom-williamson-interview-transcript/).** The interview emphasizes contextual variation. The lecture PDF could not be fetched; the decomposed commons patterns remain research leads, not a fully verified summary of that lecture.

<a id="source-clt"></a>
**CLT — Community Land Trust Network, [What is a Community Land Trust?](https://www.communitylandtrusts.org.uk/about-clts/what-is-a-community-land-trust-clt/).** Practitioner definition and related community-led housing forms. Specific legal arrangements vary by jurisdiction.

<a id="source-time"></a>
**TIME — [TimeBanks.org](https://www.timebanks.org/).** Practitioner network and discovery source; detailed accounting, reciprocity, and governance rules require a specific timebank's documentation.

<a id="source-rjc"></a>
**RJC — Restorative Justice Council, [what restorative justice is](https://restorativejustice.org.uk/what-restorative-justice) and [principles of restorative practice](https://restorativejustice.org.uk/sites/default/files/resources/files/Principles%20of%20restorative%20practice%20-%20FINAL%2012.11.15.pdf).** Voluntary participation, preparation, and participant safety are integral, not optional add-ons.

<a id="source-arc"></a>
**ARC — International Council on Archives, [What are archives?](https://www.ica.org/discover-archives/what-are-archives/).** Records, provenance, context, and interpretation.

<a id="source-freeman"></a>
**FREEMAN — Jo Freeman, [The Tyranny of Structurelessness](https://www.jofreeman.com/joreen/tyranny.htm).** Analysis of informal power and accountability; an argument to examine, not a guarantee that formal structure solves exclusion.

<a id="source-embed"></a>
**EMBED — Mark Granovetter, [Economic Action and Social Structure: The Problem of Embeddedness](https://sociology.stanford.edu/publications/economic-action-and-social-structure-problem-embeddedness).** Research publication record and abstract.

<a id="source-ties"></a>
**TIES — Mark Granovetter, [The Strength of Weak Ties](https://sociology.stanford.edu/publications/strength-weak-ties).** Research publication record and abstract; avoid interpreting every weak tie as a useful bridge.

<a id="source-stig"></a>
**STIG — [Stigmergy in Open Collaboration](https://www.tandfonline.com/doi/full/10.1080/07421222.2023.2229119).** Research on coordination through shared artifacts; abstract/excerpts used, not a full evidence review.

<a id="source-ilo"></a>
**ILO — International Labour Organization, [What is collective bargaining?](https://www.ilo.org/resource/what-collective-bargaining) and [business and collective bargaining](https://www.ilo.org/resource/other/ilo-helpdesk-business-and-collective-bargaining).** Institutional definitions of worker representation and negotiated employment conditions. The entries explain mechanisms, not jurisdiction-specific legal advice.

<a id="source-ilo-a"></a>
**ILO-A — [Quality Apprenticeships Recommendation, 2023 (No. 208)](https://www.ilo.org/resource/other/ilc/111/recommendation-concerning-quality-apprenticeships) and [policymaker guide](https://www.ilo.org/publications/guide-policymakers-quality-apprenticeships-recommendation-2023-no-208).** Adds a contemporary institutional definition to the broader historical concept: structured learning, agreed responsibilities, compensation, and recognized qualifications.

<a id="source-seeds"></a>
**SEEDS — Seeds for Change, [Consensus Decision Making](https://www.seedsforchange.org.uk/consensus).** Practitioner guide distinguishing support, reservations, standing aside, and blocking. Different groups adopt different rules; consensus is not automatically identical to unanimity.

<a id="source-dem"></a>
**DEM — UK Parliament, [Referendum](https://www.parliament.uk/site-information/glossary/referendum/) and [How it works: Types of Democracy](https://www.parliament.uk/globalassets/about-parliament/how-parliament-works/accessible-resources/how-it-works-e-text-accessible.pdf).** Institutional explanations of direct and representative decision-making. Assembly democracy is an editorial navigation category for the convened, collectively authoritative arrangement; it is not presented as a third mutually exclusive constitutional type.

<a id="source-ath"></a>
**ATH — [Democracy and Participation in Athens](https://www.cambridge.org/core/books/democracy-and-participation-in-athens/087DFD98C944977C46BD9416AED9BA3E/listing); [From the Whole Citizen Body? The Sociology of Election and Lot in the Athenian Democracy](https://www.ascsa.edu.gr/uploads/media/hesperia/25068022.pdf); and [UK Parliament research briefing, introductory democracy discussion](https://researchbriefings.files.parliament.uk/documents/RP14-25/RP14-25.pdf).** Public summaries and indexed excerpts used for this outline, not a full reading of the book or papers. Full historical pages need period-specific primary passages and scholarship, especially for eligibility, attendance, and the distribution of authority.

<a id="source-nih-m"></a>
**NIH-M — NIH Office of Intramural Research, [Guidelines for Mentors at NIH](https://oir.nih.gov/sourcebook/mentoring-training/guidelines-mentors-nih).** Institutional guidance on regular interaction, feedback, development, and introductions. Organizational applications outside research are illustrative adaptations, not evaluated outcomes.

<a id="source-arist"></a>
**ARIST — Stanford Encyclopedia of Philosophy, [Aristotle’s Political Theory](https://plato.stanford.edu/entries/aristotle-politics/).** Explains the classical distinction between rule by a few for the common advantage and rule for their own advantage. Historical institutions and modern uses of the term require contextual distinctions.

<a id="source-merit"></a>
**MERIT — Stanford Encyclopedia of Philosophy, [Meritocracy](https://plato.stanford.edu/entries/meritocracy/) and [Equality of Opportunity](https://plato.stanford.edu/entries/equal-opportunity/).** Discusses merit as a principle of allocation, its relationship to opportunity, and competing interpretations.

### Further collections to mine

- [Supernuclear directory](https://supernuclear.substack.com/p/the-supernuclear-directory-9a9078a07258): shared living, financing, ownership, governance, rituals, and maintenance.
- [Group Works patterns by category](https://groupworksdeck.org/patterns_by_category): an additional vocabulary for facilitation, context, relationship, and group process. Many are design qualities rather than independent techniques, so avoid mechanically turning every card into a technology page.
- [Participedia](https://participedia.net/): participation methods and documented cases; useful for separating a named method from its implementation in a specific place.
- [Liberating Voices / Public Sphere Project](https://labs.publicsphereproject.org/): civic communication and collective action patterns.
- [ILO explanation of collective bargaining](https://www.ilo.org/resource/what-collective-bargaining): primary institutional starting point for worker representation and negotiated employment conditions.


<!-- research-sources-start -->

<a id="source-r-d014"></a>
**R-D014 — Homophily.** [Birds of a feather: Homophily in social networks](https://scholars.duke.edu/publication/652661) — McPherson, Smith-Lovin and Cook / Annual Review of Sociology. research review; access: abstract reviewed.


<a id="source-r-d015"></a>
**R-D015 — Reciprocity.** [Evolution of indirect reciprocity](https://pubmed.ncbi.nlm.nih.gov/16251955/) — Nowak and Sigmund / Nature. research review; access: abstract in search results.


<a id="source-r-d016"></a>
**R-D016 — Trust formation and repair.** [Removing the Shadow of Suspicion: The Effects of Apology Versus Denial for Repairing Competence- Versus Integrity-Based Trust Violations](https://ink.library.smu.edu.sg/lkcsb_research/2368/) — Kim, Ferrin, Cooper and Dirks / Journal of Applied Psychology. research paper; access: abstract reviewed. [An Integrative Model of Organizational Trust](https://journals.aom.org/doi/10.5465/amr.1995.9508080335) — Mayer, Davis and Schoorman / Academy of Management Review. theoretical research paper; access: search excerpt.


<a id="source-r-d017"></a>
**R-D017 — Free riding.** [Cooperation and Punishment in Public Goods Experiments](https://ideas.repec.org/a/aea/aecrev/v90y2000i4p980-994.html) — Fehr and Gächter / American Economic Review; RePEc abstract. research paper; access: abstract reviewed.


<a id="source-r-d018"></a>
**R-D018 — Social loafing.** [Many Hands Make Light the Work: The Causes and Consequences of Social Loafing](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Group_Dynamics/Latane_et_al_1979_Many_hands_make_light_the_work.pdf) — Latané, Williams and Harkins / Journal of Personality and Social Psychology. research paper; access: PDF sections reviewed.


<a id="source-r-d019"></a>
**R-D019 — Volunteer burnout.** [Why People Leave Community Service Organizations: A Mixed Methods Study](https://doi.org/10.1007/s11266-018-0005-z) — Milbourn, Black and Buchanan / Voluntas. research paper; access: abstract reviewed.


<a id="source-r-d020"></a>
**R-D020 — Status hierarchies.** [Striving for superiority: The human desire for status](https://irle.berkeley.edu/publications/working-papers/striving-for-superiority-the-human-desire-for-status/) — Anderson and Hildreth / UC Berkeley IRLE. research working paper; access: abstract reviewed.


<a id="source-r-d021"></a>
**R-D021 — Preference falsification.** [Rationally Speaking 198: Timur Kuran on Private Truths and Public Lies](https://sites.duke.edu/timurkuran/files/2018/03/rs198transcript-Kuran-Rationall-Speaking-2017.pdf) — Timur Kuran / Rationally Speaking; Duke author archive. author interview; access: PDF sections reviewed.


<a id="source-r-d022"></a>
**R-D022 — Pluralistic ignorance.** [Pluralistic Ignorance and Alcohol Use on Campus: Some Consequences of Misperceiving the Social Norm](https://collaborate.princeton.edu/en/publications/pluralistic-ignorance-and-alcohol-use-on-campus-some-consequences/) — Prentice and Miller / Journal of Personality and Social Psychology. research paper; access: abstract in search results.


<a id="source-r-d023"></a>
**R-D023 — Group polarization.** [On a Danger of Deliberative Democracy](https://hls.harvard.edu/bibliography/on-a-danger-of-deliberative-democracy/) — Cass Sunstein / Harvard Law School bibliography. research paper; access: abstract in search results.


<a id="source-r-d024"></a>
**R-D024 — Groupthink.** [Revisiting the Bay of Pigs and Vietnam Decisions 25 Years Later: How Well Has the Groupthink Hypothesis Stood the Test of Time?](https://pubmed.ncbi.nlm.nih.gov/9705804/) — Kramer / Organizational Behavior and Human Decision Processes. research paper; access: abstract in search results.


<a id="source-r-d025"></a>
**R-D025 — Goal displacement.** [Bureaucratic Structure and Personality](https://www.d.umn.edu/cla/faculty/jhamlin/4111/Merton/Social%20Theory%20and%20Social%20Structure%20Bureaucratic%20Structure%20a.htm) — Robert K. Merton; University of Minnesota Duluth teaching archive. theoretical research essay; access: page reviewed.


<a id="source-r-d026"></a>
**R-D026 — Metric gaming.** [Categorizing Variants of Goodhart’s Law](https://arxiv.org/abs/1803.04585) — Manheim and Garrabrant / arXiv. theoretical preprint; access: abstract reviewed.


<a id="source-r-d027"></a>
**R-D027 — Capture.** [The Theory of Economic Regulation](https://www.rasmusen.org/zg601/readings/Stigler.1971.pdf) — George Stigler / Bell Journal of Economics and Management Science. theoretical research paper; access: PDF search excerpt.


<a id="source-r-d028"></a>
**R-D028 — Principal-agent problems.** [Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure](https://doi.org/10.1016/0304-405X%2876%2990026-X) — Jensen and Meckling / Journal of Financial Economics. theoretical research paper; access: abstract and primary-paper search excerpt.


<a id="source-r-d029"></a>
**R-D029 — Path dependence.** [Competing Technologies, Increasing Returns, and Lock-In by Historical Events](https://ideas.repec.org/a/ecj/econjl/v99y1989i394p116-31.html) — W. Brian Arthur / Economic Journal; RePEc abstract. theoretical research paper; access: abstract in search results.


<a id="source-r-d030"></a>
**R-D030 — Norm drift.** [The spontaneous emergence of conventions: An experimental study of cultural evolution](https://pmc.ncbi.nlm.nih.gov/articles/PMC4343158/) — Centola and Baronchelli / PNAS. research paper; access: abstract and article sections reviewed.


<a id="source-r-d031"></a>
**R-D031 — Network brokerage.** [Structural Holes and Good Ideas](https://doi.org/10.1086/421787) — Ronald Burt / American Journal of Sociology. research paper; access: abstract in search results.


<a id="source-r-d032"></a>
**R-D032 — Boundary maintenance.** [The Study of Boundaries in the Social Sciences](https://www.annualreviews.org/content/journals/10.1146/annurev.soc.28.110601.141107) — Lamont and Molnár / Annual Review of Sociology. research review; access: abstract reviewed.


<a id="source-r-s002"></a>
**R-S002 — Socialism.** [Socialism](https://plato.stanford.edu/entries/socialism/) — Stanford Encyclopedia of Philosophy. reference; access: page sections reviewed.


<a id="source-r-s003"></a>
**R-S003 — Economic planning.** [Socialism, section 4.1: Central and Participatory Planning](https://plato.stanford.edu/entries/socialism/#CentPartPlan) — Stanford Encyclopedia of Philosophy. reference; access: page section reviewed.


<a id="source-r-s007"></a>
**R-S007 — Technocracy.** [Expert Knowledge in Democracies: Promises, Limits, and Conflict](https://doi.org/10.1146/annurev-polisci-033123-020420) — Annual Review of Political Science. research review; access: search excerpt.


<a id="source-r-s008"></a>
**R-S008 — Monarchy.** [The role of the Monarchy](https://www.royal.uk/the-role-of-the-monarchy) — The Royal Household. institutional account; access: page reviewed.


<a id="source-r-s028"></a>
**R-S028 — Polycentric governance.** [A Polycentric Approach for Coping with Climate Change](https://dlc.dlib.indiana.edu/dlc/items/ce7cf738-5200-46b4-8376-921914080e19) — Elinor Ostrom / World Bank; Indiana University repository. research working paper; access: abstract reviewed.


<a id="source-r-t003"></a>
**R-T003 — Peer learning circles.** [Facilitating Peer Learning](https://docs.p2pu.org/facilitation/facilitation-basics) — Peer 2 Peer University. practitioner method; access: search excerpt.


<a id="source-r-t005"></a>
**R-T005 — Study groups.** [Supporting Student Well-Being with Peer-Led Study Groups](https://teaching.cornell.edu/teaching-spotlight/provosts-working-group-innovation-assessment/supporting-student-well-being-peer) — Cornell University. institutional guide; access: search excerpt.


<a id="source-r-t006"></a>
**R-T006 — Journal clubs.** [Journal Club Leader Toolkit 2024](https://www.training.nih.gov/documents/31/Journal_Club_Leader_Toolkit_2024_508checked.pdf) — National Institutes of Health. institutional guide; access: search excerpt.


<a id="source-r-t007"></a>
**R-T007 — Socratic seminars.** [Socratic Seminars](https://www.readwritethink.org/professional-development/strategy-guides/socratic-seminars) — ReadWriteThink / NCTE. institutional guide; access: search excerpt.


<a id="source-r-t008"></a>
**R-T008 — Teach-back.** [Teach-back](https://www.ahrq.gov/patient-safety/reports/engage/interventions/teachback.html) — Agency for Healthcare Research and Quality. institutional guide; access: search excerpt.


<a id="source-r-t009"></a>
**R-T009 — Peer instruction.** [Incorporating Short Peer Discussion Activities for In-Class Collaborative Learning](https://teaching.cornell.edu/teaching-resources/active-collaborative-learning/collaborative-learning/incorporating-short-peer) — Cornell University. institutional guide; access: page.


<a id="source-r-t010"></a>
**R-T010 — Deliberate practice with feedback.** [The Role of Deliberate Practice in the Acquisition of Expert Performance](https://blogs.ischool.berkeley.edu/i225s14/files/2014/04/Ericsson-1993-article.pdf) — Psychological Review / Ericsson, Krampe and Tesch-Römer. research paper; access: search excerpt.


<a id="source-r-t011"></a>
**R-T011 — Job shadowing.** [Federal Leadership Development Programs: Shadowing Assignments](https://www.opm.gov/policy-data-oversight/training-and-development/federal-leadership-development-programs/) — US Office of Personnel Management. institutional guide; access: search excerpt.


<a id="source-r-t012"></a>
**R-T012 — Job rotation.** [Federal Supervisory and Managerial Frameworks and Guidance](https://www.opm.gov/policy-data-oversight/training-and-development/training-program-management/federal-supervisory-and-managerial-frameworks-and-guidance.pdf) — US Office of Personnel Management. institutional guide; access: search excerpt.


<a id="source-r-t013"></a>
**R-T013 — Cross-training.** [Creating Patient-Centered Team-Based Primary Care](https://ce.effectivehealthcare.ahrq.gov/sites/default/files/wysiwyg/ncepcr/tools/PCMH/creating-patient-centered-team-based-primary-care-white-paper.pdf) — Agency for Healthcare Research and Quality. institutional guide; access: search excerpt.


<a id="source-r-t014"></a>
**R-T014 — Office hours.** [Universal Design for Learning: Office Hours](https://teaching.cornell.edu/teaching-resources/inclusion-belonging-accessibility/universal-design-learning) — Cornell University. institutional guide; access: search excerpt.


<a id="source-r-t015"></a>
**R-T015 — Ask-me-anything sessions.** [New Ways To AMA](https://redditinc.com/news/new-ways-to-ama?version=published) — Reddit. practitioner method; access: search excerpt.


<a id="source-r-t017"></a>
**R-T017 — Show-and-tell sessions.** [Agile Tools and Techniques](https://www.gov.uk/service-manual/agile-delivery/agile-tools-techniques) — UK Government Digital Service. institutional guide; access: search excerpt.


<a id="source-r-t018"></a>
**R-T018 — Workshops.** [Instructors Handbook](https://docs.carpentries.org/handbooks/instructors.html) — The Carpentries. institutional guide; access: page.


<a id="source-r-t019"></a>
**R-T019 — Train-the-trainer.** [Understanding the Training of Trainers Model](https://www.cdc.gov/healthy-schools-training/php/tot/) — US Centers for Disease Control and Prevention. institutional guide; access: search excerpt.


<a id="source-r-t020"></a>
**R-T020 — Learning cohorts.** [Cohort Faculty Development](https://cte.tamu.edu/programming/cohorts-faculty-dev.html) — Texas A&M University. institutional guide; access: search excerpt.


<a id="source-r-t021"></a>
**R-T021 — Reading salons.** [Shared Reading FAQs](https://www.thereader.org.uk/shared-reading/shared-reading-faqs/) — The Reader. practitioner method; access: page.


<a id="source-r-t022"></a>
**R-T022 — Oral history.** [Oral History Best Practices](https://oralhistory.org/wp-content/uploads/2025/12/2025-OHA-PrinciplesBP_Best-Practices.pdf) — Oral History Association. institutional guide; access: search excerpt.


<a id="source-r-t023"></a>
**R-T023 — Storytelling.** [Storytelling: Story Dialogue Technique](https://www.betterevaluation.org/sites/default/files/Toolkit_2014.pdf) — BetterEvaluation (hosted toolkit). practitioner method; access: search excerpt.


<a id="source-r-t024"></a>
**R-T024 — Case-method discussion.** [Teaching by the Case Method](https://www.hbs.edu/teaching/case-method) — Harvard Business School. institutional guide; access: search excerpt.


<a id="source-r-t025"></a>
**R-T025 — Simulation exercises.** [WHO Simulation Exercise Manual](https://www.who.int/publications/i/item/WHO-WHE-CPI-2017.10) — World Health Organization. institutional guide; access: search excerpt.


<a id="source-r-t026"></a>
**R-T026 — After-action reviews.** [Guidance for After Action Review](https://www.who.int/publications/i/item/WHO-WHE-CPI-2019.4) — World Health Organization. institutional guide; access: search excerpt.


<a id="source-r-t028"></a>
**R-T028 — Peer review of work.** [Peer Assessment](https://teaching.cornell.edu/teaching-resources/assessing-student-learning/peer-assessment) — Cornell University. institutional guide; access: search excerpt.


<a id="source-r-t029"></a>
**R-T029 — Replication.** [Transparency and Openness Promotion Guidelines](https://www.cos.io/initiatives/top-guidelines) — Center for Open Science. institutional guide; access: search excerpt.


<a id="source-r-t030"></a>
**R-T030 — Preregistration.** [Preregistration](https://www.cos.io/initiatives/prereg) — Center for Open Science. institutional guide; access: search excerpt.


<a id="source-r-t031"></a>
**R-T031 — Open notebooks.** [Jean-Claude Bradley: Open Notebook Science](https://istcolloq.gsfc.nasa.gov/jean-claude-bradley/) — NASA Goddard Space Flight Center. research paper; access: abstract.


<a id="source-r-t035"></a>
**R-T035 — Knowledge maps.** [Understanding Knowledge Mapping](https://www.apqc.org/resource-library/resource/understanding-knowledge-mapping-0) — APQC. institutional guide; access: search excerpt.


<a id="source-r-t036"></a>
**R-T036 — Expert directories.** [Understanding Expertise Location](https://www.apqc.org/resource-library/resource/understanding-expertise-location-0) — APQC. institutional guide; access: search excerpt.


<a id="source-r-t037"></a>
**R-T037 — Open educational resources.** [Open Educational Resources](https://www.unesco.org/en/open-educational-resources?hub=370) — UNESCO. institutional guide; access: search excerpt.


<a id="source-r-t038"></a>
**R-T038 — Translation networks.** [Join the TWB Community](https://translatorswithoutborders.org/join-the-twb-community/) — Translators without Borders. practitioner method; access: search excerpt.


<a id="source-r-t039"></a>
**R-T039 — Libraries.** [IFLA-UNESCO Public Library Manifesto](https://www.ifla.org/public-library-manifesto/) — International Federation of Library Associations and Institutions / UNESCO. institutional guide; access: search excerpt.


<a id="source-r-t044"></a>
**R-T044 — Fishbowl discussion.** [Communities Care: Training Facilitators](https://www.unicef.org/media/103896/file/Communities-Care-Part-4-Facilitating-Community-Discussions-Training-Facilitators-Manual-2021.pdf) — UNICEF. institutional guide; access: search excerpt.


<a id="source-r-t047"></a>
**R-T047 — Unconferences.** [Unconferencing: How to Prepare to Attend an Unconference](https://unconference.net/unconferencing-how-to-prepare-to-attend-an-unconference-2/) — Unconference.net / Kaliya. practitioner method; access: search excerpt.


<a id="source-r-t048"></a>
**R-T048 — Delphi process.** [Methodological Guidance for Conducting and Critically Appraising Delphi Panels](https://www.rand.org/content/dam/rand/pubs/tools/TLA3000/TLA3082-1/RAND_TLA3082-1.pdf) — RAND. institutional guide; access: search excerpt.


<a id="source-r-t049"></a>
**R-T049 — Red teams.** [A Guide to Red Teaming](https://www.gov.uk/government/publications/a-guide-to-red-teaming) — UK Ministry of Defence. institutional guide; access: search excerpt.


<a id="source-r-t050"></a>
**R-T050 — Premortems.** [Premortem](https://www.gary-klein.com/premortem) — Gary Klein. practitioner method; access: search excerpt.


<a id="source-r-t053"></a>
**R-T053 — Potlucks.** [Food Safety and Service: Hosting a Potluck](https://4-h-volunteer.extension.umn.edu/keep-youth-safe/policies-practices/food) — University of Minnesota Extension. institutional guide; access: search excerpt.


<a id="source-r-t057"></a>
**R-T057 — Hospitality hosting.** [Information for Hosts](https://servas.org/information-hosts) — Servas International. practitioner method; access: search excerpt.


<a id="source-r-t058"></a>
**R-T058 — Buddy systems.** [Planning an Induction Programme](https://www.acas.org.uk/inductions/planning-an-induction-programme) — Acas. institutional guide; access: search excerpt.


<a id="source-r-t061"></a>
**R-T061 — Trial membership.** [Apple Tree House: How to Join](https://www.ic.org/directory/community/apple-tree-house/) — Foundation for Intentional Community / Apple Tree House. practitioner method; access: search excerpt.


<a id="source-r-t062"></a>
**R-T062 — Introductions by a connector.** [Organizing for Effective Advocacy: Introductions](https://ctb.ku.edu/en/book/export/html/994) — University of Kansas Community Tool Box. institutional guide; access: search excerpt.


<a id="source-r-t064"></a>
**R-T064 — Listening pairs.** [Active Listening](https://www.seedsforchange.org.uk/downloads/activelistening.pdf) — Seeds for Change. practitioner method; access: search excerpt.


<a id="source-r-t065"></a>
**R-T065 — Mutual aid networks.** [Solidarity Not Charity: Mutual Aid for Mobilization and Survival](https://www.deanspade.net/wp-content/uploads/2020/03/Mutual-Aid-Article-Social-Text-Final.pdf) — Dean Spade / Social Text. research paper; access: page.


<a id="source-r-t066"></a>
**R-T066 — Care circles.** [Circles of Support](https://cosam.org.au/wp-content/uploads/2018/11/Circles-of-Support-brochure-for-web.pdf) — Inclusion Melbourne / National Resource Centre for Circles of Support and Microboards. practitioner method; access: page.


<a id="source-r-t067"></a>
**R-T067 — Meal trains.** [Meal Train Sign-Up: How It Works](https://www.mealtrain.com/content/file/Meal-Train-sign-up.pdf) — Meal Train. practitioner method; access: search excerpt.


<a id="source-r-t068"></a>
**R-T068 — Childcare exchanges.** [Bringing Families Together: A Guide to Parent Cooperatives](https://cccd.coop/sites/default/files/resources/bft_1.pdf) — California Center for Cooperative Development. institutional guide; access: search excerpt.


<a id="source-r-t069"></a>
**R-T069 — Neighborhood associations.** [How to Organize a Neighborhood Association](https://www.orlando.gov/Our-Government/Get-Involved/iLead-Neighborhood-Leadership-Training/iLead-Guides/How-to-Organize-a-Neighborhood-Association) — City of Orlando. institutional guide; access: search excerpt.


<a id="source-r-t072"></a>
**R-T072 — Third places.** [Third Places, True Citizen Spaces](https://www.unesco.org/en/articles/third-places-true-citizen-spaces) — UNESCO / Ray Oldenburg and Karen Christensen. reference; access: search excerpt.


<a id="source-r-t073"></a>
**R-T073 — Clubs.** [Writing Bylaws: Membership](https://ctb.ku.edu/en/table-of-contents/structure/organizational-structure/write-bylaws/main) — University of Kansas Community Tool Box. institutional guide; access: search excerpt.


<a id="source-r-t074"></a>
**R-T074 — Affinity groups.** [Affinity Groups](https://seedsforchange.org.uk/affinitygroups) — Seeds for Change. practitioner method; access: search excerpt.


<a id="source-r-t075"></a>
**R-T075 — Alumni networks.** [Harvard Alumni Association Shared Interest Group FAQ](https://www.alumni.harvard.edu/sites/default/files/page/content/HAA%20SIG%20FAQ%202023_July.pdf) — Harvard Alumni Association. institutional guide; access: search excerpt.


<a id="source-r-t076"></a>
**R-T076 — Festival cycles.** [Maltese Village Festa, an Annual Community Celebration](https://ich.unesco.org/en/RL/maltese-village-festa-an-annual-community-celebration-01871) — UNESCO Intangible Cultural Heritage. history; access: search excerpt.


<a id="source-r-t077"></a>
**R-T077 — Rites of passage.** [Rituals of Transition and Conformity](https://openstax.org/books/introduction-anthropology/pages/13-4-rituals-of-transition-and-conformity) — OpenStax. reference; access: page.


<a id="source-r-t078"></a>
**R-T078 — Welcoming ceremonies.** [Naturalization: What to Expect](https://my.uscis.gov/citizenship/what_to_expect) — US Citizenship and Immigration Services. institutional guide; access: page.


<a id="source-r-t079"></a>
**R-T079 — Farewell rituals.** [Celebrating Good-Bye: Functional Components in Farewell Parties for Retiring Employees in Israel](https://cris.tau.ac.il/en/publications/celebrating-good-bye-functional-components-in-farewell-parties-fo/) — Tel Aviv University research portal. research paper; access: abstract.


<a id="source-r-t080"></a>
**R-T080 — Commemorations.** [About the War Memorials Register](https://memorials.iwm.org.uk/about-wmr) — Imperial War Museums. history; access: search excerpt.


<a id="source-r-t081"></a>
**R-T081 — Shared symbols.** [Symbolic and Sacred Space](https://openstax.org/books/introduction-anthropology/pages/13-2-symbolic-and-sacred-space) — OpenStax. reference; access: search excerpt.


<a id="source-r-t082"></a>
**R-T082 — Origin stories.** [Narrative Memory Work of Employees in Family Businesses: How Founding Stories Shape Organizational Identification](https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/27095/Baluch_2023_FBR_Narrativememory_AAM.pdf?sequence=1) — Family Business Review / Hoon, Brinkmann and Baluch; accepted manuscript at University of St Andrews. research paper; access: page.


<a id="source-r-t083"></a>
**R-T083 — Community agreements.** [A Consensus Handbook: Drawing Up a Group Agreement](https://www.seedsforchange.org.uk/downloads/handbookweb.pdf) — Seeds for Change. practitioner method; access: search excerpt.


<a id="source-r-t084"></a>
**R-T084 — Codes of conduct.** [Adopt Contributor Covenant](https://www.contributor-covenant.org/adopt/) — Contributor Covenant. practitioner method; access: search excerpt.


<a id="source-r-t086"></a>
**R-T086 — Mediation.** [How Acas Mediators Work](https://www.acas.org.uk/acas-mediation-support/how-acas-mediators-work) — Acas. institutional guide; access: search excerpt.


<a id="source-r-t088"></a>
**R-T088 — Conflict coaching.** [Conflict Coaching](https://ombuds.columbia.edu/content/conflict-coaching) — Columbia University Ombuds Office. institutional guide; access: search excerpt.


<a id="source-r-t089"></a>
**R-T089 — Repair conversations.** [Restorative Questions](https://www.iirp.edu/images/2024/K12_Resources/IIRP_Restorative_Questions.pdf) — International Institute for Restorative Practices. practitioner method; access: page.


<a id="source-r-t090"></a>
**R-T090 — Community moderation.** [Discourse Moderation Guide: Managing Content](https://meta.discourse.org/t/discourse-moderation-guide-part-3-managing-content/406266?tl=en) — Discourse. practitioner method; access: search excerpt.


<a id="source-r-t091"></a>
**R-T091 — Guest policies.** [Common House Use Handbook](https://www.cohousing.org/wp-content/uploads/2021/05/Common-House-Use-Handbook-edit-11-15-2018.pdf) — Cohousing Association of the United States (hosted community handbook). practitioner method; access: search excerpt.


<a id="source-r-t092"></a>
**R-T092 — Chore rotations.** [Irish House: Community Expectations](https://www.ic.org/directory/community/irish-house/) — Foundation for Intentional Community / Irish House. practitioner method; access: search excerpt.


<a id="source-r-t095"></a>
**R-T095 — Participation stipends.** [Citizens’ Assembly Frequently Asked Questions: Northern Ireland Edition](https://www.involve.org.uk/resource/frequently-asked-questions-citizens-assembly-ni-edition) — Involve. institutional guide; access: search excerpt.


<a id="source-r-t096"></a>
**R-T096 — Accessibility arrangements.** [Making Events Accessible](https://www.w3.org/WAI/teach-advocate/accessible-presentations/) — World Wide Web Consortium Web Accessibility Initiative. institutional guide; access: search excerpt.


<a id="source-r-t097"></a>
**R-T097 — Confidentiality agreements.** [Chatham House Rule](https://www.chathamhouse.org/about-us/chatham-house-rule) — Chatham House. practitioner method; access: page.


<a id="source-r-t098"></a>
**R-T098 — Cross-community exchanges.** [The Art of Knowledge Exchange: Study Tour](https://documents1.worldbank.org/curated/en/168121553671926460/pdf/The-Art-of-Knowledge-Exchange-A-Results-Focused-Planning-Guide-for-Climate-Change-Practitioners.pdf) — World Bank. institutional guide; access: search excerpt.


<a id="source-r-t099"></a>
**R-T099 — Peer support groups.** [Creating and Facilitating Peer Support Groups](https://ctb.ku.edu/en/table-of-contents/implement/enhancing-support/peer-support-groups/main) — University of Kansas Community Tool Box. institutional guide; access: page.


<a id="source-r-t104"></a>
**R-T104 — Town halls.** [Conducting Public Forums and Listening Sessions](https://ctb.ku.edu/en/table-of-contents/assessment/assessing-community-needs-and-resources/conduct-public-forums/main) — University of Kansas Community Tool Box. institutional guide; access: search excerpt.


<a id="source-r-t106"></a>
**R-T106 — Petitions.** [How petitions work](https://petition.parliament.uk/help) — UK Parliament. institutional guide; access: search excerpt.


<a id="source-r-t107"></a>
**R-T107 — Referendums.** [Referendum](https://www.parliament.uk/site-information/glossary/referendum/) — UK Parliament. reference; access: search excerpt.


<a id="source-r-t109"></a>
**R-T109 — Elections.** [Electoral Systems](https://aceproject.org/ero-en/misc/idea-2018international-obligations-for-elections) — International IDEA / ACE Electoral Knowledge Network. institutional guide; access: search excerpt.


<a id="source-r-t110"></a>
**R-T110 — Appointment.** [Governance Code on Public Appointments](https://www.gov.uk/government/publications/governance-code-for-public-appointments/governance-code-on-public-appointments-html) — UK Cabinet Office. institutional guide; access: search excerpt.


<a id="source-r-t112"></a>
**R-T112 — Term limits.** [Constitution Annotated: Twenty-Second Amendment](https://constitution.congress.gov/static/files/GPO-CONAN-2024-SUPP.pdf) — Library of Congress. reference; access: search excerpt.


<a id="source-r-t113"></a>
**R-T113 — Rotating chairmanship.** [The presidency of the Council of the EU](https://www.consilium.europa.eu/en/council-eu/presidency-council-eu/) — Council of the European Union. institutional guide; access: search excerpt.


<a id="source-r-t114"></a>
**R-T114 — Recall procedures.** [Recall of State Officials](https://www.ncsl.org/elections-and-campaigns/recall-of-state-officials) — National Conference of State Legislatures. reference; access: search excerpt.


<a id="source-r-t115"></a>
**R-T115 — Delegated authority.** [Domains and Delegation](https://patterns.sociocracy30.org/domain.html) — Sociocracy 3.0. practitioner method; access: search excerpt.


<a id="source-r-t116"></a>
**R-T116 — Subsidiarity.** [Principle of subsidiarity](https://eur-lex.europa.eu/EN/legal-content/glossary/principle-of-subsidiarity.html) — European Union EUR-Lex. reference; access: search excerpt.


<a id="source-r-t119"></a>
**R-T119 — Majority voting.** [Frequently Asked Questions](https://robertsrules.com/frequently-asked-questions/) — Robert's Rules Association. reference; access: search excerpt.


<a id="source-r-t120"></a>
**R-T120 — Plurality voting.** [First Past the Post](https://aceproject.org/ace-en/topics/es/ese/ese01/ese01a) — ACE Electoral Knowledge Network. institutional guide; access: search excerpt.


<a id="source-r-t121"></a>
**R-T121 — Supermajority voting.** [About Voting](https://www.senate.gov/about/powers-procedures/voting.htm) — United States Senate. reference; access: search excerpt.


<a id="source-r-t122"></a>
**R-T122 — Unanimity.** [How does the Council vote?](https://www.consilium.europa.eu/en/council-eu/how-does-the-council-vote/) — Council of the European Union. institutional guide; access: search excerpt.


<a id="source-r-t127"></a>
**R-T127 — Approval voting.** [What is Approval Voting?](https://electionscience.org/education/approval-voting) — Center for Election Science. practitioner method; access: search excerpt.


<a id="source-r-t128"></a>
**R-T128 — Ranked-choice voting.** [Ranked Choice Voting](https://portal.311.nyc.gov/article/?kanumber=KA-03692) — New York City 311. institutional guide; access: search excerpt.


<a id="source-r-t129"></a>
**R-T129 — Score voting.** [A proposal for British Columbia](https://rangevoting.org/BC2018.html) — Center for Range Voting. practitioner method; access: search excerpt.


<a id="source-r-t130"></a>
**R-T130 — Dot voting.** [Dot Voting](https://gamestorming.com/dot-voting/) — Gamestorming. practitioner method; access: search excerpt.


<a id="source-r-t131"></a>
**R-T131 — Quadratic voting.** [Quadratic Voting: How Mechanism Design Can Radicalize Democracy](https://www.aeaweb.org/articles?id=10.1257/pandp.20181002) — American Economic Association. research paper; access: abstract.


<a id="source-r-t132"></a>
**R-T132 — Liquid democracy.** [Power in Liquid Democracy: A Network Centrality Approach](https://arxiv.org/abs/2608.13188) — arXiv / Grossi and colleagues. research paper; access: abstract.


<a id="source-r-t133"></a>
**R-T133 — Proxy voting.** [Apply for a proxy vote](https://www.gov.uk/apply-proxy-vote) — UK Government. institutional guide; access: search excerpt.


<a id="source-r-t134"></a>
**R-T134 — Delegation poker.** [Delegation Poker](https://management30.com/practice/delegation-poker/) — Management 3.0. practitioner method; access: search excerpt.


<a id="source-r-t139"></a>
**R-T139 — Boards of trustees.** [The essential trustee](https://www.gov.uk/government/publications/the-essential-trustee-what-you-need-to-know-what-you-need-to-do-cc3/the-essential-trustee-what-you-need-to-know-what-you-need-to-do) — Charity Commission for England and Wales. institutional guide; access: search excerpt.


<a id="source-r-t140"></a>
**R-T140 — Worker councils.** [Greece: Actors and institutions](https://www.eurofound.europa.eu/en/countries/greece/actors-and-institutions) — Eurofound. reference; access: search excerpt.


<a id="source-r-t143"></a>
**R-T143 — Federations.** [What is Federalism?](https://www.forumfed.org/what-is-federalism/) — Forum of Federations. reference; access: search excerpt.


<a id="source-r-t144"></a>
**R-T144 — Confederations.** [Articles of Confederation (1777)](https://www.archives.gov/milestone-documents/articles-of-confederation) — United States National Archives. history; access: search excerpt.


<a id="source-r-t145"></a>
**R-T145 — Separation of powers.** [Understanding Federal Courts: The Basics](https://ord.uscourts.gov/index.php/court-info/about-the-judiciary) — US District Court for the District of Oregon. institutional guide; access: search excerpt.


<a id="source-r-t146"></a>
**R-T146 — Constitutions and charters.** [What is a Constitution? Principles and Concepts](https://www.idea.int/publications/catalogue/what-is-a-constitution) — International IDEA. institutional guide; access: search excerpt.


<a id="source-r-t148"></a>
**R-T148 — Quorum rules.** [Frequently Asked Questions](https://robertsrules.com/frequently-asked-questions/) — Robert's Rules Association. reference; access: search excerpt.


<a id="source-r-t149"></a>
**R-T149 — Agenda-setting procedures.** [Facilitating Meetings](https://seedsforchange.org.uk/downloads/facilitationmeeting.pdf) — Seeds for Change. practitioner method; access: search excerpt.


<a id="source-r-t150"></a>
**R-T150 — Speaking queues.** [Facilitation Tools for meetings and workshops](https://www.seedsforchange.org.uk/tools) — Seeds for Change. practitioner method; access: search excerpt.


<a id="source-r-t152"></a>
**R-T152 — Anonymous ballots.** [Secrecy of the Vote](https://aceproject.org/ace-es/topics/ei_new/eif/eif09/eif09a?set_language=en) — ACE Electoral Knowledge Network. institutional guide; access: search excerpt.


<a id="source-r-t153"></a>
**R-T153 — Conflict-of-interest disclosure.** [Identifying and managing conflicts of interest in a charity](https://www.gov.uk/government/publications/identifying-and-managing-conflicts-of-interest-in-a-charity-cc29) — Charity Commission for England and Wales. institutional guide; access: search excerpt.


<a id="source-r-t154"></a>
**R-T154 — Recusal.** [28 U.S. Code § 455: Disqualification of justice, judge, or magistrate judge](https://www.law.cornell.edu/uscode/text/28/455) — Cornell Legal Information Institute / US Code. reference; access: search excerpt.


<a id="source-r-t155"></a>
**R-T155 — Appeals procedures.** [Appeals](https://www.uscourts.gov/about-federal-courts/types-cases/appeals) — Administrative Office of the US Courts. institutional guide; access: search excerpt.


<a id="source-r-t156"></a>
**R-T156 — Ombuds offices.** [Comparison Table for IOA Standards of Practice](https://www.ombudsassociation.org/assets/docs/docs_2022/2022-03_IOA_Comparison_Table_for_IOA_Standards_of_Practice.pdf) — International Ombuds Association. institutional guide; access: search excerpt.


<a id="source-r-t157"></a>
**R-T157 — Sunset clauses.** [Explanatory Memorandum: Product Safety and Metrology amendment regulations](https://www.legislation.gov.uk/ukdsi/2020/9780348213393/pdfs/ukdsiem_9780348213393_en.pdf) — UK Government / legislation.gov.uk. reference; access: search excerpt.


<a id="source-r-t159"></a>
**R-T159 — Public decision records.** [Charity meetings](https://www.gov.uk/government/publications/charities-and-meetings-cc48/charities-and-meetings) — Charity Commission for England and Wales. institutional guide; access: search excerpt.


<a id="source-r-t160"></a>
**R-T160 — Emergency authority with limits.** [France: Final Opinion on Article 49.3 of the Constitution](https://docs-venice.coe.int/api/Document?pdffile=CDL-AD%282025%29025-e) — Venice Commission. institutional guide; access: page.


<a id="source-r-t162"></a>
**R-T162 — Commons-based peer production.** [Coase's Penguin, or, Linux and the Nature of the Firm](https://www.benkler.org/CoasesPenguin.PDF) — Yochai Benkler. research paper; access: search excerpt.


<a id="source-r-t163"></a>
**R-T163 — Project teams.** [Project teams as learning entities](https://www.pmi.org/learning/library/project-teams-learning-entities-9015) — Project Management Institute. research paper; access: search excerpt.


<a id="source-r-t164"></a>
**R-T164 — Working groups.** [Guide to IETF Working Groups](https://www.ietf.org/process/wgs/) — Internet Engineering Task Force. institutional guide; access: search excerpt.


<a id="source-r-t165"></a>
**R-T165 — Task forces.** [ICS Position Training: Foundations Course Reference Guide](https://training.fema.gov/emiweb/is/icsresource/assets/ics_training_reference_guide.pdf) — Federal Emergency Management Agency. institutional guide; access: search excerpt.


<a id="source-r-t166"></a>
**R-T166 — Cross-functional teams.** [The Scrum Guide (2020)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf) — Ken Schwaber and Jeff Sutherland. practitioner method; access: search excerpt.


<a id="source-r-t168"></a>
**R-T168 — Independent microenterprises.** [Extending social security to workers in micro and small enterprises](https://www.ilo.org/sites/default/files/wcmsp5/groups/public/%40ed_protect/%40soc_sec/documents/publication/wcms_749431.pdf) — International Labour Organization. institutional guide; access: search excerpt.


<a id="source-r-t169"></a>
**R-T169 — Guilds across teams.** [Scaling Agile at Spotify](https://scrummaster.dk/lib/AgileLeanLibrary/People/HenrikKniberg/SpotifyScaling.pdf) — Henrik Kniberg and Anders Ivarsson. practitioner method; access: search excerpt.


<a id="source-r-t170"></a>
**R-T170 — Hackathons.** [Run an AI hackathon](https://academy.openai.com/public/clubs/champions-ecqup/resources/hackathon-playbook-2025-09-15) — OpenAI Academy. practitioner method; access: page.


<a id="source-r-t171"></a>
**R-T171 — Sprints.** [The Scrum Guide: The Sprint](https://scrumguides.org/scrum-guide.html) — Ken Schwaber and Jeff Sutherland. practitioner method; access: search excerpt.


<a id="source-r-t172"></a>
**R-T172 — Work parties.** [Practical Conservation: Leeds Midweek Practical Team](https://www2.tcv.org.uk/cgi-bin/volunteer/activity-details?id=42637%3Bdate%3D20261112) — The Conservation Volunteers. practitioner method; access: search excerpt.


<a id="source-r-t173"></a>
**R-T173 — Barn-raising.** [Mutual Aid](https://groups.etown.edu/amishstudies/cultural-practices/mutual-aid/) — Elizabethtown College Young Center for Anabaptist and Pietist Studies. reference; access: search excerpt.


<a id="source-r-t174"></a>
**R-T174 — Pair work.** [On Pair Programming](https://martinfowler.com/articles/on-pair-programming.html) — Birgitta Böckeler and Nina Siessegger / MartinFowler.com. practitioner method; access: search excerpt.


<a id="source-r-t175"></a>
**R-T175 — Mob or ensemble work.** [Mob Programming](https://agilealliance.org/glossary/mob-programming/) — Agile Alliance. reference; access: search excerpt.


<a id="source-r-t176"></a>
**R-T176 — Shared task boards.** [The Kanban Guide (May 2025)](https://kanbanguides.org/the-kanban-guide/2025.5/) — Kanban Guides. practitioner method; access: page.


<a id="source-r-t178"></a>
**R-T178 — Work-in-progress limits.** [The Kanban Guide (May 2025)](https://kanbanguides.org/the-kanban-guide/2025.5/) — Kanban Guides. practitioner method; access: page.


<a id="source-r-t179"></a>
**R-T179 — Issue triage.** [Triaging an issue with AI](https://docs.github.com/en/issues/tracking-your-work-with-issues/administering-issues/triaging-an-issue-with-ai) — GitHub Docs. institutional guide; access: search excerpt.


<a id="source-r-t180"></a>
**R-T180 — Request-for-comments processes.** [Introduction: The Rust RFC Book](https://rust-lang.github.io/rfcs/introduction.html) — Rust Project. institutional guide; access: search excerpt.


<a id="source-r-t181"></a>
**R-T181 — Design reviews.** [NASA Systems Engineering Handbook: Life-Cycle Reviews](https://science.nasa.gov/wp-content/uploads/2023/04/nasa_systems_engineering_handbook_0.pdf) — NASA. institutional guide; access: search excerpt.


<a id="source-r-t185"></a>
**R-T185 — Release governance.** [Apache HTTP Server Release Guidelines](https://httpd.apache.org/dev/release.html) — Apache HTTP Server Project. institutional guide; access: search excerpt.


<a id="source-r-t186"></a>
**R-T186 — Standards bodies.** [Developing standards](https://committee.iso.org/developing-standards.html) — International Organization for Standardization. institutional guide; access: search excerpt.


<a id="source-r-t187"></a>
**R-T187 — Protocols and interfaces.** [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958.html) — Internet Architecture Board / RFC Editor. reference; access: page.


<a id="source-r-t188"></a>
**R-T188 — Standard operating procedures.** [Guidance for Preparing Standard Operating Procedures](https://www.epa.gov/sites/default/files/2015-06/documents/g6-final.pdf) — US Environmental Protection Agency. institutional guide; access: search excerpt.


<a id="source-r-t189"></a>
**R-T189 — Checklists.** [WHO Surgical Safety Checklist: Tools and resources](https://www.who.int/teams/integrated-health-services/quality-of-care-and-patient-safety/patient-safety-guidance-and-tools/safe-surgery/tool-and-resources) — World Health Organization. institutional guide; access: search excerpt.


<a id="source-r-t190"></a>
**R-T190 — Handoff protocols.** [Tool: Handoff](https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/handoff.html) — Agency for Healthcare Research and Quality. institutional guide; access: search excerpt.


<a id="source-r-t191"></a>
**R-T191 — Responsibility matrices.** [PMI Lexicon of Project Management Terms](https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf?rev=447328d841c249af985d14177ddd5f95) — Project Management Institute. reference; access: search excerpt.


<a id="source-r-t192"></a>
**R-T192 — Service-level agreements.** [What is an SLA?](https://aws.amazon.com/what-is/sla/) — Amazon Web Services. institutional guide; access: search excerpt.


<a id="source-r-t193"></a>
**R-T193 — Rotating duty rosters.** [On-Call](https://sre.google/workbook/on-call/) — Google Site Reliability Engineering. practitioner method; access: search excerpt.


<a id="source-r-t194"></a>
**R-T194 — Incident command.** [NIMS Overview for Senior Officials: Instructor Guide](https://training.fema.gov/gstate/xcr3wnlp/g0402%20-%20ics-402%20-%20incident%20command%20system%20%28ics%29%20overview%20for%20executives%20and%20senior%20officials/04%20ig/g402_complete_ig.pdf) — Federal Emergency Management Agency. institutional guide; access: search excerpt.


<a id="source-r-t195"></a>
**R-T195 — Blameless postmortems.** [Lessons Learned from Other Industries: Postmortem Culture](https://sre.google/sre-book/lessons-learned/) — Google Site Reliability Engineering. practitioner method; access: search excerpt.


<a id="source-r-t196"></a>
**R-T196 — Communities of contribution.** [Building Welcoming Communities](https://opensource.guide/building-community/) — GitHub Open Source Guides. practitioner method; access: search excerpt.


<a id="source-r-t197"></a>
**R-T197 — Volunteer matching.** [Your next steps to apply for a UN Volunteer assignment](https://learning.unv.org/local/uvp_user_sync/candidate_learning.php) — United Nations Volunteers. institutional guide; access: search excerpt.


<a id="source-r-t198"></a>
**R-T198 — Time-boxed commitments.** [Engage an Online Volunteer](https://www.unv.org/engage-online-volunteers) — United Nations Volunteers. institutional guide; access: search excerpt.


<a id="source-r-t199"></a>
**R-T199 — Public pledges.** [Committed (dis)honesty: A systematic meta-analytic review](https://pubmed.ncbi.nlm.nih.gov/38619478/) — Psychological Bulletin / PubMed. research paper; access: abstract.


<a id="source-r-t200"></a>
**R-T200 — Accountability partners.** [Accountability Partners: A Short Guide](https://www.gsas.columbia.edu/sites/default/files/content/docs/Accountability%20Partners%20%28updated%20April%202023%29.pdf) — Columbia University GSAS Writing Studio. institutional guide; access: search excerpt.


<a id="source-r-t201"></a>
**R-T201 — Coworking sessions.** [Getting started](https://support.focusmate.com/en/articles/9110188-getting-started) — Focusmate. practitioner method; access: search excerpt.


<a id="source-r-t202"></a>
**R-T202 — Distributed campaigns.** [Register Your Local Group](https://350.org/register-a-local-group/) — 350.org. practitioner method; access: search excerpt.


<a id="source-r-t203"></a>
**R-T203 — Coalitions.** [Coalition Building I: Starting a Coalition](https://ctb.ku.edu/en/table-of-contents/assessment/promotion-strategies/start-a-coaltion/checklist) — University of Kansas Community Tool Box. institutional guide; access: search excerpt.


<a id="source-r-t204"></a>
**R-T204 — Collective impact partnerships.** [Collective Impact](https://www.fsg.org/resource/collective-impact/) — FSG / John Kania and Mark Kramer. practitioner method; access: search excerpt.


<a id="source-r-t205"></a>
**R-T205 — Boundary-spanning roles.** [The active client: The boundary-spanning roles of internal consultants](https://journals.sagepub.com/doi/10.1177/1350507611401536) — Organization / Andrew Sturdy and Christopher Wright. research paper; access: abstract.


<a id="source-r-t212"></a>
**R-T212 — Auctions.** [Popular science background: Auction theory](https://www.nobelprize.org/uploads/2020/09/popular-economicsciencesprize2020.pdf) — Nobel Prize. reference; access: search excerpt.


<a id="source-r-t213"></a>
**R-T213 — Double auctions.** [Constructivist and Ecological Rationality in Economics](https://www.nobelprize.org/uploads/2017/05/vernon-smith-lecture.pdf) — Nobel Prize; Vernon Smith. research paper; access: search excerpt.


<a id="source-r-t214"></a>
**R-T214 — Barter.** [Publication 525: Bartering](https://www.irs.gov/publications/p525) — Internal Revenue Service. reference; access: search excerpt.


<a id="source-r-t215"></a>
**R-T215 — Mutual credit.** [From an idea to a scalable working model: Sardex](https://www.ijccr.net/article/view/9213) — International Journal of Community Currency Research. research paper; access: search excerpt.


<a id="source-r-t217"></a>
**R-T217 — Local currencies.** [About BerkShares](https://berkshares.org/about/) — BerkShares. practitioner method; access: search excerpt.


<a id="source-r-t218"></a>
**R-T218 — Gift economies.** [Exchange, Value, and Consumption](https://openstax.org/books/introduction-anthropology/pages/7-6-exchange-value-and-consumption) — OpenStax. reference; access: search excerpt.


<a id="source-r-t219"></a>
**R-T219 — Reciprocal labor exchanges.** [Pro-Actively Coping with Climate Change](https://www.fao.org/climatechange/27003-0ca48ac78232e712dc17f10f6c19e5576.pdf) — Food and Agriculture Organization. reference; access: search excerpt.


<a id="source-r-t220"></a>
**R-T220 — Rotating savings groups.** [Indigenous Savings and Credit Societies in the Developing World](https://documents1.worldbank.org/curated/en/255821468766493886/pdf/multi-page.pdf) — World Bank; F. J. A. Bouman. research paper; access: search excerpt.


<a id="source-r-t221"></a>
**R-T221 — Credit unions.** [What Is a Credit Union?](https://mycreditunion.gov/brochure-publications/brochure/what-credit-union) — National Credit Union Administration. institutional guide; access: search excerpt.


<a id="source-r-t222"></a>
**R-T222 — Mutual insurance.** [Microinsurance: Collective gains](https://www.icmif.org/blog_articles/microinsurance-collective-gains/) — International Cooperative and Mutual Insurance Federation. practitioner method; access: search excerpt.


<a id="source-r-t223"></a>
**R-T223 — Emergency mutual-aid funds.** [Elswick Solidarity Fund](https://opencollective.com/elswicksolidarityfund) — Elswick Solidarity Fund. practitioner method; access: search excerpt.


<a id="source-r-t224"></a>
**R-T224 — Crowdfunding.** [Understanding crowdfunding](https://www.fca.org.uk/investsmart/understanding-crowdfunding) — Financial Conduct Authority. institutional guide; access: search excerpt.


<a id="source-r-t225"></a>
**R-T225 — Crowdlending.** [Understanding crowdfunding](https://www.fca.org.uk/investsmart/understanding-crowdfunding) — Financial Conduct Authority. institutional guide; access: search excerpt.


<a id="source-r-t226"></a>
**R-T226 — Subscriptions.** [Subscription pricing models: A guide for businesses](https://stripe.com/resources/more/subscription-pricing-models-a-guide-for-businesses) — Stripe. practitioner method; access: search excerpt.


<a id="source-r-t227"></a>
**R-T227 — Membership dues.** [Our clubs](https://www.rotary.org/en/get-involved/our-clubs) — Rotary International. practitioner method; access: search excerpt.


<a id="source-r-t228"></a>
**R-T228 — Patronage.** [Looking to Connect with European Paintings: The Role of the Patron](https://resources.metmuseum.org/resources/metpublications/pdf/looking_to_connect_with_european_paintings_visual_approaches_for_teaching_in_the_galleries.pdf) — Metropolitan Museum of Art. history; access: search excerpt.


<a id="source-r-t229"></a>
**R-T229 — Grants.** [Grants for Arts Projects](https://www.arts.gov/grants/grants-for-arts-projects) — National Endowment for the Arts. institutional guide; access: search excerpt.


<a id="source-r-t230"></a>
**R-T230 — Prize competitions.** [Prize competitions](https://www.gsa.gov/technology/government-it-initiatives/prize-competitions) — U.S. General Services Administration. institutional guide; access: search excerpt.


<a id="source-r-t231"></a>
**R-T231 — Bounties.** [Google Open Source Software Vulnerability Reward Program Rules](https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/google-open-source-software-vulnerability-reward-program-rules.md) — Google Bug Hunters. practitioner method; access: search excerpt.


<a id="source-r-t233"></a>
**R-T233 — Quadratic funding.** [A Flexible Design for Funding Public Goods](https://www.microsoft.com/en-us/research/publication/a-flexible-design-for-funding-public-goods/) — Microsoft Research; Buterin, Hitzig, Weyl. research paper; access: search excerpt.


<a id="source-r-t234"></a>
**R-T234 — Matching grants.** [Challenge America: Grant Program Details](https://www.arts.gov/sites/default/files/FY26-CA-Grant-Program-Details-FINAL.pdf) — National Endowment for the Arts. institutional guide; access: search excerpt.


<a id="source-r-t235"></a>
**R-T235 — Endowments.** [Harvard's Endowment](https://finance.harvard.edu/endowment) — Harvard University Financial Administration. institutional guide; access: search excerpt.


<a id="source-r-t236"></a>
**R-T236 — Pooled procurement.** [Pooled Procurement Mechanism: Operational Procedures](https://resources.theglobalfund.org/media/klkdheja/cr_pooled-procurement-mechanism_op_en.pdf) — The Global Fund. institutional guide; access: search excerpt.


<a id="source-r-t237"></a>
**R-T237 — Buying clubs.** [America's Farms and Ranches at a Glance: 2022 Edition](https://www.ers.usda.gov/sites/default/files/_laserfiche/publications/105388/EIB-247.pdf) — USDA Economic Research Service. reference; access: search excerpt.


<a id="source-r-t238"></a>
**R-T238 — Tool libraries.** [How It Works](https://seattlereconomy.org/how-it-works/) — Seattle REconomy. practitioner method; access: search excerpt.


<a id="source-r-t239"></a>
**R-T239 — Resource booking systems.** [Flight simulator reservations](https://mtsu.libcal.com/reserve/sim) — Middle Tennessee State University. institutional guide; access: search excerpt.


<a id="source-r-t240"></a>
**R-T240 — Queues.** [The Championships Queue Guide 2025](https://www.wimbledon.com/pdf/The_Championships_Queue_Guide_2025.pdf) — Wimbledon. institutional guide; access: search excerpt.


<a id="source-r-t241"></a>
**R-T241 — Allocation lotteries.** [Secondary School Admissions Brochure 2025](https://www.rbkc.gov.uk/media/document/rbkc-secondary-school-admissions-brochure-2025) — Royal Borough of Kensington and Chelsea. institutional guide; access: search excerpt.


<a id="source-r-t242"></a>
**R-T242 — Needs-based allocation.** [Humanitarian principles](https://emergency.unhcr.org/protection/protection-principles/humanitarian-principles) — UNHCR. institutional guide; access: search excerpt.


<a id="source-r-t243"></a>
**R-T243 — Rationing.** [Connecting, Sharing, Learning: Second World War](https://www.iwm.org.uk/sites/default/files/fies/2021-07/connecting_sharing_learning_second_world_war.pdf) — Imperial War Museums. history; access: search excerpt.


<a id="source-r-t244"></a>
**R-T244 — Tradable quotas.** [Glossary: Catch Shares](https://www.fisheries.noaa.gov/national/sustainable-fisheries/glossary-catch-shares) — NOAA Fisheries. institutional guide; access: search excerpt.


<a id="source-r-t246"></a>
**R-T246 — Resource boundaries.** [Beyond Markets and States: Polycentric Governance of Complex Economic Systems](https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf) — Nobel Prize; Elinor Ostrom. research paper; access: search excerpt.


<a id="source-r-t247"></a>
**R-T247 — User participation in rulemaking.** [How to Use the IAD Framework](https://ostromworkshop.indiana.edu/doc/teaching/how-to-use--iad-framework-slides.pdf) — Ostrom Workshop, Indiana University. institutional guide; access: page.


<a id="source-r-t248"></a>
**R-T248 — Community monitoring.** [How to Use the IAD Framework](https://ostromworkshop.indiana.edu/doc/teaching/how-to-use--iad-framework-slides.pdf) — Ostrom Workshop, Indiana University. institutional guide; access: page.


<a id="source-r-t249"></a>
**R-T249 — Graduated sanctions.** [Beyond Markets and States: Polycentric Governance of Complex Economic Systems](https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf) — Nobel Prize; Elinor Ostrom. research paper; access: search excerpt.


<a id="source-r-t256"></a>
**R-T256 — Employee ownership.** [An Introduction to ESOPs](https://www.nceo.org/hubfs/assets/pdf/samples/An-Introduction-to-ESOPs-21st-full-cover-preview.pdf) — National Center for Employee Ownership. institutional guide; access: search excerpt.


<a id="source-r-t257"></a>
**R-T257 — Steward ownership.** [Steward-Ownership](https://purpose-economy.org/content/uploads/purposebooklet_en.pdf) — Purpose Foundation. practitioner method; access: search excerpt.


<a id="source-r-t258"></a>
**R-T258 — Revenue sharing.** [Fair Trade Music Policy](https://bandcamp.com/fair_trade_music_policy) — Bandcamp. practitioner method; access: search excerpt.


<a id="source-r-t259"></a>
**R-T259 — Profit sharing.** [Our Profit-Sharing and Charitable Contributions Formula](https://buffer.com/resources/profit-sharing/) — Buffer. practitioner method; access: search excerpt.


<a id="source-r-t260"></a>
**R-T260 — Transparent compensation formulas.** [The Next Evolution of Transparent Salaries](https://buffer.com/resources/salary-formula/) — Buffer. practitioner method; access: search excerpt.


<a id="source-r-t261"></a>
**R-T261 — Rent allocation formulas.** [Spliddit: Unleashing Fair Division Algorithms](https://www.sigecom.org/exchanges/volume_13/2/GOLDMAN.pdf) — ACM SIGecom; Goldman and Procaccia. research paper; access: search excerpt.


<a id="source-r-t262"></a>
**R-T262 — Fiscal sponsorship.** [About Fiscal Sponsorship](https://www.fiscalsponsors.org/about-fiscal-sponsorship) — National Network of Fiscal Sponsors. institutional guide; access: search excerpt.


<a id="source-r-t263"></a>
**R-T263 — Community-supported agriculture.** [Community Supported Agriculture](https://www.nal.usda.gov/farms-and-agricultural-production-systems/community-supported-agriculture) — USDA National Agricultural Library. institutional guide; access: search excerpt.


<a id="source-r-t264"></a>
**R-T264 — Repair cafés.** [About Repair Café](https://www.repaircafe.org/en/about/) — Repair Café International. practitioner method; access: search excerpt.


<a id="source-r-t265"></a>
**R-T265 — Swap events.** [What you buy, use and dispose of](https://www.westminster.gov.uk/environment-hub/take-environmental-action-resident/what-you-buy-use-and-dispose) — Westminster City Council. institutional guide; access: search excerpt.


<a id="source-r-t266"></a>
**R-T266 — Escrow.** [Escrow](https://www.law.cornell.edu/wex/escrow) — Cornell Legal Information Institute. reference; access: search excerpt.


<a id="source-r-t267"></a>
**R-T267 — Contracts.** [Contract](https://www.law.cornell.edu/wex/contract) — Cornell Legal Information Institute. reference; access: search excerpt.


<a id="source-r-t269"></a>
**R-T269 — Copyleft.** [What Is Copyleft?](https://www.gnu.org/licenses/copyleft.html) — GNU Project; Free Software Foundation. institutional guide; access: search excerpt.


<a id="source-r-t270"></a>
**R-T270 — Public provisioning.** [What Goals Should We Seek in Politics?](https://openstax.org/books/introduction-political-science/pages/2-1-what-goals-should-we-seek-in-politics) — OpenStax. reference; access: search excerpt.


<a id="source-r-t272"></a>
**R-T272 — Certification.** [Certification](https://www.iso.org/certification.html) — International Organization for Standardization. institutional guide; access: page.


<a id="source-r-t273"></a>
**R-T273 — Accreditation.** [Certification: Accreditation](https://www.iso.org/certification.html) — International Organization for Standardization. institutional guide; access: page.


<a id="source-r-t274"></a>
**R-T274 — Professional licensing.** [License Finder Help](https://cloudfront.careeronestop.org/toolkit/Training/find-licenses-help.aspx) — CareerOneStop; U.S. Department of Labor. institutional guide; access: search excerpt.


<a id="source-r-t275"></a>
**R-T275 — Portfolios.** [Types of Interview: Portfolio-based interviews](https://www.careers.ox.ac.uk/types-of-interview/) — University of Oxford Careers Service. institutional guide; access: search excerpt.


<a id="source-r-t276"></a>
**R-T276 — References.** [Reference Checking](https://www.opm.gov/policy-data-oversight/assessment-and-selection/other-assessment-methods/reference-checking/) — U.S. Office of Personnel Management. institutional guide; access: search excerpt.


<a id="source-r-t277"></a>
**R-T277 — Reputation systems.** [Reputation Systems](https://cs.uwaterloo.ca/~klarson/teaching/F04-886/papers/p45-resnick.pdf) — Communications of the ACM; Resnick, Zeckhauser, Friedman, Kuwabara. research paper; access: search excerpt.


<a id="source-r-t278"></a>
**R-T278 — Contribution records.** [Contributions on your profile](https://docs.github.com/en/account-and-profile/concepts/contributions-on-your-profile) — GitHub Docs. institutional guide; access: search excerpt.


<a id="source-r-t280"></a>
**R-T280 — Peer nominations.** [Advice for Award Nominators and Endorsers](https://awards.acm.org/binaries/content/assets/awards/advice-for-award-nominators-and-endorsers_07-2025.pdf) — Association for Computing Machinery. institutional guide; access: search excerpt.


<a id="source-r-t282"></a>
**R-T282 — Contributor credits.** [All Contributors Specification](https://allcontributors.org/en/reference/specification/) — All Contributors. practitioner method; access: search excerpt.


<a id="source-r-t283"></a>
**R-T283 — Authorship conventions.** [Defining the Role of Authors and Contributors](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html) — International Committee of Medical Journal Editors. institutional guide; access: search excerpt.


<a id="source-r-t284"></a>
**R-T284 — Merit-based selection.** [Merit System Principles](https://www.opm.gov/chcoc/transmittals/2020/attachments/2020%20Appointments%20and%20Awards%20Guidance%20Attachments.pdf) — U.S. Office of Personnel Management. institutional guide; access: search excerpt.


<a id="source-r-t285"></a>
**R-T285 — Seniority rules.** [Public Service Orders: Seniority on Promotion](https://natlex.ilo.org/dyn/natlex2/natlex2/files/download/86499/SYC86499.pdf) — Government of Seychelles; ILO NATLEX archive. reference; access: search excerpt.


<a id="source-r-t286"></a>
**R-T286 — Competitive examinations.** [Young Professionals Programme](https://careers.un.org/ypp) — United Nations Careers. institutional guide; access: search excerpt.


<a id="source-r-t287"></a>
**R-T287 — Work-sample assessments.** [Work Samples and Simulations](https://www.opm.gov/policy-data-oversight/assessment-and-selection/other-assessment-methods/work-samples-and-simulations/) — U.S. Office of Personnel Management. institutional guide; access: search excerpt.


<a id="source-r-t288"></a>
**R-T288 — Auditions.** [Tanglewood Festival Chorus Auditions](https://www.bso.org/tfc/auditions) — Boston Symphony Orchestra. institutional guide; access: page.


<a id="source-r-t289"></a>
**R-T289 — Trial projects.** [How We Hire Developers](https://automattic.com/work-with-us/how-we-hire-developers/) — Automattic. practitioner method; access: search excerpt.


<a id="source-r-t290"></a>
**R-T290 — Blind review.** [Double-blind peer review](https://www.nature.com/naturehealth/submission-guidelines/dbpr) — Nature Health. institutional guide; access: search excerpt.


<a id="source-r-t292"></a>
**R-T292 — Sponsorship for advancement.** [Catalyst Sponsorship Guide](https://www.catalyst.org/en-us/insights/2025/catalyst-sponsorship-guide) — Catalyst. institutional guide; access: search excerpt.


<a id="source-r-t294"></a>
**R-T294 — Deputy roles.** [Creating the COO Position](https://www.bridgespan.org/getmedia/c60187c0-f6b7-4019-bd32-53b8872ae283/CreatingCOOPosition.pdf?ext=.pdf) — The Bridgespan Group. institutional guide; access: search excerpt.


<a id="source-r-t295"></a>
**R-T295 — Overlapping handovers.** [Shift handover](https://www.hse.gov.uk/humanfactors/topics/shift-handover.htm) — UK Health and Safety Executive. institutional guide; access: search excerpt.


<a id="source-r-t296"></a>
**R-T296 — Graduated responsibility.** [Common Program Requirements FAQs](https://prod2.acgme.org/globalassets/pdfs/faq/common-program-requirements-faqs.pdf) — Accreditation Council for Graduate Medical Education. institutional guide; access: search excerpt.


<a id="source-r-t297"></a>
**R-T297 — Leadership pipelines.** [Succession Planning Process](https://www.opm.gov/policy-data-oversight/human-capital-framework/reference-materials/leadership-knowledge-management/successionplanning/) — U.S. Office of Personnel Management. institutional guide; access: search excerpt.


<a id="source-r-t298"></a>
**R-T298 — Founder transition agreements.** [Leadership Transition: Overcoming the Threat of Founder's Syndrome](https://www.intrac.org/app/uploads/2024/12/Praxis-Series-Paper-No-9-Leadership-Transition-Overcoming-the-Threat-of-Founders-Syndrome.pdf) — INTRAC. institutional guide; access: search excerpt.


<a id="source-r-t299"></a>
**R-T299 — Emeritus roles.** [ASF Members: Emeritus Members](https://www.apache.org/foundation/members) — Apache Software Foundation. institutional guide; access: search excerpt.


<a id="source-r-t300"></a>
**R-T300 — Exit interviews.** [Exit Interviews](https://www.gla.ac.uk/myglasgow/pod/mgrs-admin/mgr-guidance/leaverguidance/exit-int/) — University of Glasgow. institutional guide; access: search excerpt.


<a id="source-r-t301"></a>
**R-T301 — Institutional memory interviews.** [Johnson Space Center Oral History Project](https://history.nasa.gov/wp-content/uploads/static/history/alsj/JSC-OralHist.html) — NASA. history; access: search excerpt.


<a id="source-r-t302"></a>
**R-T302 — Backup ownership.** [Leadership and Governance](https://opensource.guide/pcm/leadership-and-governance/) — GitHub Open Source Guides. institutional guide; access: search excerpt.


<a id="source-r-t303"></a>
**R-T303 — Stewardship terms.** [Our 2026 Trustee Search](https://wikimediafoundation.org/our-2026-trustee-search/) — Wikimedia Foundation. institutional guide; access: search excerpt.


<a id="source-r-t305"></a>
**R-T305 — Lineage recognition.** [Steve Weintraub](https://www.sfzc.org/teachers/steve-weintraub/) — San Francisco Zen Center. history; access: search excerpt.


<a id="source-r-t306"></a>
**R-T306 — Oaths of office.** [Oath of Office](https://www.senate.gov/about/origins-foundations/senate-and-constitution/oath-of-office.htm) — United States Senate. history; access: search excerpt.


<a id="source-r-t307"></a>
**R-T307 — Citizen science.** [Citizen Science Toolkit: How To](https://www.citizenscience.gov/toolkit/howto/) — US Federal Government CitizenScience.gov. institutional guide; access: search excerpt.


<a id="source-r-t308"></a>
**R-T308 — Participatory mapping.** [Good Practices in Participatory Mapping](https://www.ifad.org/documents/38714170/39144386/PM_web.pdf/7c1eda69-8205-4c31-8912-3c25d6f90055) — International Fund for Agricultural Development. institutional guide; access: search excerpt.


<a id="source-r-t309"></a>
**R-T309 — Deliberative polling.** [What Is Deliberative Polling?](https://deliberation.stanford.edu/what-deliberative-pollingr) — Stanford Deliberative Democracy Lab. practitioner method; access: search excerpt.


<a id="source-r-t310"></a>
**R-T310 — Knowledge fairs.** [The Art of Knowledge Exchange: Knowledge Fair](https://documents1.worldbank.org/curated/en/922981470418822804/pdf/The-art-of-knowledge-exchange-a-results-focused-planning-guide-for-development-practitioners-in-the-water-sector.pdf) — World Bank. institutional guide; access: search excerpt.


<a id="source-r-t311"></a>
**R-T311 — Congregations.** [National Congregations Study Cumulative Codebook](https://sites.duke.edu/ncsweb/files/2020/09/NCS-I-IV-Cumulative-Codebook_FINAL_8Sept2020.pdf) — Duke University National Congregations Study. research paper; access: search excerpt.


<a id="source-r-t312"></a>
**R-T312 — Pilgrimage.** [Pilgrimage to the St. Thaddeus Apostle Monastery](https://ich.unesco.org/en/RL/pilgrimage-to-the-st-thaddeus-apostle-monastery-01571?RL=01571) — UNESCO Intangible Cultural Heritage. history; access: search excerpt.


<a id="source-r-t313"></a>
**R-T313 — Mutual-benefit societies.** [English Poor Laws: Friendly Societies](https://eh.net/encyclopedia/english-poor-laws/) — Economic History Association / EH.net. history; access: search excerpt.


<a id="source-r-t314"></a>
**R-T314 — Community sponsorship of newcomers.** [Sponsorship Programmes for Refugees](https://help.unhcr.org/global/sponsorship-programmes-for-refugees/) — UN Refugee Agency. institutional guide; access: page.


<a id="source-r-t317"></a>
**R-T317 — Arbitration.** [Your Questions About Arbitration, Answered](https://www.adr.org/news-and-insights/your-questions-about-arbitration-answered/) — American Arbitration Association. institutional guide; access: search excerpt.


<a id="source-r-t318"></a>
**R-T318 — Courts.** [Court Role and Structure](https://www.uscourts.gov/about-federal-courts/court-role-and-structure) — Administrative Office of the US Courts. institutional guide; access: search excerpt.


<a id="source-r-t319"></a>
**R-T319 — Jury trials.** [Types of Juries](https://www.uscourts.gov/court-programs/jury-service/types-juries) — Administrative Office of the US Courts. institutional guide; access: search excerpt.


<a id="source-r-t320"></a>
**R-T320 — Parliamentary procedure.** [Sample Rules for Electronic Meetings](https://robertsrules.com/wp-content/uploads/2020/08/electronic-meeting-sample-rules.pdf) — Robert's Rules Association. practitioner method; access: search excerpt.


<a id="source-r-t321"></a>
**R-T321 — Spokescouncils.** [The Spokescouncil](https://www.seedsforchange.org.uk/spokescouncil) — Seeds for Change. practitioner method; access: search excerpt.


<a id="source-r-t322"></a>
**R-T322 — Whistleblowing channels.** [How to File a Whistleblower Complaint](https://www.whistleblowers.gov/complaint_page) — US Occupational Safety and Health Administration. institutional guide; access: search excerpt.


<a id="source-r-t323"></a>
**R-T323 — Freedom-of-information processes.** [Request handling, Freedom of Information: Frequently Asked Questions](https://ico.org.uk/for-organisations/foi/freedom-of-information-and-environmental-information-regulations/request-handling-freedom-of-information/) — UK Information Commissioner's Office. institutional guide; access: search excerpt.


<a id="source-r-t324"></a>
**R-T324 — Social audits.** [The CDF Social Audit Guide: A Handbook for Communities](https://connect4impact.worldbank.org/system/files/2025-12/Social%20Audit%20Handbook%20for%20Constituency%20Devt%20Fund%20-%20Kenya.pdf) — Open Society Initiative of East Africa (World Bank-hosted copy). institutional guide; access: page.


<a id="source-r-t325"></a>
**R-T325 — Independent audits.** [AS 1000: General Responsibilities of the Auditor in Conducting an Audit](https://pcaobus.org/oversight/standards/auditing-standards/details/as-1000--general-responsibilities-of-the-auditor-in-conducting-an-audit) — Public Company Accounting Oversight Board. institutional guide; access: search excerpt.


<a id="source-r-t326"></a>
**R-T326 — Strikes.** [ILO Helpdesk: Questions and answers on business and collective bargaining](https://www.ilo.org/ilo-helpdesk-questions-and-answers-business-and-collective-bargaining) — International Labour Organization. institutional guide; access: search excerpt.


<a id="source-r-t327"></a>
**R-T327 — Boycotts.** [The Montgomery Bus Boycott](https://www.nps.gov/articles/montgomery-bus-boycott.htm) — US National Park Service. history; access: search excerpt.


<a id="source-r-t328"></a>
**R-T328 — Citizen journalism.** [Global Media and Information Literacy Assessment Framework](https://uis.unesco.org/sites/default/files/documents/global-media-and-information-literacy-assessment-framework-country-readiness-and-competencies-2013-en.pdf) — UNESCO. reference; access: search excerpt.


<a id="source-r-t329"></a>
**R-T329 — Monastic orders.** [The Rule of Benedict: Chapter 1, On the Kinds of Monks](https://archive.osb.org/rb/text/rbejms1.html) — Order of Saint Benedict archive. history; access: search excerpt.


<a id="source-r-t330"></a>
**R-T330 — Joint ventures.** [IFRS 11 Joint Arrangements](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-11-joint-arrangements/) — IFRS Foundation. issued standard overview; access: page.


<a id="source-r-t331"></a>
**R-T331 — Franchising.** [A Consumer's Guide to Buying a Franchise](https://www.ftc.gov/business-guidance/resources/consumers-guide-buying-franchise) — US Federal Trade Commission. institutional guide; access: page.


<a id="source-r-t332"></a>
**R-T332 — Taxation.** [Taxes](https://www.oecd.org/en/data/dashboards/ifcma-climate-policy-dashboard/instruments/taxes.html) — Organisation for Economic Co-operation and Development. reference; access: search excerpt.


<a id="source-r-t333"></a>
**R-T333 — Double-entry accounting.** [Principles of Accounting: Chapter 3 Key Terms](https://openstax.org/books/principles-financial-accounting/pages/3-key-terms) — OpenStax. reference; access: search excerpt.


<a id="source-r-t334"></a>
**R-T334 — Public asset registers.** [Strengthening Fixed Asset Management through Public Sector Accounting: Recording Assets](https://documents1.worldbank.org/curated/en/099032824083534274/pdf/P1650951b227e508a1babd150c2484b04a4.pdf) — World Bank. institutional guide; access: search excerpt.


<a id="source-r-t335"></a>
**R-T335 — Assurance contracts.** [Intelligent Cooperation: Dominant Assurance Contracts](https://foresight.org/wp-content/uploads/2021/12/Intelligent-Cooperation-2021-12-06.pdf) — Foresight Institute; Alex Tabarrok. practitioner method; access: search excerpt.


<a id="source-r-t336"></a>
**R-T336 — Risk-sharing pools.** [Strengthening Disaster Resilience and Response in Latin America and the Caribbean](https://www.worldbank.org/en/results/2025/06/30/strengthening-disaster-resilience-and-response-in-lac) — World Bank. institutional guide; access: search excerpt.


<a id="source-r-t337"></a>
**R-T337 — Peer juries for awards.** [Grant Review Process](https://www.arts.gov/grants/grant-review-process) — National Endowment for the Arts. institutional guide; access: search excerpt.


<a id="source-r-t338"></a>
**R-T338 — Recallable stewardship.** [Stewards: Confirmations and Removal of Access](https://meta.wikimedia.org/wiki/Stewards) — Wikimedia community, Meta-Wiki. practitioner method; access: page.

<!-- research-sources-end -->

## 10. Composition, gaps, and publishing priorities

### Useful combinations

| Situation | Technologies to combine | What to check |
| --- | --- | --- |
| Start a neighborhood community | Recurring open gathering + introductions + rotating hosts + shared communication norms | Are newcomers returning, and can someone else host? |
| Grow an open-source project | Open license + contribution guidelines + mentorship + maintainer delegation + decision process + succession | Can newcomers contribute and challenge decisions without the founder's personal intervention? |
| Run a focused conference | Membership criteria + lightning talks + residential time + informal conversation + public outputs | Are the selection criteria relevant, and can people outside the room benefit? |
| Share a home | Household agreements + decision thresholds + chore allocation + resource booking + wiki + conflict process | Does ordinary maintenance happen without a few people carrying it all? |
| Make a public decision | Recruitment method + assembly + evidence review + deliberation + decision rule + public response | Who was absent, and what authority does the result actually have? |
| Distribute entrepreneurship | Microenterprise units + explicit decision domains + service agreements + shared infrastructure + review | Where do local incentives conflict with the wider organization? |
| Preserve a community through growth | Cohort onboarding + buddy support + meaningful first contribution + documentation + host succession | Is teaching capacity growing alongside membership? |
| Maintain a shared resource | Boundaries + user rulemaking + monitoring + proportionate responses + conflict resolution | Are rules locally legitimate and is maintenance actually funded? |

These combinations are editorial hypotheses for page examples, not tested packages.

### Inclusion and deduplication rules

An entry belongs when it identifies a repeatable social arrangement, a distinct organizational form, or an explicitly labeled contextual system/dynamic. Different names for substantially the same mechanism should become aliases. Related mechanisms remain separate when their authority, incentives, participation, or implementation differ: mentoring is not apprenticeship; an assembly is not a voting rule; worker ownership does not necessarily imply worker control.

Keep specific methods under broader orientation pages, rather than presenting both as unrelated peers. Treat culturally situated practices in their own context. Do not inflate the count by cloning a technique for every sector or by turning general virtues such as kindness into procedural claims.

### Remaining research gaps

All 404 entries now have introductory source trails. The 282 previously marked C have individual research records with findings, limitations, access labels, and example situations in `site/research/README.md`. Evidence depth varies: some records rely on abstracts or search excerpts, and inclusion does not establish effectiveness. Full-text review, comparative evidence, and documented cases remain areas for further work.

Additional research families include Indigenous and customary governance; religious orders and congregations; rotating credit and mutual-aid traditions across regions; labor unions and industrial democracy; diplomacy and peacebuilding; mutualist and solidarity economies; public-health coordination; disaster-response organizations; and scientific institutions. Names alone are insufficient: collect mechanisms, contexts, failure modes, and documented cases.

### First publication wave

Begin with a practical cross-section: mentorship, apprenticeship, lightning talks, recurring gatherings, community wikis, cohort onboarding, assemblies, consent, advice process, decision thresholds, doocracy, BDFL governance, steering councils, open-source collaboration, autonomous microenterprises, markets, cooperatives, participatory budgeting, commons governance, and succession planning. Pair them with short orientation pages for social technologies and the institutional/extitutional lenses.

The inventory is the expansion backlog. Keep the deployed site static: templates, Markdown content, generated category anchors, an alphabetical index, related links, and a sitemap. Add the small client-side search module described above. Accounts, a database, and an application framework are unnecessary; ordinary browsing remains available without JavaScript.

<a id="source-private-ownership"></a>
**PRIVATE-OWNERSHIP — Private ownership.** [Property and Ownership](https://plato.stanford.edu/entries/property/) — Stanford Encyclopedia of Philosophy. Definition and analysis sections.

<a id="source-r-t341"></a>
**R-T341 — Intellectual property.** [What is Intellectual Property?](https://www.wipo.int/en/web/about-ip). What is Intellectual Property?. WIPO overview and linked definitions reviewed; comparison of payment arrangements is editorial synthesis.

<a id="source-r-t342"></a>
**R-T342 — Patents.** [Frequently Asked Questions: Patents](https://www.wipo.int/en/web/patents/faq_patents). Frequently Asked Questions: Patents. Reviewed exclusion, territory, disclosure, duration, commercialization, and limits. Alternatives synthesize the linked concept pages and their sources.

<a id="source-r-t343"></a>
**R-T343 — Copyright.** [What Can I Protect with a Copyright?](https://www.wipo.int/en/web/copyright/protection). What Can I Protect with a Copyright?. Reviewed protected works and idea/expression distinction; licensing connections use the existing researched pages.

<a id="source-r-t344"></a>
**R-T344 — Trade secrets.** [Frequently Asked Questions on Trade Secrets](https://www.wipo.int/en/web/trade-secrets/tradesecrets_faqs). Frequently Asked Questions on Trade Secrets. Reviewed qualification, reasonable secrecy measures, licensing, independent discovery and reverse engineering.

<a id="source-r-t345"></a>
**R-T345 — Advance market commitments.** [Pneumococcal AMC: How it works](https://www.gavi.org/investing-gavi/innovative-financing/pneumococcal-advance-market-commitment-amc/how-it-works). Pneumococcal AMC: How it works. Read the pilot mechanism, qualifying supply and manufacturer commitments. Water-sensor example is illustrative, not a reported case.

<a id="source-r-t346"></a>
**R-T346 — Commissioned research and development.** [What is innovation procurement?](https://projects.research-and-innovation.ec.europa.eu/en/node/11878). What is innovation procurement?. Reviewed European Commission explanation of buying development and staged pre-commercial procurement. General commissioning example and comparisons are editorial synthesis.

<a id="source-r-t347"></a>
**R-T347 — Patent buyouts.** [Patent Buy-Outs: A Mechanism for Encouraging Innovation](https://www.nber.org/papers/w6304). Patent Buy-Outs: A Mechanism for Encouraging Innovation. NBER abstract excerpts reviewed; direct page returned 403. Mechanism treated as a theoretical proposal, not a general empirical success claim.

<a id="source-r-t348"></a>
**R-T348 — Earning from complementary capabilities.** [Protecting Their Intellectual Assets](https://www.nber.org/papers/w7552). Protecting Their Intellectual Assets. Indexed abstract reviewed; direct page returned 403. 1994 US manufacturing R&D survey, published 2000; no claim of universal or current sector-wide effectiveness.
