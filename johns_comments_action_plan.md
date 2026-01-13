# John's Comments - Action Plan

**Document:** FOAM: A Pluralistic Architecture for Explainable and Contestable AI
**Last Edit:** January 12, 2026 at 9:28 PM by John Hines
**Captured:** January 13, 2026 (COMPLETE)

---

## OPEN COMMENTS - ASSIGNED TO DEVIN

### Comment 1: Claim Calibration (HIGH PRIORITY)
**From:** John Hines @ 9:23 PM Yesterday
**Assigned to:** @dgonier@gmail.com

#### Issue
> "5) Claim calibration: still a bit too strong in two places"
> - FOAM outputs a "contestable record" with surviving objections etc (Abstract, §3) without showing an example of that record.
> - In §6, you state the artifact can plug into "post-hoc dispute resolution." That is plausible, but not evidenced in this paper.

#### Required Fixes
1. **Abstract:** Change "outputs … a contestable record" → "outputs … a contestable record intended to support contestation"
2. **Section 6:** Change "plug into … post-hoc dispute resolution" → "support downstream review; dispute resolution requires institutional process"

#### Status: ⬜ TODO

---

### Comment 2: Tournament Design (HIGH PRIORITY)
**From:** John Hines @ 9:22 PM Yesterday
**Assigned to:** @dgonier@gmail.com
**Location:** §5.3 Judging rubric and scoring

#### Issue
> "3) The tournament design description is overcomplicated and may look like 'stacking the deck'"
>
> In §5.3 you say ties trigger evidence validation as a tiebreaker and that advancement uses bracket mechanics.
>
> A critical reviewer will ask:
> - Are Table 1 and Table 2 results computed over all 66 cases (single-pass scoring), or are they influenced by which cases advance?
> - If evidence validation is used as a tiebreaker, FOAM has a built-in advantage in advancing, which can bias any "tournament champion" narrative.

#### Required Fixes
1. **Add clarifying sentence in §5.3 or §5.5:**
   > "All 66 cases were scored once under the rubric; Tables 1–2 report aggregate statistics over the full set and do not depend on bracket advancement."
   > (If true—use the accurate variant.)

2. **If not true:** Remove "tiebreaker" and "double elimination" details; describe as blinded scoring plus summary statistics

3. **Delete:** The "tournament champion Case 045 …" anecdote in §5.5 (reads like flourish and invites "selection" criticism)

#### Status: ⬜ TODO

---

### Comment 3: Evidence Validation Methodology (HIGH PRIORITY)
**From:** John Hines @ 9:21 PM Yesterday
**Assigned to:** @dgonier@gmail.com
**Location:** §5.4 Evidence validation methodology

#### Issue
> "Evidence validation is still vulnerable to a 'favorable-by-construction' critique"
>
> Perfect Validation is still not defined in enough operational detail to survive a hostile read.
>
> **What's missing (and what reviewers will attack):**
> - What counts as the "referenced source" for human camp cases that often cite in non-URL formats?
> - What fraction of baseline citations were resolvable at all?
> - How do you tokenize/normalize text for "exact match" (case/punctuation/whitespace)?
> - Are you scoring per citation, per claim, or per card?
> - Do different conditions have different numbers of citations per case?
>
> **Why this can sink the paper:** A reviewer can argue the 76.2% vs 8.7% vs 0% result is largely an artifact of (i) FOAM's pointer-based assembly and (ii) baseline citations being non-resolvable or paraphrased by convention.

#### Required Fixes (NO NEW MODEL RUNS NEEDED)

**A) Formal definition paragraph (4-6 sentences) - Add to §5.4:**
- Normalization (lowercasing, whitespace collapse, punctuation handling)
- Exact match rule (substring match of quoted span within fetched source text)
- Resolvability rule (what if no URL; what if fetch fails)
- Unit of analysis (citation-level)

**B) Resolvability and volume stats (1-2 sentences if no space for table):**
- Mean citations per case for FOAM vs human vs zero-shot
- % citations resolvable per condition
- Perfect Validation conditional on resolvable citations

Example language:
> "Across conditions, the mean number of citations per case was X/Y/Z; resolvability was A%/B%/C%. Perfect Validation is computed over resolvable citations."

#### Status: ⬜ TODO

---

### Comment 4: Abstract Opening (HIGH PRIORITY)
**From:** John Hines @ 7:57 PM Yesterday
**Assigned to:** @dgonier@gmail.com

#### Issue
> "I prefer the previous opening sentences to the Abstract... given the focus of FAccT I think we should keep the existing/previous framing of the abstract focused upon accountability in high stakes situations"

#### Required Fix
Revert the abstract opening to the original high-stakes AI accountability framing. Keep the changes after "we propose FOAM".

**Original opening (RESTORE THIS):**
> "High-stakes AI systems increasingly mediate access to credit, healthcare, and public benefits, yet affected parties often cannot see why a decision was made or meaningfully contest it..."

**Current opening (NEEDS REVERT):**
> "When state-of-the-art reasoning models are given a hint that changes their answer, they reveal that hint in their chain-of-thought only 25–39% of the time..."

