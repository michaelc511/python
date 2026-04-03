# CONCEPTS: What You Need to Know

## Agent
An LLM that can use tools. It doesn't just generate text—it can call functions (book, search, etc.) and use the results.

## Tool
A function the agent can call. Has a name and docstring so the LLM knows when to use it. @tool makes a function a tool.

## Tool Calling
The LLM outputs "call book_appointment with these args." The framework runs the function and feeds the result back. The LLM then continues.

## Agentic
Means the system takes action—it doesn't just answer, it does things (books, updates, searches) through tools.
