class Agent:
    def __init__(self, name, llm, system_prompt, memory=None):
        self.name = name
        self.llm = llm
        self.system_prompt = system_prompt
        self.memory = memory if memory is not None else {}

    def chat(self, user_message, session_id):
        # Initialize memory for session if not exists
        if session_id not in self.memory:
            self.memory[session_id] = []

        # Add user message
        self.memory[session_id].append({"role": "user", "content": user_message})

        # Build full messages
        messages = [{"role": "system", "content": self.system_prompt}] + self.memory[session_id]

        # Call llama.cpp
        response = self.llm.create_chat_completion(messages=messages)
        assistant_reply = response["choices"][0]["message"]["content"]

        # Add assistant reply to memory
        self.memory[session_id].append({"role": "assistant", "content": assistant_reply})

        return assistant_reply
