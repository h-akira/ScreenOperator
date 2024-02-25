#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys

class SimpleDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        
        self.layout = QtWidgets.QVBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.lineEdit)
        self.button = QtWidgets.QPushButton('Submit', self)
        self.button.clicked.connect(self.on_click)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)
    
    def on_click(self):
        input_text = self.lineEdit.text()
        self.accept()
        print(f'You entered: {input_text}')
        # ここで他の関数を呼び出す
        # your_function(input_text)

app = QtWidgets.QApplication([])

def show_dialog():
    dialog = SimpleDialog()
    dialog.exec_()

show_dialog()
