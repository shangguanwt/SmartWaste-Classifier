import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QFileDialog, QFrame
from PyQt5.QtGui import QPixmap, QImage, QFont
from PyQt5.QtCore import QTimer, QSize
import torch
from PyQt5.QtCore import Qt

import os


def conver2Qimage(img):
    height, width, channel = img.shape
    return QImage(img, width, height, width * channel, QImage.Format_RGB888)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 加载模型
        self.model = torch.hub.load('../', 'custom', '../best.pt', source='local')
        self.initUI()

    def initUI(self):
        font = QFont()
        font.setFamily("三极泼墨体")
        font.setPointSize(15)
        self.setWindowTitle('YoloV5 汽车检测')
        self.setGeometry(200, 200, 800, 400)

        """
        Qlabel属性设置
        """

        self.origin_label = QLabel('原始图片/视频', self)
        self.result_label = QLabel('检测结果', self)
        self.origin_label.setFixedSize(500, 500)
        self.result_label.setFixedSize(500, 500)
        self.speed1_label = QLabel('Inference:', self)
        self.speed_label = QLabel(self)
        self.speed1_label.setFixedSize(100, 50)
        self.speed_label.setFixedSize(100, 50)
        # 设置显示区域的背景色为莫兰迪色系
        self.speed_label.setStyleSheet("background-color:#fbb957;border-radius: 10px")
        self.speed_label.setFont(font)
        self.origin_label.setStyleSheet("background-color: #68b88e")
        self.result_label.setStyleSheet("background-color: #806d9e")

        # 设置 QLabel 属性
        self.speed_label.setAlignment(Qt.AlignCenter)
        self.speed1_label.setAlignment(Qt.AlignCenter)
        self.speed1_label.setFont(font)
        self.origin_label.setAlignment(Qt.AlignCenter)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.origin_label.setFont(font)
        self.result_label.setFont(font)
        self.origin_label.setScaledContents(True)
        self.result_label.setScaledContents(True)

        """
        按钮设置
        """

        load_image_btn = QPushButton('加载图片', self)
        load_image_btn.clicked.connect(self.load_image)

        detect_image_btn = QPushButton('检测图片', self)
        detect_image_btn.clicked.connect(self.detect_image)

        load_video_btn = QPushButton('加载视频', self)
        load_video_btn.clicked.connect(self.load_video)

        detect_video_btn = QPushButton('检测视频', self)
        detect_video_btn.clicked.connect(self.detect_video)

        # 设置按钮属性
        p = QSize(100, 50)
        load_image_btn.setFixedSize(p)
        detect_image_btn.setFixedSize(p)
        load_video_btn.setFixedSize(p)
        detect_video_btn.setFixedSize(p)

        load_image_btn.setStyleSheet("border-radius: 10px;background-color:#b2cf87;margin:5px")
        detect_image_btn.setStyleSheet("border-radius: 10px;background-color:#68b88e;margin:5px")
        load_video_btn.setStyleSheet("border-radius: 10px;background-color:#b2cf87;margin:5px")
        detect_video_btn.setStyleSheet("border-radius: 10px;background-color:#68b88e;margin:5px")

        # 创建一个新的布局用于放置按钮
        button_layout = QVBoxLayout()
        button_layout.addWidget(load_image_btn)
        button_layout.addWidget(detect_image_btn)
        button_layout.addWidget(load_video_btn)
        button_layout.addWidget(detect_video_btn)

        # 设置按钮布局的对齐方式为右对齐
        button_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        # 设置参数布局
        speed_layout = QVBoxLayout()
        speed_layout.addWidget(self.speed1_label)
        speed_layout.addWidget(self.speed_label)
        speed_layout.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

        button_layout.addLayout(speed_layout)

        # 添加分割线
        line = QFrame(self)
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)

        layout = QHBoxLayout()
        layout.addWidget(self.origin_label)
        layout.addWidget(line)
        layout.addWidget(self.result_label)

        # 将按钮布局添加到右侧布局
        layout.addLayout(button_layout)
        # 添加速度显示label
        layout.addLayout(speed_layout)

        self.setLayout(layout)

        # 添加定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_video_frame)

        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.update_detect_video)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Image Files (*.jpg *.png *.jpeg)")
        if file_path:
            # 设置检测图片路径为当前图片路径
            self.detect_image_path = file_path
            pixmap = QPixmap(file_path)
            self.origin_label.setPixmap(pixmap)

    def load_video(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择视频", "", "Video Files (*.mp4)")
        if file_path:
            self.detect_video_path = file_path
            self.cap = cv2.VideoCapture(file_path)
            self.timer.start(30)  # 设置定时器刷新间隔为30毫秒，即每秒刷新30次

    def detect_image(self):
        # 检测图片路径是否存在
        if hasattr(self, 'detect_image_path') and self.detect_image_path:
            # 显示检测结果
            result = self.model(self.detect_image_path)
            pre_img = conver2Qimage(result.render()[0])
            r = f"{result.get_time()[1]:.2f}ms"
            self.speed_label.setText(r)
            self.result_label.setPixmap(QPixmap.fromImage(pre_img))

    def detect_video(self):
        # 检测视频路径是否存在
        if hasattr(self, 'detect_video_path') and self.detect_video_path:
            # 显示检测结果
            video = cv2.VideoCapture(self.detect_video_path)
            self.timer2.start(30)

    def update_detect_video(self):
        ret, frame = self.cap.read()
        if ret:
            result = self.model(frame)
            pre_img = conver2Qimage(result.render()[0])
            r = f"{result.get_time()[1]:.2f}ms"
            self.speed_label.setText(r)
            self.result_label.setPixmap(QPixmap.fromImage(pre_img))

        else:
            self.timer2.stop()
            self.cap.release()

    def update_video_frame(self):
        ret, frame = self.cap.read()
        if ret:
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImage.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(convertToQtFormat)
            self.origin_label.setPixmap(pixmap)
        else:
            self.timer.stop()
            self.cap.release()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setObjectName("MainWindow")
    mainWindow.show()
    sys.exit(app.exec_())
