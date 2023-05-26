import openai
import os

class ChatGPTConversation:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        self.conversation_history = []

    def append_user_message(self, message):
        self.conversation_history.append({"role": "user", "content": message})

    def append_assistant_message(self, message):
        self.conversation_history.append({"role": "assistant", "content": message})

    def get_last_assistant_response(self):
        for message in reversed(self.conversation_history):
            if message["role"] == "assistant":
                return message["content"]
        return None

    def generate_response(self, user_message):
        self.append_user_message(user_message)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.conversation_history
        )
        assistant_response = response.choices[0].message.content.strip()
        self.append_assistant_message(assistant_response)
        return assistant_response

# Instancia la clase ChatGPTConversation
apiKey = os.getenv('OPENAI_API_KEY')
conversation_manager = ChatGPTConversation(api_key=apiKey)

# Genera una respuesta inicial del asistente
initial_message = "Hola, ¿en qué puedo ayudarte?"
assistant_response = conversation_manager.generate_response(initial_message)
print(f"Asistente: {assistant_response}")

# Inicia un bucle de conversación
while True:
    user_input = input("Usuario: ")
    assistant_response = conversation_manager.generate_response(user_input)
    print(f"Asistente: {assistant_response}")

    # Termina el bucle si se proporciona un mensaje de finalización
    if user_input.lower() == "adiós":
        break