#### Status: ⬜ TODO

---

## OPEN COMMENTS - NOT ASSIGNED

### Comment 5: Citation Questions (MEDIUM PRIORITY)
**From:** John Hines @ 8:03 PM Yesterday
**To:** @rhetorrao@gmail.com and @dgonier@gmail.com
**Location:** §1.1 Accountability gap in high-stakes AI

#### Issues
1. Should we be including more citations for some of these claims?
2. Citation numbering is off (first citation is "18")

#### John's Suggested Citations (provided @ 8:05 PM)
```bibtex
@article{obermeyer2019dissecting,
  title = {Dissecting racial bias in an algorithm used to manage the health of populations},
  author = {Obermeyer, Ziad and Powers, Brian and Vogeli, Christine and Mullainathan, Sendhil},
  journal = {Science},
  volume = {366},
  number = {6464},
  pages = {447--453},
  year = {2019},
  doi = {10.1126/science.aax2342}
}

@inproceedings{raghavan2020mitigating,
  title = {Mitigating Bias in Algorithmic Hiring: Evaluating Claims and Practices},
  author = {Raghavan, Manish and Barocas, Solon and Kleinberg, Jon and Levy, Karen},
  booktitle = {Proceedings of FAccT '20},
  pages = {469--481},
  year = {2020},
  doi = {10.1145/3351095.3372828}
}

@misc{angwin2016machinebias,
  title = {Machine Bias: There's Software Used Across the Country to Predict Future Criminals. And It's Biased Against Blacks.},
  author = {Angwin, Julia and Larson, Jeff and Mattu, Surya and Kirchner, Lauren},
  howpublished = {ProPublica},
  year = {2016},
  month = {May}
}

@incollection{kluttz2020shaping,
  title = {Shaping Our Tools: Contestability as a Means to Promote Responsible Algorithmic Decision Making in the Professions},
  author = {Kluttz, Daniel and Kohli, Nitin and Mulligan, Deirdre K.},
  booktitle = {After the Digital Tornado},
  publisher = {Cambridge University Press},
  year = {2020}
}
```

**Note:** We already have `kaminski2021right` and `rudin2019stop` in references.bib.

#### Status: ⬜ TODO

---

### Comment 6: Missing "Related Work" Citation
**From:** John Hines @ 8:07 PM Yesterday
**Location:** ct [11] (reference appears broken in PDF)

#### Issue
> "this is missing in pdf version---'related work' claim obviously needs robust citations"

#### Required Fix
Need to identify which specific "related work" claim needs citation and add appropriate reference.

#### Status: ⬜ TODO (needs clarification on exact location)

---

### Comment 7: Adverse Impacts Statement (SUGGESTION)
**From:** John Hines @ 9:24 PM Yesterday

#### Issue
> "Add: Endmatter notes: from GPT: 6) Endmatter consistency issue: you promise an 'Adverse Impacts' statement..."

#### Required Fix
Add an Adverse Impacts statement to the paper's endmatter (after Ethical Considerations section).

#### Status: ⬜ TODO

---

### Comment 8: "Prestigious Debate Camps" Wording
**From:** John Hines @ 1:29 AM Yesterday
**Location:** "prestigious debate camps" (Dartmouth, Georgetown, Michigan, Emory)

#### Issue
> "revise"

#### Related Suggestion from John @ 6:52 PM:
> Replace "prestigious debate camps" with "expert-authored training materials from highly competitive policy debate programs"

#### Status: ⬜ TODO

---

### Comment 9: DebaterHub Structured System (Anonymization)
**From:** John Hines @ 1:29 AM Yesterday
**Location:** "DebaterHub Structured System"

#### Issue
> "needs to be fixed"

#### Required Fix
Anonymize - replace with "Anon" or similar placeholder for blind review.

#### Status: ⬜ TODO

---

## SUGGESTIONS TO ACCEPT/REJECT

### Suggestion 1: Add Baseline Controls Description (HIGH PRIORITY - ACCEPT)
**From:** John Hines @ 7:40 PM Yesterday
**Location:** §5.2 Experimental design and baselines

#### Full Suggested Text (from Google Doc)
> **Baseline controls (zero-shot AI).** To reduce confounding from artifact format and resource constraints, we generated the zero-shot baseline using Claude 4.5 in research mode, GPT-5 in deep research mode, SuperGrok Heavy, and Gemini 2.5 in research mode. We used a single standardized "mega-prompt" that enforced the same IAC conventions and constraints used by elite debate program materials and by DebaterHub's FOAM case-building pipeline FULL IAC outputs: **8 minutes of read-time target (1300-1700 words)**; debate formatting (ALL-CAPS tags, short analytic warrants above evidence); a fixed advantage/solvency structure; explicit impact calculus; and comparable evidence-density targets (**3-7 cards per advantage; 2-5 in solvency**). The prompt also enforced a strict **no-fabrication policy**: when reliable bibliographic details and quotations could not be produced, models were required to generate high-precision search strings and to mark uncertainty as **[EVIDENCE NEEDED]**. When the interface supported browsing, web access was enabled to reduce evidence-access confounds. Unlike FOAM, these baselines did not use multi-agent deliberation, typed syllogisms enforcement, or sentence-level provenance binding; thus, baseline citations remained unconstrained natural-language references and were evaluated under the same automated validation pipeline. We generated **one** case per topic per condition and used outputs **as-is** (no manual editing beyond uniform formatting normalization).

