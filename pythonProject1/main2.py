import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QVBoxLayout, QPushButton, QWidget, \
    QHBoxLayout, QLineEdit

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Aplicatia mea")

#Widgets:
name_label = QLabel("Nume:")
input_name = QLineEdit()
email_label = QLabel("Email:")
input_email = QLineEdit()
button_1 = QPushButton("Salut")
result_label = QLabel("")

def salutare():
    name = input_name.text()
    result_label.setText(f"Salut, {name}!")

button_1.clicked.connect(salutare)

#Layouts:
layout = QGridLayout()
layout.setContentsMargins(20, 0, 20, 0)

layout.addWidget(name_label, 0, 0)
layout.addWidget(input_name, 0, 1)
layout.addWidget(email_label, 1, 0)
layout.addWidget(input_email, 1, 1)
layout.addWidget(button_1, 2, 0)
layout.addWidget(result_label, 2, 1)

layout.setRowStretch(0, 1)
layout.setRowStretch(1, 1)
layout.setRowStretch(2, 1)

layout.setColumnStretch(0, 1)
layout.setColumnStretch(1, 1)

window.setLayout(layout)
window.resize(400, 300)
window.show()

app.exec()