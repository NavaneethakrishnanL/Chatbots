from tinkiner import Agent
from memory.session_memory import session_memory

system_prompt = open("prompts/system.txt").read()

chatbot = Agent(
    name="rag_chatbot",
    llm="llama.cpp",
    system_prompt=system_prompt,
    memory=session_memory
)
