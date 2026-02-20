# Synthesis Prompt Template

The bot uses this prompt structure when synthesizing Slack messages via Gemini.

## Default Prompt

```
You are a PM assistant. Analyze this Slack message from #{channel_name} by {author} and extract:

1. A one-line backlog item (actionable, concise, starts with a verb)
2. Category: one of [product-idea, interview-knowledge, ai-insight, competitive-intel, framework, other]
3. Why it matters for a PM targeting a Google AI role (one sentence)

Message:
{text}

Respond in JSON only:
{"backlog_item": "...", "category": "...", "relevance": "..."}
```

## Categories Explained

| Category | What It Captures | Example |
|----------|-----------------|---------|
| `product-idea` | New mini-product or feature to build | "Build a tool that evaluates AI features against Google's principles" |
| `interview-knowledge` | Frameworks, case studies, or insights useful for Google PM interviews | "Shreyas Doshi's framework for prioritizing under ambiguity" |
| `ai-insight` | Technical AI learnings relevant to PM work | "RAG reranking improves factuality by 40% in domain-specific queries" |
| `competitive-intel` | Product moves by Google, competitors, or the broader AI ecosystem | "Google just launched Agentspace for enterprise multi-agent workflows" |
| `framework` | Mental models, product sense patterns, decision-making tools | "The 'reversible vs irreversible decisions' framework for AI feature launches" |
| `other` | Anything that doesn't fit above but is worth capturing | General notes, links, references |

## Customizing the Prompt

To change the synthesis behavior, edit the `synthesize_with_ai()` function in `scripts/slack_bot.py`. The prompt can be adjusted to:

- Add or remove categories
- Change the target role (e.g., from Google PM to a different company)
- Add additional extraction fields (e.g., urgency, related goal)
- Reference Knowledge/ files for better context matching
