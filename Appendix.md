## **Appendix A: FOAM implementation details and audit artifacts**

### **A.1 Stance vectors and perspective-node schema**

FOAM instantiates **differentiated agents** by attaching an explicit **stance vector/perspective node to each agent, representing a multidimensional** encoding of epistemic and normative commitments (e.g., epistemological orientation, evidentiary standards, and impact ethics). Our current implementation represents this as a 24-dimensional space with coherence scoring to ensure agents remain internally consistent during deliberation.

**Data structure (reference implementation).** We recommend treating the stance vector as a typed record (not a free-form prompt paragraph), and storing it as both:

1. **Machine-readable metadata** used for routing, consistency checks, and downstream prompt injection; and  
2. **Human-readable disclosure** rendered as a compact “stance card” (for contestability).

A practical schema:

* `stance_id`: stable identifier (UUID)  
* `role_label`: short label (e.g., “Public-health regulator”, “Civil-liberties advocate”)  
* `epistemic_axes[ ]`: list of scalar axes (e.g., 0–1 or \-1–1), each with name \+ value \+ brief rationale  
* `evidence_policy`: admissibility thresholds (e.g., “peer-reviewed preferred; allow gray lit with caveats”)  
* `value_priorities`: explicit ordering or weights (e.g., {harm\_minimization:0.3, autonomy:0.2, …})  
* `scope_limits`: jurisdiction/time horizon assumptions  
* `coherence_constraints`: predicates used for drift detection (below)  
* `disclosure_text`: 2–4 sentences that summarize the stance for stakeholders

**Coherence scoring (drift detection).** 

* Maintain a rolling “stance consistency report” per agent turn:  
  * **Hard constraints:** disallowed contradictions (e.g., “claims only RCT evidence counts” then relies exclusively on anecdote without flagging it).  
  * **Soft constraints:** tolerable deviations that must be logged as exceptions (“I’m using weaker evidence due to sparse corpus coverage”).  
* Output: `coherence_score ∈ [0,1]` plus a list of violated constraints, used as a gating signal for regeneration or escalation to the evaluator agent.

### **A.2 Dialectical refinement protocol (proposer–critic–evaluator)**

Our core deliberative loop uses three roles—**proposer**, **critic**, **evaluator**—and iterates **at least three times** before convergence.

**Algorithm A1 (Dialectical refinement, reference form).**

**Inputs:** `task T`, `stance vector s`, `initial proposal p0`, `min_iters = 3`, `max_iters = K`, `stop_eps`  
**Outputs:** refined proposal `p*`, critique log `C`, evaluation log `E`

1. Set `p ← p0`  
2. For `i in 1..K`:  
   1. **Critic step:** generate critique `c_i = Critic(T, s, p)`  
      * Must include: (a) weakest warrants, (b) missing evidence hooks, (c) likely stakeholder objections.  
   2. **Evaluator step:** produce evaluation `e_i = Evaluator(T, s, p, c_i)`  
      * Must classify each critique as: `valid`, `invalid`, or `requires_more_evidence`  
      * Must recommend: `revise`, `defend`, or `branch`  
   3. **Proposer revision:** update proposal `p ← Proposer(T, s, p, c_i, e_i)`  
   4. Append `c_i` to `C` and `e_i` to `E`  
   5. If `i ≥ min_iters` and improvement `< stop_eps`, break  
3. Return `p* = p` with logs `C, E`

**Audit artifact:** Store each `c_i` and `e_i` in the mediation graph (Appendix A.4), enabling stakeholders to contest *why* a criticism was accepted/rejected.

### **A.3 Sublation operator output format**

We distinguish sublation from winner-take-all selection or averaging, producing a synthesis that preserves productive tension.

A FAccT-friendly implementation detail is to force the operator to emit **two coupled artifacts**:

1. `Synthesis`: the “best current” integrated position (actionable, coherent)  
2. `Dissent memo`: structured minority report capturing:  
   * the strongest unresolved objection(s),  
   * which stance(s) raised them,  
   * what empirical evidence would change the conclusion,  
   * what value trade-off is being made (explicitly)

**Template (required fields).**

* **Synthesis (1–2 paragraphs)**  
* **What we agree on (bullets; cite evidence IDs)**  
* **Open disagreements (bullets; cite critique IDs)**  
* **Dissent memo (short; attributable to stance IDs, not people)**  
* **Contestability hooks:** “To challenge this, dispute (a) evidence sentence IDs, (b) warrants, or (c) value weights.”

