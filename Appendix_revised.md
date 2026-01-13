# Appendix: FOAM Implementation Details

This appendix provides technical specifications for the FOAM architecture components described in the main paper. All specifications are derived from the reference implementation.

---

## Appendix A: Core FOAM Components

### A.1 Perspective Nodes

A **Perspective Node** is a composite configuration that establishes the philosophical and methodological orientation for an agent throughout the deliberation process. Unlike a simple role assignment, perspective nodes encode multi-dimensional worldview parameters that constrain all downstream generation.

**Dimension Categories (32 total dimensions):**

| Category | Count | Examples |
|----------|-------|----------|
| Debate Technique | 11 | `resolution_stance`, `argument_architecture`, `negative_strategy`, `organization_structure`, `evidence_integration`, `rhetorical_framing`, `clash_orientation`, `impact_articulation`, `argument_depth_distribution`, `warrant_density`, `theory_deployment` |
| Epistemological | 2 | `epistemological_stance` (empirical_positivism, constructivism, critical_realism, standpoint_theory, pragmatism, etc.), `evidence_hierarchy` |
| Ethical/Impact | 2 | `impact_framework` (utilitarian, deontological, virtue_ethics, existential_risk, structural_violence), `risk_calculus` |
| Strategic | 1 | `strategic_posture` |
| Belief Paradigm | 8 | `truth_orientation`, `theism_metaphysics`, `moral_objectivity`, `human_nature`, `source_authority`, `free_will_stance`, `progress_narrative`, `meaning_of_life` |
| Policy Paradigm | 8 | `fiscal_orientation`, `market_vs_state`, `equity_vs_efficiency`, `social_policy_lens`, `global_vs_national`, `environmental_stance`, `temporal_horizon`, `governance_style` |

**Coherence Scoring:**

Perspective nodes include a coherence score (0.0-1.0) that measures internal consistency across dimensions. The scoring algorithm:

1. Starts at neutral (0.5)
2. Applies affinity bonuses: `score += rule.strength * 0.1` for compatible dimension pairs
3. Applies incompatibility penalties: `score -= rule.severity * 0.15` for conflicting pairs
4. Clamps to [0.0, 1.0]

**Generation via Shuffle:**

New perspective nodes are generated using a `shuffle()` method that:
- Accepts optional constraints (fixed dimension values)
- Enforces minimum coherence threshold (default 0.3)
- Retries up to 100 times to find coherent combinations
- Validates against incompatibility rules before accepting

```python
perspective = PerspectiveNode.shuffle(
    constraints={"argument_architecture": "critical_kritik"},
    min_coherence=0.5
)
```

---

### A.2 Dialectical Refinement Protocol

The dialectical refinement protocol implements iterative improvement through structured adversarial dialogue. This is implemented using DSPy's `ConfigurableAdversarialRefinement` module.

**Architecture:**

```
                    ┌─────────────┐
                    │   Proposer  │
                    │  (BestOfN)  │
                    └──────┬──────┘
                           │ proposal
                           ▼
                    ┌─────────────┐
                    │    Critic   │
                    │  (BestOfN)  │
                    └──────┬──────┘
                           │ criticism
                           ▼
                    ┌─────────────┐
                    │  Evaluator  │
                    │  (ChainOfThought) │
                    └──────┬──────┘
                           │ score_difference, reasoning
                           ▼
                    ┌─────────────┐
                    │   Refiner   │
                    │  (BestOfN)  │
                    └──────┴──────┘
                           │
                    [loop until convergence]
```

**Configuration Parameters:**

| Parameter | Default | Description |
|-----------|---------|-------------|
| `max_iterations` | 5 | Maximum refinement cycles |
| `convergence_threshold` | 0.0 | Score variance threshold for early stopping |
| `best_of_n` | 3 | Candidates generated per role |
| `use_cot` | True | Enable chain-of-thought reasoning |

**Convergence Detection:**

The system monitors `score_differences` (positive = proposal wins, negative = critic wins) across iterations. Convergence occurs when:
- Score variance falls below threshold, OR
- Proposal achieves strong defense (score_diff > 5.0), OR
- Maximum iterations reached

**Rubric-Based Evaluation:**

Each role uses configurable rubrics:
- **ProposalRubric**: Relevance, clarity, feasibility, innovation, completeness
- **CriticRubric**: Identifies genuine flaws, provides specific criticism, challenges assumptions
- **EvaluatorRubric**: Weighs proposal strengths vs. criticism validity

---

