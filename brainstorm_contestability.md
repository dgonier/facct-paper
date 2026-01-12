# Brainstorm: Integrating Template Traversal & Dialectical Critic as Contestability Mechanisms

## Executive Summary

The current FAccT draft under-emphasizes two powerful contestability mechanisms that are well-documented in the NSF report: **Template Tree Traversal** and **Dialectical Refinement (Critic-Evaluator Loop)**. These aren't just implementation details—they're first-class contestability primitives that enable stakeholders to challenge *how* arguments are structured and *whether* they survived scrutiny.

---

## 1. Template Tree Traversal as Contestability

### Current State
The paper mentions "typed syllogisms" (Section 3.5) and "template traversal" (Section 4.2) but treats them as planning mechanisms rather than contestability mechanisms.

### The Contestability Argument

Template Tree Traversal makes **structural decisions auditable**:

1. **Decision Point Transparency**: The tree structure records *which* argumentative form was chosen (traditional vs. kritik, utilitarian vs. deontological impact framing) and *what alternatives were available but not taken*.

2. **Resource Allocation Justification**: Word allocation (e.g., 30% to impact, 40% to link) is not hidden inside a black-box generation—it's an explicit, contestable parameter. A stakeholder can ask: "Why did the system allocate only 200 words to environmental impacts vs. 400 to economic impacts?"

3. **Completeness Enforcement**: Typed syllogisms guarantee that arguments have required components. If an Advantage lacks Impact evidence, the system flags it. This makes "missing warrant" challenges trivially verifiable.

