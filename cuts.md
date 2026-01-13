# FOAM Paper Cuts - Target: 1.5 pages reduction

**Goal:** Get conclusion to end on page 14 (currently ~page 15.5)

---

## ✅ IMPLEMENTATION STATUS

| Cut | Description | Status | File |
|-----|-------------|--------|------|
| Cut 2.1 | Condense §2.1 Explainability | ✅ DONE | `02_related_work_cc_cuts2.tex` |
| Cut 2.2 | Condense §2.2 GDPR discussion | ✅ DONE | `02_related_work_cc_cuts2.tex` |
| Cut 2.3 | Condense §2.3 Pluralistic approaches | ✅ DONE | `02_related_work_cc_cuts2.tex` |
| Cut 4.1 | Condense Phase 4 steps | ✅ DONE | `04_case_study_cc_cuts2.tex` |
| Cut 4.2 | Condense contestability properties | ✅ DONE | `04_case_study_cc_cuts2.tex` |
| Cut 5.1 | Condense baseline controls | ✅ DONE | `05_evaluation_cc_cuts2.tex` |
| Cut 5.2 | Condense validation methodology | ✅ DONE | `05_evaluation_cc_cuts2.tex` |
| Cut 5.3 | Remove duplicate FOAM validation para | ✅ DONE | `05_evaluation_cc_cuts2.tex` |
| Cut 6.1 | Condense template trees para | ✅ DONE | `06_implications_cc_cuts2.tex` |
| Cut 7.1 | Delete Third limitation (verifiability) | ✅ DONE | `07_limitations_cc_cuts2.tex` |
| Cut 7.2 | Condense Fifth→Fourth (cultural) | ✅ DONE | `07_limitations_cc_cuts2.tex` |
| Cut 7.3 | Condense Future Work | ✅ DONE | `07_limitations_cc_cuts2.tex` |
| Move 1 | Tournament format → Appendix ref | ✅ DONE | `05_evaluation_cc_cuts2.tex` |
| Move 2 | Citation categories → Appendix ref | ✅ DONE | `05_evaluation_cc_cuts2.tex` |
| Move 3 | Rubric list → Appendix ref | ✅ DONE | `05_evaluation_cc_cuts2.tex` |
| Cut 3.1 | FOAM approach last sentence | ⏳ PENDING | `03_foam_approach_cc_cuts.tex` |
| Cut 5.4 | Condense "Task selection" para | ✅ DONE | `05_evaluation_cc_cuts2.tex` |
| Cut 5.5 | Condense "Evidence corpus" para | ✅ DONE | `05_evaluation_cc_cuts2.tex` |
| Cut 5.6 | Condense "Debate artifact" para | ✅ DONE | `05_evaluation_cc_cuts2.tex` |
| Cut 5.7 | Condense "Model separation" para | ✅ DONE | `05_evaluation_cc_cuts2.tex` |

**Current status:** ✅ **24 pages** (619KB) - down from 26 pages!

### Additional Cuts Applied (~8 lines)

#### Cut 5.4: Condense "Task selection" paragraph ✅ DONE
**Find:**
```latex
\textbf{Task selection.} We evaluate in evidence-grounded policy debate generation because it combines (i) long-horizon argumentative planning, (ii) adversarial robustness expectations (arguments must survive challenge), and (iii) strict evidentiary norms (claims are conventionally supported with citations). In computational argumentation, even highly resourced systems have historically relied on constrained debate settings and bespoke pipelines; the Project Debater line of work illustrates both the ambition of debate as a benchmark and the practical need to structure and constrain the task for reliable evaluation~\cite{slonim2021autonomous}.
```

**Replace with:**
```latex
\textbf{Task selection.} We evaluate in policy debate generation because it combines long-horizon argumentative planning, adversarial robustness expectations, and strict evidentiary norms~\cite{slonim2021autonomous}.
```

**Savings:** ~4 lines

#### Cut 5.5: Condense "Evidence corpus" paragraph ✅ DONE
**Find:**
```latex
\textbf{Evidence corpus for provenance.} \foam{}'s evidence retrieval and validation leverage a structured debate-evidence corpus derived from OpenDebateEvidence, which (as released) contains \textbf{3.5M+} competitive debate documents with metadata useful for downstream argument mining and citation~\cite{roush2024opendebate}. Operationally, our system queries a vector database of $\sim$85,000 curated ``cards'' plus any newly processed sources, and the generation pipeline preserves \emph{sentence-level identifiers} so that downstream reviewers can trace claims to exact supporting spans.
```