### A.3 Flow Models (Deliberation Record)

The deliberation record is captured using a hierarchical **Flow** model that tracks all arguments, evidence, and their relationships throughout a debate round.

**Schema Hierarchy:**

```
Flow
├── topic: str
├── flow_pages: List[FlowPage]
│   ├── name: str (e.g., "Case", "Disadvantage 1")
│   ├── page_type: str ("case", "off_case", "theory", "kritik")
│   └── flow_page_speeches: List[FlowPageSpeech]
│       ├── speech_type: str ("1AC", "1NC", "2AC", etc.)
│       └── arguments: List[Argument]
│           ├── content: str
│           ├── argument_type: str
│           ├── syllogism: Reference[Syllogism]
│           ├── template_node: Reference[TemplateNode]
│           ├── evidence: Reference[DebateEvidence]
│           ├── rebuttal_to: Reference[Argument]
│           ├── perspective: Reference[PerspectiveNode]
│           └── selected_evidence_ids: List[str]
└── cross_examinations: List[CrossExaminationExchange]
```

**Provenance Tracking:**

Each `Argument` maintains explicit references to:
- The **syllogism type** that structures its logical form
- The **template node** that allocated its word budget
- The **evidence** supporting its claims (with sentence-level IDs)
- The **perspective** that guided its construction
- Any **argument it rebuts** (for tracing dialectical chains)

---

## Appendix B: Pipeline Implementation

### B.1 Five-Phase Generation Pipeline

The FOAM pipeline operates through five sequential phases:

**Phase 1: Perspective Assignment**
- Generate or select a PerspectiveNode
- Validate coherence score meets threshold
- Persist perspective for downstream constraint enforcement

**Phase 2: Plan Generation & Refinement**
- Generate 4 candidate policy positions
- Select most promising approach
- Apply dialectical refinement (minimum 3 iterations)
- Conduct targeted web research for policy specifics

**Phase 3: Template Tree Traversal**
- Navigate hierarchical decision tree (critical vs. traditional, etc.)
- Allocate word budgets across syllogism types
- Generate `TemplateTraversal` objects for each leaf node

**Phase 4: Research & Evidence Gathering**
- Query vector database (OpenDebateEvidence, ~85k cards)
- Conduct web research via multiple APIs (Tavily, arXiv, Google)
- Apply sentence-level provenance: number each sentence in source documents
- LLM identifies relevant sentence IDs (never reproduces text directly)
- Validate quotes against source fulltext

**Phase 5: Compilation**
- Assemble syllogisms in proper order
- Verify perspective consistency
- Validate evidence-claim alignment
- Output complete deliberation artifact

---

### B.2 Typed Syllogisms

FOAM enforces logical validity through **17 typed syllogisms**, each with required argument components:

| Syllogism Type | Required Components | Usage Context |
|----------------|---------------------|---------------|
| `advantage` | uniqueness, link, internal_link, impact | Affirmative benefits |
| `inherency` | barrier_type, current_status, barriers | Why status quo fails |
| `solvency` | mechanism, actor_capability, effectiveness | How plan works |
| `disadvantage` | uniqueness, link, impact | Negative harms |
| `counterplan` | text, competition, net_benefit | Alternative policy |
| `topicality` | interpretation, violation, standards, voter | Definitional challenges |
| `kritik` | link, impact, alternative | Systemic critique |
| `case_turn` | target, direction, impact | Flip affirmative argument |
| `rebuttal` | target, response_type, warrant | Direct refutation |
| `framework` | interpretation, standards | Evaluative lens |
| `extension` | original_argument, development | Expand existing arg |
| `contention` | claim, warrant, impact | Generic argument |
| `critical_opening` | hook, theoretical_framework | K-aff introduction |
| `critical_link` | target, connection | K link story |
| `critical_impact` | type, description, ongoing_nature | K impact framing |
| `critical_alternative` | advocacy, mechanism, praxis | K solvency |
| `role_of_ballot` | description, framing, impact | Judge instruction |

**Validation Rules:**

Each syllogism type includes validators ensuring structural completeness. For example, an `advantage` requires:
- At least 30% of word allocation to impact explanation
- Non-empty uniqueness and link components
- Evidence references for empirical claims

---

### B.3 Template Tree Traversal

The template tree is a hierarchical decision structure that guides argument generation and resource allocation. Each path from root to leaf represents a complete argument specification with word budget.

**Node Types:**

