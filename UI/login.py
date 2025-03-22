from PyQt5 import QtCore, QtGui, QtWidgets
import image.login_rc

class Ui_loginui(object):
    def setupUi(self, loginui):
        loginui.setObjectName("loginui")
        # 将登录界面设置为固定大小
        loginui.setFixedSize(984, 627)
        loginui.resize(984, 627)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(True)
        loginui.setFont(font)
        self.centralwidget = QtWidgets.QWidget(loginui)
        self.centralwidget.setObjectName("centralwidget")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(0, 0, 985, 596))
        self.listView_2.setStyleSheet("border-image: url(:/login1.jpg);\n"
"border-radius:10px;\n"
"\n"
"")
        self.listView_2.setObjectName("listView_2")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 0, 985, 596))
        self.listView.setStyleSheet("background-color: rgba(229, 229, 229,0.3);\n"
"border-radius:10px;\n"
"")
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(228, 35, 589, 78))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(28)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(236,245,250,0.8);\n"
"color: rgb(62, 62, 62);\n"
"border: 1px solid rgb(179,216,250);\n"
"border-radius:12px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(534, 448, 290, 57))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(-1)
        font.setBold(True)
        self.button_login.setFont(font)
        self.button_login.setStyleSheet("QPushButton {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    padding: 12px 24px;\n"
"    background-color: rgba(19, 176, 200, 0.5);\n"
"    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(19, 176, 200, 0.7); /* 悬停时较深的海洋蓝色 */\n"
"    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(-2px);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(20, 176, 220, 1.0); /* 点击时更深的海洋蓝色 */\n"
"    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);\n"
"    transform: translateY(2px);\n"
"}\n"
"\n"
"/* 添加默认状态的样式 */\n"
"QPushButton:!hover:!pressed {\n"
"    background-color: rgba(19, 176, 200, 0.5);\n"
"    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);\n"
"}\n"
"")
        self.button_login.setObjectName("button_login")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 210, 200, 200))
        self.label_2.setStyleSheet("border-image: url(:/imge.jpg);\n"
"border-radius:100px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit_account = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_account.setGeometry(QtCore.QRect(564, 238, 235, 43))
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.lineEdit_account.clear()  # 清除账号输入框中的内容

        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(564, 357, 235, 43))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)  # 设置密码输入框的显示模式为密码模式
        self.lineEdit_password.clear()  # 清除密码输入框中的内容

        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(20)
        font.setBold(False)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("color: #333333;\n"
"border: 2px solid #cccccc;\n"
"border-radius: 10px;\n"
"padding: 10px 15px;\n"
"background-color: #f0f0f0;\n"
"selection-background-color: #b3d4fc;\n"
"selection-color: #333333;\n"
"box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(468, 245, 91, 36))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(26)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(474, 364, 91, 36))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(26)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # 添加注册按钮
        self.button_register = QtWidgets.QPushButton(self.centralwidget)
        self.button_register.setGeometry(QtCore.QRect(534, 520, 290, 57))  # 设置注册按钮的位置
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(-1)
        font.setBold(True)
        self.button_register.setFont(font)
        self.button_register.setStyleSheet("QPushButton {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    padding: 12px 24px;\n"
"    background-color: rgba(19, 176, 200, 0.5);\n"
"    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(19, 176, 200, 0.7); /* 悬停时较深的海洋蓝色 */\n"
"    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.3);\n"
"    transform: translateY(-2px);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(20, 176, 220, 1.0); /* 点击时更深的海洋蓝色 */\n"
"    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);\n"
"    transform: translateY(2px);\n"
"}\n"
"\n"
"/* 添加默认状态的样式 */\n"
"QPushButton:!hover:!pressed {\n"
"    background-color: rgba(19, 176, 200, 0.5);\n"
"    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);\n"
"}\n"
"")
        self.button_register.setObjectName("button_register")
        self.button_register.setText("注册")  # 设置注册按钮的文本内容

        loginui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(loginui)
        self.statusbar.setObjectName("statusbar")
        loginui.setStatusBar(self.statusbar)

        self.retranslateUi(loginui)
        QtCore.QMetaObject.connectSlotsByName(loginui)
        # 在 setupUi 方法中的适当位置添加账号密码输入框的代码



    def retranslateUi(self, loginui):
        _translate = QtCore.QCoreApplication.translate
        loginui.setWindowTitle(_translate("loginui", "MainWindow"))
        self.label.setText(_translate("loginui", "输入账号密码进入任意门"))
        self.button_login.setWhatsThis(_translate("loginui", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">登陆</span></p></body></html>"))
        self.button_login.setText(_translate("loginui", "进入小哆啦的任意门"))
        self.label_3.setText(_translate("loginui", "账号："))
        self.label_4.setText(_translate("loginui", "密码："))