**Replace with:**
```latex
\textbf{Evidence corpus.} \foam{} retrieves from OpenDebateEvidence ($\sim$85,000 curated cards)~\cite{roush2024opendebate}, preserving sentence-level identifiers for downstream traceability.
```

**Savings:** ~4 lines

---

## Summary of Recommended Cuts

| Section | Estimated Savings | Priority | Status |
|---------|-------------------|----------|--------|
| §2 Related Work | ~0.4 pages | High | ✅ DONE |
| §4 Case Study | ~0.3 pages | High | ✅ DONE |
| §5 Evaluation | ~0.4 pages | Medium | ✅ DONE |
| §7 Limitations | ~0.3 pages | Medium | ✅ DONE |
| §6 Implications | ~0.1 pages | Low | ✅ DONE |
| Move to Appendix | ~0.4 pages | Medium | ✅ DONE |
| **Total Applied** | **~1.9 pages** | |

---

## Section 1: Introduction (Keep as-is)
**Recommendation:** No cuts. Introduction is tight and sets up key contributions.

---

## Section 2: Related Work (~0.4 pages savings)

### Cut 2.1: Condense §2.1 (Explainability requirements)
**Current (lines 10-12):** Two dense paragraphs on explainability vs transparency.

**Proposed cut:** Merge into single paragraph, remove Adebayo citation discussion.

**Find:**
```latex
For accountability, explanations must be more than persuasive narratives; they must be \textbf{diagnostically useful} and \textbf{robust to strategic manipulation}. Empirically, Adebayo et al.\ show that post-hoc explanations can fail as diagnostic tools---\eg they may not reliably reveal spurious correlations that drive model behavior---undercutting the hope that explanation interfaces alone can serve as accountability checks~\cite{adebayo2022posthoc}. More broadly, the NLP interpretability literature distinguishes \emph{plausibility} (does an explanation look reasonable to humans?) from \emph{faithfulness} (does it track the true basis of the model's output?), and argues that faithful explanations require evaluation criteria and designs that go beyond ``nice-sounding'' rationales~\cite{jacovi2020towards}. As a result, explainability requirements in FAccT-relevant deployments should be stated in terms of \textbf{checkability}: the ability to trace claims to concrete support, interrogate counterfactuals, and isolate points of disagreement, rather than merely presenting a single coherent story~\cite{miller2019explanation,jacovi2020towards}.
```

**Replace with:**
```latex
For accountability, explanations must be more than persuasive narratives; they must be \textbf{diagnostically useful} and \textbf{robust to strategic manipulation}. The NLP interpretability literature distinguishes \emph{plausibility} (does an explanation look reasonable?) from \emph{faithfulness} (does it track the true basis of the output?), arguing that faithful explanations require evaluation criteria beyond ``nice-sounding'' rationales~\cite{jacovi2020towards}. Explainability requirements in FAccT-relevant deployments should be stated in terms of \textbf{checkability}: tracing claims to concrete support and isolating points of disagreement~\cite{miller2019explanation,jacovi2020towards}.
```

**Savings:** ~4 lines

### Cut 2.2: Condense §2.2 (Contestability)
**Current:** GDPR discussion is lengthy.

**Find:**
```latex
The GDPR is relevant here not only through transparency provisions, but also because Article 22 and associated provisions are commonly read as requiring procedural hooks such as the ability to obtain human intervention and contest certain automated decisions, even if the precise informational entitlements are debated~\cite{eu2016gdpr,wachter2017right}. Complementing legal requirements, the EU High-Level Expert Group's Trustworthy AI guidance explicitly treats accountability as including mechanisms for redress and the capacity to challenge outcomes, which aligns with FAccT's emphasis on socio-technical accountability rather than purely technical interpretability~\cite{eu2019trustworthy}. These sources jointly motivate a design target: \textbf{contestability must be implemented as an end-to-end workflow} that links reasons to evidence and enables structured challenge, rather than as a static explanatory artifact~\cite{raji2020closing,alfrink2023contestable}.
```

**Replace with:**
```latex
Legal and governance frameworks reinforce this design target: GDPR Article 22 provisions and EU Trustworthy AI guidance treat accountability as including mechanisms for redress and challenge~\cite{eu2016gdpr,eu2019trustworthy}. This motivates \textbf{contestability as an end-to-end workflow} linking reasons to evidence and enabling structured challenge~\cite{raji2020closing,alfrink2023contestable}.
```

