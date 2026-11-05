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

**Heading:** “How people organize to get things done.”

**Opening explanation:** Social technologies are repeatable ways of organizing human relationships and actions. Laws, classrooms, contracts, ceremonies, and professional credentials help people know what to expect from one another and make cooperation possible at larger scales.

**Everyday example:** A library depends on more than books and a building. Membership rules, lending procedures, trained librarians, and shared expectations turn those physical resources into a public service.

**How they shape society:** These arrangements influence who can cooperate, who holds authority, what earns recognition, and which knowledge survives. They help sustain material technologies too: a hospital needs equipment, but also training, responsibilities, trust, and ways to coordinate care.

**The lens behind the toolkit:** Samo Burja argues that effective institutions depend on people who design, maintain, and adapt these arrangements. Preserving their outward forms is not enough to preserve their usefulness. Present this as the manuscript's perspective, rather than an uncontested theory of history.

**Invitation:** “Explore the tools that make cooperation possible—and the conditions that make them work.” Link to the grid.

Keep this introduction short: approximately 150–200 words in the finished site.

### Technology grid

**Heading:** “Explore social technologies.”

Use a responsive grid grouped by the six purposes in section 5, with an alphabetical index and anchor links. The original 20 outlines below are the foundation; section 6 expands the inventory. Publish cards only when their full pages are ready. Separate broad systems and social dynamics from practical methods. Add client-side title search above the grid, as specified below. Each card contains:

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

### Browse by the problem you are trying to solve

| Primary purpose | Reader's question |
| --- | --- |
| Learning and knowledge | How do we learn, teach, and remember? |
| Belonging and relationships | How do people meet, trust one another, and stay connected? |
| Decisions and authority | Who decides, how, and with what accountability? |
| Collaboration and production | How do we organize and complete shared work? |
| Resources and ownership | How do we allocate, exchange, finance, and steward resources? |
| Recognition and succession | How do we recognize contributions and transfer responsibility? |

