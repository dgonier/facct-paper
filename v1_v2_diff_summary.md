# v1 → v2 Diff Summary

Full diff: 1364 lines of changes. Key substantive differences:

---

## 1. Abstract
**v1**: No abstract in LaTeX sections (likely in main.tex)
**v2**: Full abstract included in markdown

**Action**: Check if abstract needs updating in main.tex

---

## 2. Section 1 (Introduction)
**v1**: Uses `\cite{}` references, enumerated lists for contributions
**v2**: Uses `[##]` bracketed references, inline prose for contributions

**Substantive difference**: v2 compresses the 3 contributions from enumerated list to inline prose. Otherwise nearly identical.

**Action**: Minor - could compress enumerated list if space needed

---

## 3. Section 3.4 (Sublation)
**v1 (original)**:
```
Operationally, FOAM's sublation emits a structured output with (at minimum) three parts:
1. A consensus core (claims that survived critique across stances),
2. A set of conditional or branch claims ("if autonomy is prioritized..."), and
3. A minority report / dissent memo that records unresolved conflicts...

Sublation preserves dissent explicitly.
```

**v2**:
```
Sublation emits three artifacts: a consensus core (claims surviving cross-stance critique), conditional claims (branching on unresolved value priorities), and a dissent memo (recording conflicts and contested premises).
```

**Action**: ALREADY DONE - I compressed this

---

## 4. Section 3.5 (Argument Structure) - NEW PARAGRAPH
**v1**: Ends after typed syllogisms description
**v2**: Adds new paragraph about template tree traversal:

```
Template tree traversal operationalizes structural contestability. At each branch point, the system records which template was selected (e.g., "traditional 1AC with 3 advantages" vs. "kritik with alternative"), what resource allocation was applied, and whether any novel templates were generated. This trace enables a distinct class of challenges: stakeholders can dispute not only what claims were made, but why the argumentative structure took this form rather than another. For instance, a reviewer might contest that a utilitarian impact calculus was chosen when the underlying values favor a rights-based framing—and the template selection trace makes this challenge actionable. Furthermore, unlike traditional chain-of-thought reasoning where reasoning and response are interwoven and in some cases reasoning is not always a reliable indicator for why outputs occurred, the template tree traversal process is a discrete step occurring prior and serving as a foundational infrastructure to drafting.
```

**Action**: NEED TO ADD this paragraph to end of Section 3.5

---

## 5. Section 4.3 (Phases 1-3) - MAJOR EXPANSION
**v1** (~60 words):
```
Phases 1–3 produce an inspectable argumentative plan: the system selects an explicit perspective, drafts a typed strategic blueprint, and expands it into a structured scaffold with evidence slots. These phases are implementation detail for our case-study pipeline; we summarize the key outputs here (full prompt and protocol detail are available in supplementary materials). The primary accountability mechanisms evaluated in this paper are sentence-level provenance (Phase 4) and verification checks (Phase 5).
```

**v2** (~180 words):
```
Phases 1–3 produce an inspectable argumentative plan through three contestability-relevant operations. In Phase 1, the system assigns an explicit perspective node (Section 3.2), making the evaluative frame a first-class auditable choice. In Phase 2, a dialectical refinement loop stress-tests the strategic plan: a Critic agent issues typed objections (logical gap, missing evidence, value conflict, scope overreach), an Evaluator scores each objection's materiality, and the Proposer revises or rebuts. This cycle iterates at least three times, and all objections—including dismissed ones—remain in the mediation graph, enabling downstream reviewers to inspect whether a weakness was raised and why the response was deemed adequate.

In Phase 3, template tree traversal expands the plan into a typed syllogism scaffold (e.g., Advantage = Uniqueness + Link + Impact). At each branch point, the system records which template was selected, what word allocation was applied (e.g., 30% impact, 40% link), and whether novel templates were generated. This trace enables a distinct class of challenges: stakeholders can dispute not only what claims were made, but why the argumentative structure took this form rather than another—for instance, contesting that a utilitarian impact calculus was chosen when the underlying values favor a rights-based framing.
```

**Action**: NEED TO REPLACE Section 4.3

---

## 6. Section 6 (Implications) - NEW SECTION
**v1**: Does not exist
**v2**: New section "Implications for accountable AI systems"

```
FOAM reframes explanation as a contestable record rather than a post‑hoc narrative. Instead of producing a single rationale, the system outputs (i) an auditable argument structure (claims, warrants, rebuttals), (ii) explicit perspective configurations, and (iii) sentence‑level provenance linking each substantive claim to a checkable source span. This shifts accountability from "did the explanation sound plausible?" to "which premises and evidence does the output depend on, and where can a challenge be lodged?"

Operationally, FOAM supports contestation at three levels: (1) evidence disputes (a cited sentence does not support the tagged claim; missing counterevidence), (2) inferential disputes (the warrant connecting evidence to conclusion is invalid or incomplete), and (3) normative disputes (the perspective/value configuration is illegitimate or incomplete for the context). Because these objects are explicit, a reviewer can localize disagreement to specific nodes and request revision without reopening the entire output as free‑form prose.

Institutionally, the resulting artifact functions as an auditable dossier that can plug into existing governance workflows (internal review, incident response, assurance audits, and post‑hoc dispute resolution). The technical contribution is not replacing due process, but supplying the structured, traceable materials that make procedural review feasible at scale.
```

**Action**: Check if 06_implications.tex exists and matches

---

## 7. Section 7 (Limitations) - RESTRUCTURED
**v1**: Three subsections (methodological, safety, future work)
**v2**: Same structure with minor wording changes

**Action**: Check for any substantive differences

---

## 8. Section 8 (Conclusion) - MINOR UPDATES
**v1/v2**: Very similar, some wording tweaks

**Action**: Check for any substantive differences

---

# ACTIONS NEEDED

1. ✅ Section 3.4 - DONE (compressed sublation)
2. ⬜ Section 3.5 - ADD template tree traversal paragraph
3. ⬜ Section 4.3 - REPLACE with expanded version
4. ⬜ Section 6 - VERIFY 06_implications.tex content
5. ⬜ Section 7 - CHECK for differences
6. ⬜ Section 8 - CHECK for differences