**Savings:** ~5 lines

### Cut 2.3: Condense §2.3 (Pluralistic approaches)
**Find:**
```latex
In many high-stakes settings, disagreement is not merely empirical (``what are the facts?'') but normative (``which values should dominate?''). Feminist epistemology and science studies have long argued that knowledge claims are situated and that purportedly ``view from nowhere'' objectivity can mask whose interests and assumptions are being operationalized~\cite{haraway1988situated}. In governance terms, Dewey's account of public problem-solving similarly emphasizes that collective inquiry is iterative and that institutions must be structured to surface and revise the premises that guide decision-making, especially under conditions of uncertainty and plural publics~\cite{dewey1927public}. For AI accountability, these traditions motivate an architectural stance: rather than forcing a single model to output one authoritative rationale, systems should be designed to make \textbf{value trade-offs explicit} and to preserve dissenting considerations in a form that can be examined and contested~\cite{miller2019explanation,haraway1988situated}.
```

**Replace with:**
```latex
In high-stakes settings, disagreement is not merely empirical but normative. Feminist epistemology argues that knowledge claims are situated and ``view from nowhere'' objectivity can mask whose interests are operationalized~\cite{haraway1988situated}. For AI accountability, this motivates an architectural stance: systems should make \textbf{value trade-offs explicit} and preserve dissenting considerations that can be examined and contested~\cite{miller2019explanation,haraway1988situated}.
```

**Savings:** ~4 lines

---

## Section 3: FOAM Approach (Keep mostly as-is)
**Recommendation:** Minimal cuts. This section is essential for understanding the architecture.

### Cut 3.1: Minor trim in §3.5 (last paragraph)
**Find (end of section):**
```latex
Furthermore, unlike traditional chain-of-thought reasoning where reasoning and response are interwoven and in some cases reasoning is not always a reliable indicator for why outputs occurred, the template tree traversal process is a discrete step occurring prior and serving as a foundational infrastructure to drafting.
```

**Action:** DELETE this sentence entirely. The point is already made earlier.

**Savings:** ~2 lines

---

## Section 4: Case Study (~0.3 pages savings)

### Cut 4.1: Condense Phase 4 explanation
**Current:** Steps (a) and (b) are verbose.

**Find:**
```latex
\textbf{Step (a): sentence indexing and retrieval.} The system queries (i) a debate-evidence store (implemented in our current system as a vector database over a large set of debate ``cards'') and (ii) any other preprocessed sources permitted by the pipeline. Retrieved documents are segmented into sentences, each assigned a stable index, and returned to the deliberation workspace as a set of candidates with identifiers of the form \texttt{(document\_id, sentence\_id)} plus immutable citation metadata.

\textbf{Step (b): evidence selection and tagging.} The LLM is then prompted to (1) select which sentence IDs support each argument slot created in Phase 3 and (2) generate only a short ``tag'' that states what the selected evidence is being used to establish. Importantly, the model is not asked to restate the evidence; the evidence content in the final speech is assembled from the retrieved sentences themselves. This design eliminates an entire class of failure (fabricated quotations and invented citations) by construction: the model can be wrong about \emph{which} sentences to use, but it cannot invent sentences that are not in the retrieved set.
```

**Replace with:**
```latex
\textbf{Step (a): sentence indexing.} The system queries a debate-evidence store (vector database of debate ``cards'') and segments retrieved documents into sentences with stable identifiers \texttt{(document\_id, sentence\_id)}.

\textbf{Step (b): evidence selection.} The LLM selects sentence IDs supporting each argument slot and generates short ``tags'' stating what each sentence establishes. The model never restates evidence; final content is assembled from retrieved sentences directly. This eliminates fabricated quotations by construction: the model can select wrong sentences but cannot invent ones not in the retrieved set.
```

**Savings:** ~5 lines

### Cut 4.2: Condense "Accountability and contestability properties" paragraph
**Find:**
```latex
\textbf{Accountability and contestability properties.} Sentence-level provenance changes the contestation workflow from ``argue about what the model meant'' to ``inspect exactly what the model relied on.'' A stakeholder can challenge (i) \emph{relevance} (``this sentence does not establish the warrant you claim''), (ii) \emph{adequacy} (``the evidence is too weak/out of context''), or (iii) \emph{selection bias} (``you ignored stronger counterevidence available in the same corpus'')---and each challenge targets a concrete object (a sentence ID and its parent source). This is especially aligned with policy debate's evidence norms, which already treat quoted and highlighted text as the unit of disputation under cross-examination.
```

