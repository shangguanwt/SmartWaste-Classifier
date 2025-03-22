import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('布局示例')
        self.setGeometry(100, 100, 300, 200)

        # 创建按钮
        button1 = QPushButton('按钮1', self)
        button2 = QPushButton('按钮2', self)
        button3 = QPushButton('按钮3', self)
        label1 = QLabel('实施内容')

        # 创建垂直布局管理器
        layout = QVBoxLayout()

        # 将按钮添加到布局中
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(label1)

        # 将布局设置为窗口的主布局
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
