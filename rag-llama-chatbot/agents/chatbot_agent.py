from .agent import Agent
from load_model import llm

system_prompt = open("prompts/system.txt").read()

chatbot = Agent(
    name="rag_chatbot",
    llm=llm,
    system_prompt=system_prompt,
    memory={}  # session-based memory
)
