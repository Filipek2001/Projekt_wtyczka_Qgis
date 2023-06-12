# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wtyczka_projekt_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Wtyczka_Projekt3DialogBase(object):
    def setupUi(self, Wtyczka_Projekt3DialogBase):
        Wtyczka_Projekt3DialogBase.setObjectName("Wtyczka_Projekt3DialogBase")
        Wtyczka_Projekt3DialogBase.resize(939, 620)
        self.button_box = QtWidgets.QDialogButtonBox(Wtyczka_Projekt3DialogBase)
        self.button_box.setGeometry(QtCore.QRect(120, 530, 211, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label_wynik = QtWidgets.QLabel(Wtyczka_Projekt3DialogBase)
        self.label_wynik.setGeometry(QtCore.QRect(250, 180, 131, 21))
        self.label_wynik.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_wynik.setText("")
        self.label_wynik.setObjectName("label_wynik")
        self.pushButton_zlicz = QtWidgets.QPushButton(Wtyczka_Projekt3DialogBase)
        self.pushButton_zlicz.setGeometry(QtCore.QRect(90, 130, 93, 28))
        self.pushButton_zlicz.setObjectName("pushButton_zlicz")
        self.label_wybor_warstwa = QtWidgets.QLabel(Wtyczka_Projekt3DialogBase)
        self.label_wybor_warstwa.setGeometry(QtCore.QRect(70, 80, 121, 16))
        self.label_wybor_warstwa.setObjectName("label_wybor_warstwa")
        self.label_lb_obiektow = QtWidgets.QLabel(Wtyczka_Projekt3DialogBase)
        self.label_lb_obiektow.setGeometry(QtCore.QRect(60, 180, 181, 16))
        self.label_lb_obiektow.setObjectName("label_lb_obiektow")
        self.mMapLayerComboBox = QgsMapLayerComboBox(Wtyczka_Projekt3DialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(200, 70, 201, 27))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.label_aktywna_warstwa = QtWidgets.QLabel(Wtyczka_Projekt3DialogBase)
        self.label_aktywna_warstwa.setGeometry(QtCore.QRect(60, 270, 161, 16))
        self.label_aktywna_warstwa.setObjectName("label_aktywna_warstwa")
        self.label_wynik_aktywna = QtWidgets.QLabel(Wtyczka_Projekt3DialogBase)
        self.label_wynik_aktywna.setGeometry(QtCore.QRect(240, 270, 141, 21))
        self.label_wynik_aktywna.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_wynik_aktywna.setText("")
        self.label_wynik_aktywna.setObjectName("label_wynik_aktywna")
        self.label_wsp_wybr = QtWidgets.QLabel(Wtyczka_Projekt3DialogBase)
        self.label_wsp_wybr.setGeometry(QtCore.QRect(60, 330, 191, 16))
        self.label_wsp_wybr.setObjectName("label_wsp_wybr")
        self.pushButton_wsp = QtWidgets.QPushButton(Wtyczka_Projekt3DialogBase)
        self.pushButton_wsp.setGeometry(QtCore.QRect(120, 460, 141, 28))
        self.pushButton_wsp.setObjectName("pushButton_wsp")
        self.label_wyniki_wsp = QtWidgets.QLabel(Wtyczka_Projekt3DialogBase)
        self.label_wyniki_wsp.setGeometry(QtCore.QRect(80, 360, 201, 71))
        self.label_wyniki_wsp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_wyniki_wsp.setText("")
        self.label_wyniki_wsp.setObjectName("label_wyniki_wsp")
        self.label_dH = QtWidgets.QLabel(Wtyczka_Projekt3DialogBase)
        self.label_dH.setGeometry(QtCore.QRect(580, 70, 231, 16))
        self.label_dH.setObjectName("label_dH")
        self.label_wynik_dH = QtWidgets.QLabel(Wtyczka_Projekt3DialogBase)
        self.label_wynik_dH.setGeometry(QtCore.QRect(620, 150, 131, 21))
        self.label_wynik_dH.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_wynik_dH.setText("")
        self.label_wynik_dH.setObjectName("label_wynik_dH")
        self.pushButton_dH = QtWidgets.QPushButton(Wtyczka_Projekt3DialogBase)
        self.pushButton_dH.setGeometry(QtCore.QRect(640, 100, 93, 28))
        self.pushButton_dH.setObjectName("pushButton_dH")
        self.label_p = QtWidgets.QLabel(Wtyczka_Projekt3DialogBase)
        self.label_p.setGeometry(QtCore.QRect(580, 220, 241, 16))
        self.label_p.setObjectName("label_p")
        self.pushButton_pole = QtWidgets.QPushButton(Wtyczka_Projekt3DialogBase)
        self.pushButton_pole.setGeometry(QtCore.QRect(640, 260, 93, 28))
        self.pushButton_pole.setObjectName("pushButton_pole")
        self.label_wynik_p = QtWidgets.QLabel(Wtyczka_Projekt3DialogBase)
        self.label_wynik_p.setGeometry(QtCore.QRect(620, 310, 131, 21))
        self.label_wynik_p.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_wynik_p.setText("")
        self.label_wynik_p.setObjectName("label_wynik_p")

        self.retranslateUi(Wtyczka_Projekt3DialogBase)
        self.button_box.accepted.connect(Wtyczka_Projekt3DialogBase.accept)
        self.button_box.rejected.connect(Wtyczka_Projekt3DialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(Wtyczka_Projekt3DialogBase)

    def retranslateUi(self, Wtyczka_Projekt3DialogBase):
        _translate = QtCore.QCoreApplication.translate
        Wtyczka_Projekt3DialogBase.setWindowTitle(_translate("Wtyczka_Projekt3DialogBase", "Wtyczka_Projekt"))
        self.pushButton_zlicz.setText(_translate("Wtyczka_Projekt3DialogBase", "Zlicz"))
        self.label_wybor_warstwa.setText(_translate("Wtyczka_Projekt3DialogBase", "Wybierz warstwę:"))
        self.label_lb_obiektow.setText(_translate("Wtyczka_Projekt3DialogBase", "Liczba obiektów w warstwie:"))
        self.label_aktywna_warstwa.setText(_translate("Wtyczka_Projekt3DialogBase", "Nazwa aktywnej warstwy:"))
        self.label_wsp_wybr.setText(_translate("Wtyczka_Projekt3DialogBase", "Współrzędne wybranych obiektów:"))
        self.pushButton_wsp.setText(_translate("Wtyczka_Projekt3DialogBase", "Pokaż współrzędne"))
        self.label_dH.setText(_translate("Wtyczka_Projekt3DialogBase", "Różnica wysokości wybranych obiektów:"))
        self.pushButton_dH.setText(_translate("Wtyczka_Projekt3DialogBase", "Oblicz dH"))
        self.label_p.setText(_translate("Wtyczka_Projekt3DialogBase", "Pole powierzchni wybranych obiektów:"))
        self.pushButton_pole.setText(_translate("Wtyczka_Projekt3DialogBase", "Oblicz pole"))

from qgsmaplayercombobox import QgsMapLayerComboBox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wtyczka_Projekt3DialogBase = QtWidgets.QDialog()
    ui = Ui_Wtyczka_Projekt3DialogBase()
    ui.setupUi(Wtyczka_Projekt3DialogBase)
    Wtyczka_Projekt3DialogBase.show()
    sys.exit(app.exec_())

