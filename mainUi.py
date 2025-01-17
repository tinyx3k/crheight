# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 383)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("qrc/bird.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 691, 381))
        self.stackedWidget.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(20, 0, 321, 81))
        self.label.setStyleSheet("font: 40pt \\\"MS Shell Dlg 2\\\";\n"
"")
        self.label.setObjectName("label")
        self.labelHight = QtWidgets.QLabel(self.page)
        self.labelHight.setGeometry(QtCore.QRect(40, 200, 231, 41))
        self.labelHight.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\";")
        self.labelHight.setObjectName("labelHight")
        self.checkBoy = QtWidgets.QCheckBox(self.page)
        self.checkBoy.setGeometry(QtCore.QRect(290, 160, 70, 17))
        self.checkBoy.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\"")
        self.checkBoy.setObjectName("checkBoy")
        self.checkGirl = QtWidgets.QCheckBox(self.page)
        self.checkGirl.setGeometry(QtCore.QRect(380, 160, 70, 17))
        self.checkGirl.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\"")
        self.checkGirl.setObjectName("checkGirl")
        self.checkGay = QtWidgets.QCheckBox(self.page)
        self.checkGay.setGeometry(QtCore.QRect(460, 160, 81, 17))
        self.checkGay.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\"")
        self.checkGay.setObjectName("checkGay")
        self.labelSex = QtWidgets.QLabel(self.page)
        self.labelSex.setGeometry(QtCore.QRect(40, 150, 221, 41))
        self.labelSex.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\";")
        self.labelSex.setObjectName("labelSex")
        self.labelName = QtWidgets.QLabel(self.page)
        self.labelName.setGeometry(QtCore.QRect(40, 90, 231, 41))
        self.labelName.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\";")
        self.labelName.setObjectName("labelName")
        self.comboCung = QtWidgets.QComboBox(self.page)
        self.comboCung.setGeometry(QtCore.QRect(290, 270, 251, 51))
        self.comboCung.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\"")
        self.comboCung.setObjectName("comboCung")
        self.comboCung.addItem("")
        self.comboCung.addItem("")
        self.comboCung.addItem("")
        self.comboCung.addItem("")
        self.comboCung.addItem("")
        self.comboCung.addItem("")
        self.comboCung.addItem("")
        self.comboCung.addItem("")
        self.comboCung.addItem("")
        self.comboCung.addItem("")
        self.comboCung.addItem("")
        self.comboCung.addItem("")
        self.labelCung = QtWidgets.QLabel(self.page)
        self.labelCung.setGeometry(QtCore.QRect(40, 270, 231, 41))
        self.labelCung.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\";")
        self.labelCung.setObjectName("labelCung")
        self.checkRobot = QtWidgets.QCheckBox(self.page)
        self.checkRobot.setGeometry(QtCore.QRect(120, 350, 231, 31))
        self.checkRobot.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\"")
        self.checkRobot.setObjectName("checkRobot")
        self.btnStart = QtWidgets.QPushButton(self.page)
        self.btnStart.setGeometry(QtCore.QRect(600, 90, 51, 51))
        self.btnStart.setStyleSheet("border: 0px;")
        self.btnStart.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("qrc/start.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnStart.setIcon(icon1)
        self.btnStart.setIconSize(QtCore.QSize(50, 50))
        self.btnStart.setObjectName("btnStart")
        self.btnSetting = QtWidgets.QPushButton(self.page)
        self.btnSetting.setGeometry(QtCore.QRect(600, 180, 51, 51))
        self.btnSetting.setStyleSheet("border: 0px;")
        self.btnSetting.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("qrc/setting.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSetting.setIcon(icon2)
        self.btnSetting.setIconSize(QtCore.QSize(50, 50))
        self.btnSetting.setObjectName("btnSetting")
        self.btnAbout = QtWidgets.QPushButton(self.page)
        self.btnAbout.setGeometry(QtCore.QRect(600, 270, 51, 51))
        self.btnAbout.setStyleSheet("border: 0px;")
        self.btnAbout.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("qrc/about.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnAbout.setIcon(icon3)
        self.btnAbout.setIconSize(QtCore.QSize(50, 50))
        self.btnAbout.setObjectName("btnAbout")
        self.inputHeight = QtWidgets.QPlainTextEdit(self.page)
        self.inputHeight.setGeometry(QtCore.QRect(290, 200, 251, 41))
        self.inputHeight.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\";")
        self.inputHeight.setObjectName("inputHeight")
        self.inputName = QtWidgets.QLineEdit(self.page)
        self.inputName.setGeometry(QtCore.QRect(290, 90, 251, 41))
        self.inputName.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\";")
        self.inputName.setObjectName("inputName")
        self.stackedWidget.addWidget(self.page)
        self.pageSetting = QtWidgets.QWidget()
        self.pageSetting.setObjectName("pageSetting")
        self.comboUnit = QtWidgets.QComboBox(self.pageSetting)
        self.comboUnit.setGeometry(QtCore.QRect(230, 110, 181, 41))
        self.comboUnit.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\"")
        self.comboUnit.setObjectName("comboUnit")
        self.comboUnit.addItem("")
        self.comboUnit.addItem("")
        self.comboUnit.addItem("")
        self.comboUnit.addItem("")
        self.comboUnit.addItem("")
        self.labelUnit = QtWidgets.QLabel(self.pageSetting)
        self.labelUnit.setGeometry(QtCore.QRect(120, 110, 81, 41))
        self.labelUnit.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\";")
        self.labelUnit.setObjectName("labelUnit")
        self.labelSetting = QtWidgets.QLabel(self.pageSetting)
        self.labelSetting.setGeometry(QtCore.QRect(50, 10, 321, 81))
        self.labelSetting.setStyleSheet("font: 40pt \\\"MS Shell Dlg 2\\\";\n"
"")
        self.labelSetting.setObjectName("labelSetting")
        self.btnUpdate = QtWidgets.QPushButton(self.pageSetting)
        self.btnUpdate.setGeometry(QtCore.QRect(420, 340, 161, 31))
        self.btnUpdate.setStyleSheet("QPushButton{color: rgb(56, 56, 56);background-color: rgb(255, 255, 155);border: 1px soild grey;border-radius: 5px;font: 14pt \\\"MS Shell Dlg 2\\\"}QPushButton:hover{background-color: rgb(255, 255, 105)}")
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnDele = QtWidgets.QPushButton(self.pageSetting)
        self.btnDele.setGeometry(QtCore.QRect(260, 340, 141, 31))
        self.btnDele.setStyleSheet("QPushButton{color: rgb(56, 56, 56);background-color: rgb(255, 255, 155);border: 1px soild grey;border-radius: 5px;font: 14pt \\\"MS Shell Dlg 2\\\"}QPushButton:hover{background-color: rgb(255, 255, 105)}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("qrc/dele.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnDele.setIcon(icon4)
        self.btnDele.setIconSize(QtCore.QSize(24, 24))
        self.btnDele.setObjectName("btnDele")
        self.labelAI = QtWidgets.QLabel(self.pageSetting)
        self.labelAI.setGeometry(QtCore.QRect(120, 180, 81, 41))
        self.labelAI.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\";")
        self.labelAI.setObjectName("labelAI")
        self.comboAI = QtWidgets.QComboBox(self.pageSetting)
        self.comboAI.setGeometry(QtCore.QRect(230, 180, 181, 41))
        self.comboAI.setStyleSheet("font: 16pt \\\"MS Shell Dlg 2\\\"")
        self.comboAI.setObjectName("comboAI")
        self.comboAI.addItem("")
        self.comboAI.addItem("")
        self.comboAI.addItem("")
        self.comboAI.addItem("")
        self.comboAI.addItem("")
        self.stackedWidget.addWidget(self.pageSetting)
        self.pageAbout = QtWidgets.QWidget()
        self.pageAbout.setObjectName("pageAbout")
        self.about = QtWidgets.QTextBrowser(self.pageAbout)
        self.about.setGeometry(QtCore.QRect(10, 20, 671, 351))
        self.about.setObjectName("about")
        self.stackedWidget.addWidget(self.pageAbout)
        self.pageProcess = QtWidgets.QWidget()
        self.pageProcess.setObjectName("pageProcess")
        self.process = QtWidgets.QLabel(self.pageProcess)
        self.process.setGeometry(QtCore.QRect(140, 70, 471, 81))
        self.process.setStyleSheet("font: 40pt \\\"MS Shell Dlg 2\\\";\n"
"")
        self.process.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.process.setObjectName("process")
        self.labelDark = QtWidgets.QLabel(self.pageProcess)
        self.labelDark.setGeometry(QtCore.QRect(190, 180, 381, 41))
        self.labelDark.setStyleSheet("font: 20pt \\\"MS Shell Dlg 2\\\";\n"
"")
        self.labelDark.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelDark.setObjectName("labelDark")
        self.btnStop = QtWidgets.QPushButton(self.pageProcess)
        self.btnStop.setGeometry(QtCore.QRect(350, 260, 51, 51))
        self.btnStop.setStyleSheet("border: 0px;")
        self.btnStop.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("qrc/stop.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnStop.setIcon(icon5)
        self.btnStop.setIconSize(QtCore.QSize(50, 50))
        self.btnStop.setObjectName("btnStop")
        self.stackedWidget.addWidget(self.pageProcess)
        self.minkalexvina = QtWidgets.QLabel(self.centralwidget)
        self.minkalexvina.setGeometry(QtCore.QRect(610, 360, 81, 21))
        self.minkalexvina.setStyleSheet("font: 8pt \\\"MS Shell Dlg 2\\\";\n"
"")
        self.minkalexvina.setObjectName("minkalexvina")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(30, 330, 141, 41))
        self.btnBack.setStyleSheet("QPushButton{color: rgb(56, 56, 56);background-color: rgb(255, 255, 155);border: 1px soild grey;border-radius: 5px;font: 28pt \\\"MS Shell Dlg 2\\\"}QPushButton:hover{background-color: rgb(255, 255, 105)}")
        self.btnBack.setIcon(icon)
        self.btnBack.setIconSize(QtCore.QSize(40, 40))
        self.btnBack.setObjectName("btnBack")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crush Height"))
        self.label.setText(_translate("MainWindow", "Chiều cao ny"))
        self.labelHight.setText(_translate("MainWindow", "Nhập chiều cao của bạn"))
        self.checkBoy.setText(_translate("MainWindow", "Nam"))
        self.checkGirl.setText(_translate("MainWindow", "Nữ"))
        self.checkGay.setText(_translate("MainWindow", "Bê đê"))
        self.labelSex.setText(_translate("MainWindow", "Giới tính"))
        self.labelName.setText(_translate("MainWindow", "Họ và tên"))
        self.comboCung.setItemText(0, _translate("MainWindow", "BẠCH DƯƠNG\n"
"(21/3-20/4)"))
        self.comboCung.setItemText(1, _translate("MainWindow", "KIM NGƯU\n"
"(21/4-20/5)"))
        self.comboCung.setItemText(2, _translate("MainWindow", "SONG TỬ\n"
"(21/5-21/6)"))
        self.comboCung.setItemText(3, _translate("MainWindow", "CỰ GIẢI\n"
"(22/6-22/7)"))
        self.comboCung.setItemText(4, _translate("MainWindow", "SƯ TỬ\n"
"(23/7-22/8)"))
        self.comboCung.setItemText(5, _translate("MainWindow", "XỬ NỮ\n"
"(23/8-22/9)"))
        self.comboCung.setItemText(6, _translate("MainWindow", "THIÊN BÌNH\n"
"(23/9-23/10)"))
        self.comboCung.setItemText(7, _translate("MainWindow", "BỌ CẠP\n"
"(24/10-22/11)"))
        self.comboCung.setItemText(8, _translate("MainWindow", "NHÂN MÃ\n"
"(23/11-21/12)"))
        self.comboCung.setItemText(9, _translate("MainWindow", "MA KẾT\n"
"(22/12-19/1)"))
        self.comboCung.setItemText(10, _translate("MainWindow", "BẢO BÌNH\n"
"(20/1-18/2)"))
        self.comboCung.setItemText(11, _translate("MainWindow", "SONG NGƯ\n"
"(19/2-20/3)"))
        self.labelCung.setText(_translate("MainWindow", "Cung"))
        self.checkRobot.setText(_translate("MainWindow", "Tôi hem phải Robot"))
        self.inputHeight.setPlaceholderText(_translate("MainWindow", "Đơn vị: mét. VD: 1.73"))
        self.comboUnit.setItemText(0, _translate("MainWindow", "mét"))
        self.comboUnit.setItemText(1, _translate("MainWindow", "đề-xi-mét"))
        self.comboUnit.setItemText(2, _translate("MainWindow", "feet"))
        self.comboUnit.setItemText(3, _translate("MainWindow", "cen-ti-mét"))
        self.comboUnit.setItemText(4, _translate("MainWindow", "mi-li-mét"))
        self.labelUnit.setText(_translate("MainWindow", "Đơn vị"))
        self.labelSetting.setText(_translate("MainWindow", "Cài đặt"))
        self.btnUpdate.setText(_translate("MainWindow", "Kiểm tra cập nhật"))
        self.btnDele.setText(_translate("MainWindow", "Xoá dữ liệu"))
        self.labelAI.setText(_translate("MainWindow", "Chọn AI"))
        self.comboAI.setItemText(0, _translate("MainWindow", "Anna"))
        self.comboAI.setItemText(1, _translate("MainWindow", "Lisa"))
        self.comboAI.setItemText(2, _translate("MainWindow", "Rose"))
        self.comboAI.setItemText(3, _translate("MainWindow", "Ngô Khá"))
        self.comboAI.setItemText(4, _translate("MainWindow", "Huấn"))
        self.about.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Crush Height</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto Light\'; font-size:8pt;\">Copyright ©2021 Crush Height _ MINK</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Ứng dụng dự đoán chiều cao ny bằng AI</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Cách sử dụng: Nhập thông tin về bản thân và để việc còn lại cho AI.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">*Lưu ý: Kết quả có thể không chính xác 100% như bài Tarot</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Follow my Youtube: </span><a href=\"https://www.youtube.com/c/minkalexvina/\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">https://www.youtube.com/c/minkalexvina/</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Follow my Facebook: </span><a href=\"https://www.facebook.com/minkalexvina/\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">https://www.facebook.com/minkalexvina/</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Follow my Instagram: </span><a href=\"https://www.instagram.com/minkalexvina/\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">https://www.instagram.com/minkalexvina/</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Thank you for using my program :&gt;</span></p></body></html>"))
        self.process.setText(_translate("MainWindow", "Processing..."))
        self.labelDark.setText(_translate("MainWindow", "Chờ đợi là hạnh phúc"))
        self.minkalexvina.setText(_translate("MainWindow", "@minkalexvina"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
