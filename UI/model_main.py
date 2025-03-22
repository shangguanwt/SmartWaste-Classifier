from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from login import Ui_loginui
from main_ui import Ui_main_ui
from PyQt5 import uic
import sys
import os


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginui()
        self.ui.setupUi(self)
        self.ui.button_login.clicked.connect(self.login_clicked)
        self.ui.button_register.clicked.connect(self.register_clicked)

    def login_clicked(self):
        # 获取账号和密码
        account = self.ui.lineEdit_account.text()
        password = self.ui.lineEdit_password.text()

        # 判断账号和密码是否为空
        if not account or not password:
            QMessageBox.warning(self, "错误", "账号或密码不能为空！", QMessageBox.Ok)
            return

        # 判断用户是否存在于 user_info.txt 文件中
        with open("user_info.txt", "r") as file:
            existing_users = file.readlines()
            for user in existing_users:
                user_info = user.strip().split(',')
                if account == user_info[0] and password == user_info[1]:
                    QMessageBox.information(self, "欢迎", "欢迎光临！", QMessageBox.Ok)
                    self.main_window = MainWindow()
                    self.main_window.show()
                    self.close()
                    return

        QMessageBox.warning(self, "错误", "账号或密码错误，请重新输入！", QMessageBox.Ok)
        self.ui.lineEdit_account.clear()
        self.ui.lineEdit_password.clear()

    def register_clicked(self):
        # 获取新的账号和密码
        new_account = self.ui.lineEdit_account.text()
        new_password = self.ui.lineEdit_password.text()

        # 判断账号和密码是否为空
        if not new_account or not new_password:
            QMessageBox.warning(self, "错误", "账号或密码不能为空！", QMessageBox.Ok)
            return

        # 判断用户是否已经存在于 user_info.txt 文件中
        with open("user_info.txt", "r") as file:
            existing_users = file.readlines()
            for user in existing_users:
                user_info = user.strip().split(',')
                if new_account == user_info[0]:
                    QMessageBox.warning(self, "错误", "该账号已存在，请直接登录！", QMessageBox.Ok)
                    return

        # 将新的账号和密码写入 user_info.txt 文件中
        with open("user_info.txt", "a") as file:
            file.write(f"{new_account},{new_password}\n")

        QMessageBox.information(self, "注册成功", "注册成功，请登录！", QMessageBox.Ok)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_ui()
        self.ui.setupUi(self)


def main():
    app = QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec_()


if __name__ == "__main__":
    main()
