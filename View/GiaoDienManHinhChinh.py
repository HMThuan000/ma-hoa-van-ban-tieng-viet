import sys
sys.path.append("D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/Control")
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ThietKe.ThietKeManHinhChinh import Ui_MainWindow
from GiaoDienMaHoaCeasar import MyDialogMHCeasar#import cửa sổ con [1]
from GiaoDienGiaiMaCeasar import MyDialogGMCeasar #[4]
from GiaoDienMaHoaVignere import MyDialogMHVignere
from GiaoDienGiaiMaVignere import MyDialogGMVignere
from GiaoDienMaHoaTrithemius import MyDialogMHTrithemius
from GiaoDienGiaiMaTrithemius import MyDialogGMTrithemius
from GiaoDienMaHoaBelasco import MyDialogMHBelasco
from GiaoDienGiaiMaBelasco import MyDialogGMBelasco
from GiaoDienMaHoaHaiDong import MyDialogMHHaiDong
from GiaoDienGiaiMaHaiDong import MyDialogGMHaiDong
from GiaoDienMaHoaNhieuDong import MyDialogMHNhieuDong
from GiaoDienGiaiMaNhieuDong import MyDialogGMNhieuDong
from GiaoDienMaHoaXORCeasar import MyDialogMHXORCeasar#import cửa sổ con [1]
from GiaoDienGiaiMaXORCeasar import MyDialogGMXORCeasar #[4]
from GiaoDienMaHoaXORVignere import MyDialogMHXORVignere#import cửa sổ con [1]
from GiaoDienGiaiMaXORVignere import MyDialogGMXORVignere #[4]
from GiaoDienMaHoaXORTrithemius import MyDialogMHXORTrithemius#import cửa sổ con [1]
from GiaoDienGiaiMaXORTrithemius import MyDialogGMXORTrithemius #[4]
from GiaoDienMaHoaXORBelasco import MyDialogMHXORBelasco#import cửa sổ con [1]
from GiaoDienGiaiMaXORBelasco import MyDialogGMXORBelasco #[4]
from GiaoDienMaHoaSDES import MyDialogMHSDES#import cửa sổ con [1]
from GiaoDienGiaiMaSDES import MyDialogGMSDES #[4]
from GiaoDienMaHoaRSA import MyDialogMHRSA#import cửa sổ con [1]
from GiaoDienGiaiMaRSA import MyDialogGMRSA #[4]
from GiaoDienMaHoaAES import MyDialogMHAES#import cửa sổ con [1]
from GiaoDienGiaiMaAES import MyDialogGMAES #[4]
from GiaoDienLoginDialog import LoginDialog
from GiaoDienSignupDialog import SignupDialog

