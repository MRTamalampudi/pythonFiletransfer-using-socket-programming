# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panchuko.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 675)
        MainWindow.setMinimumSize(QtCore.QSize(900, 675))
        MainWindow.setMaximumSize(QtCore.QSize(900, 675))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/iconn.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 900, 675))
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setMinimumSize(QtCore.QSize(900, 675))
        self.home.setMaximumSize(QtCore.QSize(900, 675))
        self.home.setObjectName("home")
        self.panchuko = QtWidgets.QLabel(self.home)
        self.panchuko.setGeometry(QtCore.QRect(375, 43, 150, 29))
        self.panchuko.setText("")
        self.panchuko.setPixmap(QtGui.QPixmap("resources/send recieve/SVG/panchuko.svg"))
        self.panchuko.setObjectName("panchuko")
        self.send = QtWidgets.QToolButton(self.home)
        self.send.setEnabled(True)
        self.send.setGeometry(QtCore.QRect(385, 315, 135, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/send recieve/SVG/send .svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send.setIcon(icon1)
        self.send.setIconSize(QtCore.QSize(130, 45))
        self.send.setCheckable(False)
        self.send.setAutoRepeat(False)
        self.send.setAutoExclusive(False)
        self.send.setAutoRaise(True)
        self.send.setObjectName("send")
        self.background = QtWidgets.QLabel(self.home)
        self.background.setGeometry(QtCore.QRect(0, 0, 900, 675))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("resources/main bg.svg"))
        self.background.setObjectName("background")
        self.background.raise_()
        self.panchuko.raise_()
        self.send.raise_()
        self.stackedWidget.addWidget(self.home)
        self.makesure = QtWidgets.QWidget()
        self.makesure.setMinimumSize(QtCore.QSize(900, 675))
        self.makesure.setMaximumSize(QtCore.QSize(900, 675))
        self.makesure.setObjectName("makesure")
        self.background_2 = QtWidgets.QLabel(self.makesure)
        self.background_2.setGeometry(QtCore.QRect(0, 0, 900, 675))
        self.background_2.setText("")
        self.background_2.setPixmap(QtGui.QPixmap("resources/main bg.svg"))
        self.background_2.setObjectName("background_2")
        self.label = QtWidgets.QLabel(self.makesure)
        self.label.setGeometry(QtCore.QRect(147, 325, 606, 24))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/make sure/SVG/next.svg"))
        self.label.setObjectName("label")
        self.makesurenext = QtWidgets.QToolButton(self.makesure)
        self.makesurenext.setGeometry(QtCore.QRect(400, 572, 110, 50))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/make sure/SVG/nextt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.makesurenext.setIcon(icon2)
        self.makesurenext.setIconSize(QtCore.QSize(100, 45))
        self.makesurenext.setAutoRaise(True)
        self.makesurenext.setObjectName("makesurenext")
        self.stackedWidget.addWidget(self.makesure)
        self.readytogo = QtWidgets.QWidget()
        self.readytogo.setObjectName("readytogo")
        self.background_4 = QtWidgets.QLabel(self.readytogo)
        self.background_4.setGeometry(QtCore.QRect(0, 0, 900, 675))
        self.background_4.setText("")
        self.background_4.setPixmap(QtGui.QPixmap("resources/main bg.svg"))
        self.background_4.setObjectName("background_4")
        self.listWidget = QtWidgets.QListWidget(self.readytogo)
        self.listWidget.setGeometry(QtCore.QRect(45, 90, 780, 475))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color:\"#dddddd\"")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setObjectName("listWidget")
        self.filenamesize = QtWidgets.QLabel(self.readytogo)
        self.filenamesize.setGeometry(QtCore.QRect(45, 45, 161, 24))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.filenamesize.setFont(font)
        self.filenamesize.setStyleSheet("color:\"#dddddd\"")
        self.filenamesize.setObjectName("filenamesize")
        self.readytogonext = QtWidgets.QToolButton(self.readytogo)
        self.readytogonext.setGeometry(QtCore.QRect(400, 572, 110, 50))
        self.readytogonext.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/enter pass code/SVG/next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.readytogonext.setIcon(icon3)
        self.readytogonext.setIconSize(QtCore.QSize(100, 45))
        self.readytogonext.setAutoRaise(True)
        self.readytogonext.setObjectName("readytogonext")
        self.stackedWidget.addWidget(self.readytogo)
        self.fragementsareout = QtWidgets.QWidget()
        self.fragementsareout.setObjectName("fragementsareout")
        self.label_2 = QtWidgets.QLabel(self.fragementsareout)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 900, 675))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("resources/main bg.svg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.fragementsareout)
        self.label_3.setGeometry(QtCore.QRect(0, 299, 900, 78))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:\"#dddddd\";")
        self.label_3.setPixmap(QtGui.QPixmap("resources/fragments are out.svg"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.filessent = QtWidgets.QLabel(self.fragementsareout)
        self.filessent.setGeometry(QtCore.QRect(0, 480, 900, 50))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        self.filessent.setFont(font)
        self.filessent.setStyleSheet("color:\"#dddddd\"")
        self.filessent.setAlignment(QtCore.Qt.AlignCenter)
        self.filessent.setObjectName("filessent")
        self.stackedWidget.addWidget(self.fragementsareout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "panchuko"))
        self.send.setText(_translate("MainWindow", "..."))
        self.makesurenext.setText(_translate("MainWindow", "..."))
        self.filenamesize.setText(_translate("MainWindow", "Files Name & Size"))
        self.label_3.setText(_translate("MainWindow", "Fragments are now open to air :-)"))
        self.filessent.setText(_translate("MainWindow", "Files sent : 00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
