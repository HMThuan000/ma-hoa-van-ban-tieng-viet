import sys
sys.path.append("D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/Control")
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox #[1]????????????
from ThietKe.ThietKeGiaiMaNhieuDong import Ui_Dialog  #?????????????????
from mahoachuyenvinhieudong_class import CChuyenViNhieuDong #???????????
#========================================================================================
class MyDialogGMNhieuDong(QDialog, Ui_Dialog):#[2]???????????????????????
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Thêm xử lý sự kiện và tuỳ chỉnh giao diện người dùng tại đây
        self.textk = '' #khai báo toàn cục của lớp THIS => datamember
        self.btnGiaiMa.clicked.connect(self.GiaiMa) #????????????????????????
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
    def GiaiMa(self):
        if not self.textk:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!!")
            self.txtKey.setFocus()
        else:
            textci = self.txtCiphertext.toPlainText() #lấy dữ liệu trong text plaintext của ThietKeMaHoaNhieuDong
            if not textci:
                QMessageBox.information(self, "Thông báo", "Bạn chưa mở file dữ liệu!!!!")
                self.btnOpenFile.setFocus()
            else:
                cChuyenViNhieuDong= CChuyenViNhieuDong("",None,textci) #khai báo đối tượng của lớp CNhieuDong
                k = [ int(item) for item in self.textk.split(' ') ]
                cChuyenViNhieuDong.SetKey(k)
                s = cChuyenViNhieuDong.GiaiMa() #gọi hàm mã hoá của đối tượng này
                self.txtVanBanGoc.setPlainText(s) #xuất dữ liệu (chuỗi) ra text ciphertext của ThietKeMaHoaNhieuDong
    def MoFile(self):
        # Mở file đã mã hoá riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File Đã mã hoá", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                s=''
                line = file.readline()
                while line:
                    s+=line
                    line = file.readline()
                self.txtCiphertext.setPlainText(s)
        # Mở file KEY riêng
        filePath, _ = QFileDialog.getOpenFileName(self, "Open File KEY", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'r', encoding='utf-8') as file:
                self.textk = file.read()
                self.txtKey.setPlainText(self.textk)
                
    def GhiFile(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(self.txtVanBanGoc.toPlainText())
#========================================================================================
def main():
    app = QApplication(sys.argv)
    mainMyDialog = MyDialogGMNhieuDong()
    mainMyDialog.show()
    sys.exit(app.exec())
#========================================================================================
if __name__ == "__main__":
    main()
