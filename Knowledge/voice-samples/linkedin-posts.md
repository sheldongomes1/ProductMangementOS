# LinkedIn Voice Samples

8 published LinkedIn posts used for voice training. See `examples/tutorials/voice-training.md` for the full voice training workflow.

---

## Post 1: Bedtime Story Generator
**Date posted**: 2026-01-29
**Engagement**: 1300 impressions
**Status**: Published, live demo

Try my Bedtime Story Generator if you want to be the best storyteller for your little ones, even when you're tired after a hard day's work :)

Live demo: https://lnkd.in/ehUS9R5C

It creates a custom bedtime story + illustration + voice narration in one click.

Built entirely on Google Cloud:
- Gemini 2.5 Flash → story
- Vertex AI Imagen → illustration
- Google Text-to-Speech → narration
- Deployed on Cloud Run (Python + Streamlit)

Honestly, the "fun demo" part was easy. The real work was getting the details right: prompt quality, state flow, IAM/service accounts, and making it stable enough to share as a live link.

A stat that stuck with me is that in NSCH 2022 data, only 39.1% of US kids ages 0-5 are read to every day, and the AAP encourages shared reading starting at birth. This was my small way of making nightly story time a little easier.

Give me your feedback, I'd love that.

#GoogleCloud #CloudRun #VertexAI #Gemini #Imagen #TextToSpeech #Python #GenAI #LLMOps #ProductEngineering #AI #Google

---

## Post 2: RAG with Google 10K Earnings Data
**Date posted**: 2026-10-31
**Engagement**: 800 impressions
**Status**: Published

I wanted to play with RAG (Retrieval Augmented Generation) using Vertex AI Gemini API. I used Google Cloud as the host platform and imported Google's 10K quarterly earnings data with charts, tables and images. The model is a black box - but the clarity of the answers blew me away. The prompts and context data provided to the model provided simplified results and conclusions. No hallucinations! As advertised :)

I can see how if you integrate 10Ks and earning call data of vendors, competitors and benchmark indices you might be able to unlock very powerful predictive capabilities.

#RAG #Gemini #VertexAI #GoogleCloud #AIProduct #FintechAI #Google

---

## Post 3: Strategic Fit Canvas (BEST PERFORMER — 3000 impressions)
**Date posted**: 2026-08-31
**Engagement**: 3000 impressions
**Status**: Published, live demo

My coach and mentor Sebastien LEDUC and I were discussing how hard it is to evaluate candidates not just for what they can do now, but what they might deliver in 1, 3, or 10 years.

That inspired me to build something:
- A lightweight AI-powered tool that reads a resume and job description — and outputs:
- A radar chart of strategic fit
- A timeline of expected value (1/3/5/10 years)
- A one-word resume summary and a "fit forecast" icon

I built the entire MVP: design, backend, deployment, all using Replit + GPT-4, powered by prompts alone. The experience was 10/10. Refinements were tricky, but execution was fast. Thanks Amjad Masad and Lenny Rachitsky

For fun, I tested myself: The model gave me a 70% match to a theoretical JD for Tomer Cohen's CPO role at Google. Not bad... and no, it didn't just flatter :)

Try it: https://lnkd.in/e3HsUnav
Sample Output: https://lnkd.in/eF3gbeYu

It's just an MVP and a way to keep learning, so take it with a grain of salt.

Would love your thoughts! I'll keep the site up for a week or so.

#ProductManagement #AIProjects #Replit #CareerTools #BuildInPublic #StrategicFitCanvas #GoogleAI #VertexAI #NoCode #PromptEngineering #HiringInnovation

---

## Post 4: AI Fit Score A/B Test Thought Experiment
**Date posted**: 2026-07-15
**Engagement**: Unknown
**Status**: Published

Thought Exercise: Could an AI Fit Score improve job seeker confidence and application rates on LinkedIn?

After listening to Mayur Kamat on Lenny Rachitsky's podcast discuss experimentation driven product rigor, I started thinking about a common job search friction point:

"What if LinkedIn showed an AI-generated Fit Score on job listings?"

As a thought experiment, I simulated an A/B test:

Group A saw job listings with the Fit Score
Group B did not

I wanted to explore:
- Does a Fit Score increase application conversion?
- Does it affect time spent on the listing?
- How confident does it make the candidate feel?

I created dummy data for job posts, resumes, and engagement signals — then ran the analysis in Google Cloud (BigQuery).

Here's what I found:
Conversion Rate: 60% (with Fit Score) vs. 40% (without)
Confidence Score: 5.8 vs. 3.2 (out of 7)
Avg Time on Page: 47s vs. 29s

Even in simulation, the insight was clear: Confidence converts.

This was just a quick weekend experiment but a fun exercise in AI usability, job seeker empathy, and decision-enabling design.

Curious how PMs at Google and LinkedIn would think about this. How would you evolve this feature?

#productmanagement #experimentation #aiux #googlecloud #productdesign #google

---

## Post 5: AI-Powered Google Slides Pipeline
**Date posted**: 2026-06-15
**Engagement**: 600 impressions
**Status**: Published, live demo + public form

