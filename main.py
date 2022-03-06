import os
import os.path
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import Thread

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(160, 105)
        icon = QIcon()
        icon.addPixmap(QPixmap("logo.png"), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget {\n"
"max-width: 160px;\n"
"max-height: 110px;\n"
"}\n"
"* { \n"
"    background-color: rgb(0, 0, 0); \n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton {\n"
"   background-color: #fff;\n"
"   color: black;\n"
"   border: 2px solid transparent;\n"
"}\n"
"\n"
"")
        self.start = QPushButton(Form)
        self.start.setGeometry(QRect(20, 20, 121, 31))
        self.start.setStyleSheet("#start {\n"
"    background-color: rgb(67, 202, 0);\n"
"    color: rgb(255, 255, 255);  \n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.start.setObjectName("start")
        self.start.clicked.connect(self.starter)


        self.stop = QPushButton(Form)
        self.stop.setGeometry(QRect(20, 60, 121, 31))
        self.stop.setStyleSheet("#stop {\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.stop.setObjectName("stop")
        self.stop.clicked.connect(self.stopper)


        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OOO"))
        self.start.setText(_translate("Form", "Start"))
        self.stop.setText(_translate("Form", "Stop"))

    def sta(self):
            import onoroff
            print("stated")
    def starter(self):
        open("run.run", "w+")
        p = Thread(target=self.sta)
        p.start()
        print("continuing")
 
    def stopper(self):
        if os.path.isfile("run.run"):
             os.remove("run.run")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