### **A.4 Mediation graph and provenance log schema**

To make deliberation inspectable, we recommend explicitly logging a **mediation graph**.

**Node types (minimum viable).**

* `AgentTurn` (role, stance\_id, timestamp, model\_id)  
* `Claim` (normalized, typed syllogism slot)  
* `Warrant`  
* `EvidenceSentence` (doc\_id, sent\_id)  
* `Critique`  
* `Evaluation`  
* `Synthesis`  
* `ValidationResult` (exact/partial/paraphrase/fabricated)

**Edge types.**

* `proposes(AgentTurn → Claim)`  
* `supports(EvidenceSentence → Claim)`  
* `warrants(Warrant → Claim)`  
* `attacks(Critique → Claim/Warrant/EvidenceSentence)`  
* `rates(Evaluation → Critique)`  
* `revises(AgentTurn → Claim)`  
* `synthesizes(Synthesis → Claim-set)`  
* `validates(ValidationResult → EvidenceSentence)`

**JSONL record (illustrative).**

* `event_id`, `event_type`, `parent_ids[]`, `stance_id`, `artifact_id`, `payload{...}`

## **Appendix B: Evidence-grounded debate generation pipeline details**

### **B.1 Phase 1 — Perspective assignment (seeding)**

**Goal:** Initialize diversity by selecting a perspective node (stance vector) to be tracked across all downstream prompts and checks.

**Reference procedure.**

1. Determine stakeholder set `S` (domain-dependent; for debate cases, map to common strategic orientations).  
2. Select `m` stance vectors:  
   * (a) fixed library (predefined stances) and/or  
   * (b) programmatic sampling over the 24-D space  
3. Run stance coherence self-check; write `stance_card` disclosure.

### **B.2 Phase 2 — Plan generation with dialectical refinement**

**Goal:** generate multiple candidate high-level strategies consistent with the stance vector, then refine through the proposer/critic/evaluator loop with a minimum of three iterations.

**Artifact:** `plantext` containing:

* strategic goal,  
* argument portfolio,  
* anticipated opposition,  
* evidence needs (queries to retrieve).

### **B.3 Phase 3 — Template tree traversal (typed syllogisms \+ validators)**

**Template node contract.**

* `template_type`: one of the 15 syllogism types  
* `slots`: required fields (Claim, Grounds, Warrant, Backing, Qualifier, Rebuttal, plus debate-specific slots)  
* `validators`: slot-level checks (non-empty, evidence-linked, stance-consistent)  
* `children`: refinements/variants (e.g., different impact calculus)

**Validator behavior (recommended).**

* If a required slot is missing: trigger *targeted generation* for that slot only (rather than re-generating the whole argument).  
* If evidence is missing: trigger phase-4 retrieval constrained to that slot.

### **B.4 Phase 4 — Research with sentence-level provenance (mechanism spec)**

We describe Phase 4 as our “critical innovation for contestability”: instead of asking an LLM to reproduce the source text, we number sentences in source documents and have the LLM output sentence indices, plus tags that connect evidence to argument structure. The model “never generates source content, only sentence indices.”

**Evidence record schema (minimum viable).**

* `doc_id` (stable)  
* `url` (or corpus pointer)  
* `sent_ids[]` (integer list)  
* `quote_text` (server-side assembled verbatim from the indexed sentences)  
* `tag` (what this evidence supports)  
* `links_to`: `{claim_id, syllogism_slot}`

**Retrieval sources.** Your draft notes querying a vector DB of \~85,000 cards from OpenDebateEvidence plus previously processed sources.

**Safety/faithfulness invariant (must hold).**

* The LLM may propose *which* sentence IDs to cite, but the system—not the model—assembles the quoted text.  
* Invalid IDs hard-fail validation (no silent fallback to paraphrase).

### **B.5 Phase 5 — Compilation and verification (checks)**

**Verification checklist (recommended).**

* **Stance consistency:** no contradiction with stance constraints without an explicit exception note.  
* **Slot completeness:** all required typed-syllogism slots filled.  
* **Evidence linkage:** every non-trivial claim has ≥1 `EvidenceSentence` edge.  
* **Evidence freshness disclaimer:** if the corpus is time-bounded, label it.  
* **Compilation integrity:** no dangling citations; all doc/sentence IDs resolvable.

