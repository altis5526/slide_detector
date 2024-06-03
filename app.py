from PyQt6.QtWidgets import QVBoxLayout, QStackedWidget, QListView, QLabel, QApplication, QWidget, QMainWindow, QPushButton, QFileDialog
from PyQt6.QtGui import QImage, QPixmap, QIcon
from PyQt6 import QtCore, uic
from PyQt6.QtCore import QObject, pyqtSignal, QThread
import cv2
# Only needed for access to command line arguments
import sys
from utils.detector import Detector
from pptx import Presentation
from pptx.util import Inches
import os
from first import First
from second import Second

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # ui_file_path = os.path.join(sys._MEIPASS, 'app_design.ui')
        ui_file_path = "./app_design.ui"

        self.setWindowTitle("My App")
        uic.loadUi(ui_file_path, self)

        self.first = First()
        self.stackedWidget.addWidget(self.first)
        self.first.youtubepage_button.clicked.connect(self.gotoSecond)
        self.second = Second()
        self.stackedWidget.addWidget(self.second)
        self.second.back_button.clicked.connect(self.gotoFirst)

        # self.central_widget = QWidget()
        # main_layout = QVBoxLayout(self.central_widget)
        # main_layout.addWidget(self.stackedWidget)

    def gotoFirst(self):
        self.stackedWidget.setCurrentIndex(0)

    def gotoSecond(self):
        self.stackedWidget.setCurrentIndex(1)


    
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # icon_file_path = os.path.join(sys._MEIPASS, 'icon.png')
    # app_icon = QIcon(icon_file_path)
    # app.setWindowIcon(app_icon)

    # Create a Qt widget, which will be our window.
    window = MainWindow()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()
