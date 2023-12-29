Hesap Makinesi Uygulaması


import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QApplication, QWidget


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Pencerenin başlığı ve boyutlarını ayarladık
        self.setWindowTitle('Hesap Makinesi')
        self.setGeometry(100, 100, 400, 500)

        # Sonuç gösterilecek olan okunabilir bir metin kutusu oluşturduk.
        self.result_field = QLineEdit()
        self.result_field.setReadOnly(True)
        self.result_field.setFixedHeight(50)

        font = QFont("Arial", 20, QFont.Weight.Bold)
        self.result_field.setFont(font)

        # Dikey sayfa düzeni oluşturduk
        self.layout = QVBoxLayout()

        # Layout'a sonuç alanını ekledik.
        self.layout.addWidget(self.result_field)

        # 'Clear' butonu oluşturulup layout'a eklendi
        clear_button = QPushButton('Clear')
        clear_button.setFixedSize(100, 50)
        clear_button.clicked.connect(self.clear_result_field)
        self.layout.addWidget(clear_button)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            button_sizer = QHBoxLayout()
            for button in row:
                button = QPushButton(button)
                button.setFixedSize(100, 100)
                button.clicked.connect(self.on_button_click)
                button.setStyleSheet('font-size: 22px')
                button_sizer.addWidget(button)
            self.layout.addLayout(button_sizer)

        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

    def on_button_click(self, s):
        sender = self.sender()
        button_text = sender.text()

        if button_text == '=':
            try:
                expression = self.result_field.text()
                result = eval(expression)
                self.result_field.setText(str(result))
            except Exception as e:
                self.result_field.setText("Hata!")
        else:
            current_text = self.result_field.text()
            new_text = current_text + button_text
            self.result_field.setText(new_text)

    def clear_result_field(self):
        self.result_field.clear()


def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
