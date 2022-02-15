from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from mainUi import *

import sys
import random

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.widgets = self.ui
        self.msg = QMessageBox()
        self.msg.setWindowIcon(QIcon("qrc/bird.png"))
        self.msg.setWindowTitle("Nhờn")
        self.widgets.btnBack.hide()
        self.widgets.btnBack.clicked.connect(lambda: (self.widgets.stackedWidget.setCurrentIndex(0), self.widgets.btnBack.hide()))
        self.widgets.btnSetting.clicked.connect(lambda: (self.widgets.stackedWidget.setCurrentIndex(1), self.widgets.btnBack.show()))
        self.widgets.btnAbout.clicked.connect(lambda: (self.widgets.stackedWidget.setCurrentIndex(2), self.widgets.btnBack.show()))
        self.widgets.btnStart.clicked.connect(self.btnStart_active)
        self.widgets.btnUpdate.clicked.connect(lambda: (self.msg.setText("Không có bản cập nhật nào mới!"), self.msg.exec()))
        self.widgets.btnDele.clicked.connect(lambda: (self.msg.setText("Xoá dữ liệu cũng như xoá đi những kỉ niệm!"), self.msg.exec()))

    def btnStart_active(self):
        if self.widgets.inputHeight.toPlainText() == '':
            self.msg.setText("Không được để trống")
            self.msg.exec()
            return
        if float(self.widgets.inputHeight.toPlainText())<1 or float(self.widgets.inputHeight.toPlainText())>3:
            self.msg.setText("Ảdu chiều cao dảk wá")
            self.msg.exec()
            return
        if not self.widgets.checkRobot.isChecked():
            self.msg.setText("Ảdu u are Robot")
            self.msg.exec()
            return
        self.widgets.stackedWidget.setCurrentIndex(3)
        self.widgets.process.setText("Processing...")
        self.widgets.labelDark.setText("Chờ đợi là hạnh phúc")
        self.widgets.btnStop.show()
        self.timer = QTimer()
        self.timer.timeout.connect(self.done)
        self.timer.start(random.randint(1000,3000))

    def done(self):
        self.widgets.btnBack.show()
        haha = random.randint(0,9)
        if haha in [0,1,2]:
            self.widgets.process.setText(f"Hahahaha mày ế =))")
        else:
            height = random.randint(70,205)
            if self.widgets.comboUnit.currentText() == "mét":
                height/=100
            elif self.widgets.comboUnit.currentText() == "đề-xi-mét":
                height/=10
            elif self.widgets.comboUnit.currentText() == "feet":
                height*=0.0328
            elif self.widgets.comboUnit.currentText() == "mi-li-mét":
                height*=10
            self.widgets.process.setText(f"{height:.2f} {self.widgets.comboUnit.currentText()}")
        self.widgets.labelDark.setText("Done")
        self.widgets.btnStop.hide()
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
