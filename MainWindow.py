# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(279, 506)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/images/Upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = ListBoxWidget(self.tab)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line.setFont(font)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 3)
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 80))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 3)
        self.pushButton_select = QtWidgets.QPushButton(self.tab)
        self.pushButton_select.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_select.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 5px;  /* Assuming height is 40px for a perfect circle. Adjust if necessary */\n"
"    background-color: #F0FFF0;  /* Light Gray. Change as needed */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#DBF9DB    ;  /* Slightly darker gray on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DBF9DB    ;  /* Slightly darker gray when pressed, same as hover */\n"
"}")
        self.pushButton_select.setObjectName("pushButton_select")
        self.gridLayout.addWidget(self.pushButton_select, 4, 0, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.tab)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_clear.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 5px;  /* Assuming height is 40px for a perfect circle. Adjust if necessary */\n"
"    background-color: #FFA07A;  /* Light Gray. Change as needed */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#F9966B    ;  /* Slightly darker gray on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #F9966B    ;  /* Slightly darker gray when pressed, same as hover */\n"
"}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 4, 1, 1, 1)
        self.pushButton_submit = QtWidgets.QPushButton(self.tab)
        self.pushButton_submit.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_submit.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 5px;  /* Assuming height is 40px for a perfect circle. Adjust if necessary */\n"
"    background-color: #82CAFF;  /* Light Gray. Change as needed */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:#79BAEC;  /* Slightly darker gray on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #79BAEC;  /* Slightly darker gray when pressed, same as hover */\n"
"}")
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.gridLayout.addWidget(self.pushButton_submit, 4, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_url = QtWidgets.QLabel(self.tab_2)
        self.label_url.setMinimumSize(QtCore.QSize(60, 0))
        self.label_url.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_url.setObjectName("label_url")
        self.horizontalLayout_3.addWidget(self.label_url)
        self.lineEdit_url = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.horizontalLayout_3.addWidget(self.lineEdit_url)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setMinimumSize(QtCore.QSize(65, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_secretKey = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_secretKey.setObjectName("lineEdit_secretKey")
        self.horizontalLayout_2.addWidget(self.lineEdit_secretKey)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_3.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_bucketName = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_bucketName.setObjectName("lineEdit_bucketName")
        self.horizontalLayout.addWidget(self.lineEdit_bucketName)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 316, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 279, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "S3 File Uploader"))
        self.checkBox.setText(_translate("MainWindow", "SBL Daily File"))
        self.pushButton_select.setText(_translate("MainWindow", "Select Files"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear list"))
        self.pushButton_submit.setText(_translate("MainWindow", "Upload"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "File"))
        self.label_url.setText(_translate("MainWindow", "S3 UR:"))
        self.label_2.setText(_translate("MainWindow", "Secerate Key:"))
        self.label_3.setText(_translate("MainWindow", "Bucekt Name:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Setting"))
from ListBoxWidget import ListBoxWidget
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