**Replace with:**
```latex
\textbf{Contestability properties.} Sentence-level provenance changes contestation from ``argue about what the model meant'' to ``inspect what the model relied on.'' Stakeholders can challenge (i) \emph{relevance}, (ii) \emph{adequacy}, or (iii) \emph{selection bias}---each targeting a concrete sentence ID. This aligns with policy debate norms where quoted text is the unit of disputation.
```

**Savings:** ~3 lines

---

## Section 5: Evaluation (~0.4 pages savings)

### Cut 5.1: Condense "Baseline controls" paragraph
**Current:** Very detailed mega-prompt description.

**Find:**
```latex
\textbf{Baseline controls (zero-shot AI).} To reduce confounding from artifact format and resource constraints, we generated the zero-shot baseline using Claude 4.5 in research mode, GPT-5 in deep research mode, SuperGrok Heavy, and Gemini 2.5 in research mode. We used a single standardized ``mega-prompt'' that enforced the same 1AC conventions and constraints used by elite debate program materials and by our FOAM case-building pipeline: \textbf{8 minutes of read-time target (1300--1700 words)}; debate formatting (ALL-CAPS tags, short analytic warrants above evidence); a fixed advantage/solvency structure; explicit impact calculus; and comparable evidence-density targets (\textbf{3--7 cards per advantage; 2--5 in solvency}). The prompt also enforced a strict \textbf{no-fabrication policy}: when reliable bibliographic details and quotations could not be produced, models were required to generate high-precision search strings and to mark uncertainty as \textbf{[EVIDENCE NEEDED]}. When the interface supported browsing, web access was enabled to reduce evidence-access confounds. Unlike FOAM, these baselines did not use multi-agent deliberation, typed syllogisms enforcement, or sentence-level provenance binding; thus, baseline citations remained unconstrained natural-language references and were evaluated under the same automated validation pipeline. We generated \textbf{one} case per topic per condition and used outputs \textbf{as-is} (no manual editing beyond uniform formatting normalization).
```

**Replace with:**
```latex
\textbf{Baseline controls (zero-shot AI).} We generated baselines using Claude 4.5, GPT-5, SuperGrok Heavy, and Gemini 2.5 in research modes with a standardized ``mega-prompt'' enforcing the same 1AC conventions: \textbf{1300--1700 words}, debate formatting, fixed advantage/solvency structure, and a strict \textbf{no-fabrication policy} requiring models to mark uncertainty as \textbf{[EVIDENCE NEEDED]}. Unlike FOAM, baselines did not use multi-agent deliberation, typed syllogisms, or sentence-level provenance; citations remained unconstrained and were evaluated under the same validation pipeline. We generated one case per topic per condition and used outputs as-is.
```

**Savings:** ~6 lines

### Cut 5.2: Condense validation methodology
**Find:**
```latex
\textbf{Why evidence validation is an accountability metric (not just ``anti-hallucination'').} In contestable systems, stakeholders must be able to \emph{locate} and \emph{evaluate} the grounds of a claim---especially where persuasive language can obscure weak or missing support. Audit frameworks similarly emphasize that assurance depends on traceable evidence artifacts rather than outcome plausibility alone~\cite{raji2020closing,lam2024assurance}. We therefore operationalize verifiability as a measurable property of each case's citations.
```

**Replace with:**
```latex
\textbf{Why evidence validation matters.} In contestable systems, stakeholders must locate and evaluate claim grounds. Audit frameworks emphasize that assurance depends on traceable evidence artifacts~\cite{raji2020closing,lam2024assurance}. We operationalize verifiability as a measurable property of citations.
```

**Savings:** ~3 lines

### Cut 5.3: Remove "How FOAM changes the validation problem" paragraph
**Reason:** This duplicates information in the "Validation procedure" paragraph.

**Find:**
```latex
\textbf{How \foam{} changes the validation problem.} \foam{}'s sentence-level provenance changes citation validation from a semantic retrieval problem into a \emph{pointer integrity} problem: the model is never asked to reproduce source text, but instead selects sentence indices from retrieved documents and attaches them to specific argument components. This design greatly reduces degrees of freedom for fabrication and enables deterministic re-checking of a case's evidentiary backbone.
```

**Action:** DELETE entirely.

**Savings:** ~4 lines

---

## Section 6: Implications (~0.1 pages savings)

