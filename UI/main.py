import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5 import uic
import image.login_rc


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui', self)
        self.show()

        # 加载保存的账号和密码
        self.load_credentials()

        # 绑定按钮点击事件
        self.button_login.clicked.connect(self.login)

    def login(self):
        # 在这里编写登录逻辑
        # 例如，获取账号和密码输入框的文本
        account = self.lineEdit_account.text()
        password = self.lineEdit_password.text()

        # 保存账号和密码
        self.save_credentials(account, password)

    def save_credentials(self, account, password):
        # 将账号和密码保存到文件中
        with open('credentials.txt', 'w') as f:
            f.write(f'{account}\n')
            f.write(f'{password}\n')

    def load_credentials(self):
        # 从文件中加载账号和密码
        try:
            with open('credentials.txt', 'r') as f:
                account = f.readline().strip()
                password = f.readline().strip()
                self.lineEdit_account.setText(account)
                self.lineEdit_password.setText(password)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())
