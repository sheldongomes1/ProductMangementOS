# PersonalOS — Portfolio Roadmap (One Page)

Goal: Pick **2–3 projects** that most credibly signal “Google-level PM/TPM” by demonstrating **product judgment + agentic AI + grounded RAG + evals + shipping**.

---

## 1) The 3 Bets (what to focus on)

### BET #1 — Flagship: Strategic Fit Canvas (Recruiter-facing interactive resume/JD)
**Why this wins:** feels like a real product, showcases PM thinking + UX + AI, and is instantly shareable.
- **Target users:** recruiters + hiring managers
- **Core promise:** upload JD + resume → get a structured “fit view” (radar, timeline, narrative, gaps, next actions)
- **North Star metric:** % of viewers who interact with ≥2 widgets + click “Share” / “Download summary”

**Google-bait upgrades (must-have):**
- **Agent workflow:** “Evaluator agent” (fit scoring) + “Coach agent” (gap plan) + “Editor agent” (tight narrative)
- **Evals:** golden set of 20 JDs/resumes → measure consistency of fit dimensions + hallucination checks
- **Telemetry:** track which dimensions users hover/click, where they drop off
- **Artifacts:** 2-min demo video + public demo link + README “How it works” + eval report

**Definition of done (V1):**
- JD + resume upload, dimension config, radar chart, impact timeline, 1-page summary export, eval report page.

---

### BET #2 — Credibility Anchor: Investing Fees “Silent Killers” Assistant (SEC/FINRA-grounded RAG)
**Why this wins:** shows you understand **grounding + citations + trust**, which is exactly what serious AI product teams care about.
- **Target users:** everyday investors + advisors + curious professionals
- **Core promise:** ask “what fees am I paying / what does this term mean / what should I watch for?” with **citations**
- **North Star metric:** citation-backed answer rate + “helpfulness” score from eval set

**Google-bait upgrades (must-have):**
- **Grounding discipline:** authoritative sources only (SEC, FINRA, broker disclosures)
- **RAG quality:** chunking + retrieval + reranking + citation formatting
- **Evals:** test set of 50 questions → score factuality, citation correctness, refusal behavior
- **UX twist:** “Show me the receipts” mode (answers side-by-side with cited excerpts)

**Definition of done (V1):**
- Ask a question → answer with citations + “why this matters” + common pitfalls + confidence/limits + eval dashboard.

---

### BET #3 — Technical Flex: Narrative Divergence Detector (Crypto narratives vs price)
**Why this wins:** demonstrates multi-source pipelines, agentic reasoning, and measurable signals.
- **Target users:** crypto-curious investors (and hiring managers who like data/ML thinking)
- **Core promise:** detect when **social momentum diverges** from price action; explain “why” with evidence
- **North Star metric:** weekly active users + “insight usefulness” rating + model precision on labeled examples

**Google-bait upgrades (must-have):**
- **Agent pipeline:** collector → cleaner → topic/narrative extractor → divergence scorer → explainer
- **Evals:** label a small dataset (20–50 events) for “true divergence” vs noise → evaluate precision/recall
- **Transparency:** “evidence view” showing top sources behind each insight
- **Production feel:** scheduled runs + caching + monitoring + cost/latency budget

**Definition of done (V1):**
- Dashboard of top divergences + drill-down explanation + evidence links + eval summary + weekly email digest.

---

## 2) What to Deprioritize (for now) — “good ideas, weaker signal”
These are fine, but they either (a) look like plumbing, (b) don’t scream “serious AI product craft,” or (c) overlap with better bets.

- **Notion conversation bot (Zapier loop)** — too workflow-y; better as an implementation detail inside a flagship.
- **Landbot generic bot experiences** — good UI shell, but needs a strong core use-case (attach it to Bet #2 or #1).
- **Stack Overflow AI trends data viz** — nice content, but weak agentic/evals signal.
- **Zevi music hook generator** — cool, but risks “toy project” perception unless it has strong evals + differentiated UX.
- **Tax season assistant** — high utility but can balloon into complexity; keep as optional “fast add-on” later.
- **Bedtime story generator** — keep as a “polish + upgrade” project, not a primary bet (unless you want consumer AI focus).

---

## 3) How to Upgrade the Remaining 7 into “Google-bait” (if you revisit)
Use this checklist to “level up” any project quickly:

### The Google-bait checklist (add these 5 things)
1. **Grounding** (citations or clear provenance)  
2. **Agentic workflow** (multi-step tool use, not one-shot chat)  
3. **Evals** (golden set, regression tests, measurable improvements)  
4. **Telemetry** (usage analytics + failure logging)  
5. **Shipping artifacts** (demo link, repo, 2-min video, write-up)

---

## 4) Recommended Build Order (fast momentum + compounding)
1) **Fees Assistant (Bet #2)** — fastest credibility win; easiest to show citations + evals quickly  
2) **Strategic Fit Canvas (Bet #1)** — flagship polish; best recruiter virality + narrative alignment  
3) **Divergence Detector (Bet #3)** — technical flex; strongest “systems + data + evals” signal  

---

## 5) Public Output Package (what each project must ship with)
For each of the 3 bets, ship the same “professional bundle”:

- **Live demo**
- **Repo with clean README**
- **Architecture diagram**
- **Eval report** (what you tested + results + what you improved)
- **2-minute demo video**
- **1 LinkedIn post** with: problem → demo GIF → what’s novel (agents/RAG/evals) → link

---

## 6) My Recommendation on the 10 Ideas (status)
- **Focus now:** Strategic Fit Canvas, Fees Assistant, Divergence Detector
- **Upgrade later (nice-to-have):** Bedtime Story Generator (add evals + safety + multimodal), Tax Assistant
- **Park for now:** Notion bot plumbing, Landbot generic, Stack Overflow viz, Music hook generator, AI Fit Score experiment (unless you want a pure experimentation case study)

---

## 7) If you want the “2-project only” version (even tighter)
If you want maximum concentration:
- **Strategic Fit Canvas** (flagship)
- **Fees Assistant** (grounded RAG credibility)

Then weave the divergence detector ideas as “future work” in the write-up.