What do you think of this AI-generated Google Slides deck?

Improved with Napkin.AI: https://lnkd.in/erdnMXZm

Here is the link to the public Google Form. Feel free to use it and message me! I'll send over your slide deck!
https://lnkd.in/eeHBBq8x

I wanted to build something useful and AI-powered using only Google Cloud.

Use case: Improving engagement on Google Finance by boosting personalization and customization for individual investors.

No third-party tools. No UI. No extra infra.
Just signal in → insight out.

The low-code pipeline:
→ Google Forms (to capture user intent: goal, audience, pain point, desired outcome)
→ Apps Script (JS trigger)
→ Cloud Run (Python backend)
→ Vertex AI (Gemini Flash model)
→ Slides API (auto-generates a 5-slide exec-style deck)

To enhance the visuals, I also ran the output through Napkin.ai — Here is the original Google generated version: https://lnkd.in/eiNZrdAv

This was a great way to explore what's possible when AI, cloud-native tools, and lightweight workflows come together.

#GoogleCloud #VertexAI #Gemini #ProductDesign #SlidesAPI #AIworkflow #LowCode #BuiltOnGoogle #TechnicalProductManager

---

## Post 6: Landbot + Zapier + GPT-4 Chatbot Loop
**Date posted**: 2026-06-01
**Engagement**: 600 impressions
**Status**: Published

Next up - I built a no-code chatbot that connects Landbot + Zapier + GPT-4 into a real-time conversational loop.

User input (Landbot) → Webhook → GPT-4 prompt → AI response → back to chat.

Handles async response flow. Uses bidirectional Webhooks for input/output sync. Designed prompt logic for smart summarization & tone shift.

A lightweight build — but a strong proof of how AI, automation, and UX design can fuse into real utility.

Built for learning. Ready to scale. Happy to share the setup.

#AI #ChatGPT #NoCode #Zapier #Landbot #ProductManagement #PromptDesign #GoogleCloud #Automation

---

## Post 7: GPT-Powered Google Cloud News Digest
**Date posted**: 2026-05-30
**Engagement**: 600 impressions
**Status**: Published

To stay sharp on the latest in cloud innovation, I built a no-code automation that delivers a GPT-powered daily digest of Google Cloud news directly to my inbox.

It's a small project, but it's already made a big difference in keeping me informed about the latest Google cloud topics while demonstrating how AI + automation can drive real productivity.

Built with Zapier + OpenAI + RSS, no code required.

If you're exploring ways to dip your toes into AI or want to stay current without spending hours online, happy to share the setup!

#AI #GoogleCloud #ProductManagement #Zapier #GPT #NoCode #CloudComputing #AIinProduct

---

## Post 8: No-Code Automation (Earlier Version of News Digest)
**Date posted**: 2026-04-15
**Engagement**: 1000 impressions
**Status**: Published (earlier iteration of the same concept as Post 7)

To stay sharp on the latest in cloud innovation, I built a no-code automation that delivers a GPT-powered daily digest of Google Cloud news directly to my inbox.

It's a small project, but it's already made a big difference in keeping me informed about the latest Google cloud topics while demonstrating how AI + automation can drive real productivity.

Built with Zapier + OpenAI + RSS, no code required.

If you're exploring ways to dip your toes into AI or want to stay current without spending hours online, happy to share the setup!

---

## Voice Analysis

### How Sheldon Sounds (extracted from posts above)
- Direct and conversational, like explaining something to a smart friend over coffee. Not patronizing. No LinkedIn slop.
- Data-forward — leads with a specific number, stat, or concrete observation when possible (39.1% stat, 70% match score, 60% vs 40% conversion)
- No hype, no buzzwords — would rather undersell and let the demo speak
- Wants people to walk away feeling like "this guy is genuine and trying hard"

### Patterns From Published Posts
- **Opens with**: The thing he built or a specific observation, not throat-clearing
- **Structure**: Brief context → what he built → tech stack → honest reflection → invitation for feedback
- **Closes with**: Genuine ask for feedback ("Give me your feedback", "Would love your thoughts", "How would you evolve this feature?")
- **Tone**: Humble but confident. Acknowledges limitations ("just an MVP", "take it with a grain of salt") while still showing the work
- **Data usage**: Drops specific numbers naturally (39.1%, 70% match, 60% vs 40%, 5.8 vs 3.2)
- **Tech details**: Lists full stack plainly, no flexing — just "here's what I used"
- **Hashtags**: Heavy Google Cloud tagging, always includes #Google
- **Emoji usage**: Minimal — occasional :) or single emoji, never strings of them
- **Never does**: Corrective reframing, fake suspense, breathless hype, "key insight" language

### Best Performing Post Pattern
Post 3 (Strategic Fit Canvas, 3000 impressions) worked because:
- Built something people can try (live demo link)
- Personal story as hook (conversation with mentor)
- Self-deprecating humor (tested himself, got 70%)
- Named real people (Sebastien, Amjad, Lenny, Tomer Cohen)
- Clear tech stack without over-explaining
- Humble close ("just an MVP", "take it with a grain of salt")
