# TEACH: Script for Teaching This Project

## Opening

"This is an 'agentic' assistant. It doesn't just chat—it has tools. It can book appointments, add records, search info. The AI decides which tool to use based on what you say."

## Key Idea: Tools

"Each tool is a Python function with @tool. The LLM reads your message. If you say 'book an appointment', it calls book_appointment. The function runs, returns a result, the LLM turns that into a reply. The AI is the coordinator. The tools do the work."

## Demo

1. "Book an appointment for Alice with a cardiologist on March 25" → book_appointment runs
2. "What is diabetes?" → search_medical_info runs
3. "Add a record for Alice: visited for checkup" → add_patient_record runs
4. "What's Alice's history?" → get_patient_history runs

## Closing

"Agentic = AI + tools. The AI chooses. You give it capabilities, it figures out when to use them."
