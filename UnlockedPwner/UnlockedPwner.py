from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from time import *
import sys

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)
    def __init__(self, ):
        super().__init__()
        self.color_list = ["yellow", "blue", "green", "red"]

    def run(self):
        count = 0
        while True:
            sleep(0.1)
            print(self.color_list[count])
            self.progress.emit(self.color_list[count])
            count = (count+1) % 4
        self.finished.emit()
  
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Python ")        
        self.setWindowFlags(Qt.FramelessWindowHint)

        #self.wlayout = QHBoxLayout()
        #self.setLayout(self.wlayout)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.runLong()

    def runLong(self):

        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.changeBackground)
        self.thread.start()

    def changeBackground(self, color):
        self.setStyleSheet("background-color: " + color + ";")
        #self.label.setText(color)
  
    # method for widgets
    def UiComponents(self):
        
  
        # creating label
        self.label = QLabel("Verrouille ton PC", self)
        self.label.setFont(QFont('Times', 30))
        self.label.resize(410, 60)
        p = self.frameGeometry().center() - QRect(QPoint(), self.label.sizeHint()).center()
        self.label.move(p)
        # adding border to label
        self.label.setStyleSheet("border : 2px solid black")

        #self.layout.addWidget(self.label)
        
        self.showMaximized()
  
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
window.show()
  
# start the app
sys.exit(App.exec())