#### Why Important
This paragraph explains how the zero-shot baseline was constructed with equivalent constraints to FOAM, addressing potential criticism that the comparison is unfair.

#### Status: ⬜ ACCEPT (add to LaTeX §5.2)

---

### Suggestion 2: Replace "Prestigious Debate Camps"
**From:** John Hines @ 6:52 PM Yesterday

#### Suggestion
> Replace: "prestigious debate camps" (Dartmouth, Georgetown, Michigan, Emory) with "expert-authored training materials from highly competitive policy debate programs"

#### Status: ⬜ ACCEPT

---

### Suggestion 3: Task Selection Section (from John @ 6:57 PM)
**Location:** Devin's suggestion to delete "Task selection" paragraph

#### John's Note:
> "@dgonier@gmail.com this still exists in the pdf version--which I think is a good thing...can we reject this suggestion?"

#### Status: ⬜ REJECT (keep the Task Selection paragraph)

---

## DEVIN'S SUGGESTIONS (Formatting)

- Delete: "How FOAM changes the validation problem..." - ⬜ REVIEW
- Format: bold, font - ⬜ REVIEW
- Replace: "DebaterHub" with "Anon" - ⬜ ACCEPT
- Delete: "Debate artifact." - ⬜ REVIEW
- Delete: "This is especially aligned with policy debate's evidence norms..." - ⬜ REVIEW

---

## RESOLVED COMMENTS (by John @ 9:26-9:28 PM Yesterday)

These items have been marked resolved and do not require action:

1. ✅ Template tree traversal paragraph - added by Devin, marked resolved
2. ✅ Phases 1-3 heading discussion - resolved (put details in Appendix)
3. ✅ Abstract claim verification against Table 1 - confirmed
4. ✅ Table 2 claims (76.2% vs 8.7% vs 0%) - confirmed against final table
5. ✅ Table 1 claims (81.7 vs 70.1 vs 50.6) - confirmed against final table
6. ✅ Perfect Validation definition clarity - resolved (Devin @ 2:11 PM)
7. ✅ "A Claude Opus 4 judge" - resolved (judges question addressed)
8. ✅ "Gemini/Claude/ChatGPT/Grok" - specified
9. ✅ Figure 2 reference (Phase 4/5) - confirmed
10. ✅ Figure 2 summary verification - confirmed
11. ✅ Figure 1 system overview - connected to updated figure
12. ✅ Empirical validation claims - verified after experiments
13. ✅ Abstract claims - revised after experiments
14. ✅ Adverse impacts statement reference - confirmed consistent
15. ✅ Future work human-subject evaluation - addressed
16. ✅ Claude Opus 4 judge limitations - addressed

---

## SUMMARY ACTION ITEMS (Priority Order)

| # | Task | Priority | Location | Status |
|---|------|----------|----------|--------|
| 1 | Revert Abstract opening to high-stakes framing | HIGH | Abstract | ⬜ |
| 2 | Soften "contestable record" claim in Abstract | HIGH | Abstract | ⬜ |
| 3 | Fix §6 "post-hoc dispute resolution" claim | HIGH | §6 | ⬜ |
| 4 | **Add Baseline Controls paragraph** | HIGH | §5.2 | ⬜ |
| 5 | Add formal Perfect Validation definition | HIGH | §5.4 | ⬜ |
| 6 | Add resolvability/volume stats | HIGH | §5.4 | ⬜ |
| 7 | Clarify scoring is over all 66 cases | HIGH | §5.3/§5.5 | ⬜ |
| 8 | Delete "tournament champion Case 045" anecdote | HIGH | §5.5 | ⬜ |
| 9 | Add Obermeyer et al. 2019 citation | MEDIUM | §1.1 | ⬜ |
| 10 | Add Raghavan et al. 2020 citation | MEDIUM | §1.1 | ⬜ |
| 11 | Add Angwin et al. 2016 (COMPAS) citation | MEDIUM | §1.1 | ⬜ |
| 12 | Add Kluttz et al. 2020 citation | MEDIUM | §1.1 | ⬜ |
| 13 | Clarify and fix "related work" citation | MEDIUM | §2? | ⬜ |
| 14 | Add Adverse Impacts statement to endmatter | MEDIUM | Endmatter | ⬜ |
| 15 | Replace "prestigious debate camps" wording | MEDIUM | §5.2 | ⬜ |
| 16 | Anonymize "DebaterHub Structured System" | MEDIUM | Throughout | ⬜ |
| 17 | Review Devin's formatting suggestions | LOW | Various | ⬜ |
