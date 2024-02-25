#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import pyautogui
import keyboard
from PyQt5 import QtWidgets, QtCore, QtGui


# import pygetwindow as gw
# window = gw.getWindowsWithTitle()
# print(window)
# window.moveTo(100, 100) 
# window.resizeTo(500,400)
# sys.exit()


pyautogui.FAILSAFE = False


screen_width, screen_height = pyautogui.size()
# 6マスのグリッドのサイズを定義（3x2グリッド）
grid_width = screen_width // 3
grid_height = screen_height // 2

# マス目の座標を定義
grid_positions = {
  "A": (0, 0),
  "B": (grid_width, 0),
  "C": (2 * grid_width, 0),
  "D": (0, grid_height),
  "E": (grid_width, grid_height),
  "F": (2 * grid_width, grid_height),
}

def move_window(key1, key2):
  x1, y1 = grid_positions[key1]
  x2, y2 = grid_positions[key2]
  
  width = abs(x2 - x1) + grid_width
  height = abs(y2 - y1) + grid_height

  print("------------------------")
  print(pyautogui.size())
  print("------------------------")

  pyautogui.moveTo(x1 + width // 2, y1 + height // 2)
  pyautogui.dragTo(x1, y1, button='left')
  pyautogui.moveTo(x1, y1)
  pyautogui.dragRel(width, height, button='left')

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

def main():
  app = QtWidgets.QApplication(sys.argv)
  ex = BlockWindow()
  sys.exit(app.exec_())
  print("hogehoge")

def test():
  move_window("A","B")

if __name__ == "__main__":
  main()
  # test()



