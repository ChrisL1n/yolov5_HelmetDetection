# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelmetDetect.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(906, 665)
        self.detect_button = QtWidgets.QPushButton(Form)
        self.detect_button.setGeometry(QtCore.QRect(60, 240, 111, 51))
        self.detect_button.setObjectName("detect_button")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(570, 80, 47, 21))
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 80, 191, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(400, 20, 201, 51))
        self.label_2.setObjectName("label_2")
        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setGeometry(QtCore.QRect(60, 310, 111, 51))
        self.cancel_button.setObjectName("cancel_button")
        self.png_label = QtWidgets.QLabel(Form)
        self.png_label.setGeometry(QtCore.QRect(210, 110, 561, 451))
        self.png_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.png_label.setText("")
        self.png_label.setObjectName("png_label")
        self.result_label = QtWidgets.QLabel(Form)
        self.result_label.setGeometry(QtCore.QRect(310, 590, 341, 41))
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.detect_button.setText(_translate("Form", "Detect"))
        self.toolButton.setText(_translate("Form", "..."))
        self.label.setText(_translate("Form", "Select Your Input Image"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Helmet Detection</span></p></body></html>"))
        self.cancel_button.setText(_translate("Form", "Cancel"))