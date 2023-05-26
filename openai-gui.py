import json
import sys
import requests
import os
import openai
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from dotenv import load_dotenv, find_dotenv


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación OpenAI")
        self.setGeometry(100, 100, 400, 300)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 10, 380, 200)

        self.btn_send = QPushButton("Enviar", self)
        self.btn_send.setGeometry(150, 230, 100, 30)
        self.btn_send.clicked.connect(self.send_request)

        _ = load_dotenv(find_dotenv())
        openai.api_key  = os.getenv('OPENAI_API_KEY')

    def send_request(self):
        text = self.text_edit.toPlainText()
        if text:
            response = self.get_completion(text)
            if response is not None:
                self.save_to_file(response)

    def get_completion(prompt, model="gpt-3.5-turbo"):
        prompt = json.dumps(prompt)
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0, # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    def save_to_file(self, response):
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
        if file_name:
            with open(file_name, "w") as file:
                file.write(response)
            QMessageBox.information(self, "Guardado", "El archivo se guardó correctamente.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
