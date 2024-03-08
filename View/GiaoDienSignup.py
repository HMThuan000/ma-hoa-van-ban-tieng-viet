import sys
sys.path.append("D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/Control")
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from ThietKe.signup import Ui_MainWindow as Ui_Signup
from GiaoDienLogin import LoginApp as Ui_Login
import mahoasha3 #function
class SignupApp(QMainWindow, Ui_Signup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Khai báo một biến để theo dõi trạng thái của mật khẩu
        self.password_visible = False
        
        # Khi nút Đăng nhập được nhấn, kiểm tra tên đăng nhập và mật khẩu
        self.signupButton.clicked.connect(self.check_signup)
        # Khi nút "Hiển thị mật khẩu" được nhấn, chuyển đổi echoMode
        self.showPasswordButton.clicked.connect(self.toggle_password_visibility)
        self.showPasswordButton2.clicked.connect(self.toggle_password_visibility)

        self.cancelButton.clicked.connect(self.on_cancelButton_click)
        
    def on_cancelButton_click(self):
        self.close()
    def toggle_password_visibility(self):
        if self.password_visible:
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
            self.passwordInput2.setEchoMode(QLineEdit.EchoMode.Password)
            self.password_visible = False
        else:
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Normal)
            self.passwordInput2.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password_visible = True
    
         
    def check_signup(self):
        self.username = self.usernameInput.text()
        self.password = self.passwordInput.text()
        password2 = self.passwordInput2.text()
        if(self.password != password2):
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Icon.Information)  # Loại biểu tượng (Information)
            message_box.setWindowTitle('Thông báo')  # Tiêu đề
            message_box.setText('Bạn nhập password lần hai chưa đúng.')  # Nội dung thông báo
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)  # Các nút (OK)
            result = message_box.exec()  # Hiển thị hộp thoại và chờ đợi phản hồi từ người dùng
            self.passwordInput2.setFocus()
        else:
            us = mahoasha3.MaHoaSha3(self.username)
            ps = mahoasha3.MaHoaSha3(self.password)
            
            
            with open("D:/ĐẠI HỌC/ĐẠI HỌC/BẢO MẬT/DETAI_BMHTTT/Data/account.txt", "a", encoding='utf-8') as file:
                file.write(us+","+ps+"\n")
            self.openLoginWindow()

    def openLoginWindow(self):
        self.login_window = Ui_Login()
        self.login_window.usernameInput.setText(self.username)
        self.login_window.passwordInput.setText(self.password)
        self.login_window.show() #mở màn hình login
        self.close() #đóng màn hình login lại
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignupApp()
    window.show()
    sys.exit(app.exec())