| Type | Description | Example |
|------|-------------|---------|
| `root` | Entry point for debate format | "Policy Debate" |
| `speech` | Speech type container | "1AC", "1NC", "2AR" |
| `branch` | Strategic decision point | "Traditional" vs "Critical", "Advantages" |
| `leaf` | Terminal argument specification | "Economic Impact", "Uniqueness" |
| `meta` | Cross-cutting template groups | "Impact Scenarios" |

**TemplateNode Schema:**

```python
class TemplateNode:
    # Identity
    name: str                      # Human-readable name
    node_type: str                 # root, speech, branch, leaf, meta

    # Hierarchy
    parent_id: str                 # Parent node reference
    children_ids: List[str]        # Child node references
    depth: int                     # Tree depth (root=0)
    path_from_root: List[str]      # Full path for tracing

    # Content specification
    syllogism_type: str            # Required syllogism (leaf nodes)
    leaf_argument_type: str        # Specific argument type
    word_budget: int               # Allocated words
    terminal_branch: bool          # All children are leaves

    # Strategic guidance
    strategic_considerations: List[str]
    evidence_requirements: List[str]
    children_choice_prompt: str    # LLM guidance for child selection
```

**Example: Traditional 1AC Template Tree**

```
Policy Debate (root)
└── 1AC (speech, word_budget=1300)
    ├── Plan Text (branch, 50 words)
    │   └── USFG Action (leaf, syllogism=null)
    │
    ├── Inherency (branch, 150 words, syllogism=inherency)
    │   ├── Structural Barrier (leaf, 75 words)
    │   └── Current Status (leaf, 75 words)
    │
    ├── Solvency (branch, 200 words, syllogism=solvency)
    │   ├── Mechanism (leaf, 100 words)
    │   └── Actor Capability (leaf, 100 words)
    │
    └── Advantages (branch, 900 words)
        │
        ├── Economic Advantage (branch, 450 words, syllogism=advantage)
        │   ├── Uniqueness (leaf, 100 words, type=uniqueness)
        │   ├── Link (leaf, 100 words, type=link)
        │   ├── Internal Link (leaf, 100 words, type=internal_link)
        │   └── Impact (leaf, 150 words, type=impact)
        │
        └── Security Advantage (branch, 450 words, syllogism=advantage)
            ├── Uniqueness (leaf, 100 words, type=uniqueness)
            ├── Link (leaf, 100 words, type=link)
            ├── Internal Link (leaf, 100 words, type=internal_link)
            └── Impact (leaf, 150 words, type=impact)
```

**Traversal Process:**

1. **Start at root**: Load debate format template
2. **Select speech**: Navigate to speech type (1AC)
3. **Branch decisions**: At each branch, LLM evaluates `children_choice_prompt` to select path based on:
   - Assigned perspective constraints
   - Plan specifics
   - Strategic goals
4. **Leaf allocation**: When reaching leaves, system generates `TemplateTraversal` objects:

```python
TemplateTraversal(
    session_id="abc123",
    speech_type="1AC",
    path_nodes=["root", "1AC", "Advantages", "Economic", "Impact"],
    path_names=["Policy Debate", "1AC", "Advantages", "Economic Advantage", "Impact"],
    word_budget=150,
    research_order=4,
    leaf_template_id="econ_impact_001",
    syllogism_type="advantage"
)
```

**Word Budget Allocation:**

The system enforces word budgets through validation:
- Parent budget = sum of children budgets
- Minimum allocations per syllogism component (e.g., impact ≥ 30% of advantage)
- Overruns trigger automatic condensation or reallocation

**Dynamic Template Generation:**

When the existing template tree lacks an appropriate path, the system can:
1. Generate new `TemplateNode` with appropriate `syllogism_type`
2. Mount it to an existing branch node
3. Propagate word budget from parent
4. Continue traversal through the new node

This allows the template library to grow organically as the system encounters novel argumentative needs while maintaining structural validity.

---

### B.4 Sentence-Level Provenance

The sentence-level provenance system prevents hallucination by constraining LLM outputs to reference existing text rather than reproduce it.

**Process:**

1. **Indexing**: Each sentence in a source document receives a unique ID
2. **Selection**: LLM outputs sentence IDs (e.g., `[sent_14, sent_15, sent_18]`) rather than quoted text
3. **Assembly**: System retrieves actual sentences by ID and formats as evidence card
4. **Validation**: `QuoteValidator` confirms selected text exists in source

**QuoteValidator Algorithm:**

