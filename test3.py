#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class BlockWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Block Selector')
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)
        
        self.labels = {}
        for i, label in enumerate("ABCDEF"):
            self.labels[label] = QtWidgets.QLabel(label, self)
            self.labels[label].setAlignment(QtCore.Qt.AlignCenter)
            self.labels[label].setFont(QtGui.QFont('Arial', 50))
            self.labels[label].setStyleSheet("border: 2px solid black; background-color: rgba(211, 211, 211, 120)")
            row, col = divmod(i, 3)
            self.grid.addWidget(self.labels[label], row, col)
        
        self.selected_labels = []
        self.showFullScreen()
    
    def keyPressEvent(self, event):
        if event.key() >= QtCore.Qt.Key_A and event.key() <= QtCore.Qt.Key_F:
            label = chr(event.key())
            if label not in self.selected_labels:
                self.selected_labels.append(label)
                self.labels[label].setStyleSheet("border: 2px solid black; background-color: rgba(255, 255, 0, 120)")
            
            if len(self.selected_labels) == 2:
                print(f'Selected Blocks: {self.selected_labels}')
                
                # Reset selection and close the window
                for label in "ABCDEF":
                    self.labels[label].clear()
                self.close()

app = QtWidgets.QApplication(sys.argv)
ex = BlockWindow()
sys.exit(app.exec_())
