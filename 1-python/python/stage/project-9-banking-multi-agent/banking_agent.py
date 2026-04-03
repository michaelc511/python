"""
Banking Customer Support AI Agent using Multi-Agent Architecture
Classifies messages (feedback vs query), responds by sentiment, tracks tickets.
Uses simple multi-handler pattern (student-level multi-agent).
"""

import os
from openai import OpenAI
import gradio as gr

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Fake ticket database
tickets_db = {}
ticket_counter = 0


def classify_message(message: str) -> str:
    """Classify: 'feedback_positive', 'feedback_negative', or 'query'."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Classify this customer message as exactly one of: feedback_positive, feedback_negative, query. Message: {message}"}],
        temperature=0,
    )
    text = response.choices[0].message.content.strip().lower()
    if "positive" in text:
        return "feedback_positive"
    if "negative" in text:
        return "feedback_negative"
    return "query"


def handle_feedback_positive(message: str) -> str:
    """Respond to positive feedback."""
    return "Thank you so much for your kind words! We're glad we could help. Is there anything else we can assist you with?"


def handle_feedback_negative(message: str) -> str:
    """Respond to negative feedback and create ticket."""
    global ticket_counter
    ticket_counter += 1
    ticket_id = f"TKT-{ticket_counter}"
    tickets_db[ticket_id] = {"message": message, "status": "open"}
    return f"We're sorry to hear that. We've created ticket {ticket_id} for our team to follow up. Our team will reach out within 24 hours."


def handle_query(message: str) -> str:
    """Respond to general query using GPT."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful banking customer support agent. Answer questions about accounts, fees, loans, or services. Be concise and friendly."},
                  {"role": "user", "content": message}],
    )
    return response.choices[0].message.content


def get_ticket_status(ticket_id: str) -> str:
    """Get status of a ticket."""
    if ticket_id in tickets_db:
        return f"Ticket {ticket_id}: {tickets_db[ticket_id]['status']}"
    return f"Ticket {ticket_id} not found."


def route_and_respond(message: str) -> str:
    """Main router: classify, then send to the right handler."""
    if message.lower().startswith("status ") or "ticket" in message.lower():
        parts = message.split()
        for p in parts:
            if p.startswith("TKT-"):
                return get_ticket_status(p)
        return "Please provide a ticket ID like TKT-1"

    classification = classify_message(message)
    if classification == "feedback_positive":
        return handle_feedback_positive(message)
    if classification == "feedback_negative":
        return handle_feedback_negative(message)
    return handle_query(message)


def chat_fn(message, history):
    return route_and_respond(message)


demo = gr.ChatInterface(
    fn=chat_fn,
    title="Banking Customer Support Agent",
    description="Leave feedback, ask questions, or check ticket status (e.g., 'status TKT-1').",
)

if __name__ == "__main__":
    demo.launch()
