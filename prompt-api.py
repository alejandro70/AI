import sys
import openai
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt

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

    def send_request(self):
        text = self.text_edit.toPlainText()
        if text:
            response = self.make_request(text)
            if response is not None:
                self.save_to_file(response)

    def make_request(self, text):
        # Configura tu clave de API de OpenAI
        api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = api_key
        engine = "davinci-codex"

        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=text,
                max_tokens=100
            )
            return response.choices[0].text
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error de conexión: {str(e)}")
        return None

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
