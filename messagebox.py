from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MessageBox(object):
    def setupUi(self, MessageBox):
        MessageBox.setObjectName("MessageBox")
        MessageBox.resize(300, 200)
        self.buttonBox = QtWidgets.QDialogButtonBox(MessageBox)
        self.buttonBox.setGeometry(QtCore.QRect(220, 170, 151, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(MessageBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 141))
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setObjectName("label")
        self.days = QtWidgets.QLineEdit(MessageBox)
        self.days.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.days.setReadOnly(True)
        self.days.setObjectName("days")

        self.retranslateUi(MessageBox)
        self.buttonBox.accepted.connect(MessageBox.accept)
        self.buttonBox.rejected.connect(MessageBox.reject)
        QtCore.QMetaObject.connectSlotsByName(MessageBox)

    def retranslateUi(self, MessageBox):
        _translate = QtCore.QCoreApplication.translate
        MessageBox.setWindowTitle(_translate("MessageBox", "Dialog"))
        self.label.setText(_translate("MessageBox", "# 提示\n"
"## 您选择的第几天：\n"
"## 请先输入验证码（如有）后\n"
"## 选择座位后点击OK。"))
        self.days.setText(_translate("MessageBox", "1"))
