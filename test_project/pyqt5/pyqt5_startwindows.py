# -*- coding: utf-8 -*-

#@version:1.0.1
# Created by: Python3.9.6
#@author:鹄思鹄想bit森
# WARNING: run again.  Do not edit this file unless you know what you are doing.
# @Time    : 2021/8/2 0002 上午 11:19
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,QDateTime
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.resize(1098, 842)    #设置可视化界面长1098，宽842
        self.label_100 = QtWidgets.QLabel(Form)  #Ui界面里创建一个可视化界面label_100
        self.label_100.setGeometry(QtCore.QRect(410, 0, 360, 41))  #label_100里面设置框的大小为左右410，上下0,宽360,高41
        self.Timer=QTimer()     #自定义QTimer
        self.Timer.start(500)   #每0.5秒运行一次
        self.Timer.timeout.connect(self.updateTime)   #连接updateTime
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def updateTime(self):
        self.label_100.setText(QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss dddd'))         #显示时间的格式
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
