# EXPLAIN: Agentic Healthcare Assistant

## What This Does

A chatbot that can do four things (tools):
1. Book appointment
2. Add patient record
3. Get patient history
4. Search medical info

The LLM decides which tool to use based on what you ask. You say "Book an appointment for John with Dr. Smith on Friday" → it calls book_appointment. You say "What is diabetes?" → it calls search_medical_info. That's the "agentic" part: the AI chooses the right tool.

---

## Key Parts

### @tool
Decorator that turns a function into a LangChain tool. The LLM sees the function name and docstring. When it wants to use it, it calls the function with the right arguments.

### Tools
Each tool does one thing. book_appointment, add_patient_record, get_patient_history, search_medical_info. Simple functions with clear inputs.

### Agent
The agent = LLM + tools + prompt. The prompt says "use these tools." The LLM reads your message, picks a tool, calls it, gets the result, and responds to you.

### AgentExecutor
Runs the agent. Handles the loop: LLM thinks → calls tool → gets result → LLM responds. Can call multiple tools if needed.

---

## Medical Info

We use a simple dictionary for demo. In real use you'd connect to Medline, WHO, or another API. Same pattern: tool calls an external source and returns text.