4. **Template Expansion as Audit Trail**: When the system generates a *new* template (because existing ones don't fit), this is logged. Stakeholders can contest: "Why was a novel template needed? What about the standard forms was inadequate?"

### Suggested Integration

**In Section 3.5 (Inspectable argument structure)**, add a paragraph:

> Template tree traversal operationalizes structural contestability. At each branch point, the system records which template was selected (e.g., "traditional 1AC with 3 advantages" vs. "kritik with alternative"), what resource allocation was applied, and whether any novel templates were generated. This trace enables a distinct class of challenges: stakeholders can dispute not only *what* claims were made, but *why the argumentative structure took this form rather than another*. For instance, a reviewer might contest that a utilitarian impact calculus was chosen when the underlying values favor a rights-based framing—and the template selection trace makes this challenge actionable.

### Where to Trim to Make Room

**Section 3.4 (Sublation)** is currently verbose. The three-part structure (consensus core, conditional claims, dissent memo) could be compressed. Suggested cut (~80 words):

Current:
> Operationally, FOAM's sublation emits a structured output with (at minimum) three parts:
> 1. A consensus core (claims that survived critique across stances),
> 2. A set of conditional or branch claims ("if autonomy is prioritized over aggregate welfare, then..."), and
> 3. A minority report / dissent memo that records unresolved conflicts, the strongest arguments on each side, and which premises are contested.
>
> Sublation preserves dissent explicitly.

Suggested revision:
> Sublation emits three artifacts: a *consensus core* (claims surviving cross-stance critique), *conditional claims* (branching on unresolved value priorities), and a *dissent memo* (recording conflicts and contested premises).

---

## 2. Dialectical Refinement (Critic-Evaluator) as Contestability

### Current State

The paper mentions "cross-examination" and "evaluation" in the mediation loop (Section 3.3) but doesn't detail the Critic → Evaluator → Proposer cycle from the NSF report.

### The Contestability Argument

Dialectical refinement provides **pre-publication adversarial testing** that is itself auditable:

1. **Structured Objection Records**: The Critic agent generates *typed objections* (logical gap, missing evidence, value conflict, scope overreach). Each objection is a first-class object in the mediation graph.

2. **Evaluator Decisions are Traceable**: When the Evaluator scores a critique as "material" vs. "immaterial," that judgment is logged with reasoning. Stakeholders can contest: "You dismissed this objection as immaterial—why?"

3. **Revision History**: Each revision is diff-able against the prior draft. If a claim changed after critique, the system can show *what critique prompted the change*.

4. **Iteration Count as Quality Signal**: The NSF report notes 3+ rounds of refinement. The number of iterations and which objections were raised/resolved in each round is audit-relevant metadata.

### Suggested Integration

**In Section 3.3 (Deliberative protocol)**, expand the cross-examination description:

Cross-examination instantiates a **dialectical refinement loop**: a Critic agent issues structured objections (classified as logical gap, missing evidence, value conflict, or scope overreach), an Evaluator agent scores each objection's materiality, and the original Proposer either revises or rebuts. This cycle repeats for a minimum of three iterations. Critically, *all objections and evaluator decisions are logged*—even dismissed critiques remain in the mediation graph. This enables a distinctive form of contestation: a downstream reviewer can examine whether a particular weakness was raised, how it was evaluated, and why the response was deemed adequate. The system cannot claim an argument is "robust" without showing the specific challenges it survived.

### Where to Trim to Make Room

**Section 3.2 (Differentiated agents)** has redundancy. The paragraph about "second-order contestation" repeats the point about contesting perspective selection. Suggested cut (~60 words):

Cut this:
> This matters because pluralistic systems can otherwise "value-wash" by claiming inclusivity while quietly privileging one evaluative frame.

This point is already made by the preceding sentence about legitimacy.

---

## 3. Areas to Cut (Page Budget)

### High-Priority Cuts

| Section | Current Words (approx) | Suggested Cut | Rationale |
|---------|----------------------|---------------|-----------|
| 3.2 (Differentiated agents) | ~400 | Cut ~80 | Redundancy on "value-wash" point |
| 3.4 (Sublation) | ~200 | Cut ~50 | Compress the three-part list |
| 4.1 (Why policy debate) | ~180 | Cut ~40 | The "card" explanation is detailed for FAccT audience |
| 4.3 (Phases 1-3) | ~60 | Expand this | Currently too sparse—needs template traversal |
| 5.3 (Judging rubric) | ~150 | Cut ~30 | Rubric list could be a table instead |

### Medium-Priority Cuts

1. **Section 2 (Related Work)**: If over page limit, consider moving some citations to footnotes or consolidating the XAI and contestable AI paragraphs.

2. **Evaluation methodology (Section 5.2)**: The Swiss-bracket explanation is detailed. Could compress to: "A modified Swiss-system bracket with double elimination, stratified by strategic approach to minimize judge-adaptation artifacts."

3. **Section 5.4 (Evidence validation methodology)**: The four-bucket classification (exact/partial/paraphrase/fabricated) could be a footnote.

---

## 4. Opinion on Secondary Experiments

### What You Have
- Primary experiment: 66-case tournament with 3 baselines (FOAM, human expert, zero-shot AI)
- Metrics: Overall score, 5 sub-dimensions, Perfect Validation rate

### What's Missing (and Whether to Add)

#### A. Ablation Study (Recommended if space permits)
**Question**: What's the marginal contribution of each contestability mechanism?

| Condition | Perfect Validation | Overall Score |
|-----------|-------------------|---------------|
| Full FOAM pipeline | 76.2% | 81.7 |
| w/o sentence-level provenance | ? | ? |
| w/o dialectical refinement | ? | ? |
| w/o typed syllogisms | ? | ? |

**My opinion**: This would be the *most valuable* secondary experiment for FAccT. The current paper claims these mechanisms matter, but doesn't isolate their contributions. Even a 2x2 ablation (±provenance, ±refinement) on 10-20 cases would strengthen the causal story.

**Cost**: Moderate. You'd rerun generation with components disabled. Judge cost is ~$0.12/case.

#### B. Human Evaluation of Contestability (Nice-to-Have)
**Question**: Do humans actually find FOAM outputs *easier to contest*?

Design: Give reviewers (debate judges or policy analysts) outputs from FOAM vs. zero-shot, ask them to:
1. Identify the weakest claim
2. Locate supporting evidence
3. Rate confidence in their critique

**My opinion**: This would be compelling for FAccT's human-centered focus, but it's a significant IRB/logistics burden. Consider for camera-ready or follow-up work.

#### C. Provenance Trace Utility (Lower Priority)
**Question**: Do auditors actually *use* the mediation graph?

Design: Eye-tracking or click-tracking study where auditors review outputs with/without access to the mediation graph.

**My opinion**: Interesting but tangential. The current paper is about *producing* contestable outputs; whether auditors *use* them well is a separate research question.

#### D. Adversarial Robustness (Out of Scope)
**Question**: Can an adversary manipulate FOAM to produce biased but "auditable" outputs?

**My opinion**: Important for dual-use discussion but probably out of scope for this paper. Mention in limitations.

---

## 5. Specific Paragraph-Level Recommendations

### Must Strengthen

1. **Section 4.3 (Phases 1-3)**: Currently a single paragraph that defers to supplementary materials. This is where Template Traversal lives. Expand to ~150 words explaining:
   - Template tree structure (branch points)
   - Word allocation as explicit parameter
   - Typed syllogisms as completeness validators
   - The contestability payoff

2. **Section 3.3 (Deliberative protocol)**: Add the Critic → Evaluator → Proposer loop explicitly. Currently just says "cross-examination" and "evaluation" without showing they're iterative and logged.

### Must Trim

1. **Section 3.2, paragraph 3** ("Perspective nodes also make second-order contestation practical..."): This paragraph makes a good point but takes too long. Compress from ~100 words to ~50.

2. **Section 4.1, last sentence** ("Competitive success is strongly coupled to evidence quality..."): Redundant with the preceding sentence about provenance/verifiability.

3. **Section 5.1, RQ list**: Consider whether RQ3 ("attributable to accountability mechanisms") is adequately addressed by current evidence. If not, either add ablation or soften the claim.

---

## 6. Structural Suggestion

Consider renaming Section 4.3 from:
> "Phases 1-3: perspective assignment, planning, and template traversal"

To:
> "Phases 1-3: Structural Contestability via Template Traversal and Dialectical Refinement"

This foregrounds the contestability framing rather than treating these phases as mere "implementation detail."

---

## Summary Table

| Mechanism | Current Treatment | Recommended Change |
|-----------|------------------|-------------------|
| Sentence-level provenance | Well-covered (Section 4.4) | Keep as-is |
| Verification checks | Covered (Section 4.5) | Keep as-is |
| Template tree traversal | Mentioned but not framed as contestability | Expand in Section 3.5 and 4.3 |
| Dialectical refinement | Mentioned as "cross-examination" | Expand with Critic→Evaluator→Proposer detail |
| Perspective nodes | Well-covered (Section 3.2) | Trim redundancy |
| Typed syllogisms | Covered (Section 3.5) | Connect more explicitly to template traversal |

---

## Next Steps

1. Decide on ablation: Do you want to run a quick ±provenance, ±refinement ablation? Would strengthen RQ3 significantly.

2. Rewrite Section 4.3: This is the biggest gap. Currently 60 words; should be 150-200.

3. Trim Sections 3.2 and 3.4: ~130 words recoverable.

4. Update figure caption: The contestability_mechanics.png caption should explicitly mention template traversal as a contestability mechanism.
