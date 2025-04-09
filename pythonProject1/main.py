import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QVBoxLayout, QPushButton, QWidget, \
    QHBoxLayout, QLineEdit

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Aplicatia mea")

#Widgets:
label = QLabel("Numele tau")
input_name = QLineEdit()
button_1 = QPushButton("Salut")
result_label = QLabel("")

def salutare():
    name = input_name.text()
    result_label.setText(f"Salut, {name}!")

button_1.clicked.connect(salutare)

#Layouts:
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(input_name)
layout.addWidget(button_1)
layout.addWidget(result_label)

window.setLayout(layout)
window.resize(300, 200)
window.show()

app.exec()