from PyQt5.QtCore import (QPointF, QRectF, Qt)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem)
import sys


class TicTacToe(QGraphicsItem):
    num_lines = 50  # количество строк
    num_column = 50  # количество столбцов
    param_x = 600 // num_lines
    param_y = 600 // num_column

    def __init__(self):
        super(TicTacToe, self).__init__()
        self.board = [[-1 for j in range(self.num_lines)] for i in range(self.num_column)]
        self.symbol_AI = 0
        self.symbol_Human = 1
        self.turn = self.symbol_AI

    def reset(self):
        for x in range(self.num_lines):
            for y in range(self.num_column):
                self.board[x][y] = -1
        self.turn = self.symbol_AI
        self.update()

    def select(self, x, y):
        if x < 0 or y < 0 or x >= self.num_lines or y >= self.num_column:
            return
        if self.board[x][y] == -1:
            self.board[x][y] = self.turn
            self.turn = 1 - self.turn

    def paint(self, painter, option, widget):  # рисуем при каждом нажатии мыши
        painter.setPen(Qt.black)
        for i in range((600 // self.num_lines), 600, (600 // self.num_column)):
            painter.drawLine(0, i, 600, i)
            painter.drawLine(i, 0, i, 600)

        for y in range(self.num_column):
            for x in range(self.num_lines):
                if self.board[x][y] == self.symbol_AI:
                    painter.setPen(Qt.red)
                    painter.drawEllipse(
                        QPointF(int(self.param_x / 2) + x * self.param_x,
                                int(self.param_y / 2) + y * self.param_y),
                                int(self.param_x / 2) - 2, int(self.param_y / 2) - 2)
                    print(int(self.param_x / 2) + x * self.param_x,
                          int(self.param_y / 2) + y * self.param_y)
                elif self.board[x][y] == self.symbol_Human:
                    painter.setPen(Qt.blue)
                    painter.drawLine(x * self.param_x + 2, y * self.param_y + 2,
                                     int(self.param_x) - 2 + x * self.param_x,
                                     int(self.param_y) - 2 + y * self.param_y)
                    painter.drawLine(int(self.param_x) - 2 + x * self.param_x, y * self.param_y + 2,
                                     x * self.param_x + 2, int(self.param_y) - 2 + y * self.param_y)

    def boundingRect(self):  # функция определяет внешние границы прямоугольника
        return QRectF(0, 0, 600, 600)  # возвращает прямоугольник на плоскости

    def mousePressEvent(self, event):
        pos = event.pos()
        print(pos.x(), pos.y())
        print(int(pos.x() / self.param_x), int(pos.y() / self.param_y))
        self.select(int(pos.x() / self.param_x), int(pos.y() / self.param_y))
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
