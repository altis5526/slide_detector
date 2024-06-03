from PyQt6.QtWidgets import QMessageBox, QListView, QLabel, QApplication, QWidget, QMainWindow, QPushButton, QFileDialog
from PyQt6 import QtCore, uic
from PyQt6.QtCore import QObject, pyqtSignal, QThread
import cv2
# Only needed for access to command line arguments
import sys
from utils.detector import Detector
import os
import ssl
from pytube import YouTube
import requests

class Second(QWidget):
    def __init__(self):
        super(Second, self).__init__()
        ssl._create_default_https_context = ssl._create_stdlib_context
        # ui_file_path = os.path.join(sys._MEIPASS, 'second_page.ui')
        ui_file_path = "./second_page.ui"
        uic.loadUi(ui_file_path, self)
        self.LoadButton.clicked.connect(lambda: self.open("load"))
        self.ChooseOutputButton.clicked.connect(lambda: self.open("output"))

        self.output = "./output"

    def open(self, method):
        if method == "load":
            if self.URLEdit.text():
                if self.check_video_url(self.URLEdit.text()):
                    self.worker = DownloadWorker(self.URLEdit.text(), self.output)
                    self.thread = QThread()
                    self.worker.moveToThread(self.thread)
                    self.worker.start.connect(self.downloading_display)
                    self.worker.finished.connect(self.thread.quit)
                    self.worker.finished_download.connect(self.finished_display)

                    self.thread.started.connect(self.worker.download)
                    self.thread.start()
                    self.Download_status.setText("Download Status: Finished")
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Icon.Critical)
                    msg.setText("Error")
                    msg.setInformativeText('Is this a valid Youtube URL?')
                    msg.setWindowTitle("Error")
                    msg.exec()
            
        elif method == "output":
            filename = QFileDialog.getExistingDirectory(self, 'Open File', '.')
            self.output_text.setText("Output directory: " + filename)
            self.output = filename

    def check_video_url(self, video_url):
        common_code = video_url.split("=")[0]
        if common_code == "https://www.youtube.com/watch?v":
            return True
        else:
            return False
    
    def downloading_display(self):
        self.Download_status.setText("Download Status: Downloading")
    
    def finished_display(self):
        self.Download_status.setText("Download Status: Finished")

class DownloadWorker(QObject):
    start = pyqtSignal()
    finished = pyqtSignal()
    finished_download = pyqtSignal()
    
    def __init__(self, url, output_path):
        super(DownloadWorker, self).__init__()
        self.url = url
        self.output_path = output_path
    
    def download(self):
        self.start.emit()
        yt = YouTube(self.url)
        yt.streams.filter().get_highest_resolution().download(self.output_path)
        self.finished.emit()
        self.finished_download.emit()
