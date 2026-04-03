# CONCEPTS: What You Need to Know

## Multi-Agent (Simple Definition)
Multiple specialized behaviors. Here: classifier + handler for feedback + handler for queries + handler for tickets. One system, many roles.

## Router
A function that decides where to send the input. Classify first, then call the right handler.

## Sentiment
Positive vs. negative. We use GPT to classify. Could also use a sentiment model (more advanced).

## Ticket System
When something goes wrong, we create a record (ticket). User gets an ID. They can check status later. Simple dict for demo; real system uses a database.
