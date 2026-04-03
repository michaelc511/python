# EXPLAIN: Banking Multi-Agent

## What This Does

One chatbot that routes to different "agents" (handlers) based on what the user said:
1. **Positive feedback** → Thank them
2. **Negative feedback** → Apologize, create a ticket
3. **Query** → Send to GPT for answer
4. **Ticket status** → Look up ticket in our DB

We use a "router" pattern: first classify the message, then call the right handler. Each handler is like a mini-agent—it does one job.

---

## Multi-Agent in Student Terms

We don't use separate LangChain agents. We use:
- **Classifier** – GPT decides: feedback_positive, feedback_negative, or query
- **Handlers** – Each is a function. Positive → canned reply. Negative → create ticket + canned reply. Query → full GPT.
- **Router** – One function that calls the classifier, then calls the right handler.

Simple, clear, gets the job done. "Multi-agent" here means multiple specialized behaviors, not multiple LLM agents talking to each other.

---

## Ticket Tracking

When feedback is negative, we create a ticket (TKT-1, TKT-2, ...) and store it. User can ask "status TKT-1" to check. We parse the message for the ticket ID and look it up.