####################################################################################
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionCeasar_MaHoa.triggered.connect(self.on_MaHoaCeasar_click) #[2]
        self.actionCeasar_GiaiMa.triggered.connect(self.on_GiaiMaCeasar_click)
        self.actionVignere_MaHoa.triggered.connect(self.on_MaHoaVignere_click)
        self.actionVignere_GiaiMa.triggered.connect(self.on_GiaiMaVignere_click)
        self.actionTrithemius_MaHoa.triggered.connect(self.on_MaHoaTrithemius_click)
        self.actionTrithemius_GiaiMa.triggered.connect(self.on_GiaiMaTrithemius_click)
        self.actionBelasco_MaHoa.triggered.connect(self.on_MaHoaBelasco_click)
        self.actionBelasco_GiaiMa.triggered.connect(self.on_GiaiMaBelasco_click)
        self.actionHai_dong_MaHoa.triggered.connect(self.on_MaHoaHaiDong_click)
        self.actionHai_dong_GiaiMa.triggered.connect(self.on_GiaiMaHaiDong_click)
        self.actionNhieu_dong_MaHoa.triggered.connect(self.on_MaHoaNhieuDong_click)
        self.actionNhieu_dong_GiaiMa.triggered.connect(self.on_GiaiMaNhieuDong_click)
        self.actionCeasar_XOR_MaHoa.triggered.connect(self.on_MaHoaXORCeasar_click) #[2]
        self.actionCeasar_XOR_GiaiMa.triggered.connect(self.on_GiaiMaXORCeasar_click)
        self.actionVignere_XOR_MaHoa.triggered.connect(self.on_MaHoaXORVignere_click) #[2]
        self.actionVignere_XOR_GiaiMa.triggered.connect(self.on_GiaiMaXORVignere_click)
        self.actionTrithemius_XOR_MaHoa.triggered.connect(self.on_MaHoaXORTrithemius_click) #[2]
        self.actionTrithemius_XOR_GiaiMa.triggered.connect(self.on_GiaiMaXORTrithemius_click)
        self.actionBelasco_XOR_MaHoa.triggered.connect(self.on_MaHoaXORBelasco_click) #[2]
        self.actionBelasco_XOR_GiaiMa.triggered.connect(self.on_GiaiMaXORBelasco_click)
        self.actionSDES_MaHoa.triggered.connect(self.on_MaHoaSDES_click) #[2]
        self.actionSDES_GiaiMa.triggered.connect(self.on_GiaiMaSDES_click)
        self.actionRSA_MaHoa.triggered.connect(self.on_MaHoaRSA_click) #[2]
        self.actionRSA_GiaiMa.triggered.connect(self.on_GiaiMaRSA_click)
        self.actionAES_MaHoa.triggered.connect(self.on_MaHoaAES_click) #[2]
        self.actionAES_GiaiMa.triggered.connect(self.on_GiaiMaAES_click)
        self.actionLogin.triggered.connect(self.on_Login_click)
        self.actionSignup.triggered.connect(self.on_Signup_click)
        self.actionLogout.triggered.connect(self.on_Logout_click)
        
        self.menuM_ho.setDisabled(True)
        self.menuGi_i_m.setDisabled(True)
        self.actionLogout.setDisabled(True)

    def on_Login_click(self):
        self.login_window = LoginDialog()
        # Kết nối tín hiệu từ Dialog với khe (slot) của MainWindow
        self.login_window.data_signal.connect(self.receive_data_from_dialog)
        self.login_window.show() #mở màn hình login

    def on_Signup_click(self):
        self.Signup_window = SignupDialog()
        self.Signup_window.show() #mở màn hình login

    def on_Logout_click(self):
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Icon.Information)  # Loại biểu tượng (Information)
        message_box.setWindowTitle('Thông báo')  # Tiêu đề
        message_box.setText('Bạn đã đăng xuất!!!')  # Nội dung thông báo
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)  # Các nút (OK)
        result = message_box.exec()  # Hiển thị hộp thoại và chờ đợi phản hồi từ người dùng
        
        self.menuM_ho.setDisabled(True)
        self.menuGi_i_m.setDisabled(True)
        self.actionLogout.setDisabled(True)
        self.actionSignup.setEnabled(True)
        self.actionLogin.setEnabled(True)
    
    def receive_data_from_dialog(self, data):
        #print(f"Received data from Dialog: {data}")
        if data == 'ok':
            self.menuM_ho.setEnabled(True)
            self.menuGi_i_m.setEnabled(True)
            self.actionLogout.setEnabled(True)
            self.actionSignup.setDisabled(True)
            self.actionLogin.setDisabled(True)
    
    def on_MaHoaCeasar_click(self):######### [3]
        dialog = MyDialogMHCeasar()
        dialog.exec()
    def on_MaHoaVignere_click(self):######### [3]
        dialog = MyDialogMHVignere()
        dialog.exec()
    def on_MaHoaTrithemius_click(self):######### [3]
        dialog = MyDialogMHTrithemius()
        dialog.exec()
    def on_MaHoaBelasco_click(self):######### [3]
        dialog = MyDialogMHBelasco()
        dialog.exec()
    def on_MaHoaHaiDong_click(self):######### [3]
        dialog = MyDialogMHHaiDong()
        dialog.exec()
    def on_GiaiMaHaiDong_click(self):
        dialog = MyDialogGMHaiDong()
        dialog.exec()
    def on_MaHoaNhieuDong_click(self):######### [3]
        dialog = MyDialogMHNhieuDong()
        dialog.exec()
    def on_GiaiMaNhieuDong_click(self):
        dialog = MyDialogGMNhieuDong()
        dialog.exec()
    def on_GiaiMaCeasar_click(self):
        dialog = MyDialogGMCeasar()
        dialog.exec()
    def on_GiaiMaVignere_click(self):
        dialog = MyDialogGMVignere()
        dialog.exec()
    def on_GiaiMaTrithemius_click(self):
        dialog = MyDialogGMTrithemius()
        dialog.exec()
    def on_GiaiMaBelasco_click(self):
        dialog = MyDialogGMBelasco()
        dialog.exec()
    def on_MaHoaXORCeasar_click(self):######### [3]
        dialog = MyDialogMHXORCeasar()
        dialog.exec()
    def on_GiaiMaXORCeasar_click(self):
        dialog = MyDialogGMXORCeasar()
        dialog.exec()
    def on_MaHoaXORVignere_click(self):######### [3]
        dialog = MyDialogMHXORVignere()
        dialog.exec()
    def on_GiaiMaXORVignere_click(self):
        dialog = MyDialogGMXORVignere()
        dialog.exec()
    def on_MaHoaXORTrithemius_click(self):######### [3]
        dialog = MyDialogMHXORTrithemius()
        dialog.exec()
    def on_GiaiMaXORTrithemius_click(self):
        dialog = MyDialogGMXORTrithemius()
        dialog.exec()
    def on_MaHoaXORBelasco_click(self):######### [3]
        dialog = MyDialogMHXORBelasco()
        dialog.exec()
    def on_GiaiMaXORBelasco_click(self):
        dialog = MyDialogGMXORBelasco()
        dialog.exec()
    def on_MaHoaSDES_click(self):######### [3]
        dialog = MyDialogMHSDES()
        dialog.exec()
    def on_GiaiMaSDES_click(self):
        dialog = MyDialogGMSDES()
        dialog.exec()
    def on_MaHoaRSA_click(self):######### [3]
        dialog = MyDialogMHRSA()
        dialog.exec()
    def on_GiaiMaRSA_click(self):
        dialog = MyDialogGMRSA()
        dialog.exec()
    def on_MaHoaAES_click(self):######### [3]
        dialog = MyDialogMHAES()
        dialog.exec()
    def on_GiaiMaAES_click(self):
        dialog = MyDialogGMAES()
        dialog.exec()
#======================================================================================
def main():
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())
#=============================================================================
if __name__ == "__main__":
    main()







'''

'''
