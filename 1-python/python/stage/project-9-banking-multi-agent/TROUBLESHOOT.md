# TROUBLESHOOT: Common Issues

## Wrong classification
GPT might misclassify. Improve the classify prompt: "Classify as exactly one of: feedback_positive, feedback_negative, query. Reply with only that word."

## Ticket not found
Tickets are in-memory. Restart = lost. For persistence, save to a file or database.

## Query gets feedback response
Check the classifier output. Add a fallback: if unclear, treat as query.
