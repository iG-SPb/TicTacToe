from PyQt5.QtCore import (QPointF, QRectF, Qt)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem)
import sys


class TicTacToe(QGraphicsItem):


    def __init__(self):
        super(TicTacToe, self).__init__()
        self.board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.symbol_AI = 0
        self.symbol_Human = 1
        self.turn = self.symbol_AI

    def reset(self):
        for y in range(3):
            for x in range(3):
                self.board[y][x] = -1
        self.turn = self.symbol_AI
        self.update()

    def select(self, x, y):
        if x < 0 or y < 0 or x >= 3 or y >= 3:
            return
        if self.board[y][x] == -1:
            self.board[y][x] = self.turn
            self.turn = 1 - self.turn

    def paint(self, painter, option, widget):  # рисуем игровое поле
        painter.setPen(Qt.black)
        for i in range((600//15), 600, (600//15)):
            painter.drawLine(0, i, 600, i)
            painter.drawLine(i, 0, i, 600)

        for y in range(3):
            for x in range(3):
                if self.board[y][x] == self.symbol_AI:
                    painter.setPen(Qt.red)
                    painter.drawEllipse(
                        QPointF(50 + x * 100, 50 + y * 100), 30, 30)
                elif self.board[y][x] == self.symbol_Human:
                    painter.setPen(Qt.blue)
                    painter.drawLine(20 + x * 100, 20 + y * 100,
                                     80 + x * 100, 80 + y * 100)
                    painter.drawLine(20 + x * 100, 80 + y * 100,
                                     80 + x * 100, 20 + y * 100)

    def boundingRect(self):
        return QRectF(0, 0, 600, 600)

    def mousePressEvent(self, event):
        pos = event.pos()
        self.select(int(pos.x() / 200), int(pos.y() / 200))
        self.update()
        super(TicTacToe, self).mousePressEvent(event)


class MainWindow(QGraphicsView):
    def __init__(self):
        super(MainWindow, self).__init__()
        scene = QGraphicsScene(self)
        self.tic_tac_toe = TicTacToe()
        scene.addItem(self.tic_tac_toe)
        scene.setSceneRect(0, 0, 600, 600)
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setWindowTitle("Tic Tac Toe")

    def keyPressEvent(self, event):
        key = event.key()  # ожидание нажатия клавиши на клавиатуре
        if key == Qt.Key_R:  # нажата клавиша R
            self.tic_tac_toe.reset()  # сброс ходов
        super(MainWindow, self).keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