### Cut 6.1: Trim "Template trees as contestability scaffolds"
**Find:**
```latex
\textbf{Template trees as contestability scaffolds.} Template tree traversal (Section~\ref{sec:appendix-template-tree}) operationalizes these challenge pathways architecturally. Each typed syllogism component---uniqueness, link, internal link, impact---corresponds to a discrete contestation target with explicit evidentiary bindings. The traversal log records not only \textit{what} claims were made but \textit{why} the structure took its current form. This enables three challenge modalities: (1) \textbf{evidence challenges} (``sentence ID 47 does not support this link''), (2) \textbf{structural challenges} (``the impact calculus lacks probability estimation''), and (3) \textbf{normative challenges} (``why utilitarian framing over rights-based?''). Stakeholders can contest at the level of epistemic assumptions, not only conclusions---distinguishing \foam{} from systems that expose reasoning traces without exposing structural choices.
```

**Replace with:**
```latex
\textbf{Template trees as contestability scaffolds.} Each typed syllogism component---uniqueness, link, impact---corresponds to a discrete contestation target with evidentiary bindings. The traversal log records \textit{what} claims were made and \textit{why} the structure took this form, enabling evidence, structural, and normative challenges at the level of epistemic assumptions, not only conclusions.
```

**Savings:** ~4 lines

---

## Section 7: Limitations (~0.3 pages savings)

### Cut 7.1: Merge limitations Third and Fourth
**Current:** Third (verifiability vs contestability) and Fourth (narrow scope) are partially redundant.

**Find (Third paragraph):**
```latex
Third, our evaluation measures verifiability rather than full contestability. A complete contestability evaluation would measure: (i) \textit{localization efficiency}---time/steps to identify a disputed premise in the mediation graph; (ii) \textit{challenge success rate}---whether targeted counterevidence triggers appropriate revision; (iii) \textit{revision locality}---how much structure changes to fix an identified issue; and (iv) \textit{perceived procedural fairness}---whether affected parties find the workflow comprehensible. We treat these as essential follow-on studies (Section~\ref{sec:future-work}).
```

**Action:** DELETE entirely. This information is already in the research questions scope discussion and the fourth limitation covers the key point.

**Savings:** ~4 lines

### Cut 7.2: Condense Fifth limitation (cultural assumptions)
**Find:**
```latex
Fifth, our evaluation embeds cultural assumptions that may limit generalizability. American competitive policy debate reflects particular adversarial norms---burden-shifting, time-constrained advocacy, winner-take-all adjudication---that do not map cleanly onto all contestation contexts. In settings where affected parties lack advocacy resources, adversarial framing may exacerbate power asymmetries. \foam{}'s architecture is agnostic to adversarial vs.\ collaborative deliberation; future work should explore instantiations in participatory governance settings (\eg citizen assemblies, collaborative sensemaking) where the goal is joint understanding rather than competitive victory.
```

**Replace with:**
```latex
Fourth, our evaluation embeds cultural assumptions. American policy debate reflects adversarial norms that may not map to all contestation contexts; in settings where parties lack advocacy resources, adversarial framing may exacerbate power asymmetries. Future work should explore collaborative deliberation instantiations (\eg citizen assemblies).
```

**Savings:** ~3 lines (and renumber)

### Cut 7.3: Condense Future Work
**Find:**
```latex
A first priority is human-subject evaluation of contestability as an interaction property rather than a static artifact property. We plan controlled studies in which participants (including domain experts and affected stakeholders) attempt to (i) locate supporting evidence for a contested sentence, (ii) challenge a warrant or inference step, and (iii) request or compare alternative perspective nodes. Primary outcomes should include time-to-challenge, challenge success rates, perceived procedural fairness, and the degree to which the system supports actionable revision pathways (\eg retracting a claim, swapping evidence, or surfacing counter-arguments) rather than merely producing longer explanations.

A second priority is extending \foam{} with optimization and training methods while preserving contestability constraints. Preliminary results in iterative preference learning suggest that tactic selection and evidence integration can be improved, but also reveal failure modes that matter for accountable deliberation. Future work should explore training objectives that explicitly reward faithful warrant-evidence alignment (not only persuasiveness) and contestation-aware curricula.
```

**Replace with:**
```latex
First, human-subject evaluation of contestability as an interaction property: measuring time-to-challenge, challenge success rates, and perceived procedural fairness when participants attempt to locate evidence, challenge warrants, or compare perspective nodes.

Second, extending \foam{} with optimization methods while preserving contestability constraints, including training objectives that reward faithful warrant-evidence alignment rather than only persuasiveness.
```

