import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('ui.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = UI()
    ex.show()

    sys.exit(app.exec())
