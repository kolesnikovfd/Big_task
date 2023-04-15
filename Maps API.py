import sys
import requests
from requests.models import Response
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QButtonGroup


class ResponsiveVar:
    def __init__(self, type_, var, widgetSetFunction):
        self.type = type_
        self.func = widgetSetFunction
        try:
            self._var = self.type(var)
        except:
            self._var = var

    def _set_var(self, x):
        try:
            self._var = self.type(x)
        except:
            self._var = x

    def set(self, x):
        self._set_var(x)
        self.func(str(self._var))

    def _set(self, x):
        self._set_var(x)

    def get(self):
        return self._var


def clamp(min_, x, max_):
    return min(max_, max(x, min_))


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uiNew.ui', self)

        # Подсказки классов
        self.xInput: QLineEdit
        self.yInput: QLineEdit
        self.searchInput: QLineEdit
        self.addressInput: QLineEdit
        self.searchBtn: QPushButton
        self.searchClearBtn: QPushButton
        self.scaleInput: QLineEdit
        self.scaleUp: QPushButton
        self.scaleDown: QPushButton
        self.mapStyleMap: QPushButton
        self.mapStyleSat: QPushButton
        self.mapStyleMix: QPushButton
        self.mapStyleGroup: QButtonGroup
        self.map: QLabel
        self.errorLabel: QLabel

        self.connectLineEdits()

        # Параметры
        self.pt = None
        self.z = ResponsiveVar(
            int, self.scaleInput.text(), self.scaleInput.setText)
        self.xCord = ResponsiveVar(
            float, self.xInput.text(), self.xInput.setText)
        self.yCord = ResponsiveVar(
            float, self.yInput.text(), self.yInput.setText)
        self.updateDelay = 1000  # в мсек

        self.updateTimer = QTimer(self)
        self.updateTimer.setSingleShot(True)
        self.updateTimer.timeout.connect(self.updateImage)
        self.updateImage()
        self.hide_error()

        # Подключение
        self.xInput.textEdited.connect(self.xCord._set)
        self.yInput.textEdited.connect(self.yCord._set)
        self.scaleInput.textEdited.connect(self.z._set)
        self.scaleUpBtn.pressed.connect(
            lambda: (self.scaleUp(), self.updateImage()), Qt.QueuedConnection)
        self.scaleDownBtn.pressed.connect(
            lambda: (self.scaleDown(), self.updateImage()), Qt.QueuedConnection)
        self.mapStyleGroup.buttonToggled.connect(
            self.updateImage, Qt.QueuedConnection)
        self.searchClearBtn.pressed.connect(
            lambda: (self.clear_point(), self.clear_search()))
        self.searchBtn.pressed.connect(self.search)
        self.searchInput.returnPressed.connect(self.search)

    def get_params(self):
        """ Обновляем параметры отображаемой карты """
        width = min(self.map.width(), 650)
        height = min(self.map.height(), 450)
        mapStyle = self.mapStyleGroup.checkedButton()

        res = {
            "ll": f"{self.xCord.get()},{self.yCord.get()}",
            "z": self.z.get(),
            "size": f"{width},{height}"
        }

        if mapStyle is self.mapStyleMap:
            res["l"] = 'map'
        elif mapStyle is self.mapStyleSat:
            res["l"] = 'sat'
        elif mapStyle is self.mapStyleMix:
            res["l"] = 'sat,skl'
        if self.pt:
            res["pt"] = self.pt

        return res

    def validate_params(self):
        validType = all((
            isinstance(self.z.get(), int),
            isinstance(self.xCord.get(), float),
            isinstance(self.yCord.get(), float),
        ))
        if not validType:
            self.show_error()
            return

        valid = all((
            0 <= self.z.get() <= 17,
            -180 <= self.xCord.get() <= 180,
            -90 <= self.yCord.get() <= 90
        ))

        if not valid:
            self.show_error()
            return False

        self.hide_error()
        return True

    def show_error(self):
        self.errorLabel.setVisible(True)

    def hide_error(self):
        self.errorLabel.setVisible(False)

    def clear_point(self):
        self.pt = None

    def clear_search(self):
        self.searchInput.setText('')
        self.addressInput.setText('')
        self.updateImage()

    def place_point(self):
        self.pt = f'{self.xCord.get()},{self.yCord.get()},org'

    def search(self):
        promt = self.searchInput.text()
        params = {
            "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
            "text": promt,
            "ll": f"{self.xCord.get()},{self.yCord.get()}",
            "lang": "ru_RU",
            "results": 1
        }
        response = requests.get(
            'https://search-maps.yandex.ru/v1/', params=params)
        f = response.json()['features'][0]
        # with open('a.json', 'w', encoding='utf-8') as file:
        #     json.dump(response.json(), file, ensure_ascii=False)
        point = f['geometry']['coordinates']
        if 'GeocoderMetaData' in f['properties']:
            text = f['properties']['GeocoderMetaData']['text']
        elif 'CompanyMetaData' in f['properties']:
            text = f['properties']['CompanyMetaData']['address']
        self.xCord.set(point[0])
        self.yCord.set(point[1])
        self.addressInput.setText(text)
        self.place_point()
        self.updateImage()

    def connectLineEdits(self):
        self.xInput.textEdited.connect(
            self.validate_params, Qt.QueuedConnection)
        self.yInput.textEdited.connect(
            self.validate_params, Qt.QueuedConnection)
        self.scaleInput.textEdited.connect(
            self.validate_params, Qt.QueuedConnection)
        self.xInput.textEdited.connect(
            lambda: self.updateTimer.start(self.updateDelay), Qt.QueuedConnection)
        self.yInput.textEdited.connect(
            lambda: self.updateTimer.start(self.updateDelay), Qt.QueuedConnection)
        self.scaleInput.textEdited.connect(
            lambda: self.updateTimer.start(self.updateDelay), Qt.QueuedConnection)

    def updateImage(self):
        if not self.validate_params():
            return

        response: Response = requests.get(
            "http://static-maps.yandex.ru/1.x/", params=self.get_params())

        if not response:
            self.errorLabel.setText('Некорректные параметры')
            return

        # Выводим изображение в надпись self.map
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(response.content)
        self.map.setPixmap(self.pixmap)

    def clearThread(self):
        self.thread = None
        self.worker = None

    def scaleUp(self):
        self.z.set(clamp(0, self.z.get() + 1, 17))

    def scaleDown(self):
        self.z.set(clamp(0, self.z.get() - 1, 17))

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        update = False
        if event.key() == Qt.Key.Key_PageUp:
            self.scaleUp()
            update = True
        if event.key() == Qt.Key.Key_PageDown:
            self.scaleDown()
            update = True
        if event.key() == Qt.Key.Key_Right:
            value = self.xCord.get() + 360 / 2 ** self.z.get()
            if value > 180:
                value = value - 360
            value = round(value, 6)
            self.xCord.set(value)
            update = True
        if event.key() == Qt.Key.Key_Left:
            value = self.xCord.get() - 360 / 2 ** self.z.get()
            if value < -180:
                value = value + 360
            value = round(value, 6)
            self.xCord.set(value)
            update = True
        if event.key() == Qt.Key.Key_Up:
            value = self.yCord.get() + 180 / 2 ** self.z.get()
            if value > 90:
                value = value - 90
            value = round(value, 6)
            self.yCord.set(value)
            update = True
        if event.key() == Qt.Key.Key_Down:
            value = self.yCord.get() - 180 / 2 ** self.z.get()
            if value < -90:
                value = value + 180
            value = round(value, 6)
            self.yCord.set(value)
            update = True
        if update:
            self.updateImage()
        return super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