Assign one primary purpose and optional secondary purposes. These are navigation aids, not claims that each technology has only one function. An open-source community can combine a BDFL, mentorship, contributor recognition, public proposals, and lightning talks.

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
- **Athenian democracy:** present a dated historical account of how its institutions combined, who was excluded, and how participation worked. Link to assembly democracy, sortition, elected offices, rotation, and accountability. End with when this case helps analyze institutional design; avoid presenting the historical system as a ready-made prescription.

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
| T001 | Mentorship | P | An experienced person supports another's development over time. | Help a new maintainer grow into responsibility. | C |
| T002 | Apprenticeship | F | Learn a craft through supervised participation in real work. | Train someone where written instructions omit important judgment. | [GFT](#source-gft), [ILO-A](#source-ilo-a) |
| T003 | Peer learning circles | F | Peers meet repeatedly to work through shared learning goals. | Study a difficult subject without a permanent teacher. | C |
| T004 | Communities of practice | F | Practitioners sustain shared learning around a common domain. | Connect isolated people doing similar work. | [COP](#source-cop) |
| T005 | Study groups | F | Members jointly read, discuss, and solve problems. | Maintain momentum through a course or reading program. | C |
| T006 | Journal clubs | P | A group critically examines research papers together. | Build shared standards for interpreting evidence. | C |
| T007 | Socratic seminars | P | Participants examine claims through disciplined questioning. | Explore assumptions behind a disputed idea. | C |
| T008 | Teach-back | P | Learners explain material in their own words. | Find misunderstandings after an explanation. | C |
| T009 | Peer instruction | P | Learners discuss conceptual questions and reconsider answers. | Expose reasoning differences in a classroom. | C |
| T010 | Deliberate practice with feedback | P | Repeat targeted tasks with feedback on specific weaknesses. | Improve a clearly defined component of a skill. | C |
| T011 | Job shadowing | P | Observe an experienced person's work in context. | Reveal everyday decisions before assuming a role. | C |
| T012 | Job rotation | P | Move people through different responsibilities. | Develop cross-functional understanding and backup capacity. | C |
| T013 | Cross-training | P | Teach several people to perform critical tasks. | Reduce dependence on a single specialist. | C |
| T014 | Office hours | P | Reserve recurring times for accessible advice. | Make expert help available without constant interruption. | C |
| T015 | Ask-me-anything sessions | P | Participants question someone with relevant experience. | Surface concerns hidden by a prepared presentation. | C |
| T016 | Lightning talks | P | Short presentations expose a group to many interests. | Discover fellow residents' skills. | [SN-L](#source-sn-l) |
| T017 | Show-and-tell sessions | P | People demonstrate work and explain choices. | Share progress through concrete artifacts. | C |
| T018 | Workshops | P | Participants learn through facilitated hands-on activity. | Practice a method together before using it independently. | C |
| T019 | Train-the-trainer | P | Prepare participants to teach the next cohort. | Expand teaching capacity beyond the original instructor. | C |
| T020 | Learning cohorts | F | Participants progress together through a defined learning period. | Provide peer support during intensive study. | C |
| T021 | Reading salons | P | Conversation around selected texts connects ideas and people. | Build an intellectual community across specialties. | C |
| T022 | Oral history | P | Record participants' accounts of events and practices. | Preserve experience before long-standing members leave. | C |
| T023 | Storytelling | P | Narratives communicate situations, choices, and consequences. | Transmit practical judgment through memorable cases. | C |
| T024 | Case-method discussion | P | Participants analyze a concrete situation before comparing judgments. | Practice decisions under incomplete information. | C |
| T025 | Simulation exercises | P | Rehearse coordinated responses in a constructed scenario. | Prepare a team for unusual disruptions. | C |
| T026 | After-action reviews | P | Compare intended and actual events to identify lessons. | Learn from a completed operation while memories are fresh. | C |
| T027 | Retrospectives | P | Review collaboration and agree on improvements. | Adjust a team's recurring work. | [S3](#source-s3) |
| T028 | Peer review of work | P | Others inspect an artifact and provide substantive criticism. | Improve a draft before release. | C |
| T029 | Replication | P | Independently repeat a procedure to test reproducibility. | Check whether a finding survives a different team. | C |
| T030 | Preregistration | P | Record intended questions and analyses before observing outcomes. | Distinguish planned tests from exploratory interpretation. | C |
| T031 | Open notebooks | P | Expose ongoing methods and observations for others to inspect. | Let collaborators follow how a result emerged. | C |
| T032 | Community wikis | P | Members maintain shared reference material. | Reduce repeated onboarding questions. | [SN-W](#source-sn-w) |
| T033 | Institutional archives | F | Preserve records with provenance and retrieval practices. | Recover decisions and obligations after personnel change. | [ARC](#source-arc) |
| T034 | Decision logs | P | Record decisions and rationale. | Explain why a policy exists. | [S3](#source-s3) |
| T035 | Knowledge maps | P | Map expertise, documents, and unanswered questions. | Find who can answer an unfamiliar problem. | C |
| T036 | Expert directories | P | Maintain searchable accounts of people's skills and interests. | Route requests to relevant people. | C |
| T037 | Open educational resources | P | Share learning materials under permissions enabling reuse. | Let teachers adapt materials to local needs. | C |
| T038 | Translation networks | F | Coordinate people who translate and review shared materials. | Make knowledge accessible across language communities. | C |
| T039 | Libraries | F | Organize shared collections and access to them. | Provide durable access beyond individual ownership. | C |
| T040 | 1-2-4-All | P | Move from individual reflection to pairs, fours, and plenary. | Broaden participation in idea generation. | [LS](#source-ls) |
| T041 | Troika Consulting | P | Three participants alternate receiving and offering help. | Explore a challenge with peers. | [LS](#source-ls) |
| T042 | Appreciative Interviews | P | Interview partners about successful experiences. | Discover existing strengths. | [LS](#source-ls) |
| T043 | What, So What, Now What | P | Separate observations, interpretations, and next actions. | Reflect after an event. | [LS](#source-ls) |
| T044 | Fishbowl discussion | P | A small visible conversation is observed by a larger group. | Let others learn from practitioner dialogue. | C |
| T045 | World Café | P | Rotate small-table conversations and share emerging insights. | Explore a common question across a large gathering. | [WC](#source-wc) |
| T046 | Open Space Technology | P | Participants propose sessions and choose where to contribute. | Convene around a shared concern without a fixed agenda. | [OS](#source-os) |
| T047 | Unconferences | P | Attendees help determine the event's sessions. | Match discussion topics to participants' actual interests. | C |
| T048 | Delphi process | P | Experts respond through successive rounds with summarized feedback. | Explore judgments without requiring simultaneous discussion. | C |
| T049 | Red teams | P | Assign a group to challenge plans or assumptions. | Expose weaknesses before committing resources. | C |
| T050 | Premortems | P | Imagine a plan has failed and identify plausible causes. | Surface reservations before execution. | C |
| T307 | Citizen science | P | Participants contribute observations or analysis to a research project. | Expand inquiry while defining data quality and participant roles. | C |
| T308 | Participatory mapping | P | Participants collectively represent places, resources, or relationships. | Make local knowledge visible in planning. | C |
| T309 | Deliberative polling | P | Compare opinions before and after structured informed deliberation. | Study how judgments change with information and discussion. | C |
| T310 | Knowledge fairs | P | Participants offer demonstrations and exchange expertise across stations. | Discover capabilities across a large community. | C |


### Belonging and relationships

| ID | Technology | Kind | Coordination mechanism | Example / when to consider it | Evidence |
| --- | --- | --- | --- | --- | --- |
| T051 | Recurring open gatherings | P | Meet at a predictable time with low entry requirements. | Make casual neighborhood encounters repeatable. | [SN-S](#source-sn-s) |
| T052 | Shared meals | P | Eating together creates recurring opportunities for interaction. | Connect people whose daily activities rarely overlap. | Adaptation: [BSC](#source-bsc) |
| T053 | Potlucks | P | Participants contribute food to a shared meal. | Distribute hosting effort and invite participation. | C |
| T054 | Residential retreats | P | Participants share a place for sustained interaction. | Develop relationships beyond scheduled sessions. | [BSC](#source-bsc) |
| T055 | Protected unstructured time | P | Leave room for participant-led interaction. | Let conference conversations continue. | Adaptation: [BSC](#source-bsc) |
| T056 | Shared journeys | P | Travel together creates extended informal contact. | Help a cohort meet before an event. | Adaptation: [BSC](#source-bsc) |
| T057 | Hospitality hosting | P | A host welcomes and introduces guests. | Help unfamiliar participants enter a gathering. | C |
| T058 | Buddy systems | P | Pair newcomers with someone who can orient them. | Reduce the social cost of asking basic questions. | C |
| T059 | Cohort onboarding | P | Introduce newcomers together through a shared orientation. | Balance growth with teaching capacity. | Adaptation: [BSC](#source-bsc) |
| T060 | Membership curation | P | Use explicit criteria to select participants. | Assemble a focused working retreat; examine exclusion effects. | [BSC](#source-bsc) |
| T061 | Trial membership | P | Use a defined mutual evaluation period before commitment. | Test expectations in a shared living arrangement. | C |
| T062 | Introductions by a connector | P | Someone identifies relevant common interests between people. | Help strangers begin a useful conversation. | C |
| T063 | Check-in rounds | P | Invite each person to share their current state. | Begin a meeting with awareness of participants. | [S3](#source-s3) |
| T064 | Listening pairs | P | Partners alternate speaking and attentive listening. | Provide space for concerns outside a large meeting. | C |
| T065 | Mutual aid networks | F | People organize reciprocal support around shared needs. | Coordinate neighborhood help during disruption. | C |
| T066 | Care circles | F | A small group shares ongoing support responsibilities. | Prevent support from falling on one person. | C |
| T067 | Meal trains | P | Schedule contributions of prepared meals. | Support a household during a demanding period. | C |
| T068 | Childcare exchanges | P | Participants arrange reciprocal care with clear responsibilities. | Coordinate support among trusted households. | C |
| T069 | Neighborhood associations | F | Residents organize around local concerns and relationships. | Maintain recurring coordination across households. | C |
| T070 | Coliving households | F | Residents combine private living with shared spaces and practices. | Support everyday companionship and shared responsibilities. | [SN-D](#source-sn-d) |
| T071 | Cohousing communities | F | Households retain homes while jointly organizing common facilities. | Combine privacy with intentional community. | [CLT](#source-clt) |
| T072 | Third places | F | Accessible social settings support repeated informal encounters. | Create a gathering point outside home and work. | C |
| T073 | Clubs | F | Members sustain activities around a shared interest. | Provide continuity beyond a one-off event. | C |
| T074 | Affinity groups | F | People organize around a shared experience or concern. | Offer focused peer support within a larger organization. | C |
| T075 | Alumni networks | F | Former participants maintain relationships after a shared experience. | Keep expertise and support accessible after departure. | C |
| T076 | Festival cycles | P | Recurring collective celebrations renew relationships and identity. | Bring dispersed participants together periodically. | C |
| T077 | Rites of passage | P | Mark recognized transitions in social role or status. | Acknowledge a cohort completing an apprenticeship. | C |
| T078 | Welcoming ceremonies | P | Publicly recognize newcomers and introduce shared commitments. | Make entry into a group visible. | C |
| T079 | Farewell rituals | P | Mark departures and acknowledge relationships and contributions. | End participation without silently losing institutional memory. | C |
| T080 | Commemorations | P | Collectively recall events and people. | Transmit a group's history across generations. | C |
| T081 | Shared symbols | P | Use recognizable signs to express collective identity. | Help a dispersed community recognize its affiliation. | C |
| T082 | Origin stories | P | Tell how a group began and what problems shaped it. | Explain inherited priorities while permitting correction. | C |
| T083 | Community agreements | P | Participants articulate expectations for interacting. | Clarify norms before predictable friction occurs. | C |
| T084 | Codes of conduct | P | State behavioral boundaries and reporting processes. | Make participation expectations explicit at events. | C |
| T085 | Principle-based norms | P | Use shared principles to guide contextual judgment. | Handle situations too varied for detailed rules. | [SN-P](#source-sn-p) |
| T086 | Mediation | P | A third party helps disputants seek an agreement. | Address a conflict that direct conversation has stalled. | C |
| T087 | Restorative conferences | P | Prepared, voluntary dialogue addresses harm and responsibilities. | Consider repair where participants can engage safely. | [RJC](#source-rjc) |
| T088 | Conflict coaching | P | Help a participant prepare for a difficult conversation. | Clarify needs and choices before escalation. | C |
| T089 | Repair conversations | P | Acknowledge an interaction's effects and negotiate changes. | Restore cooperation after a manageable breach. | C |
| T090 | Community moderation | P | Designated participants apply discussion boundaries. | Keep a shared forum usable as participation grows. | C |
| T091 | Guest policies | P | Define how visitors enter and use shared spaces. | Resolve recurring ambiguity in a household. | C |
| T092 | Chore rotations | P | Rotate recurring maintenance responsibilities. | Distribute necessary but unattractive work. | C |
| T093 | Notice-and-claim protocols | P | Announce an item before removing or reallocating it. | Clear abandoned shared-space belongings. | [SN-C](#source-sn-c) |
| T094 | Shared-space labeling | P | Make storage locations and expectations visible. | Reduce repeated household coordination. | [SN-C](#source-sn-c) |
| T095 | Participation stipends | P | Compensate time or expenses incurred by participants. | Make attendance possible beyond those with spare resources. | C |
| T096 | Accessibility arrangements | P | Provide agreed supports for participation. | Include people excluded by the default meeting setup. | C |
| T097 | Confidentiality agreements | P | Agree what information may be shared and with whom. | Support candid discussion of sensitive organizational issues. | C |
| T098 | Cross-community exchanges | P | Arrange visits or joint activities between groups. | Build relationships beyond a familiar social circle. | C |
| T099 | Peer support groups | F | People with related experiences support one another. | Reduce isolation without assuming professional treatment. | C |
| T100 | Rotating hosts | P | Share responsibility for convening recurring gatherings. | Sustain a group beyond its original organizer. | Adaptation: [SN-S](#source-sn-s) |
| T311 | Congregations | F | People sustain recurring shared religious practice and mutual obligations. | Understand community through worship, care, and governance. | C |
| T312 | Pilgrimage | P | A meaningful journey organizes shared commitment and encounter. | Study religious or cultural participation in its own tradition. | C |
| T313 | Mutual-benefit societies | F | Members organize continuing support and benefits for one another. | Study collective care predating or supplementing public provision. | C |
| T314 | Community sponsorship of newcomers | P | A group commits resources and relationships to welcoming new arrivals. | Coordinate practical integration beyond a one-time welcome. | C |


### Decisions and authority

| ID | Technology | Kind | Coordination mechanism | Example / when to consider it | Evidence |
| --- | --- | --- | --- | --- | --- |
| T101 | Assemblies | F | A convened body deliberates on shared matters. | Bring members together for consequential choices. | [OECD](#source-oecd) |
| T102 | Citizens' assemblies | F | A broadly representative recruited group deliberates on public issues. | Examine a complex policy question in depth. | [OECD](#source-oecd) |
| T103 | Citizens' juries | P | A smaller deliberative panel hears evidence and forms recommendations. | Review a bounded public question. | [OECD](#source-oecd) |
| T104 | Town halls | P | An open meeting gathers questions and discussion. | Hear concerns; distinguish consultation from binding decisions. | C |
| T105 | Public consultations | P | Invite input before an authority decides. | Collect affected people's knowledge about a proposal. | [OECD](#source-oecd) |
| T106 | Petitions | P | Aggregate support for a request to an authority. | Demonstrate demand for reconsidering a decision. | C |
| T107 | Referendums | P | Eligible voters decide a specified question directly. | Resolve an issue assigned to the electorate. | C |
| T108 | Sortition | P | Select participants by lottery, sometimes with stratification. | Reduce dependence on self-selection or campaigning. | [OECD](#source-oecd) |
| T109 | Elections | P | Participants select officeholders through a defined ballot process. | Authorize representatives for a term. | C |
| T110 | Appointment | P | An authorized person or body chooses a role holder. | Fill a responsibility requiring specific judgment. | C |
| T111 | Nomination with reasons | P | Explain role nominations before selection. | Make selection criteria discussable. | [S3](#source-s3) |
| T112 | Term limits | P | Limit how long someone may retain an office. | Create predictable leadership turnover. | C |
| T113 | Rotating chairmanship | P | Rotate responsibility for chairing meetings. | Spread facilitation experience and reduce dependence. | C |
| T114 | Recall procedures | P | Provide a defined route to remove a representative. | Respond to lost confidence before a term expires. | C |
| T115 | Delegated authority | P | Give another person specified decision rights. | Move decisions closer to relevant expertise. | C |
| T116 | Subsidiarity | P | Assign decisions to the lowest competent level. | Avoid escalating choices that local groups can handle. | C |
| T117 | Single accountable decision maker | P | One named person decides within a stated remit. | Avoid unclear ownership for a time-sensitive choice. | [SN-D](#source-sn-d) |
| T118 | Advice process | P | A decision maker consults affected people and relevant experts. | Combine initiative with informed input. | [ADV](#source-adv) |
| T119 | Majority voting | P | Adopt an option exceeding half of the relevant votes. | Resolve a binary question under agreed voting rules. | C |
| T120 | Plurality voting | P | The option receiving the most votes wins. | Choose among candidates without requiring a majority. | C |
| T121 | Supermajority voting | P | Require a specified threshold greater than half. | Raise the bar for consequential changes. | C |
| T122 | Unanimity | P | Require every eligible decision maker's agreement. | Give each party a veto over a shared commitment. | C |
| T123 | Consensus process | P | Seek an agreement participants can support or accept under explicit rules. | Work through concerns before committing collectively. | [SEEDS](#source-seeds) |
| T124 | Consent decision-making | P | Test proposals for reasoned objections. | Try a revisable policy. | [S3](#source-s3) |
| T125 | Rough consensus | P | Address substantive objections without equating agreement to a vote tally. | Resolve technical proposals through reasoned discussion. | [IETF](#source-ietf) |
| T126 | Fist-to-five checks | P | Participants signal degrees of support with their hands. | Locate reservations before deciding; specify binding rules separately. | [SN-D](#source-sn-d) |
| T127 | Approval voting | P | Voters mark every acceptable candidate; the highest total wins. | Choose among several acceptable alternatives. | C |
| T128 | Ranked-choice voting | P | Voters rank options; a specified counting rule determines outcomes. | Capture preferences beyond a single first choice. | C |
| T129 | Score voting | P | Voters rate options on a defined scale. | Compare degrees of support with explicit tally rules. | C |
| T130 | Dot voting | P | Participants allocate limited marks across options. | Prioritize discussion topics; avoid treating it as full deliberation. | C |
| T131 | Quadratic voting | P | Additional voting intensity costs progressively more credits. | Explore preference intensity; design identity and budget rules carefully. | C |
| T132 | Liquid democracy | P | Participants vote directly or delegate revocable voting authority. | Allow issue-specific representation. | C |
| T133 | Proxy voting | P | Authorize another person to cast a vote under stated rules. | Represent an absent member. | C |
| T134 | Delegation poker | P | Discuss and compare desired levels of delegated authority. | Clarify how much autonomy a team has. | C |
| T135 | Decision thresholds by impact | P | Match required participation to consequences and reversibility. | Separate minor purchases from membership decisions. | [SN-D](#source-sn-d) |
| T136 | Doocracy | P | People take initiative within understood boundaries. | Complete low-risk reversible work without repeated approval. | [SN-P](#source-sn-p) |
| T137 | BDFL governance | F | A recognized leader retains final authority over project direction. | Understand founder-led coordination and its succession problem. | [OSS](#source-oss) |
| T138 | Steering councils | F | A small group holds defined governance responsibilities. | Distribute project leadership beyond one founder. | [PY](#source-py) |
| T139 | Boards of trustees | F | A governing body stewards an organization's purpose and assets. | Separate enduring oversight from daily management. | C |
| T140 | Worker councils | F | Workers select representatives for collective workplace participation. | Create recurring representation within an enterprise. | C |
| T141 | Circles with domains | F | A team governs a defined responsibility. | Clarify the scope of self-management. | [S3](#source-s3) |
| T142 | Double linking | P | Connect groups through representation in both directions. | Coordinate adjacent governance domains. | [S3](#source-s3) |
| T143 | Federations | F | Autonomous member bodies coordinate through shared arrangements. | Act jointly while retaining local control. | C |
| T144 | Confederations | F | Members retain substantial autonomy under limited shared authority. | Coordinate independent organizations around narrow commitments. | C |
| T145 | Separation of powers | P | Allocate governing functions to different bodies. | Reduce concentrated control through mutual constraints. | C |
| T146 | Constitutions and charters | P | Define basic purposes, rights, offices, and amendment rules. | Make foundational governance commitments explicit. | C |
| T147 | Bylaws | P | Codify internal governance procedures. | Maintain organizational continuity. | [S3](#source-s3) |
| T148 | Quorum rules | P | Require minimum participation for valid decisions. | Prevent a tiny attendance from committing everyone. | C |
| T149 | Agenda-setting procedures | P | Specify how issues reach a decision forum. | Make control of discussion visible and contestable. | C |
| T150 | Speaking queues | P | Maintain an explicit order for contributions. | Reduce competition for attention in a meeting. | C |
| T151 | Facilitated rounds | P | Offer each participant a turn. | Hear voices beyond frequent speakers. | [S3](#source-s3) |
| T152 | Anonymous ballots | P | Separate voter identity from recorded choice. | Reduce interpersonal pressure on a sensitive decision. | C |
| T153 | Conflict-of-interest disclosure | P | Reveal interests relevant to a decision. | Let others evaluate potential bias. | C |
| T154 | Recusal | P | A decision maker steps aside from a particular matter. | Address a specific conflict of interest. | C |
| T155 | Appeals procedures | P | Permit review by another authority under defined grounds. | Correct decisions without relying on personal influence. | C |
| T156 | Ombuds offices | F | Provide an independent channel for concerns and navigation. | Surface problems outside ordinary reporting lines. | C |
| T157 | Sunset clauses | P | Expire a rule unless it is deliberately renewed. | Prevent temporary measures from persisting automatically. | C |
| T158 | Policy review dates | P | Schedule reconsideration of agreements. | Adapt rules as circumstances change. | [S3](#source-s3) |
| T159 | Public decision records | P | Make decisions and reasons accessible to affected people. | Support accountability beyond meeting attendees. | C |
| T160 | Emergency authority with limits | P | Predefine temporary decision powers and their expiry. | Coordinate urgent responses while preserving later review. | C |
| T315 | Collective bargaining | P | Worker and employer representatives negotiate shared employment conditions. | Create agreements beyond individual negotiations. | [ILO](#source-ilo) |
| T316 | Trade unions | F | Workers organize representation and collective interests. | Maintain a continuing basis for workplace voice. | [ILO](#source-ilo) |
| T317 | Arbitration | P | Parties submit a dispute to a designated decision maker. | Resolve a defined dispute through an agreed process. | C |
| T318 | Courts | F | Authorized bodies hear disputes and apply recognized law. | Understand adjudication, remedies, and procedural protections. | C |
| T319 | Jury trials | P | Selected lay participants assess specified questions within a trial. | Distinguish legal adjudication from a citizens' policy jury. | C |
| T320 | Parliamentary procedure | P | Rules organize motions, debate, amendments, and votes. | Handle competing proposals in a formal assembly. | C |
| T321 | Spokescouncils | F | Small groups coordinate through selected spokespeople with defined mandates. | Coordinate many groups while retaining local deliberation. | C |
| T322 | Whistleblowing channels | P | Provide routes for reporting wrongdoing outside implicated authority. | Surface concerns that normal reporting relationships suppress. | C |
| T323 | Freedom-of-information processes | P | Define rights and procedures for requesting public records. | Make official activity more inspectable. | C |
| T324 | Social audits | P | Community participants examine records and actual delivery together. | Compare public commitments with lived implementation. | C |
| T325 | Independent audits | P | An external evaluator examines records or practices against criteria. | Add scrutiny beyond self-reporting. | C |


### Collaboration and production

| ID | Technology | Kind | Coordination mechanism | Example / when to consider it | Evidence |
| --- | --- | --- | --- | --- | --- |
| T161 | Open-source collaboration | F | Combine reusable licensed code with contribution and maintenance processes. | Let independent contributors improve a shared tool. | [OSI](#source-osi) |
| T162 | Commons-based peer production | F | Participants contribute to a shared resource without one employment hierarchy. | Understand collaborative knowledge projects. | C |
| T163 | Project teams | F | Assign a group responsibility for a defined outcome. | Coordinate work with an identifiable completion condition. | C |
| T164 | Working groups | F | Convene participants around a bounded issue or responsibility. | Develop a proposal across existing teams. | C |
| T165 | Task forces | F | Temporarily concentrate people on an urgent objective. | Address an exceptional problem with dedicated capacity. | C |
| T166 | Cross-functional teams | F | Combine different specialties within one working unit. | Reduce repeated handoffs across departments. | C |
| T167 | Autonomous microenterprise units | F | Small internal units hold business responsibilities within a larger enterprise. | Study Haier's approach to distributed entrepreneurship. | [HAIER](#source-haier) |
| T168 | Independent microenterprises | F | Very small businesses organize production and exchange. | Provide local services with a small operating unit. | C |
| T169 | Guilds across teams | F | Practitioners coordinate standards and learning across delivery teams. | Keep a specialty connected without centralizing all work. | C |
| T170 | Hackathons | P | Time-bound gatherings concentrate collaborative making. | Prototype ideas and identify potential collaborators. | C |
| T171 | Sprints | P | Commit to a short work cycle followed by review. | Deliver progress in manageable increments. | C |
| T172 | Work parties | P | Convene people to complete a shared physical task. | Maintain a garden or improve a common space. | C |
| T173 | Barn-raising | P | Community members pool labor for a substantial construction effort. | Understand reciprocal labor beyond individual household capacity. | C |
| T174 | Pair work | P | Two people work together on the same task. | Share judgment and catch misunderstandings early. | C |
| T175 | Mob or ensemble work | P | A group collaborates on one task with rotating active roles. | Combine expertise on a difficult shared problem. | C |
| T176 | Shared task boards | P | Make pending work, ownership, and progress visible. | Coordinate distributed contributions. | C |
| T177 | Pull systems | P | Take new work when capacity becomes available. | Limit overload. | [S3](#source-s3) |
| T178 | Work-in-progress limits | P | Cap concurrent tasks at a chosen stage. | Expose bottlenecks and encourage completion. | C |
| T179 | Issue triage | P | Sort incoming requests by relevance, urgency, and ownership. | Keep a public project backlog usable. | C |
| T180 | Request-for-comments processes | P | Circulate written proposals before adopting changes. | Gather review from people who cannot meet together. | C |
| T181 | Design reviews | P | Review a proposed solution before committing to implementation. | Catch incompatible assumptions across specialties. | C |
| T182 | Contribution guidelines | P | Explain how to submit, review, and accept work. | Reduce newcomer guesswork in a shared project. | Adaptation: [OSS](#source-oss) |
| T183 | Maintainer delegation | P | Assign responsibility for reviewing and integrating contributions. | Scale work beyond one central reviewer. | [OSS](#source-oss) |
| T184 | Forking | P | Create an independently governed derivative of a shared project. | Allow divergent directions where licensing permits. | Adaptation: [OSI](#source-osi) |
| T185 | Release governance | P | Specify who can authorize and coordinate a release. | Make publication responsibilities predictable. | C |
| T186 | Standards bodies | F | Participants negotiate shared technical or procedural specifications. | Enable interoperability across independent organizations. | C |
| T187 | Protocols and interfaces | P | Agree how separate actors exchange requests and results. | Coordinate without sharing every internal process. | C |
| T188 | Standard operating procedures | P | Document repeatable operations and escalation points. | Make routine work transferable. | C |
| T189 | Checklists | P | Prompt verification of specified steps or conditions. | Reduce omissions in repeatable workflows. | C |
| T190 | Handoff protocols | P | Transfer responsibility with explicit context and acknowledgment. | Preserve continuity between shifts or teams. | C |
| T191 | Responsibility matrices | P | State who acts, approves, advises, and is informed. | Resolve overlapping expectations in a project. | C |
| T192 | Service-level agreements | P | Define expected service, measurement, and response obligations. | Coordinate between teams providing and consuming a service. | C |
| T193 | Rotating duty rosters | P | Allocate recurring coverage through a schedule. | Maintain support while sharing undesirable shifts. | C |
| T194 | Incident command | F | Temporarily organize response around explicit command and coordination roles. | Manage a complex disruption. | C |
| T195 | Blameless postmortems | P | Examine contributing conditions without defaulting to individual blame. | Learn from failure while retaining responsibility for improvements. | C |
| T196 | Communities of contribution | F | Participants organize around maintaining a shared artifact or cause. | Connect occasional help to durable stewardship. | C |
| T197 | Volunteer matching | P | Match available skills and time to specified needs. | Turn willingness to help into concrete commitments. | C |
| T198 | Time-boxed commitments | P | Agree on bounded periods of responsibility. | Let volunteers contribute without indefinite obligations. | C |
| T199 | Public pledges | P | Make a commitment visible to an audience. | Coordinate expectations around a future contribution. | C |
| T200 | Accountability partners | P | Peers periodically check progress on agreed commitments. | Sustain work that otherwise receives little feedback. | C |
| T201 | Coworking sessions | P | People work alongside one another at an agreed time. | Create social support for independent tasks. | C |
| T202 | Distributed campaigns | F | Independent local actors coordinate around shared objectives and materials. | Adapt collective action to different local contexts. | C |
| T203 | Coalitions | F | Separate organizations cooperate on a shared objective. | Combine capabilities without requiring a merger. | C |
| T204 | Collective impact partnerships | F | Organizations align goals, measures, and ongoing coordination. | Study sustained cooperation across service providers. | C |
| T205 | Boundary-spanning roles | P | Assign someone to connect groups with different vocabularies or priorities. | Reduce misunderstandings across organizational interfaces. | C |
| T206 | Minimum specifications | P | Specify only essential constraints. | Leave room for local methods. | [LS](#source-ls) |
| T207 | 15% Solutions | P | Identify actions within existing discretion. | Start without waiting for additional authority. | [LS](#source-ls) |
| T208 | Discovery-and-Action Dialogue | P | Explore obstacles and locally successful behaviors. | Find practical responses within a group. | [LS](#source-ls) |
| T209 | What I Need From You | P | Exchange concrete requests across groups. | Clarify dependencies. | [LS](#source-ls) |
| T210 | Purpose-to-Practice | P | Connect purpose with participants and working arrangements. | Design a shared initiative. | [LS](#source-ls) |
| T326 | Strikes | P | Workers collectively withhold labor around stated demands. | Understand bargaining power and collective coordination. | C |
| T327 | Boycotts | P | Participants coordinate refusal to purchase or cooperate. | Express pressure through organized nonparticipation. | C |
| T328 | Citizen journalism | P | Community participants gather and publish public-interest reporting. | Document issues overlooked by established media. | C |
| T329 | Monastic orders | F | Religious communities organize life through shared rules and commitments. | Study durable collective practice in its historical tradition. | C |
| T330 | Joint ventures | F | Separate organizations establish a shared undertaking. | Combine resources while retaining distinct parent organizations. | C |
| T331 | Franchising | F | Independent operators use a shared brand and operating arrangement. | Study replication through contractual standards and support. | C |


### Resources and ownership

| ID | Technology | Kind | Coordination mechanism | Example / when to consider it | Evidence |
| --- | --- | --- | --- | --- | --- |
| T211 | Markets | P | Prices and exchange coordinate supply, demand, and allocation. | Compare decentralized allocation with negotiated or planned alternatives. | [ECON](#source-econ) |
| T212 | Auctions | P | Allocate goods or contracts through structured bidding. | Discover offers when demand or value is uncertain. | C |
| T213 | Double auctions | P | Buyers and sellers both submit offers under matching rules. | Organize repeated exchange across many participants. | C |
| T214 | Barter | P | Exchange goods or services directly. | Trade without a common monetary payment. | C |
| T215 | Mutual credit | P | Track reciprocal credits and obligations within a network. | Support exchange without requiring each trade to balance bilaterally. | C |
| T216 | Time banking | P | Account for service exchanges using time credits. | Coordinate reciprocal practical help. | [TIME](#source-time) |
| T217 | Local currencies | P | Use a means of exchange within a defined community. | Study efforts to retain exchange within a network. | C |
| T218 | Gift economies | S | Giving and reciprocal obligations organize circulation. | Understand exchange that is not priced transaction by transaction. | C |
| T219 | Reciprocal labor exchanges | P | Participants return labor across different tasks or occasions. | Coordinate seasonal work among households. | C |
| T220 | Rotating savings groups | F | Members contribute regularly and take turns receiving the pooled sum. | Understand collective saving with scheduled access. | C |
| T221 | Credit unions | F | Members jointly own a financial cooperative. | Study member-governed provision of financial services. | C |
| T222 | Mutual insurance | F | Members pool risks through an insurer organized for their benefit. | Understand collective coverage of uncertain losses. | C |
| T223 | Emergency mutual-aid funds | P | Pool contributions for agreed urgent needs. | Respond to hardship beyond individual reserves. | C |
| T224 | Crowdfunding | P | Raise contributions from many supporters for a defined project. | Test support for a proposed public artifact. | C |
| T225 | Crowdlending | P | Multiple lenders finance borrowers through coordinated arrangements. | Compare distributed lending with a single financier. | C |
| T226 | Subscriptions | P | Participants pay periodically for continuing access or support. | Fund recurring work with predictable contributions. | C |
| T227 | Membership dues | P | Members contribute under shared funding rules. | Cover a club's recurring collective costs. | C |
| T228 | Patronage | P | A supporter funds another's ongoing work or institution. | Sustain work that lacks direct paying customers. | C |
| T229 | Grants | P | Allocate funds toward specified purposes through selection processes. | Support work whose benefits are not easily sold. | C |
| T230 | Prize competitions | P | Offer a reward for achieving a defined result. | Attract multiple approaches to a bounded challenge. | C |
| T231 | Bounties | P | Attach a reward to completion of a specified task. | Recruit help for a concrete missing contribution. | C |
| T232 | Participatory budgeting | P | Community members help decide allocation of a budget. | Give residents authority over part of public spending. | [PB](#source-pb) |
| T233 | Quadratic funding | P | Use a matching formula that rewards breadth of financial support. | Explore funding of shared goods; examine identity manipulation risks. | C |
| T234 | Matching grants | P | Release funding conditional on another contribution. | Encourage co-funding of a shared project. | C |
| T235 | Endowments | F | Steward assets to support an institution over time. | Reduce dependence on a single annual fundraising cycle. | C |
| T236 | Pooled procurement | P | Combine purchasing needs across participants. | Negotiate supply for a group of small buyers. | C |
| T237 | Buying clubs | F | Members jointly arrange repeated purchases. | Access goods through coordinated demand. | C |
| T238 | Tool libraries | F | Maintain tools for shared borrowing. | Provide occasional access without individual ownership. | C |
| T239 | Resource booking systems | P | Agree how scarce shared resources are reserved and released. | Coordinate use of a workshop or common room. | C |
| T240 | Queues | P | Allocate service in an agreed sequence. | Make access predictable when capacity is limited. | C |
| T241 | Allocation lotteries | P | Randomly distribute a scarce benefit among eligible applicants. | Avoid discretionary favoritism where claims are comparable. | C |
| T242 | Needs-based allocation | P | Prioritize resources according to explicit assessments of need. | Distribute limited support across unequal circumstances. | C |
| T243 | Rationing | P | Limit individual access under defined allocation rules. | Manage a shortage without unrestricted first arrival. | C |
| T244 | Tradable quotas | P | Set aggregate limits and permit transfer of allocated shares. | Study coordination under a collectively imposed resource cap. | C |
| T245 | Commons governance | F | Users collectively maintain rules for a shared resource. | Study sustainable use beyond simple state-versus-market categories. | [OST](#source-ost) |
| T246 | Resource boundaries | P | Identify the resource and legitimate users. | Clarify who participates in commons governance. | C |
| T247 | User participation in rulemaking | P | Affected users help revise operational rules. | Adapt management to local conditions. | C |
| T248 | Community monitoring | P | Users or accountable monitors observe compliance. | Make shared commitments observable. | C |
| T249 | Graduated sanctions | P | Responses escalate with severity or repetition. | Address breaches without treating every case identically. | C |
| T250 | Community land trusts | F | Community organizations steward land for lasting local benefit. | Maintain assets beyond short-term individual resale incentives. | [CLT](#source-clt) |
| T251 | Worker cooperatives | F | Workers jointly own and democratically govern an enterprise. | Align work and ownership. | [ICA](#source-ica) |
| T252 | Consumer cooperatives | F | Customers jointly own and govern a provider. | Organize provision around member needs. | [ICA](#source-ica) |
| T253 | Producer cooperatives | F | Producers jointly organize shared services or market access. | Coordinate distribution among small producers. | [ICA](#source-ica) |
| T254 | Housing cooperatives | F | Members collectively organize housing ownership or provision. | Share residential governance. | [ICA](#source-ica) |
| T255 | Multistakeholder cooperatives | F | Different stakeholder groups share an enterprise's governance. | Balance member interests. | Adaptation: [ICA](#source-ica) |
| T256 | Employee ownership | F | Employees hold ownership interests under a defined arrangement. | Compare ownership participation with worker control. | C |
| T257 | Steward ownership | F | Ownership arrangements protect purpose and responsible control. | Study alternatives to unrestricted investor control. | C |
| T258 | Revenue sharing | P | Distribute defined shares of revenue among participants. | Coordinate collaborators with different contributions. | C |
| T259 | Profit sharing | P | Distribute part of surplus according to an agreed formula. | Connect compensation to collective results. | C |
| T260 | Transparent compensation formulas | P | Publish the criteria used to determine pay. | Make compensation reasoning open to scrutiny. | C |
| T261 | Rent allocation formulas | P | Agree how room differences and shared costs affect rent. | Reduce recurring bargaining in a shared household. | C |
| T262 | Fiscal sponsorship | F | An established organization administers support for an aligned project. | Explore support for a project without a separate organization. | C |
| T263 | Community-supported agriculture | F | Members commit to a farm's production through advance participation. | Share aspects of production risk and seasonal supply. | C |
| T264 | Repair cafés | P | Volunteers help people repair belongings at organized gatherings. | Share skills and extend the use of goods. | C |
| T265 | Swap events | P | Convene people to exchange reusable items. | Redistribute goods that participants no longer need. | C |
| T266 | Escrow | P | A third party holds assets pending agreed conditions. | Coordinate exchange when performance occurs at different times. | C |
| T267 | Contracts | P | Specify commitments and remedies between parties. | Clarify responsibilities for a joint undertaking. | C |
| T268 | Open licensing | P | Grant advance permissions for specified forms of reuse. | Allow collaboration without negotiating each permission separately. | [OSI](#source-osi) |
| T269 | Copyleft | P | Condition redistribution on preserving specified licensing freedoms. | Maintain downstream sharing obligations. | C |
| T270 | Public provisioning | F | Public bodies organize access to goods or services. | Compare collective provision with individual purchasing. | C |
| T332 | Taxation | P | Public authorities collect resources under defined rules. | Understand how collective functions are financed. | C |
| T333 | Double-entry accounting | P | Maintain linked records of transactions within a balancing system. | Make organizational resource flows inspectable. | C |
| T334 | Public asset registers | P | Record assets, stewardship responsibilities, and relevant rights. | Clarify what an institution holds and who maintains it. | C |
| T335 | Assurance contracts | P | Contributions take effect only if specified participation conditions are met. | Coordinate a project requiring a minimum funding threshold. | C |
| T336 | Risk-sharing pools | P | Agree how uncertain costs are distributed among participants. | Compare collective exposure with isolated individual risk. | C |


### Recognition and succession

| ID | Technology | Kind | Coordination mechanism | Example / when to consider it | Evidence |
| --- | --- | --- | --- | --- | --- |
| T271 | Credentials | P | Recognized attestations communicate qualifications. | Help strangers assess claimed competence. | [GFT](#source-gft) |
| T272 | Certification | P | Assess conformity with defined requirements and attest results. | Make a specific standard legible across organizations. | C |
| T273 | Accreditation | P | Evaluate organizations or programs against recognized criteria. | Support trust in institutions that train or assess others. | C |
| T274 | Professional licensing | P | Authorize practice through a public regulatory arrangement. | Understand entry controls and public accountability. | C |
| T275 | Portfolios | P | Present examples of completed work. | Evaluate demonstrated capability beyond formal credentials. | C |
| T276 | References | P | People with direct experience offer testimony about someone. | Add context to a selection decision. | C |
| T277 | Reputation systems | P | Aggregate assessments of past interactions. | Help unfamiliar participants evaluate prospective partners. | C |
| T278 | Contribution records | P | Document work, maintenance, and support that people provide. | Recognize contributions otherwise overlooked. | C |
| T279 | Awards | P | Publicly recognize selected achievements. | Direct attention to work a community values. | [GFT](#source-gft) |
| T280 | Peer nominations | P | Invite participants to identify others' contributions. | Surface valuable work beyond managers' visibility. | C |
| T281 | Public appreciation | P | Make specific contributions visible and acknowledged. | Recognize everyday maintenance in shared living. | [SN-C](#source-sn-c) |
| T282 | Contributor credits | P | Attribute work to its contributors. | Preserve recognition in a collective artifact. | C |
| T283 | Authorship conventions | P | Agree what contribution qualifies for authorship and ordering. | Reduce ambiguity around credit before publication. | C |
| T284 | Merit-based selection | P | Select using explicit evidence relevant to the responsibility. | Choose a maintainer through demonstrated work; scrutinize criteria. | C |
| T285 | Seniority rules | P | Assign priority according to length of participation or service. | Make advancement or allocation predictable. | C |
| T286 | Competitive examinations | P | Use a common assessment to compare applicants. | Select at scale under published criteria. | C |
| T287 | Work-sample assessments | P | Evaluate performance on a relevant task. | Assess practical capability for a specific role. | C |
| T288 | Auditions | P | Observe candidates performing representative work. | Select performers or contributors through demonstration. | C |
| T289 | Trial projects | P | Use a bounded collaboration before a longer commitment. | Test working compatibility and capability. | C |
| T290 | Blind review | P | Conceal specified identity information during evaluation. | Reduce some identity cues in initial assessment. | C |
| T291 | Peer promotion | P | Existing participants evaluate readiness for greater responsibility. | Expand a project's trusted contributor group. | Adaptation: [OSS](#source-oss) |
| T292 | Sponsorship for advancement | P | An established member advocates for someone's opportunities. | Connect demonstrated ability to access and responsibility. | C |
| T293 | Succession planning | P | Identify and prepare people to assume critical responsibilities. | Reduce disruption when a founder leaves. | [GFT](#source-gft) |
| T294 | Deputy roles | P | Give a second person substantive responsibility alongside a role holder. | Build continuity and an informed substitute. | C |
| T295 | Overlapping handovers | P | Incoming and outgoing role holders work together temporarily. | Transfer judgment as well as documents. | C |
| T296 | Graduated responsibility | P | Increase authority as capability is demonstrated. | Develop successors without transferring everything at once. | C |
| T297 | Leadership pipelines | F | Connect development experiences to progressively demanding roles. | Prepare future leaders across generations. | C |
| T298 | Founder transition agreements | P | Specify the founder's future authority and transfer of control. | Avoid ambiguity after operational leadership changes. | C |
| T299 | Emeritus roles | P | Retain optional advisory affiliation after active responsibility ends. | Preserve knowledge without blocking new leadership. | C |
| T300 | Exit interviews | P | Ask departing participants about their experience and unfinished work. | Detect issues missed by routine feedback. | C |
| T301 | Institutional memory interviews | P | Capture a role holder's reasoning and relationships before departure. | Transfer context absent from formal procedures. | C |
| T302 | Backup ownership | P | Assign an informed alternate for important responsibilities. | Maintain continuity during absence. | C |
| T303 | Stewardship terms | P | Assign responsibility for a defined period with review. | Renew commitment without making positions permanent. | C |
| T304 | Knowledge succession demonstrations | P | Have successors perform critical work before handover. | Check that competence transferred alongside authority. | Adaptation: [GFT](#source-gft) |
| T305 | Lineage recognition | P | Trace teaching or authority through acknowledged predecessors. | Understand continuity claims in craft or religious traditions. | C |
| T306 | Oaths of office | P | Publicly affirm obligations attached to a role. | Mark accountability when assuming authority. | C |
| T337 | Peer juries for awards | P | A selected panel evaluates submissions against stated criteria. | Distribute recognition using deliberated judgments. | C |
| T338 | Recallable stewardship | P | Grant stewardship with an explicit community removal process. | Combine continuing responsibility with contestable authority. | C |


## 7. Systems, domains, and historical arrangements

These orientation pages explain bundles and connect them to actionable components. The original 20 page outlines remain useful, but broad domains such as healthcare should not appear to be interchangeable with a meeting technique. The table preserves the remaining original concepts and adds the larger systems discussed later.

| ID | Concept | Kind | What the page should distinguish | Illustrative context / components | Evidence |
| --- | --- | --- | --- | --- | --- |
| S001 | Capitalism | S | Private capital, employment, investment, and markets are related but distinct. | Compare ownership and allocation arrangements. | [ECON](#source-econ) |
| S002 | Socialism | S | A contested family of social-ownership arrangements, not one operational recipe. | Compare cooperative, public, and planned forms; further research required. | C |
| S003 | Economic planning | S | Allocation through plans can coexist with markets. | Compare centralized planning and participatory planning variants. | C |
| S004 | Democracy | S | Participation, representation, rights, and decision rules vary independently. | Link assemblies, elections, sortition, and accountability. | C |
| S005 | Aristocracy | S | Rule by a privileged elite; historical forms often involve hereditary status. | Examine inherited authority and exclusion; not a recommendation. | C |
| S006 | Meritocracy | S | An ideal or legitimating account of rule by merit, distinct from a particular selection procedure. | Ask who defines merit and who has opportunities to demonstrate it. | C |
| S007 | Technocracy | S | Authority grounded in claimed technical expertise. | Compare expert advice with expert control. | C |
| S008 | Monarchy | S | Authority vested in a monarch under varying succession and constitutional rules. | Connect hereditary succession, appointment, and checks on authority. | C |
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
| S028 | Polycentric governance | S | Multiple decision centers with overlapping or nested responsibilities. | Compare resource governance across local and wider levels. | C |
| S029 | Open-source ecosystems | S | Licenses, maintainers, users, contributors, funders, and governance interact. | Distinguish permission to reuse from power to decide. | [OSI](#source-osi), [OSS](#source-oss) |
| S030 | Extitutional theory | S | A relational analytical lens, not an organizational template. | Study participation and mutual recognition alongside formal roles. | [EXT](#source-ext) |
| S031 | Assembly democracy | S | Members exercise collective authority through a convened assembly; distinguish eligibility from attendance and a binding body from an advisory forum. | Compare a member assembly, a mass referendum, and an elected legislature. | Adaptation: [DEM](#source-dem), [ATH](#source-ath) |
| S032 | Direct democracy | S | Eligible participants decide issues themselves; universal turnout and face-to-face discussion are not requirements. | Compare assembly decisions and referendums; specify proposal rights and voting rules. | [DEM](#source-dem) |
| S033 | Representative democracy | S | Elected representatives exercise decision authority on behalf of constituents. | Examine mandates, discretion, oversight, and decisions reserved to voters. | [DEM](#source-dem) |
| S034 | Athenian democracy | S | A historically changing combination of assembly, council, courts, lot, and elections within a restricted citizen body. | Study participation and institutional composition without treating it as a small-group model or modern universal suffrage. | [ATH](#source-ath) |

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
| D014 | Homophily | Similar people may form ties more readily. | Does apparent shared interest conceal restricted access? | C |
| D015 | Reciprocity | Help can create expectations of future return. | Are those expectations understood and sustainable? | C |
| D016 | Trust formation and repair | Reliability, interpretation, and vulnerability affect willingness to cooperate. | What would demonstrate changed behavior after a breach? | C |
| D017 | Free riding | Some benefit without contributing to maintenance. | Distinguish unwillingness from inability and unclear expectations. | C |
| D018 | Social loafing | Individual effort may decline when contributions are difficult to identify. | Make responsibilities intelligible without excessive surveillance. | C |
| D019 | Volunteer burnout | Work concentrates on people who struggle to disengage. | Bound commitments, distribute responsibility, and enable succession. | C |
| D020 | Status hierarchies | Prestige shapes whose speech and work receive attention. | Are evaluations tracking relevant contributions? | C |
| D021 | Preference falsification | Public agreement can conceal private disagreement. | Offer credible channels for dissent. | C |
| D022 | Pluralistic ignorance | People can misread one another's private beliefs from public behavior. | Test assumptions about what others support. | C |
| D023 | Group polarization | Discussion can shift participants toward more extreme positions. | Include substantive disagreement and examine information sources. | C |
| D024 | Groupthink | Pressure for cohesion may suppress critical examination. | Assign challenge roles and separate proposals from commitments. | C |
| D025 | Goal displacement | Procedures or proxy measures become objectives themselves. | Compare measured success with the original purpose. | C |
| D026 | Metric gaming | Rewards attached to indicators encourage strategic reporting or behavior. | Examine what the indicator leaves out. | C |
| D027 | Capture | A subset redirects governance toward its own interests. | Inspect entry, oversight, appeals, and concentrated benefits. | C |
| D028 | Principal-agent problems | Delegates and delegators have differing incentives or information. | Clarify discretion, reporting, and accountability. | C |
| D029 | Path dependence | Earlier choices constrain later possibilities. | Identify switching costs before adding another dependency. | C |
| D030 | Norm drift | Expectations change through repeated behavior and shifting membership. | Compare stated norms with actual practice. | C |
| D031 | Network brokerage | Intermediaries connect groups that otherwise interact little. | Who controls access, interpretation, and introductions? | C |
| D032 | Boundary maintenance | Communities negotiate membership and acceptable participation. | Can boundaries protect purpose without insulating power? | C |

## 9. Research sources and provenance

Codes link inventory entries to research trails. A source may describe a practice without testing its effectiveness. The candidate label C intentionally leaves gaps visible rather than attaching loosely related citations. Search-result extracts were sufficient for discovery of some entries; full entry drafting still requires reading and checking the primary material.

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

### Further collections to mine

- [Supernuclear directory](https://supernuclear.substack.com/p/the-supernuclear-directory-9a9078a07258): shared living, financing, ownership, governance, rituals, and maintenance.
- [Group Works patterns by category](https://groupworksdeck.org/patterns_by_category): an additional vocabulary for facilitation, context, relationship, and group process. Many are design qualities rather than independent techniques, so avoid mechanically turning every card into a technology page.
- [Participedia](https://participedia.net/): participation methods and documented cases; useful for separating a named method from its implementation in a specific place.
- [Liberating Voices / Public Sphere Project](https://labs.publicsphereproject.org/): civic communication and collective action patterns.
- [ILO explanation of collective bargaining](https://www.ilo.org/resource/what-collective-bargaining): primary institutional starting point for worker representation and negotiated employment conditions.

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

The breadth here exceeds the evidence depth. **286 entries remain marked C**; the remaining 118 have a source trail or an explicitly labeled adaptation, not necessarily evidence of effectiveness. Prioritize sources for entries marked C, especially voting systems, finance and ownership, kinship, religious organization, labor organizing, and non-Western governance traditions. For living traditions, use practitioner and community-authored sources alongside scholarship. Distinguish an account of what people do from evidence that it produces a desired outcome.

Additional research families include Indigenous and customary governance; religious orders and congregations; rotating credit and mutual-aid traditions across regions; labor unions and industrial democracy; diplomacy and peacebuilding; mutualist and solidarity economies; public-health coordination; disaster-response organizations; and scientific institutions. Names alone are insufficient: collect mechanisms, contexts, failure modes, and documented cases.

### First publication wave

Begin with a practical cross-section: mentorship, apprenticeship, lightning talks, recurring gatherings, community wikis, cohort onboarding, assemblies, consent, advice process, decision thresholds, doocracy, BDFL governance, steering councils, open-source collaboration, autonomous microenterprises, markets, cooperatives, participatory budgeting, commons governance, and succession planning. Pair them with short orientation pages for social technologies and the institutional/extitutional lenses.

The inventory is the expansion backlog. Keep the deployed site static: templates, Markdown content, generated category anchors, an alphabetical index, related links, and a sitemap. Add the small client-side search module described above. Accounts, a database, and an application framework are unnecessary; ordinary browsing remains available without JavaScript.
