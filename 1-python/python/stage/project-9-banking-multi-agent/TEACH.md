# TEACH: Script for Teaching This Project

## Opening

"This is a 'multi-agent' system for banking support. One chat window, but behind the scenes we have different handlers: one for positive feedback, one for negative (creates a ticket), one for questions. We route based on what the user said."

## Key Idea: Router Pattern

"Step 1: Classify. We use GPT to say 'is this positive feedback, negative feedback, or a question?' Step 2: Route. Based on that, we call the right function. Step 3: Respond. Each handler returns the right reply."

## Demo

1. "Your service is amazing!" → Positive handler → Thank you
2. "I'm very unhappy with the fees" → Negative handler → Ticket created, apology
3. "What are your overdraft fees?" → Query handler → GPT answer
4. "status TKT-1" → Ticket lookup

## Closing

"Multi-agent doesn't have to mean complex. It can mean: one classifier + several handlers. Same idea as NewsGenie—route to the right place."
