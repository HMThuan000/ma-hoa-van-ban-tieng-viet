import sys
sys.path.append("D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/Control")
import math
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox #[1]????????????
from ThietKe.ThietKeMaHoaRSA import Ui_Dialog
import mahoaRSA #???????????
#========================================================================================
class MyDialogMHRSA(QDialog, Ui_Dialog):#[2]???????????????????????
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.c = []
        self.s = ''
        self.btnMaHoa.clicked.connect(self.MaHoa)
        self.btnOpenFile.clicked.connect(self.MoFile)
        self.btnSaveFile.clicked.connect(self.GhiFile)
        self.btnClose.clicked.connect(self.Close)
        
    def Close(self):
        choice = QMessageBox.question(self, "Xác nhận thoát", "Bạn có chắc muốn thoát ứng dụng?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if choice == QMessageBox.StandardButton.Yes:
            self.close()
        else:
            pass #nothing
    def MaHoa(self):
        textpl = self.txtPlaintext.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaVignere
        if not textpl:
            QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
            self.btnOpenFile.setFocus()
        else:
            e=65537
            n=4255903
            self.c = mahoaRSA.MaHoa(textpl,e,n) #gọi hàm mã hoá của đối tượng này
            #print(self.c)
            self.s = ''
            for i in self.c:
                self.s += str(i)+' '
            #print(self.s)
            self.txtCiphertext.setPlainText(self.s)
    def MoFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.txtPlaintext.setPlainText(fileContent)
    def GhiFile(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w') as file:
                file.write(self.s)
                #for i in self.c:
                    #file.write("%d " % i)
                
#========================================================================================
def main():
    app = QApplication(sys.argv)
    mainMyDialog = MyDialogMHRSA()
    mainMyDialog.show()
    sys.exit(app.exec())
#========================================================================================
if __name__ == "__main__":
    main()
