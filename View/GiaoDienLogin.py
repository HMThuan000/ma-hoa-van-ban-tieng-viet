import sys
sys.path.append("D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/Control")
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from ThietKe.login import Ui_MainWindow as Ui_Login
#from ThietKe.ThietKeManHinhChinh import Ui_MainWindow as Ui_Main
from GiaoDienManHinhChinh import MyMainWindow
import mahoasha3 #function
class LoginApp(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Khai báo một biến để theo dõi trạng thái của mật khẩu
        self.password_visible = False
        
        # Khi nút Đăng nhập được nhấn, kiểm tra tên đăng nhập và mật khẩu
        self.loginButton.clicked.connect(self.check_login)
        # Khi nút "Hiển thị mật khẩu" được nhấn, chuyển đổi echoMode
        self.showPasswordButton.clicked.connect(self.toggle_password_visibility)

        self.cancelButton.clicked.connect(self.on_cancelButton_click)
        
    def on_cancelButton_click(self):
        self.close()

    def toggle_password_visibility(self):
        if self.password_visible:
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
            self.password_visible = False
        else:
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password_visible = True

    def check_Account(self,us,ps):
        with open("D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/Data/account.txt", "r", encoding='utf-8') as file:
            for line in file:
                if line.strip() == us+","+ps:
                    return True
            return False
    
    def check_login(self):
        username = self.usernameInput.text()
        us = mahoasha3.MaHoaSha3(username) 
        password = self.passwordInput.text()
        ps = mahoasha3.MaHoaSha3(password)
        if self.check_Account(us,ps):
            self.openMainWindow()
        else:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Icon.Information)  # Loại biểu tượng (Information)
            message_box.setWindowTitle('Thông báo')  # Tiêu đề
            message_box.setText('Bạn nhập sai username và password.')  # Nội dung thông báo
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)  # Các nút (OK)
            result = message_box.exec()  # Hiển thị hộp thoại và chờ đợi phản hồi từ người dùng
            self.usernameInput.setFocus()

    def openMainWindow(self):
        self.main_window = MyMainWindow()
        self.main_window.menuM_ho.setEnabled(True)
        self.main_window.menuGi_i_m.setEnabled(True)
        self.main_window.show() #mở màn hình chính
        self.close() #đóng màn hình login lại
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())