```python
def validate_quote(spoken_text, fulltext, similarity_threshold=0.85):
    # Split by delimiter " /.../ "
    segments = spoken_text.split(' /.../ ')

    for segment in segments:
        # Try exact match
        if normalize(segment) in normalize(fulltext):
            found_quotes.append(segment)
        # Try fuzzy match
        elif find_fuzzy_match(segment, fulltext) >= threshold:
            found_quotes.append(segment)
        # Check for hallucination
        elif is_hallucinated(segment, fulltext):
            hallucinated.append(segment)

    return QuoteValidationResult(
        is_valid=(len(missing) == 0 and len(hallucinated) == 0),
        match_ratio=len(found) / len(segments)
    )
```

---

## Appendix C: Evaluation Methodology

### C.1 Tournament Dataset

The evaluation corpus consisted of 66 first affirmative constructive (1AC) cases:

| Source | Count | Description |
|--------|-------|-------------|
| FOAM System | 22 | Generated using full pipeline with Claude Haiku 3/Sonnet 3.5 for generation |
| Human Expert | 23 | Randomly selected from Dartmouth, Georgetown, Michigan, Emory debate camps |
| Zero-Shot AI | 21 | Generated by Gemini, Claude, ChatGPT, Grok with deep research settings |

**Model Separation:** FOAM system outputs were generated using Claude Haiku 3 (primary generation) and Sonnet 3.5 (refinement). Tournament judging was performed by Claude Opus 4, ensuring separation between generation and evaluation models to prevent self-enhancement bias.

### C.2 Tournament Protocol

**Anonymization:**
- All cases assigned unique IDs (e.g., "Case_001")
- Metadata and formatting cues stripped
- Origin completely hidden from judges

**Bracket Structure:**
- Modified Swiss-system with double elimination
- Initial grouping by strategic approach (Traditional, Kritik, Soft-Left)
- Head-to-head evaluation in groups of 2-3
- Top 50% advance per group
- Losers' bracket provides second chances
- Statistical ties (within 2.0 points) resolved by evidence validation

### C.3 Judging Criteria

Evaluation by Claude Opus 4 across five weighted dimensions:

| Dimension | Weight | Components |
|-----------|--------|------------|
| Argumentation Strength | 25% | Logical consistency, warrant quality, impact development, causal reasoning |
| Evidence Quality | 25% | Source authenticity, author expertise, contextual completeness, validation scores |
| Strategic Coherence | 20% | Internal consistency, game-theoretic positioning, preemptive objection handling |
| Innovation & Uniqueness | 15% | Novel arguments, creative positioning, differentiation |
| Competitive Viability | 15% | Practical success potential, appropriate scope, opponent difficulty |

### C.4 Evidence Validation

**Classification Categories:**

| Match Type | Definition | Validation Score |
|------------|------------|------------------|
| `exact` | Verbatim match in source | 1.0 |
| `partial` | Substring match with high overlap | 0.7-0.9 |
| `paraphrase` | Semantic match via keyword overlap | 0.5-0.7 |
| `not_found` | No match in retrieved source | 0.0 |
| `error` | Source URL unreachable | N/A |

**Perfect Validation Rate:**
Percentage of cases where ALL cited evidence achieves `exact` or `partial` match status.

| Source | Perfect Validation Rate |
|--------|------------------------|
| FOAM System | 76.2% |
| Human Expert | 8.7% |
| Zero-Shot AI | 0.0% |

---

## Appendix D: Evaluation Rubric

The complete rubric used for LLM-as-judge evaluation:

```
EVALUATION CRITERIA (100 points total):

1. ARGUMENTATION STRENGTH (25 points)
   - Logical consistency and warrant quality
   - Impact development and link chains
   - Advantage/disadvantage structure
   - Causal reasoning coherence

2. EVIDENCE QUALITY (25 points)
   - Source credibility and recency
   - Accurate citation and quotation
   - Relevance to claims made
   - Validation scores from automated checking

3. STRATEGIC COHERENCE (20 points)
   - Internal consistency of approach
   - Judge adaptation potential
   - Topicality and resolution connection
   - Preemptive objection handling

4. INNOVATION & UNIQUENESS (15 points)
   - Novel arguments or approaches
   - Creative strategic positioning
   - Differentiation from common cases

5. COMPETITIVE VIABILITY (15 points)
   - Practical debate round success potential
   - Difficulty for opponents to answer
   - Time allocation efficiency
   - Appropriate scope for format
```

---

*Implementation available at: https://github.com/dgonier/oneac_tournament*
