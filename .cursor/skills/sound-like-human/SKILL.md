---
name: sound-like-human
description: Use when drafting or polishing LinkedIn posts to sound natural, specific, and human.
---

# Sound Like Human

# Writing That Doesn't Sound Like AI (LinkedIn-ready)

## When to use this skill
- User asks to draft, rewrite, or polish a LinkedIn post/caption/comment.
- User asks to make writing "sound human", "less AI", or "less slop".
- User wants a voice match to their prior writing samples.

## Project-specific context to pull before writing
- `Knowledge/linkedin-strategy.md` for anti-slop and platform strategy.
- `Knowledge/voice-samples/` for tone/rhythm matching.
- Relevant shipped artifact context (demo, metrics, tradeoffs) for specificity.

## Output standard for this project
- Lead with a specific observation or concrete result.
- Include at least one real detail (number, tradeoff, failure mode, or decision).
- Avoid hype language and formulaic AI structure.
- End with a natural stopping point or a focused CTA.

## Quick LinkedIn template (use by default)
Use this lightweight structure unless the user asks for a different format:

1) Hook (1 line)
- Specific observation, result, or tension.

2) Proof (2-4 lines)
- What was built/done.
- One concrete detail (metric, failure mode, tradeoff, or decision).

3) Lesson (2-3 lines)
- What changed in your thinking/process.
- Why this matters for PM execution or product quality.

4) CTA (1 line)
- One focused question or invitation for discussion.

A reusable “skill” you can paste into Cursor/Claude/ChatGPT to draft faster **without** the telltale LLM voice.  
Core idea: **You own the structure; the model fills it.** Then you run a quick judge → revise loop.

---

## What “sounds like AI” usually is

Most people react to **structure**, not just vocabulary.

### Common AI-structure fingerprints
- Too many bullet lists instead of developed paragraphs
- Many similar subheadings (“Understanding X”, “The Future of Y”)
- Standard essay frame: broad intro → 3 neat sections → generic recap
- Heavy signposting / meta (“In this section we’ll…”, “Now that we’ve explored…”)
- Same-sized paragraphs with identical rhythm
- Writing about the piece instead of the topic
- Generic examples that add no new info (“Businesses can use AI to streamline…”)
- Vague zoom-out ending (“As AI evolves…”)

**Fix:** change the skeleton before changing words.

---

## Structural rules (make it read human)

### 1) Decide the outline yourself
- Sketch a quick outline (uneven sections are good).
- Tell the model: **“Turn this outline into prose. Do not add extra sections.”**

### 2) Favor paragraphs over lists
- Use bullets only when genuinely needed (steps, distinct items).
- Prefer continuous narrative with concrete examples.

### 3) Limit analogies
- Max **one** analogy unless explicitly requested.
- No “Imagine…” / “Think of it like this…” intros.

### 4) Kill meta + signposting
- Ban “In this section…”, “As mentioned earlier…”, “Now that we’ve…”.

### 5) Break symmetry on purpose
- Vary paragraph length.
- Don’t end every section with a mini-summary.

### 6) Use AI for building blocks, not whole chapters
Prompt for components:
- “Give 3 alternative ways to structure this section.”
- “List **specific** examples that make this concrete.”
- “Suggest 2 transitions that **don’t recap** the previous paragraph.”

### 7) Do a structural pass first
- Convert each paragraph into a **one-line summary**.
- If it reads like “definition → list → recap → vague future”, reorder/cut.
- Often: delete the first paragraph, trim recaps, end one step earlier.

---

## Language rules (anti-slop)

### Repetition
- Vary sentence openings.
- Don’t reuse the same transitions (“Moreover”, “Furthermore”).
- Don’t restate the same idea in different words.

### Openings + endings
- No generic scene-setting (“In today’s fast-paced world…”).
- Start with a concrete claim, problem, or specific moment.
- Don’t end with “In conclusion” or a recap. End when the argument ends.

### Adjectives
Avoid vague/hype adjectives unless they add **concrete information** (scale, constraints, performance).
Replace:
- “robust system” → “handles 10k req/s without dropping events”
- “seamless experience” → “2-click flow with no re-auth”

### Politeness
- Use direct, neutral professional tone.
- Cut stock phrases (“I hope this finds you well…”).
- Remove softeners unless relationship needs them (“just”, “kindly”, “humbly”).

### Word/phrase blacklist (starter pack)
Avoid unless you explicitly want them:
- delve, dive into, embark, realm, tapestry, vibrant, endeavour
- leverage, harness, seamlessly, pivotal, groundbreaking, transformative, paradigm
- ever-evolving landscape, unlock the potential, “real magic happens”
- “not just X, but Y”; “X is more than just Y; it’s Z”; “This is where X comes in”
- dramatic marketing adjectives (amazing, must-read, mind-blowing)

