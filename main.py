# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compiler.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from random import randint

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(918, 655)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Queshen = QtWidgets.QLabel(self.centralwidget)
        self.Queshen.setGeometry(QtCore.QRect(0, 0, 921, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Queshen.setFont(font)
        self.Queshen.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.Queshen.setStyleSheet("background-color: rgb(170, 170, 170, 50%);\n"
"border-radius: 20px;")
        self.Queshen.setAlignment(QtCore.Qt.AlignCenter)
        self.Queshen.setObjectName("Queshen")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 911, 461))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.groupBox.setFont(font)
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255, 80%);\n"
"border-radius: 25px;")
        self.groupBox.setObjectName("groupBox")
        self.Answer1 = QtWidgets.QRadioButton(self.groupBox)
        self.Answer1.setGeometry(QtCore.QRect(20, 90, 411, 121))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.Answer1.setFont(font)
        self.Answer1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Answer1.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.Answer1.setObjectName("Answer1")
        self.Answer3 = QtWidgets.QRadioButton(self.groupBox)
        self.Answer3.setGeometry(QtCore.QRect(20, 270, 421, 131))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.Answer3.setFont(font)
        self.Answer3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Answer3.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.Answer3.setObjectName("Answer3")
        self.Answer4 = QtWidgets.QRadioButton(self.groupBox)
        self.Answer4.setGeometry(QtCore.QRect(490, 270, 401, 131))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.Answer4.setFont(font)
        self.Answer4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Answer4.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.Answer4.setObjectName("Answer4")
        self.Answer2 = QtWidgets.QRadioButton(self.groupBox)
        self.Answer2.setGeometry(QtCore.QRect(490, 90, 401, 121))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(18)
        self.Answer2.setFont(font)
        self.Answer2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Answer2.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.Answer2.setObjectName("Answer2")
        self.Answer = QtWidgets.QPushButton(self.centralwidget)
        self.Answer.setGeometry(QtCore.QRect(270, 570, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setItalic(True)
        self.Answer.setFont(font)
        self.Answer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Answer.setStyleSheet("border-radius: 25px;\n"
"background-color: rgb(176, 0, 0);")
        self.Answer.setObjectName("Answer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.LeftValue = 0
        self.reval()
        self.display_as_new()
        self.EvalResult()
        self.RightValue = 0
        self.MessageBoxW = QMessageBox()
        self.MessageBoxW2 = QMessageBox()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mokaka"))
        self.Queshen.setText(_translate("MainWindow", "Кто первым открыл Америку?"))
        self.groupBox.setTitle(_translate("MainWindow", "Варианты ответов"))
        self.Answer1.setText(_translate("MainWindow", "Колумб"))
        self.Answer3.setText(_translate("MainWindow", "Магелан"))
        self.Answer4.setText(_translate("MainWindow", "Васко дэ Гама"))
        self.Answer2.setText(_translate("MainWindow", "Викинги"))
        self.Answer.setText(_translate("MainWindow", "Ответить"))

    def reval(self):
        self.Answer.clicked.connect(self.on_click)


    def display_as_new(self):
        questions = ["Дата убийства Ронина Робесра", "Дата установления нацизма в Германии", "Дата закрытие соседского магазина"]
        question = questions[randint(0, len(questions)-1)]
        self.Queshen.setText(question)

        return question

    def EvalResult(self):
        result = self.display_as_new()
        current_answer = "988"

        if result == "Дата убийства Ронина Робесра":
            self.Answer1.setText(str(randint(100, 990)))
            self.Answer2.setText(str(randint(100, 990)))
            self.Answer3.setText(str(randint(100, 1990)))
            self.Answer4.setText("988")
            current_answer = self.Answer4.text()

        elif result == "Дата установления нацизма в Германии":
            self.Answer1.setText(str(randint(100, 1900)))
            self.Answer2.setText(str(randint(100, 1700)))
            self.Answer3.setText("1933")
            self.Answer4.setText(str(randint(100, 1990)))
            current_answer = self.Answer3.text()

        elif result == "Дата закрытие соседского магазина":
            self.Answer1.setText(str(randint(500, 1900)))
            self.Answer2.setText(str(randint(-100, 1900)))
            self.Answer3.setText("1921")
            self.Answer4.setText(str(randint(100, 1990)))
            current_answer = self.Answer3.text()

        return current_answer


    def on_click(self):
        self.LeftValue += 1
        if self.LeftValue == 1:
            self.groupBox.setTitle("Вопрос 1")

        if self.LeftValue == 2:
            self.groupBox.setTitle("Вопрос 2")

        if self.LeftValue == 3:
            self.groupBox.setTitle("Вопрос 3")

        if self.LeftValue == 3:
            self.MessageBoxW2.setWindowTitle("Вопросы кончились!")
            currentResult = "Количество правильных ответов: " + str(self.RightValue) + " \n Нажмите ок чтобы повторить"
            str(currentResult)
            self.MessageBoxW2.setText(currentResult)
            self.MessageBoxW2.show()
            self.LeftValue -= 3

        get_answer = self.EvalResult()
        if get_answer == "988":
            self.Answer1.clicked.connect(self.lose)
            self.Answer2.clicked.connect(self.lose)
            self.Answer3.clicked.connect(self.lose)
            self.Answer4.clicked.connect(self.win)
        if get_answer == "1933":
            self.Answer1.clicked.connect(self.lose)
            self.Answer2.clicked.connect(self.lose)
            self.Answer3.clicked.connect(self.win)
            self.Answer4.clicked.connect(self.lose)
        if get_answer == "1921":
            self.Answer1.clicked.connect(self.lose)
            self.Answer2.clicked.connect(self.lose)
            self.Answer3.clicked.connect(self.win)
            self.Answer4.clicked.connect(self.lose)

        self.MessageBoxW.setWindowTitle("Результат")
        self.MessageBoxW.setFixedSize(100, 60)
        self.MessageBoxW.show()


    def win(self):
        self.MessageBoxW.setText("Правильно!")
        self.RightValue += 1

    def lose(self):
        self.MessageBoxW.setText("Неправильно!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
