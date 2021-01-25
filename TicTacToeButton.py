#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from ctypes import windll

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QGridLayout, QPushButton, QApplication)


class Ex(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(Ex, self).__init__(*args, **kwargs)

        windows_size_x = windll.user32.GetSystemMetrics(0)
        windows_size_y = windll.user32.GetSystemMetrics(1)
        self.layout = QGridLayout(self)
        self.layout.setSpacing(1)
        positions = [(i, j) for i in range(10) for j in range(10)]
        for position in positions:
            self.button = QPushButton()
            self.button.setFixedSize(40, 40)
            self.button.clicked.connect(self.buttonClicked)
            self.layout.addWidget(self.button, *position)
        self.setWindowTitle('TicTacToe')
        self.show()
        w_pos_x = (windows_size_x - self.size().width()) // 2
        w_pos_y = (windows_size_y - self.size().height()) // 2
        self.move(w_pos_x, w_pos_y)
        print(self.size().width(), self.size().height())

    def buttonClicked(self):
        button = self.sender()
        button.setFont(QFont('CeraPro-Bold', 28))
        button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        button.setText("X")
        idx = self.layout.indexOf(button)
        location = self.layout.getItemPosition(idx)
        print(location[:2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ex()
    sys.exit(app.exec_())
