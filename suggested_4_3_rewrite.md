# Suggested Rewrite for Section 4.3

## Current Version (~60 words)

**Section title:** Phases 1–3: perspective assignment, planning, and template traversal

Phases 1–3 produce an inspectable argumentative plan: the system selects an explicit perspective, drafts a typed strategic blueprint, and expands it into a structured scaffold with evidence slots. These phases are implementation detail for our case-study pipeline; we summarize the key outputs here (full prompt and protocol detail are available in supplementary materials). The primary accountability mechanisms evaluated in this paper are sentence-level provenance (Phase 4) and verification checks (Phase 5).

---

## Suggested Replacement (~200 words)

**Section title:** Phases 1–3: structural contestability via template traversal and dialectical refinement

Phases 1–3 produce an inspectable argumentative plan through three contestability-relevant operations. In **Phase 1**, the system assigns an explicit perspective node (Section 3.2), making the evaluative frame a first-class auditable choice. In **Phase 2**, a dialectical refinement loop stress-tests the strategic plan: a Critic agent issues typed objections (logical gap, missing evidence, value conflict, scope overreach), an Evaluator scores each objection's materiality, and the Proposer revises or rebuts. This cycle iterates at least three times, and *all objections—including dismissed ones—remain in the mediation graph*, enabling downstream reviewers to inspect whether a weakness was raised and why the response was deemed adequate.

In **Phase 3**, template tree traversal expands the plan into a typed syllogism scaffold (e.g., Advantage = Uniqueness + Link + Impact). At each branch point, the system records which template was selected, what word allocation was applied (e.g., 30% impact, 40% link), and whether novel templates were generated. This trace enables a distinct class of challenges: stakeholders can dispute not only *what* claims were made, but *why the argumentative structure took this form rather than another*—for instance, contesting that a utilitarian impact calculus was chosen when the underlying values favor a rights-based framing.

---

## Key Changes

1. **Renamed section** to foreground contestability

2. **Phase 2 made explicit** - Critic → Evaluator → Proposer loop:
   - Typed objections: logical gap, missing evidence, value conflict, scope overreach
   - Evaluator scores materiality
   - All objections remain in mediation graph (even dismissed ones)

3. **Phase 3 framed as contestability mechanism**:
   - Branch point decisions are recorded
   - Word allocation is explicit and contestable
   - Novel template generation is logged
   - Concrete example: contesting utilitarian vs rights-based framing

4. **Removed**: "These phases are implementation detail"
