"""
Agentic Healthcare Assistant for Medical Task Automation
Books appointments, manages records, retrieves history, searches medical info.
Uses simple tools + LLM (student-level agentic pattern).
"""

import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import gradio as gr

# Fake database for demo - replace with real data in production
appointments_db = []
records_db = {}

Medical_Info = {
    "flu": "Influenza: viral infection. Symptoms: fever, cough, fatigue. Rest, fluids, antivirals if severe.",
    "diabetes": "Diabetes: blood sugar regulation. Type 1: insulin-dependent. Type 2: lifestyle + meds. Monitor glucose.",
    "hypertension": "High blood pressure. Lifestyle: diet, exercise. Meds: ACE inhibitors, etc. Regular monitoring.",
}


@tool
def book_appointment(patient_name: str, doctor: str, date: str) -> str:
    """Book a medical appointment. Give patient name, doctor type, and date."""
    appointments_db.append({"patient": patient_name, "doctor": doctor, "date": date})
    return f"Appointment booked for {patient_name} with {doctor} on {date}."


@tool
def add_patient_record(patient_name: str, record_text: str) -> str:
    """Add or update a patient's medical record. Give patient name and the record text."""
    if patient_name not in records_db:
        records_db[patient_name] = []
    records_db[patient_name].append(record_text)
    return f"Record added for {patient_name}."


@tool
def get_patient_history(patient_name: str) -> str:
    """Retrieve a patient's medical history. Give the patient name."""
    if patient_name not in records_db:
        return f"No records found for {patient_name}."
    return " | ".join(records_db[patient_name])


@tool
def search_medical_info(topic: str) -> str:
    """Search for disease/medical information. Give a topic like 'flu' or 'diabetes'."""
    topic_lower = topic.lower()
    if topic_lower in Medical_Info:
        return Medical_Info[topic_lower]
    return f"No information found for {topic}. Try: flu, diabetes, hypertension."


def create_agent():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    tools = [book_appointment, add_patient_record, get_patient_history, search_medical_info]
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a healthcare assistant. Use the tools to book appointments, manage records, get history, or search medical info. Be helpful and clear."),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)


agent_executor = create_agent()


def chat_fn(message, history):
    result = agent_executor.invoke({"input": message})
    return result["output"]


demo = gr.ChatInterface(
    fn=chat_fn,
    title="Agentic Healthcare Assistant",
    description="Book appointments, add records, get patient history, or search medical info.",
)

if __name__ == "__main__":
    demo.launch()