---

## **Appendix C: Tournament evaluation and evidence validation details**

This appendix provides the full evaluation procedure for your double-blind tournament of **66 policy debate cases**, including category sizes, blinding, bracket structure, scoring dimensions, and the evidence validation pipeline.

### **C.1 Corpus composition and anonymization**

The corpus comprised three generation methods (structured system n=22; human expert baseline n=23; zero-shot AI n=21) and was anonymized with unique tournament IDs to prevent origin detection.

## **The Mega‑Prompt used for zero-shot AI**

You are a veteran **American policy debate coach and evidence editor**. Your task is to generate **distinct, high‑quality First Affirmative Constructives (1ACs)** that mirror the structure and tone used by elite programs and summer institutes (e.g., Michigan, DDI, CNDI). Treat this as a professional brief‑writing assignment.

### **PARAMETERS (edit these)**

* **\[RESOLUTION\]**: “Resolved: The United States federal government should substantially \[insert the resolution text verbatim\].”

* **\[NUM\_CASES\]**: 40 *(any number up to 40\)*

* **\[OUTPUT\_MODE\]**: `OUTLINE` or `FULL`

  * `OUTLINE` \= index \+ case skeletons (fast overview)

  * `FULL` \= complete 1AC text for the requested cases

* **\[CASE\_SELECTION\]**: `ALL` or a comma‑separated list of case numbers (e.g., `3, 9, 17`) *(use when OUTPUT\_MODE=FULL)*

* **\[AFF\_TYPE\_MIX\]**: `{ "policy": 70, "kritik": 20, "hybrid/performance": 10 }` *(percent split across the set)*

* **\[READ\_TIME\_MIN\]**: 8 *(minutes of 1AC speaking time)*

* **\[WORDS\_TARGET\]**: 1300–1700 words per 1AC (align to \[READ\_TIME\_MIN\] at \~170–210 wpm)

* **\[EVIDENCE\_DENSITY\]**: 3–7 cards per advantage; 2–5 cards in solvency

* **\[CITATION\_MODE\]**: `SUGGEST_SOURCES` or `CARDS_WITH_QUOTES`

  * `SUGGEST_SOURCES`: **Do not fabricate citations**. Provide precise search strings, author names you are confident exist, journals, and publication year windows; include URLs only if certain they exist. Mark items that need researcher follow‑up with `[EVIDENCE NEEDED]`.

  * `CARDS_WITH_QUOTES`: Provide **verbatim quotes** and full cards **only if** you can **reliably** produce accurate bibliographic info. If not certain, fall back to `SUGGEST_SOURCES`.

* **\[STYLE\_NOTES\]**: “Use debate‑friendly formatting: ALL‑CAPS TAGS, short analytic warrants before cards, and clean plan text. Keep impacts comparative with timeframe/probability/magnitude analysis. Avoid purple prose.”

---

### **GLOBAL REQUIREMENTS**

1. **Diversity & novelty**

   * Produce **distinct mechanisms** and **distinct advantage stories** across cases.

   * Vary **agencies, legal authorities, implementation tools** (statute, executive memo, rulemaking, treaty, MOUs, grants, procurement, Title 10/22/50/19, etc.).

   * Mix **domains** (security, economy, climate, tech, health, rights, courts, space, maritime, immigration, cyber, education, infrastructure, public health), plus **kritik & hybrid/performance** cases.

