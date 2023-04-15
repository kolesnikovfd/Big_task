# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Python Projects\Big_task\uiNew.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 450)
        MainWindow.setMinimumSize(QtCore.QSize(650, 450))
        MainWindow.setMaximumSize(QtCore.QSize(650, 450))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setStyleSheet("QLineEdit {\n"
"background-color: white;\n"
"border: 1px solid #aaaaaa;\n"
"border-radius: 10px\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: #efefef;\n"
"}\n"
"QPushButton {\n"
"border: 1px solid #aaaaaa;\n"
"border-radius: 10px;\n"
"background-color: white;\n"
"}\n"
" QPushButton:pressed {\n"
"background-color: #eeeeee;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.map = QtWidgets.QLabel(self.centralwidget)
        self.map.setEnabled(True)
        self.map.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.map.setMinimumSize(QtCore.QSize(650, 450))
        self.map.setMaximumSize(QtCore.QSize(650, 450))
        self.map.setText("")
        self.map.setPixmap(QtGui.QPixmap("Z:/Картинки/Скриншоты/Screenshots/2023-04/Firework 15.24.png"))
        self.map.setScaledContents(True)
        self.map.setAlignment(QtCore.Qt.AlignCenter)
        self.map.setWordWrap(False)
        self.map.setObjectName("map")
        self.CordsFrame = QtWidgets.QFrame(self.centralwidget)
        self.CordsFrame.setGeometry(QtCore.QRect(0, 29, 650, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CordsFrame.sizePolicy().hasHeightForWidth())
        self.CordsFrame.setSizePolicy(sizePolicy)
        self.CordsFrame.setStyleSheet("")
        self.CordsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CordsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CordsFrame.setObjectName("CordsFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.CordsFrame)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.xInput = QtWidgets.QLineEdit(self.CordsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xInput.sizePolicy().hasHeightForWidth())
        self.xInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.xInput.setFont(font)
        self.xInput.setAlignment(QtCore.Qt.AlignCenter)
        self.xInput.setObjectName("xInput")
        self.horizontalLayout.addWidget(self.xInput)
        self.yInput = QtWidgets.QLineEdit(self.CordsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yInput.sizePolicy().hasHeightForWidth())
        self.yInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yInput.setFont(font)
        self.yInput.setStyleSheet("")
        self.yInput.setAlignment(QtCore.Qt.AlignCenter)
        self.yInput.setObjectName("yInput")
        self.horizontalLayout.addWidget(self.yInput)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 3)
        self.scaleFrame = QtWidgets.QFrame(self.centralwidget)
        self.scaleFrame.setGeometry(QtCore.QRect(612, 0, 38, 450))
        self.scaleFrame.setStyleSheet("")
        self.scaleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scaleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scaleFrame.setObjectName("scaleFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scaleFrame)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.scaleUpBtn = QtWidgets.QPushButton(self.scaleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleUpBtn.sizePolicy().hasHeightForWidth())
        self.scaleUpBtn.setSizePolicy(sizePolicy)
        self.scaleUpBtn.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.scaleUpBtn.setFont(font)
        self.scaleUpBtn.setObjectName("scaleUpBtn")
        self.verticalLayout.addWidget(self.scaleUpBtn)
        self.scaleInput = QtWidgets.QLineEdit(self.scaleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleInput.sizePolicy().hasHeightForWidth())
        self.scaleInput.setSizePolicy(sizePolicy)
        self.scaleInput.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scaleInput.setFont(font)
        self.scaleInput.setAlignment(QtCore.Qt.AlignCenter)
        self.scaleInput.setObjectName("scaleInput")
        self.verticalLayout.addWidget(self.scaleInput)
        self.scaleDownBtn = QtWidgets.QPushButton(self.scaleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleDownBtn.sizePolicy().hasHeightForWidth())
        self.scaleDownBtn.setSizePolicy(sizePolicy)
        self.scaleDownBtn.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.scaleDownBtn.setFont(font)
        self.scaleDownBtn.setObjectName("scaleDownBtn")
        self.verticalLayout.addWidget(self.scaleDownBtn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.errorFrame = QtWidgets.QFrame(self.centralwidget)
        self.errorFrame.setGeometry(QtCore.QRect(0, 375, 650, 38))
        self.errorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.errorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.errorFrame.setObjectName("errorFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.errorFrame)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(185, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.errorLabel = QtWidgets.QLabel(self.errorFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorLabel.sizePolicy().hasHeightForWidth())
        self.errorLabel.setSizePolicy(sizePolicy)
        self.errorLabel.setMinimumSize(QtCore.QSize(256, 0))
        self.errorLabel.setStyleSheet("color: red;\n"
"background-color: white;\n"
"border: 1px solid #aaaaaa;\n"
"border-radius: 10px")
        self.errorLabel.setScaledContents(True)
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.horizontalLayout_2.addWidget(self.errorLabel)
        spacerItem5 = QtWidgets.QSpacerItem(185, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.mapStyleFrame = QtWidgets.QFrame(self.centralwidget)
        self.mapStyleFrame.setGeometry(QtCore.QRect(0, 408, 650, 42))
        self.mapStyleFrame.setStyleSheet("QPushButton {\n"
"background-color: #dddddd;\n"
"border: 1px solid #aaaaaa;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: white;\n"
"}")
        self.mapStyleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mapStyleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mapStyleFrame.setObjectName("mapStyleFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.mapStyleFrame)
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(157, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.mapStyleMap = QtWidgets.QPushButton(self.mapStyleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapStyleMap.sizePolicy().hasHeightForWidth())
        self.mapStyleMap.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mapStyleMap.setFont(font)
        self.mapStyleMap.setStyleSheet("border-top-right-radius: 0; border-bottom-right-radius: 0; border-right: none;")
        self.mapStyleMap.setCheckable(True)
        self.mapStyleMap.setChecked(True)
        self.mapStyleMap.setDefault(False)
        self.mapStyleMap.setFlat(False)
        self.mapStyleMap.setObjectName("mapStyleMap")
        self.mapStyleGroup = QtWidgets.QButtonGroup(MainWindow)
        self.mapStyleGroup.setObjectName("mapStyleGroup")
        self.mapStyleGroup.addButton(self.mapStyleMap)
        self.horizontalLayout_3.addWidget(self.mapStyleMap)
        self.mapStyleSat = QtWidgets.QPushButton(self.mapStyleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapStyleSat.sizePolicy().hasHeightForWidth())
        self.mapStyleSat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mapStyleSat.setFont(font)
        self.mapStyleSat.setStyleSheet("border-radius: 0;")
        self.mapStyleSat.setCheckable(True)
        self.mapStyleSat.setObjectName("mapStyleSat")
        self.mapStyleGroup.addButton(self.mapStyleSat)
        self.horizontalLayout_3.addWidget(self.mapStyleSat)
        self.mapStyleMix = QtWidgets.QPushButton(self.mapStyleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapStyleMix.sizePolicy().hasHeightForWidth())
        self.mapStyleMix.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mapStyleMix.setFont(font)
        self.mapStyleMix.setStyleSheet("border-top-left-radius: 0; border-bottom-left-radius: 0; border-left: none;")
        self.mapStyleMix.setCheckable(True)
        self.mapStyleMix.setObjectName("mapStyleMix")
        self.mapStyleGroup.addButton(self.mapStyleMix)
        self.horizontalLayout_3.addWidget(self.mapStyleMix)
        spacerItem7 = QtWidgets.QSpacerItem(157, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(4, 3)
        self.searchFrame = QtWidgets.QFrame(self.centralwidget)
        self.searchFrame.setGeometry(QtCore.QRect(0, 0, 650, 38))
        self.searchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.searchFrame)
        self.horizontalLayout_4.setContentsMargins(4, 2, 4, 4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.searchInput = QtWidgets.QLineEdit(self.searchFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchInput.sizePolicy().hasHeightForWidth())
        self.searchInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchInput.setFont(font)
        self.searchInput.setStyleSheet("padding-left: 6px;border-top-right-radius: 0; border-bottom-right-radius: 0; border-right: 0;")
        self.searchInput.setText("")
        self.searchInput.setObjectName("searchInput")
        self.horizontalLayout_4.addWidget(self.searchInput)
        self.searchClearBtn = QtWidgets.QPushButton(self.searchFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchClearBtn.sizePolicy().hasHeightForWidth())
        self.searchClearBtn.setSizePolicy(sizePolicy)
        self.searchClearBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.searchClearBtn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.searchClearBtn.setFont(font)
        self.searchClearBtn.setStyleSheet("border-radius: 0; border-left: none;")
        icon = QtGui.QIcon.fromTheme("Cancel")
        self.searchClearBtn.setIcon(icon)
        self.searchClearBtn.setObjectName("searchClearBtn")
        self.horizontalLayout_4.addWidget(self.searchClearBtn)
        self.searchBtn = QtWidgets.QPushButton(self.searchFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy)
        self.searchBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.searchBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.searchBtn.setFont(font)
        self.searchBtn.setStyleSheet("border-top-left-radius: 0; border-bottom-left-radius: 0; border-left: 0;")
        icon = QtGui.QIcon.fromTheme("Cancel")
        self.searchBtn.setIcon(icon)
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout_4.addWidget(self.searchBtn)
        spacerItem9 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 12)
        self.horizontalLayout_4.setStretch(3, 2)
        self.horizontalLayout_4.setStretch(4, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Большая задача"))
        self.xInput.setText(_translate("MainWindow", "37.617698"))
        self.yInput.setText(_translate("MainWindow", "55.755864"))
        self.scaleUpBtn.setText(_translate("MainWindow", "+"))
        self.scaleInput.setText(_translate("MainWindow", "7"))
        self.scaleDownBtn.setText(_translate("MainWindow", "-"))
        self.errorLabel.setText(_translate("MainWindow", "Некорректные параметры"))
        self.mapStyleMap.setText(_translate("MainWindow", "Схема"))
        self.mapStyleSat.setText(_translate("MainWindow", "Спутник"))
        self.mapStyleMix.setText(_translate("MainWindow", "Гибрид"))
        self.searchInput.setPlaceholderText(_translate("MainWindow", "Поиск"))
        self.searchClearBtn.setText(_translate("MainWindow", "X"))
        self.searchBtn.setText(_translate("MainWindow", "Найти"))
