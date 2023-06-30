from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.url = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(10, 100, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.url.setFont(font)
        self.url.setObjectName("url")
        self.getticket = QtWidgets.QPushButton(self.centralwidget)
        self.getticket.setGeometry(QtCore.QRect(310, 440, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.getticket.setFont(font)
        self.getticket.setObjectName("getticket")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.account = QtWidgets.QLineEdit(self.centralwidget)
        self.account.setGeometry(QtCore.QRect(50, 180, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.account.setFont(font)
        self.account.setMaxLength(256)
        self.account.setObjectName("account")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(50, 210, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.password.setFont(font)
        self.password.setInputMask("")
        self.password.setMaxLength(32767)
        self.password.setObjectName("password")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 390, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.card1 = QtWidgets.QLineEdit(self.centralwidget)
        self.card1.setGeometry(QtCore.QRect(70, 390, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.card1.setFont(font)
        self.card1.setText("")
        self.card1.setMaxLength(4)
        self.card1.setObjectName("card1")
        self.save_config = QtWidgets.QPushButton(self.centralwidget)
        self.save_config.setGeometry(QtCore.QRect(310, 410, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.save_config.setFont(font)
        self.save_config.setObjectName("save_config")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 390, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.card2 = QtWidgets.QLineEdit(self.centralwidget)
        self.card2.setGeometry(QtCore.QRect(120, 390, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.card2.setFont(font)
        self.card2.setText("")
        self.card2.setMaxLength(4)
        self.card2.setObjectName("card2")
        self.card3 = QtWidgets.QLineEdit(self.centralwidget)
        self.card3.setGeometry(QtCore.QRect(170, 390, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.card3.setFont(font)
        self.card3.setText("")
        self.card3.setMaxLength(4)
        self.card3.setObjectName("card3")
        self.card4 = QtWidgets.QLineEdit(self.centralwidget)
        self.card4.setGeometry(QtCore.QRect(220, 390, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.card4.setFont(font)
        self.card4.setInputMask("")
        self.card4.setText("")
        self.card4.setMaxLength(32767)
        self.card4.setDragEnabled(False)
        self.card4.setPlaceholderText("")
        self.card4.setClearButtonEnabled(False)
        self.card4.setObjectName("card4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 270, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.biryear = QtWidgets.QLineEdit(self.centralwidget)
        self.biryear.setGeometry(QtCore.QRect(70, 270, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.biryear.setFont(font)
        self.biryear.setText("")
        self.biryear.setMaxLength(4)
        self.biryear.setObjectName("biryear")
        self.birmouth = QtWidgets.QLineEdit(self.centralwidget)
        self.birmouth.setGeometry(QtCore.QRect(120, 270, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.birmouth.setFont(font)
        self.birmouth.setText("")
        self.birmouth.setMaxLength(2)
        self.birmouth.setObjectName("birmouth")
        self.birday = QtWidgets.QLineEdit(self.centralwidget)
        self.birday.setGeometry(QtCore.QRect(160, 270, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.birday.setFont(font)
        self.birday.setText("")
        self.birday.setMaxLength(2)
        self.birday.setObjectName("birday")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 270, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.yourname = QtWidgets.QLineEdit(self.centralwidget)
        self.yourname.setGeometry(QtCore.QRect(100, 240, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.yourname.setFont(font)
        self.yourname.setMaxLength(32)
        self.yourname.setObjectName("yourname")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 240, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 300, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.telephone = QtWidgets.QLineEdit(self.centralwidget)
        self.telephone.setGeometry(QtCore.QRect(70, 300, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.telephone.setFont(font)
        self.telephone.setMaxLength(64)
        self.telephone.setObjectName("telephone")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 420, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.card_mouth = QtWidgets.QLineEdit(self.centralwidget)
        self.card_mouth.setGeometry(QtCore.QRect(100, 420, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.card_mouth.setFont(font)
        self.card_mouth.setText("")
        self.card_mouth.setMaxLength(2)
        self.card_mouth.setFrame(True)
        self.card_mouth.setObjectName("card_mouth")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(100, 420, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.card_year = QtWidgets.QLineEdit(self.centralwidget)
        self.card_year.setGeometry(QtCore.QRect(140, 420, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.card_year.setFont(font)
        self.card_year.setText("")
        self.card_year.setMaxLength(2)
        self.card_year.setObjectName("card_year")
        self.xyk_type = QtWidgets.QComboBox(self.centralwidget)
        self.xyk_type.setGeometry(QtCore.QRect(90, 360, 301, 22))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.xyk_type.setFont(font)
        self.xyk_type.setObjectName("xyk_type")
        self.xyk_type.addItem("")
        self.xyk_type.addItem("")
        self.xyk_type.addItem("")
        self.xyk_type.addItem("")
        self.xyk_type.addItem("")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 330, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 360, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 470, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(50, 470, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.timeup_hour = QtWidgets.QLineEdit(self.centralwidget)
        self.timeup_hour.setGeometry(QtCore.QRect(50, 470, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.timeup_hour.setFont(font)
        self.timeup_hour.setText("")
        self.timeup_hour.setMaxLength(2)
        self.timeup_hour.setObjectName("timeup_hour")
        self.timeup_min = QtWidgets.QLineEdit(self.centralwidget)
        self.timeup_min.setGeometry(QtCore.QRect(90, 470, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.timeup_min.setFont(font)
        self.timeup_min.setText("")
        self.timeup_min.setMaxLength(2)
        self.timeup_min.setObjectName("timeup_min")
        self.is_open_timeup = QtWidgets.QCheckBox(self.centralwidget)
        self.is_open_timeup.setGeometry(QtCore.QRect(10, 450, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.is_open_timeup.setFont(font)
        self.is_open_timeup.setObjectName("is_open_timeup")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(170, 450, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(10, 52, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.webdriver_select = QtWidgets.QComboBox(self.centralwidget)
        self.webdriver_select.setGeometry(QtCore.QRect(150, 50, 241, 22))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.webdriver_select.setFont(font)
        self.webdriver_select.setObjectName("webdriver_select")
        self.webdriver_select.addItem("")
        self.webdriver_select.addItem("")
        self.webdriver_select.addItem("")
        self.webdriver_select.addItem("")
        self.webdriver_select.addItem("")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(10, 152, 54, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(60, 150, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.days = QtWidgets.QLineEdit(self.centralwidget)
        self.days.setGeometry(QtCore.QRect(80, 150, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.days.setFont(font)
        self.days.setObjectName("days")
        self.start_hour = QtWidgets.QLineEdit(self.centralwidget)
        self.start_hour.setGeometry(QtCore.QRect(150, 470, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.start_hour.setFont(font)
        self.start_hour.setText("")
        self.start_hour.setMaxLength(2)
        self.start_hour.setObjectName("start_hour")
        self.start_min = QtWidgets.QLineEdit(self.centralwidget)
        self.start_min.setGeometry(QtCore.QRect(190, 470, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.start_min.setFont(font)
        self.start_min.setText("")
        self.start_min.setMaxLength(2)
        self.start_min.setObjectName("start_min")
        self.start_sec = QtWidgets.QLineEdit(self.centralwidget)
        self.start_sec.setGeometry(QtCore.QRect(230, 470, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.start_sec.setFont(font)
        self.start_sec.setText("")
        self.start_sec.setMaxLength(2)
        self.start_sec.setObjectName("start_sec")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(150, 470, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.is_reload = QtWidgets.QCheckBox(self.centralwidget)
        self.is_reload.setGeometry(QtCore.QRect(50, 76, 71, 20))
        self.is_reload.setObjectName("is_reload")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(10, 500, 141, 21))
        self.label_22.setObjectName("label_22")
        self.timeout_sec = QtWidgets.QLineEdit(self.centralwidget)
        self.timeout_sec.setGeometry(QtCore.QRect(100, 500, 31, 20))
        self.timeout_sec.setMaxLength(3)
        self.timeout_sec.setObjectName("timeout_sec")
        self.label_18.raise_()
        self.label_12.raise_()
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.url.raise_()
        self.getticket.raise_()
        self.label_3.raise_()
        self.account.raise_()
        self.label_4.raise_()
        self.password.raise_()
        self.label_5.raise_()
        self.save_config.raise_()
        self.label_6.raise_()
        self.card1.raise_()
        self.card2.raise_()
        self.card3.raise_()
        self.card4.raise_()
        self.label_7.raise_()
        self.biryear.raise_()
        self.birmouth.raise_()
        self.birday.raise_()
        self.yourname.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.telephone.raise_()
        self.label_11.raise_()
        self.card_mouth.raise_()
        self.card_year.raise_()
        self.xyk_type.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.timeup_hour.raise_()
        self.timeup_min.raise_()
        self.is_open_timeup.raise_()
        self.label_17.raise_()
        self.label_19.raise_()
        self.webdriver_select.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.days.raise_()
        self.start_hour.raise_()
        self.start_min.raise_()
        self.start_sec.raise_()
        self.is_reload.raise_()
        self.label_22.raise_()
        self.timeout_sec.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.webdriver_select, self.is_reload)
        MainWindow.setTabOrder(self.is_reload, self.url)
        MainWindow.setTabOrder(self.url, self.days)
        MainWindow.setTabOrder(self.days, self.account)
        MainWindow.setTabOrder(self.account, self.password)
        MainWindow.setTabOrder(self.password, self.yourname)
        MainWindow.setTabOrder(self.yourname, self.biryear)
        MainWindow.setTabOrder(self.biryear, self.birmouth)
        MainWindow.setTabOrder(self.birmouth, self.birday)
        MainWindow.setTabOrder(self.birday, self.telephone)
        MainWindow.setTabOrder(self.telephone, self.xyk_type)
        MainWindow.setTabOrder(self.xyk_type, self.card1)
        MainWindow.setTabOrder(self.card1, self.card2)
        MainWindow.setTabOrder(self.card2, self.card3)
        MainWindow.setTabOrder(self.card3, self.card4)
        MainWindow.setTabOrder(self.card4, self.card_mouth)
        MainWindow.setTabOrder(self.card_mouth, self.card_year)
        MainWindow.setTabOrder(self.card_year, self.is_open_timeup)
        MainWindow.setTabOrder(self.is_open_timeup, self.timeup_hour)
        MainWindow.setTabOrder(self.timeup_hour, self.timeup_min)
        MainWindow.setTabOrder(self.timeup_min, self.start_hour)
        MainWindow.setTabOrder(self.start_hour, self.start_min)
        MainWindow.setTabOrder(self.start_min, self.start_sec)
        MainWindow.setTabOrder(self.start_sec, self.save_config)
        MainWindow.setTabOrder(self.save_config, self.getticket)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GlobalInterPark 抢票软件"))
        self.label.setText(_translate("MainWindow", "# GlobalInterPark 抢票软件"))
        self.label_2.setText(_translate("MainWindow", "网址："))
        self.getticket.setText(_translate("MainWindow", "开始抢票"))
        self.label_3.setText(_translate("MainWindow", "账号："))
        self.label_4.setText(_translate("MainWindow", "密码："))
        self.label_5.setText(_translate("MainWindow", "信用卡号："))
        self.save_config.setText(_translate("MainWindow", "保存配置"))
        self.label_6.setText(_translate("MainWindow", "       -       -        -"))
        self.label_7.setText(_translate("MainWindow", "出生日期："))
        self.label_8.setText(_translate("MainWindow", "       /      /"))
        self.label_9.setText(_translate("MainWindow", "名字(全英文)："))
        self.label_10.setText(_translate("MainWindow", "联系电话："))
        self.label_11.setText(_translate("MainWindow", "信用卡有效期："))
        self.label_12.setText(_translate("MainWindow", "     -"))
        self.xyk_type.setItemText(0, _translate("MainWindow", "请选择"))
        self.xyk_type.setItemText(1, _translate("MainWindow", "Visa"))
        self.xyk_type.setItemText(2, _translate("MainWindow", "Master"))
        self.xyk_type.setItemText(3, _translate("MainWindow", "JCB"))
        self.xyk_type.setItemText(4, _translate("MainWindow", "银联"))
        self.label_13.setText(_translate("MainWindow", "声明：本程序假设您用的是非韩国信用卡"))
        self.label_14.setText(_translate("MainWindow", "信用卡类型："))
        self.label_15.setText(_translate("MainWindow", "定时："))
        self.label_16.setText(_translate("MainWindow", "     :"))
        self.is_open_timeup.setText(_translate("MainWindow", "开启定时"))
        self.label_17.setText(_translate("MainWindow", "提前登录时间："))
        self.label_19.setText(_translate("MainWindow", "请选择你要用的浏览器："))
        self.webdriver_select.setItemText(0, _translate("MainWindow", "Microsoft Edge"))
        self.webdriver_select.setItemText(1, _translate("MainWindow", "Google Chrome"))
        self.webdriver_select.setItemText(2, _translate("MainWindow", "Firefox"))
        self.webdriver_select.setItemText(3, _translate("MainWindow", "Safari(不推荐使用)"))
        self.webdriver_select.setItemText(4, _translate("MainWindow", "IE(不推荐使用)"))
        self.label_20.setText(_translate("MainWindow", "场次："))
        self.label_21.setText(_translate("MainWindow", "第          天"))
        self.days.setText(_translate("MainWindow", "1"))
        self.label_18.setText(_translate("MainWindow", "     :      :"))
        self.is_reload.setText(_translate("MainWindow", "是否刷新"))
        self.label_22.setText(_translate("MainWindow", "加载超时时间：       秒"))
        self.timeout_sec.setText(_translate("MainWindow", ""))