2. **Professional 1AC structure (each case)**

   * **Header**: Case title (6–12 words).

   * **Overview** (2–5 sentences): What the plan does and the theory of change.

   * **Plan Text**: “The United States federal government should …” Include:

     * **Agent** (branch/agency) \+ **action** (clear mandates)

     * **Funding** (if relevant), **enforcement**, **timeline**, **definitions** (as needed)

     * Brief **implementation notes** (normal means)

   * **Inherency** (1 short blip): Why the SQ fails (legal, political, capacity, info, market).

   * **Advantages** (2–3 per case), each with:

     * **TAGLINE** (ALL‑CAPS)

     * **Uniqueness** (where we are now)

     * **Internal Link Chain** (plan → mechanism → effect → impact)

     * **Impact** \+ **Impact Calculus** (timeframe, probability, magnitude, reversibility)

     * **Evidence**:

       * If `[CITATION_MODE]=SUGGEST_SOURCES`: give **3–7 bulleted “card prompts”** with **author(s)/org(s)** you’re confident exist, **venue types**, **years**, **specific search strings** and what the card would say. Mark unknowns with `[EVIDENCE NEEDED]`.

       * If `[CITATION_MODE]=CARDS_WITH_QUOTES`: give **3–7 full cards** with Author (qualifications), Year, Title, Publication, Date, and a **short, accurate quote** (2–5 sentences). No invented sources. If uncertain, switch to “Suggested Source” format.

   * **Solvency**

     * Mechanism explanation, comparative solvency vs. counterplans, common pushback answers.

     * **Evidence** per `[CITATION_MODE]`.

   * **Theory/Framing (as needed)**

     * For kritik/hybrid/performance affs: **Role of the Ballot**, **Method**, **Framework**, **Topical Nexus** (how the plan is reasonably topical or why plan‑less performance is a valid model).

   * **Counter‑strategy prep** (1 short block): **2–4 bullets** anticipating the common neg (DA, CP, K, T) and a one‑line answer to each.

3. **Style & formatting**

   * Use **ALL‑CAPS TAGS**, short analytic warrants above evidence.

   * Keep plan text crisp.

   * When estimating reading length, target **\[WORDS\_TARGET\]**.

   * No filler; emphasize **clean internal links** and **impact calculus**.

4. **No fabrication policy**

   * **Never** invent a non‑existent source, title, or quote.

   * If unsure, mark `[EVIDENCE NEEDED]` and provide **searchable prompts**.

   * Prefer **think tanks, journals, government docs, court filings, CRS, GAO, CBO, OECD, WHO, IPCC, IEA**, major newspapers.

5. **Accessibility**

   * Write in clear, debate‑friendly prose with strong signposting.

   * Keep jargon minimal unless it’s widely used in the literature.

---

### **OUTPUT FORMAT**

#### **When `[OUTPUT_MODE]=OUTLINE`**

1. **Case Index Table** (numbered 1…\[NUM\_CASES\])

   * Columns: **\#**, **Case Title**, **Aff Type (policy/kritik/hybrid)**, **Plan one‑liner**, **Advantages (tags only)**, **Primary Agency/Authority**.

2. **Skeletons** (for each case)

   * **Title**

   * **Plan (1–2 sentences)**

   * **Advantages (2–3 tags)** with **1–2 line link chain each**

   * **Solvency approach** (2–3 bullets)

   * **Evidence roadmap**: 3–6 “must‑find” sources (authors/orgs, venues, year windows, search strings)

#### **When `[OUTPUT_MODE]=FULL`**

* If `[CASE_SELECTION]=ALL`: print all cases in full.

* If a list: print only the selected case numbers.

* For each **full** 1AC, use this order and formatting:

`# [Case Title]`

`**Overview.** 2–5 sentences on the plan and theory of change.`

`**PLAN TEXT.**`

`The United States federal government should [clear mandates].`

`— Agent:`

`— Mandates:`

`— Funding/Enforcement/Timeline:`

`— Definitions/Notes (as needed):`

`**INHERENCY.** [one blip]`

`**ADVANTAGE 1: [ALL‑CAPS TAG]**`

`— Uniqueness:`

`— Link chain:`

`— Impact + calculus (timeframe/probability/magnitude/reversibility):`

`— Evidence:`

   `• If SUGGEST_SOURCES: bullet list of source prompts with search strings.`

   `• If CARDS_WITH_QUOTES: full cards (accurate; no fabrication). If unsure: switch to “Suggested Source”.`

`**ADVANTAGE 2: [ALL‑CAPS TAG]**`

`[repeat structure]`

`**(Optional) ADVANTAGE 3: [ALL‑CAPS TAG]**`

`[repeat structure]`

`**SOLVENCY**`

`— Mechanism explanation:`

`— Comparative solvency vs. common CPs:`

`— Evidence per CITATION_MODE.`

`**(If kritik/hybrid/performance) FRAMEWORK / METHOD**`

`— Role of the ballot:`

`— Theoretical warrants:`

`— Topical nexus (why this is a fair model of aff):`

`— Evidence per CITATION_MODE.`

`**NEG PREP (one‑liners)**`

`— vs DA:`

`— vs CP:`

`— vs K:`

`— vs T:`

`**[Estimated words: ~XXXX | Est. read time @ 190 wpm: ~YY min]**`

---

