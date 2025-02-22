import sys
import random

from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)

        self.drawButton.clicked.connect(self.draw_circles)

        # Список для хранения окружностей
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, diameter in self.circles:
            painter.setBrush(QColor("yellow"))
            painter.drawEllipse(x, y, diameter, diameter)

    def draw_circles(self):
        # Генерация случайного положения и диаметра окружности
        x = random.randint(0, self.width() - 50)
        y = random.randint(0, self.height() - 50)
        diameter = random.randint(20, 100)

        self.circles.append((x, y, diameter))
        self.update()  # Обновляем вид, чтобы перерисовать окружности

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
