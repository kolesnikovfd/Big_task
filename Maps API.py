import os
import sys

import requests
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)
        self.getImage()


    def updateParams(self):
        """ Обновляем параметры отображаемой карты """
        self.params = {
            "ll": ",".join([self.long_input.text(), self.width_input.text()]),
            "z": self.scale_input.text(),
            "l": "map"
        }


    def getImage(self):
        api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(api_server, params=self.params)

        if not response:
            # Обработка ошибок
            pass

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

        # Выводим изображение в надпись self.map
        self.pixmap = QPixmap(self.map_file)
        self.map.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