**Tip:** keep your own evolving blacklist. Add any phrase that makes you cringe.

### Fidelity and certainty
- Don’t invent facts.
- If it’s not in sources, omit or mark uncertain.
- Don’t overstate confidence.

### POV consistency
- Pick **one** POV (“I” or “we” or “you”) and stick to it.
- Avoid mixing POV in the same piece.

### Punctuation
- Avoid em dashes (—). Use commas or periods.

---

## Bulletproof prompt template (paste + fill)

> Copy everything below into your prompt.

```text
You are helping me draft high-quality, non-sloppy writing with a human voice.

[1] Task & context
- Format: [LinkedIn post / short article / email / script]
- Topic: [what this is about]
- Why: [why you're writing it]
- Source material (facts to stay faithful to):
[paste notes, outline, quotes, metrics]

[2] Audience & goal
- Audience: [role + familiarity]
- They already know: [skip re-explaining]
- After reading, they should be able to: [1–3 outcomes]

[3] Structure (I own the outline; you fill it)
- Follow this outline ONLY:
1) [...]
2) [...]
3) [...]
- Do NOT add an intro or conclusion beyond what’s in the outline.
- Write primarily in complete sentences and well-structured paragraphs.
- Use bullets only for truly distinct items (steps, discrete lists).
- Use subheadings sparingly; do not add a heading for every paragraph.
- No meta lines or signposting (“in this section…”, “now that we’ve…”).
- Vary paragraph length; do not end each section with a mini-summary.

[4] Voice & tone
- Clear, neutral professional tone; slightly playful/witty only when it helps.
- No hype, no marketing language, no theatrics.
- Be direct. No filler. No Q→A hook device.
- Use ONE consistent point of view: [I/we/you].

[Optional voice match]
- Match rhythm and tone of this sample:
[paste 1–2 paragraphs you wrote]

[5] Anti-slop language constraints
- Avoid these words/phrases:
delve, embark, realm, tapestry, vibrant, endeavour,
leverage, harness, seamlessly, pivotal, groundbreaking, transformative,
ever-evolving landscape, unlock the potential,
“not just X, but Y”, “X is more than just Y; it’s Z”, “This is where X comes in”.
- Avoid vague adjectives unless they add concrete info.
- Analogies: max one, only if non-obvious and clarifying.
- No em dash (—).

[6] Accuracy
- Stay faithful to sources. Don’t add certainty beyond what’s provided.
- If unsure, omit or label as uncertain.

[7] Output requirements
- Provide the final draft only.
- Before you output, silently self-check for: banned words, repetition, generic intro/outro, signposting.
```

---

## Revision loop (writer → judge → rewrite)

### Step 0: Draft (Writer)
- Use the template above to get **Version 0**.

### Step 1: Diagnose (Judge — do not rewrite)
Paste into a second chat/model:

```text
You are reviewing a draft for AI slop and style issues, not rewriting it.

Rules:
[paste the structure + anti-slop constraints]

Draft:
[paste the draft]

1) Identify rule breaks:
- repetitive openings/transitions
- generic intro/outro
- vague adjectives or hype
- meta/signposting
- banned words/phrases
- generic examples that add no information

2) For each issue, suggest a fix in ONE short sentence.
Do not rewrite the whole piece.
```

### Step 2: Targeted rewrite (Writer)
```text
Here is the draft and the judge’s notes.
Rewrite the draft fixing ONLY these issues:
- remove generic intro/outro
- vary repetitive openings
- replace vague adjectives with concrete detail (or delete)
- remove meta/signposting
- remove banned words/phrases
Keep the structure and main arguments the same.
Output final draft only.
```

### Step 3: Human pass (5 minutes)
- Read the **one-line summaries** of each paragraph. Does the flow match how you’d say it?
- Add **one** personal detail: a number, a mistake you made, a tradeoff, a quick story.
- Cut any sentence that doesn’t add new information.

---

## LinkedIn-specific “human” texture (optional add-ons)
Use one or two (not all):
- A specific number (time saved, latency, cost, adoption)
- A concrete moment (“We hit X failure mode in prod…”)
- A tradeoff (“We chose A over B because…”)
- A punchy closing line that’s specific, not a vague future statement

---

## Quick checklist before posting
- [ ] First paragraph is specific (not generic scene-setting)
- [ ] No meta/signposting lines
- [ ] Minimal bullets; paragraphs do the work
- [ ] No banned words/phrases; no em dashes
- [ ] Concrete examples > generic claims
- [ ] Ending is specific and stops naturally (no recap)
