# Form implementation generated from reading ui file 'D:\ĐẠI HỌC\ĐẠI HỌC\BẢO MẬT\DETAI_BMHTTT\View\ThietKe\ThietKeGiaiMaSDES.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1152, 649)
        self.b_grad = QtWidgets.QLabel(parent=Dialog)
        self.b_grad.setGeometry(QtCore.QRect(-90, 0, 1241, 661))
        self.b_grad.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 255));")
        self.b_grad.setText("")
        self.b_grad.setObjectName("b_grad")
        self.btnSaveFile = QtWidgets.QPushButton(parent=Dialog)
        self.btnSaveFile.setGeometry(QtCore.QRect(830, 570, 93, 28))
        self.btnSaveFile.setStyleSheet("QPushButton#btnSaveFile{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(25, 54, 82, 255), stop:1 rgba(33, 34, 36, 255));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#btnSaveFile:hover{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0  rgba(37, 82, 125, 255), stop:1 rgba(57, 60, 64, 255));\n"
"     transition: background 0.5s;\n"
"}\n"
"QPushButton#btnSaveFile:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/View/Image_and_icons/1157987.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        self.btnSaveFile.setIcon(icon)
        self.btnSaveFile.setObjectName("btnSaveFile")
        self.txtVanBanGoc = QtWidgets.QTextEdit(parent=Dialog)
        self.txtVanBanGoc.setGeometry(QtCore.QRect(400, 350, 671, 211))
        self.txtVanBanGoc.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 15);")
        self.txtVanBanGoc.setObjectName("txtVanBanGoc")
        self.btnClose = QtWidgets.QPushButton(parent=Dialog)
        self.btnClose.setGeometry(QtCore.QRect(980, 570, 93, 28))
        self.btnClose.setStyleSheet("QPushButton#btnClose{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(25, 54, 82, 255), stop:1 rgba(33, 34, 36, 255));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#btnClose:hover{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0  rgba(37, 82, 125, 255), stop:1 rgba(57, 60, 64, 255));\n"
"     transition: background 0.5s;\n"
"}\n"
"QPushButton#btnClose:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 255);\n"
"}")
        self.btnClose.setObjectName("btnClose")
        self.btnOpenFile = QtWidgets.QPushButton(parent=Dialog)
        self.btnOpenFile.setGeometry(QtCore.QRect(830, 290, 93, 28))
        self.btnOpenFile.setStyleSheet("QPushButton#btnOpenFile, #btnClose{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(25, 54, 82, 255), stop:1 rgba(33, 34, 36, 255));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#btnOpenFile:hover{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0  rgba(37, 82, 125, 255), stop:1 rgba(57, 60, 64, 255));\n"
"     transition: background 0.5s;\n"
"}\n"
"QPushButton#btnOpenFile:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/View/Image_and_icons/3748664.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        self.btnOpenFile.setIcon(icon1)
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.btnGiaiMa = QtWidgets.QPushButton(parent=Dialog)
        self.btnGiaiMa.setGeometry(QtCore.QRect(980, 290, 93, 28))
        self.btnGiaiMa.setStyleSheet("QPushButton#btnGiaiMa{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(25, 54, 82, 255), stop:1 rgba(33, 34, 36, 255));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#btnGiaiMa:hover{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0  rgba(37, 82, 125, 255), stop:1 rgba(57, 60, 64, 255));\n"
"     transition: background 0.5s;\n"
"}\n"
"QPushButton#btnGiaiMa:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/View/Image_and_icons/4797194-200.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        self.btnGiaiMa.setIcon(icon2)
        self.btnGiaiMa.setObjectName("btnGiaiMa")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 50, 181, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(400, 290, 131, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.txtKey = QtWidgets.QLabel(parent=Dialog)
        self.txtKey.setGeometry(QtCore.QRect(460, 290, 131, 31))
        self.txtKey.setStyleSheet("color: rgb(255, 255, 255);")
        self.txtKey.setObjectName("txtKey")
        self.b_img = QtWidgets.QLabel(parent=Dialog)
        self.b_img.setGeometry(QtCore.QRect(-60, -100, 1221, 761))
        self.b_img.setStyleSheet("background-image: url(D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/View/Image_and_icons/637e4098f94e074e846e965d_data-processing-applications-clearpoint.jpeg);")
        self.b_img.setText("")
        self.b_img.setObjectName("b_img")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(110, 50, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 330, 181, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.txtCiphertext = QtWidgets.QTextEdit(parent=Dialog)
        self.txtCiphertext.setGeometry(QtCore.QRect(400, 70, 671, 211))
        self.txtCiphertext.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 15);")
        self.txtCiphertext.setObjectName("txtCiphertext")
        self.b_img.raise_()
        self.b_grad.raise_()
        self.btnSaveFile.raise_()
        self.txtVanBanGoc.raise_()
        self.btnClose.raise_()
        self.btnOpenFile.raise_()
        self.btnGiaiMa.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.txtKey.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.txtCiphertext.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnSaveFile.setText(_translate("Dialog", "Lưu file"))
        self.btnClose.setText(_translate("Dialog", "Thoát"))
        self.btnOpenFile.setText(_translate("Dialog", "Mở file"))
        self.btnGiaiMa.setText(_translate("Dialog", "Giải mã "))
        self.label_2.setText(_translate("Dialog", "Nội dung đã mã hoá:"))
        self.label_3.setText(_translate("Dialog", "Key:"))
        self.txtKey.setText(_translate("Dialog", "Key"))
        self.label.setText(_translate("Dialog", "Giải mã SDES"))
        self.label_4.setText(_translate("Dialog", "Nội dung đã giải mã:"))