### **CASE DIVERSITY MANDATE (examples you can draw from)**

* **Security**: missile defense posture; allied assurance; Arctic governance; maritime domain awareness; biosecurity surge; cyber CISA mandates; space surveillance; nuclear C2 modernization (narrow slice); ISR sharing; port & rail hardening.

* **Economy & Industry**: critical minerals supply chains (non‑China); grid modernization; port decarbonization; advanced manufacturing workforce; AI standards in procurement; export finance reforms.

* **Climate & Environment**: permafrost science cooperation; wildfire EMS and satellite data; methane fee enforcement; coastal resilience finance; transmission siting reforms.

* **Health & Welfare**: pandemic early warning; fentanyl precursor controls; rural telehealth reimbursement; heat‑wave adaptation.

* **Rights & Justice**: voting access infrastructure; tribal consultation mandates; immigration court backlog tools.

* **Tech & Data**: NIST standards; open science/data; privacy‑preserving federal data sharing; AI safety evals in federal grants.

* **Legal/Courts**: APA reforms; standing/venue consolidation for nationwide injunctions (narrow); specialized Article I pilot.

* **Kritik/Hybrid**: security epistemology; anthropocene/degrowth; abolitionist public health; digital sovereignty; semiotics/discourse aff; performance‑based community methodology.

---

### **QUALITY CHECKLIST (apply before you print)**

* Plan is **clear, enforceable**, and **topical** under \[RESOLUTION\].

* Each advantage has **clean uniqueness → link → impact**.

* Impact calculus is explicit (timeframe/probability/magnitude/reversibility).

* Solvency explains **how** and **why** with comparative warrants.

* **No fabricated cards**. Uncertain items are flagged as `[EVIDENCE NEEDED]` with research prompts.

* Cases are **not duplicative** across mechanisms or impact stories.

---

**Begin now.** First, restate the `[RESOLUTION]` you will use and confirm the parameter values you’re applying. Then proceed according to `[OUTPUT_MODE]`.

### **C.2 Bracket procedure**

A fully explicit bracket algorithm (recommended):

1. Assign each case an anonymized ID.  
2. Round 1: pair by strategic approach strata.  
3. Score all cases on rubric dimensions.  
4. Advance top 50% per stratum; if tie within threshold, apply evidence validation tiebreak.  
5. Repeat until top-4 identified; record all matchups and scores.

### **C.3 Rubric and scoring weights**

Your draft specifies five weighted dimensions and weights (Argumentation Strength 25%, Evidence Quality 25%, Strategic Coherence 20%, Innovation 15%, Competitive Viability 15%).

ACM FAccT Draft 2.0

Include the judge prompt in the artifact repository; in the paper, keep the rubric concise and put the exact prompt text here.

### **C.4 Evidence validation pipeline**

Your draft describes validating citations against purported source URLs and classifying evidence as exact match, partial match, paraphrase, or fabricated, with a fidelity score based on verifiable evidence.

ACM FAccT Draft 2.0

**Operational definitions (recommended).**

* **Exact match:** retrieved source contains the quoted sentence(s) verbatim at the cited sentence IDs.  
* **Partial match:** some cited sentences match, others missing.  
* **Paraphrase:** semantic alignment but not verbatim match (should be rare if sentence-ID constraint is enforced).  
* **Fabricated:** source missing or does not contain cited content.

**Fidelity score:** `#exact / #total` (or weighted variant); “perfect validation” \= 1.0.

---

## **Appendix D: Example contestation workflow (illustrative)**

This appendix section is designed to make contestability concrete without expanding the main paper.

### **D.1 Minimal example (typed syllogism \+ sentence-level provenance)**

Provide a compact, 1–2 paragraph example showing:

* a single Claim,  
* its Warrant,  
* 2–3 EvidenceSentence IDs,  
* and a stakeholder contestation that targets either:  
  1. a specific evidence sentence as inapplicable/out-of-context, or  
  2. a warrant as normatively unacceptable, or  
  3. the stance weights as misaligned with the stakeholder’s values.

### **D.2 What the system does when contested**

Specify the required response contract:

1. **Localize** the challenged node(s) in the mediation graph (Claim/Warrant/EvidenceSentence).  
2. **Regenerate only the affected slots** (targeted repair).  
3. **Preserve the original** in the audit log (no overwrite).  
4. **Emit a revised synthesis plus dissent memo** if disagreement remains.