**Savings:** ~6 lines

---

## Section 8: Conclusion (Keep as-is)
**Recommendation:** No cuts. Conclusion is appropriately concise.

---

## Appendix Considerations

If additional cuts needed, consider:
1. Remove full syllogism table (Table in Appendix A.2) - keep only 5-6 key types
2. Condense pseudocode - keep only DIALECTICAL_REFINE, cut the others
3. Remove tournament dataset table (redundant with main text)

---

## MOVE to Appendix (~0.4 pages savings)

Content that can be moved to appendix (which doesn't count against page limit) with brief inline references.

### Move 1: Tournament format details (§5.3)
**Current:** Detailed bracket structure explanation.

**Find:**
```latex
\textbf{Tournament format and blinding.} All submissions were anonymized and assigned unique IDs (\eg \texttt{Case\_001}), and judging proceeded purely on content without revealing origin. Cases advanced through a modified Swiss-style bracket with double elimination, and pairings were balanced by strategic approach (\eg traditional policy vs.\ kritik) to reduce ``judge adaptation'' artifacts. Ties within a narrow score band triggered evidence validation as a tiebreaker, keeping accountability-relevant verifiability salient in advancement decisions. \textbf{All 66 cases were scored once under the rubric; Tables~\ref{tab:main-results}--\ref{tab:validation} report aggregate statistics over the full set and do not depend on bracket advancement.}
```

**Replace with:**
```latex
\textbf{Tournament format.} All 66 submissions were anonymized and evaluated in a double-blind tournament (Appendix~\ref{sec:appendix-evaluation}). Tables~\ref{tab:main-results}--\ref{tab:validation} report aggregate statistics over the full corpus.
```

**Savings:** ~4 lines

### Move 2: Citation classification details (§5.4)
**Current:** Four-category breakdown inline.

**Find:**
```latex
\textbf{Automated citation checks and metric definitions.} Each citation was automatically checked against the referenced source and classified into four categories: \textit{exact match} (verbatim substring present in source), \textit{partial match} ($>$85\% character overlap or minor formatting differences), \textit{paraphrase} (semantic similarity $>$0.7 but not verbatim), or \textit{fabricated} (no matching content in cited source).
```

**Replace with:**
```latex
\textbf{Automated citation checks.} Each citation was classified as exact match, partial match, paraphrase, or fabricated based on source verification (classification criteria in Appendix~\ref{sec:appendix-provenance}).
```

**Savings:** ~3 lines

### Move 3: Rubric dimension list (§5.3)
**Current:** Five-item bullet list duplicates appendix table.

**Find:**
```latex
\textbf{Rubric and judge.} Following established LLM-as-judge methodology~\cite{zheng2023judging}, a Claude Opus 4 judge evaluated each case on five weighted dimensions:
\begin{itemize}
    \item \textbf{Argumentation Strength} (25\%)
    \item \textbf{Evidence Quality} (25\%)
    \item \textbf{Strategic Coherence} (20\%)
    \item \textbf{Innovation} (15\%)
    \item \textbf{Competitive Viability} (15\%)
\end{itemize}

The rubric was designed to reward both argumentative competence and evidence-groundedness, while preserving enough structure for reproducibility.
```

**Replace with:**
```latex
\textbf{Rubric and judge.} Following LLM-as-judge methodology~\cite{zheng2023judging}, a Claude Opus 4 judge evaluated each case on five weighted dimensions (Argumentation 25\%, Evidence 25\%, Coherence 20\%, Innovation 15\%, Viability 15\%; full rubric in Appendix~\ref{sec:appendix-evaluation}).
```

**Savings:** ~6 lines

---

## Implementation Order

1. **High Priority Cuts** (do first):
   - Cut 2.1, 2.2, 2.3 (Related Work)
   - Cut 4.1, 4.2 (Case Study Phase 4)
   - Cut 5.1, 5.2, 5.3 (Evaluation baseline/validation)

2. **Medium Priority Cuts**:
   - Cut 7.1, 7.2, 7.3 (Limitations)
   - Cut 6.1 (Implications)

3. **Move to Appendix** (preserves content):
   - Move 1, 2, 3 (Evaluation details → Appendix)

4. **Low Priority** (only if still over):
   - Cut 3.1 (FOAM approach last sentence)
   - Additional appendix moves
