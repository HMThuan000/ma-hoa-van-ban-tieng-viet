# Form implementation generated from reading ui file 'D:\ĐẠI HỌC\ĐẠI HỌC\BẢO MẬT\DETAI_BMHTTT\View\ThietKe\ThietKeMaHoaCeasar.ui'
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
        self.btnSaveFile = QtWidgets.QPushButton(parent=Dialog)
        self.btnSaveFile.setGeometry(QtCore.QRect(810, 580, 93, 28))
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
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 340, 181, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.btnOpenFile = QtWidgets.QPushButton(parent=Dialog)
        self.btnOpenFile.setGeometry(QtCore.QRect(810, 280, 93, 28))
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
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 40, 181, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(400, 280, 131, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.txtKey = QtWidgets.QTextEdit(parent=Dialog)
        self.txtKey.setGeometry(QtCore.QRect(560, 280, 111, 31))
        self.txtKey.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 15);")
        self.txtKey.setObjectName("txtKey")
        self.btnMaHoa = QtWidgets.QPushButton(parent=Dialog)
        self.btnMaHoa.setGeometry(QtCore.QRect(970, 280, 93, 28))
        self.btnMaHoa.setStyleSheet("QPushButton#btnMaHoa{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(25, 54, 82, 255), stop:1 rgba(33, 34, 36, 255));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#btnMaHoa:hover{\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0  rgba(37, 82, 125, 255), stop:1 rgba(57, 60, 64, 255));\n"
"     transition: background 0.5s;\n"
"}\n"
"QPushButton#btnMaHoa:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/View/Image_and_icons/fl-feature-lock-folders.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        self.btnMaHoa.setIcon(icon2)
        self.btnMaHoa.setObjectName("btnMaHoa")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(65, 50, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.txtCiphertext = QtWidgets.QTextEdit(parent=Dialog)
        self.txtCiphertext.setGeometry(QtCore.QRect(400, 360, 671, 211))
        self.txtCiphertext.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 15);")
        self.txtCiphertext.setObjectName("txtCiphertext")
        self.txtPlaintext = QtWidgets.QTextEdit(parent=Dialog)
        self.txtPlaintext.setGeometry(QtCore.QRect(400, 60, 671, 211))
        self.txtPlaintext.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 15);")
        self.txtPlaintext.setObjectName("txtPlaintext")
        self.btnClose = QtWidgets.QPushButton(parent=Dialog)
        self.btnClose.setGeometry(QtCore.QRect(970, 580, 93, 28))
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
        self.background_img = QtWidgets.QLabel(parent=Dialog)
        self.background_img.setGeometry(QtCore.QRect(-60, -100, 1221, 761))
        self.background_img.setStyleSheet("background-image: url(D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/View/Image_and_icons/637e4098f94e074e846e965d_data-processing-applications-clearpoint.jpeg);")
        self.background_img.setText("")
        self.background_img.setObjectName("background_img")
        self.background_grad = QtWidgets.QLabel(parent=Dialog)
        self.background_grad.setGeometry(QtCore.QRect(-90, 0, 1241, 661))
        self.background_grad.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 255));")
        self.background_grad.setText("")
        self.background_grad.setObjectName("background_grad")
        self.background_img.raise_()
        self.background_grad.raise_()
        self.btnSaveFile.raise_()
        self.label_4.raise_()
        self.btnOpenFile.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.txtKey.raise_()
        self.btnMaHoa.raise_()
        self.label.raise_()
        self.txtCiphertext.raise_()
        self.txtPlaintext.raise_()
        self.btnClose.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnSaveFile.setText(_translate("Dialog", "Lưu file"))
        self.label_4.setText(_translate("Dialog", "Nội dung đã mã hoá:"))
        self.btnOpenFile.setText(_translate("Dialog", "Mở file"))
        self.label_2.setText(_translate("Dialog", "Nhập nội dung cần mã hoá:"))
        self.label_3.setText(_translate("Dialog", "Nhập key (số nguyên):"))
        self.btnMaHoa.setText(_translate("Dialog", "Mã hoá"))
        self.label.setText(_translate("Dialog", "Mã hoá Caesar"))
        self.btnClose.setText(_translate("Dialog", "Thoát"))
