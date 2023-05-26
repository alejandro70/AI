import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from chatgpt_conversation import ChatGPTConversation
from dotenv import load_dotenv, find_dotenv

class ChatWindow(QMainWindow):
    def __init__(self, api_key):
        super().__init__()
        self.setWindowTitle("ChatGPT")
        self.resize(600, 800)  # Ajusta el tamaño de la ventana

        self.api_key = api_key
        self.conversation_manager = ChatGPTConversation(api_key=self.api_key)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.layout.addWidget(self.text_area)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Escribe tu mensaje...")
        self.input_box.returnPressed.connect(self.process_user_input)
        self.layout.addWidget(self.input_box)

        self.send_button = QPushButton("Enviar")
        self.send_button.clicked.connect(self.process_user_input)
        self.layout.addWidget(self.send_button)

        self.central_widget.setLayout(self.layout)

        self.set_font_size(12)  # Ajusta el tamaño de la fuente

    def set_font_size(self, size):
        font = QFont()
        font.setPointSize(size)
        self.text_area.setFont(font)
        self.input_box.setFont(font)

    def process_user_input(self):
        user_message = self.input_box.text()
        if user_message:
            self.display_user_message(user_message)
            assistant_response = self.conversation_manager.generate_response(user_message)
            self.display_assistant_message(assistant_response)
            self.input_box.clear()

    def display_user_message(self, message):
        self.text_area.append("Usuario: " + message)

    def display_assistant_message(self, message):
        self.text_area.append("Asistente: " + message)

def main():
    _ = load_dotenv(find_dotenv())
    api_key = os.getenv('OPENAI_API_KEY')  # Reemplaza con tu propia clave de API proporcionada por OpenAI

    app = QApplication(sys.argv)
    chat_window = ChatWindow(api_key)
    chat_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
