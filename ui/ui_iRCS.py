# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iRCSnkrHsK.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setFocusPolicy(Qt.StrongFocus)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(181, 180, 180);")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.wid_topbar = QWidget(self.centralwidget)
        self.wid_topbar.setObjectName(u"wid_topbar")
        self.wid_topbar.setGeometry(QRect(0, 0, 1920, 80))
        self.wid_topbar.setStyleSheet(u"QWidget {\n"
" background-color: rgb(238, 0, 51);\n"
"}\n"
"\n"
"QPushButton  {\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgb(236, 26, 46);\n"
"	font: 87 14pt \"Arial Black\" ;\n"
"	border:None;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color:rgb(255, 255, 255);\n"
"    background-color: rgb(236, 26, 46);\n"
"	border-bottom: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color:rgb(0, 0, 0);\n"
"    background-color: rgb(236, 26, 46); \n"
"	border-bottom: 2px solid black;\n"
"}\n"
"")
        self.label = QLabel(self.wid_topbar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(15, 15, 150, 53))
        self.label.setPixmap(QPixmap(u"resource/viettel_logo.jpg"))
        self.label.setScaledContents(True)
        self.btn_monitor = QPushButton(self.wid_topbar)
        self.btn_monitor.setObjectName(u"btn_monitor")
        self.btn_monitor.setEnabled(True)
        self.btn_monitor.setGeometry(QRect(390, 20, 190, 40))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.btn_monitor.setFont(font)
        self.btn_monitor.setFocusPolicy(Qt.NoFocus)
        self.btn_monitor.setLayoutDirection(Qt.LeftToRight)
        self.btn_monitor.setStyleSheet(u"")
        self.btn_monitor.setText(u"System Monitor")
        self.btn_monitor.setIconSize(QSize(48, 48))
        self.btn_monitor.setAutoRepeat(False)
        self.btn_monitor.setAutoDefault(False)
        self.btn_task = QPushButton(self.wid_topbar)
        self.btn_task.setObjectName(u"btn_task")
        self.btn_task.setEnabled(True)
        self.btn_task.setGeometry(QRect(590, 20, 90, 40))
        self.btn_task.setFont(font)
        self.btn_task.setLayoutDirection(Qt.LeftToRight)
        self.btn_task.setStyleSheet(u"")
        self.btn_task.setText(u"Task")
        self.btn_task.setIconSize(QSize(48, 48))
        self.btn_task.setAutoRepeat(False)
        self.btn_task.setAutoDefault(False)
        self.btn_robot = QPushButton(self.wid_topbar)
        self.btn_robot.setObjectName(u"btn_robot")
        self.btn_robot.setEnabled(True)
        self.btn_robot.setGeometry(QRect(690, 20, 90, 40))
        self.btn_robot.setFont(font)
        self.btn_robot.setLayoutDirection(Qt.LeftToRight)
        self.btn_robot.setStyleSheet(u"")
        self.btn_robot.setText(u"Robot")
        self.btn_robot.setIconSize(QSize(48, 48))
        self.btn_robot.setAutoRepeat(False)
        self.btn_robot.setAutoDefault(False)
        self.btn_alarm = QPushButton(self.wid_topbar)
        self.btn_alarm.setObjectName(u"btn_alarm")
        self.btn_alarm.setEnabled(True)
        self.btn_alarm.setGeometry(QRect(790, 20, 100, 40))
        self.btn_alarm.setFont(font)
        self.btn_alarm.setLayoutDirection(Qt.LeftToRight)
        self.btn_alarm.setStyleSheet(u"")
        self.btn_alarm.setText(u"Alarm")
        self.btn_alarm.setIconSize(QSize(48, 48))
        self.btn_alarm.setAutoRepeat(False)
        self.btn_alarm.setAutoDefault(False)
        self.btn_static = QPushButton(self.wid_topbar)
        self.btn_static.setObjectName(u"btn_static")
        self.btn_static.setEnabled(True)
        self.btn_static.setGeometry(QRect(900, 20, 111, 40))
        self.btn_static.setFont(font)
        self.btn_static.setLayoutDirection(Qt.LeftToRight)
        self.btn_static.setStyleSheet(u"")
        self.btn_static.setText(u"Static")
        self.btn_static.setIconSize(QSize(48, 48))
        self.btn_static.setAutoRepeat(False)
        self.btn_static.setAutoDefault(False)
        self.btn_operation = QPushButton(self.wid_topbar)
        self.btn_operation.setObjectName(u"btn_operation")
        self.btn_operation.setEnabled(True)
        self.btn_operation.setGeometry(QRect(1020, 20, 130, 40))
        self.btn_operation.setFont(font)
        self.btn_operation.setLayoutDirection(Qt.LeftToRight)
        self.btn_operation.setStyleSheet(u"")
        self.btn_operation.setText(u"Operation")
        self.btn_operation.setIconSize(QSize(48, 48))
        self.btn_operation.setAutoRepeat(False)
        self.btn_operation.setAutoDefault(False)
        self.lb_monitor_4 = QLabel(self.wid_topbar)
        self.lb_monitor_4.setObjectName(u"lb_monitor_4")
        self.lb_monitor_4.setGeometry(QRect(1670, 25, 241, 31))
        self.lb_monitor_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\" ;")
        self.stk_wid_menu = QStackedWidget(self.centralwidget)
        self.stk_wid_menu.setObjectName(u"stk_wid_menu")
        self.stk_wid_menu.setGeometry(QRect(5, 85, 400, 990))
        self.stk_wid_menu.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;\n"
"")
        self.menu_monitor = QWidget()
        self.menu_monitor.setObjectName(u"menu_monitor")
        self.lb_monitor_2 = QLabel(self.menu_monitor)
        self.lb_monitor_2.setObjectName(u"lb_monitor_2")
        self.lb_monitor_2.setGeometry(QRect(10, 20, 151, 31))
        self.lb_monitor_2.setStyleSheet(u"color: black;\n"
"font: 87 14pt \"Arial Black\" ;")
        self.lb_monitor_3 = QLabel(self.menu_monitor)
        self.lb_monitor_3.setObjectName(u"lb_monitor_3")
        self.lb_monitor_3.setGeometry(QRect(10, 290, 171, 31))
        self.lb_monitor_3.setStyleSheet(u"color: black;\n"
"font: 87 14pt \"Arial Black\" ;")
        self.dial = QDial(self.menu_monitor)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(10, 70, 181, 181))
        self.lb_monitor_6 = QLabel(self.menu_monitor)
        self.lb_monitor_6.setObjectName(u"lb_monitor_6")
        self.lb_monitor_6.setGeometry(QRect(10, 350, 201, 31))
        self.lb_monitor_6.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_7 = QLabel(self.menu_monitor)
        self.lb_monitor_7.setObjectName(u"lb_monitor_7")
        self.lb_monitor_7.setGeometry(QRect(10, 390, 201, 31))
        self.lb_monitor_7.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_8 = QLabel(self.menu_monitor)
        self.lb_monitor_8.setObjectName(u"lb_monitor_8")
        self.lb_monitor_8.setGeometry(QRect(10, 430, 201, 31))
        self.lb_monitor_8.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_22 = QLabel(self.menu_monitor)
        self.lb_monitor_22.setObjectName(u"lb_monitor_22")
        self.lb_monitor_22.setGeometry(QRect(10, 470, 201, 31))
        self.lb_monitor_22.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_26 = QLabel(self.menu_monitor)
        self.lb_monitor_26.setObjectName(u"lb_monitor_26")
        self.lb_monitor_26.setGeometry(QRect(10, 510, 201, 31))
        self.lb_monitor_26.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_31 = QLabel(self.menu_monitor)
        self.lb_monitor_31.setObjectName(u"lb_monitor_31")
        self.lb_monitor_31.setGeometry(QRect(220, 80, 71, 31))
        self.lb_monitor_31.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_32 = QLabel(self.menu_monitor)
        self.lb_monitor_32.setObjectName(u"lb_monitor_32")
        self.lb_monitor_32.setGeometry(QRect(310, 80, 51, 31))
        self.lb_monitor_32.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_33 = QLabel(self.menu_monitor)
        self.lb_monitor_33.setObjectName(u"lb_monitor_33")
        self.lb_monitor_33.setGeometry(QRect(220, 110, 71, 31))
        self.lb_monitor_33.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_34 = QLabel(self.menu_monitor)
        self.lb_monitor_34.setObjectName(u"lb_monitor_34")
        self.lb_monitor_34.setGeometry(QRect(310, 110, 51, 31))
        self.lb_monitor_34.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_35 = QLabel(self.menu_monitor)
        self.lb_monitor_35.setObjectName(u"lb_monitor_35")
        self.lb_monitor_35.setGeometry(QRect(220, 140, 71, 31))
        self.lb_monitor_35.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_36 = QLabel(self.menu_monitor)
        self.lb_monitor_36.setObjectName(u"lb_monitor_36")
        self.lb_monitor_36.setGeometry(QRect(310, 140, 51, 31))
        self.lb_monitor_36.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_37 = QLabel(self.menu_monitor)
        self.lb_monitor_37.setObjectName(u"lb_monitor_37")
        self.lb_monitor_37.setGeometry(QRect(220, 170, 81, 31))
        self.lb_monitor_37.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_38 = QLabel(self.menu_monitor)
        self.lb_monitor_38.setObjectName(u"lb_monitor_38")
        self.lb_monitor_38.setGeometry(QRect(310, 170, 51, 31))
        self.lb_monitor_38.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_39 = QLabel(self.menu_monitor)
        self.lb_monitor_39.setObjectName(u"lb_monitor_39")
        self.lb_monitor_39.setGeometry(QRect(220, 200, 81, 31))
        self.lb_monitor_39.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_40 = QLabel(self.menu_monitor)
        self.lb_monitor_40.setObjectName(u"lb_monitor_40")
        self.lb_monitor_40.setGeometry(QRect(310, 200, 51, 31))
        self.lb_monitor_40.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_41 = QLabel(self.menu_monitor)
        self.lb_monitor_41.setObjectName(u"lb_monitor_41")
        self.lb_monitor_41.setGeometry(QRect(230, 310, 81, 31))
        self.lb_monitor_41.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_42 = QLabel(self.menu_monitor)
        self.lb_monitor_42.setObjectName(u"lb_monitor_42")
        self.lb_monitor_42.setGeometry(QRect(230, 350, 51, 31))
        self.lb_monitor_42.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_43 = QLabel(self.menu_monitor)
        self.lb_monitor_43.setObjectName(u"lb_monitor_43")
        self.lb_monitor_43.setGeometry(QRect(320, 310, 81, 31))
        self.lb_monitor_43.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_44 = QLabel(self.menu_monitor)
        self.lb_monitor_44.setObjectName(u"lb_monitor_44")
        self.lb_monitor_44.setGeometry(QRect(320, 350, 51, 31))
        self.lb_monitor_44.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_45 = QLabel(self.menu_monitor)
        self.lb_monitor_45.setObjectName(u"lb_monitor_45")
        self.lb_monitor_45.setGeometry(QRect(320, 390, 51, 31))
        self.lb_monitor_45.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_46 = QLabel(self.menu_monitor)
        self.lb_monitor_46.setObjectName(u"lb_monitor_46")
        self.lb_monitor_46.setGeometry(QRect(230, 390, 51, 31))
        self.lb_monitor_46.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_47 = QLabel(self.menu_monitor)
        self.lb_monitor_47.setObjectName(u"lb_monitor_47")
        self.lb_monitor_47.setGeometry(QRect(320, 430, 51, 31))
        self.lb_monitor_47.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_48 = QLabel(self.menu_monitor)
        self.lb_monitor_48.setObjectName(u"lb_monitor_48")
        self.lb_monitor_48.setGeometry(QRect(230, 430, 51, 31))
        self.lb_monitor_48.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_49 = QLabel(self.menu_monitor)
        self.lb_monitor_49.setObjectName(u"lb_monitor_49")
        self.lb_monitor_49.setGeometry(QRect(230, 470, 51, 31))
        self.lb_monitor_49.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_50 = QLabel(self.menu_monitor)
        self.lb_monitor_50.setObjectName(u"lb_monitor_50")
        self.lb_monitor_50.setGeometry(QRect(320, 470, 51, 31))
        self.lb_monitor_50.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_51 = QLabel(self.menu_monitor)
        self.lb_monitor_51.setObjectName(u"lb_monitor_51")
        self.lb_monitor_51.setGeometry(QRect(230, 510, 51, 31))
        self.lb_monitor_51.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_52 = QLabel(self.menu_monitor)
        self.lb_monitor_52.setObjectName(u"lb_monitor_52")
        self.lb_monitor_52.setGeometry(QRect(320, 510, 51, 31))
        self.lb_monitor_52.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.stk_wid_menu.addWidget(self.menu_monitor)
        self.menu_task = QWidget()
        self.menu_task.setObjectName(u"menu_task")
        self.dial_3 = QDial(self.menu_task)
        self.dial_3.setObjectName(u"dial_3")
        self.dial_3.setGeometry(QRect(20, 80, 141, 151))
        self.lb_monitor_9 = QLabel(self.menu_task)
        self.lb_monitor_9.setObjectName(u"lb_monitor_9")
        self.lb_monitor_9.setGeometry(QRect(10, 20, 151, 31))
        self.lb_monitor_9.setStyleSheet(u"color: black;\n"
"font: 87 14pt \"Arial Black\" ;")
        self.dial_4 = QDial(self.menu_task)
        self.dial_4.setObjectName(u"dial_4")
        self.dial_4.setGeometry(QRect(220, 80, 141, 151))
        self.dial_5 = QDial(self.menu_task)
        self.dial_5.setObjectName(u"dial_5")
        self.dial_5.setGeometry(QRect(20, 250, 141, 151))
        self.dial_6 = QDial(self.menu_task)
        self.dial_6.setObjectName(u"dial_6")
        self.dial_6.setGeometry(QRect(220, 250, 141, 151))
        self.stk_wid_menu.addWidget(self.menu_task)
        self.menu_robot = QWidget()
        self.menu_robot.setObjectName(u"menu_robot")
        self.lb_monitor_53 = QLabel(self.menu_robot)
        self.lb_monitor_53.setObjectName(u"lb_monitor_53")
        self.lb_monitor_53.setGeometry(QRect(20, 360, 71, 31))
        self.lb_monitor_53.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.dial_2 = QDial(self.menu_robot)
        self.dial_2.setObjectName(u"dial_2")
        self.dial_2.setGeometry(QRect(70, 50, 251, 241))
        self.lb_monitor_54 = QLabel(self.menu_robot)
        self.lb_monitor_54.setObjectName(u"lb_monitor_54")
        self.lb_monitor_54.setGeometry(QRect(110, 300, 51, 31))
        self.lb_monitor_54.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_55 = QLabel(self.menu_robot)
        self.lb_monitor_55.setObjectName(u"lb_monitor_55")
        self.lb_monitor_55.setGeometry(QRect(110, 360, 51, 31))
        self.lb_monitor_55.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_56 = QLabel(self.menu_robot)
        self.lb_monitor_56.setObjectName(u"lb_monitor_56")
        self.lb_monitor_56.setGeometry(QRect(210, 330, 81, 31))
        self.lb_monitor_56.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_57 = QLabel(self.menu_robot)
        self.lb_monitor_57.setObjectName(u"lb_monitor_57")
        self.lb_monitor_57.setGeometry(QRect(20, 330, 71, 31))
        self.lb_monitor_57.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_58 = QLabel(self.menu_robot)
        self.lb_monitor_58.setObjectName(u"lb_monitor_58")
        self.lb_monitor_58.setGeometry(QRect(300, 300, 51, 31))
        self.lb_monitor_58.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_5 = QLabel(self.menu_robot)
        self.lb_monitor_5.setObjectName(u"lb_monitor_5")
        self.lb_monitor_5.setGeometry(QRect(20, 10, 151, 31))
        self.lb_monitor_5.setStyleSheet(u"color: black;\n"
"font: 87 14pt \"Arial Black\" ;")
        self.lb_monitor_59 = QLabel(self.menu_robot)
        self.lb_monitor_59.setObjectName(u"lb_monitor_59")
        self.lb_monitor_59.setGeometry(QRect(20, 300, 71, 31))
        self.lb_monitor_59.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_60 = QLabel(self.menu_robot)
        self.lb_monitor_60.setObjectName(u"lb_monitor_60")
        self.lb_monitor_60.setGeometry(QRect(210, 300, 81, 31))
        self.lb_monitor_60.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_61 = QLabel(self.menu_robot)
        self.lb_monitor_61.setObjectName(u"lb_monitor_61")
        self.lb_monitor_61.setGeometry(QRect(110, 330, 51, 31))
        self.lb_monitor_61.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_62 = QLabel(self.menu_robot)
        self.lb_monitor_62.setObjectName(u"lb_monitor_62")
        self.lb_monitor_62.setGeometry(QRect(300, 330, 51, 31))
        self.lb_monitor_62.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_63 = QLabel(self.menu_robot)
        self.lb_monitor_63.setObjectName(u"lb_monitor_63")
        self.lb_monitor_63.setGeometry(QRect(210, 360, 81, 31))
        self.lb_monitor_63.setStyleSheet(u"color: black;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.lb_monitor_64 = QLabel(self.menu_robot)
        self.lb_monitor_64.setObjectName(u"lb_monitor_64")
        self.lb_monitor_64.setGeometry(QRect(300, 360, 51, 31))
        self.lb_monitor_64.setStyleSheet(u"color: lime;\n"
"font: 87 10pt \"Arial Black\" ;")
        self.stk_wid_menu.addWidget(self.menu_robot)
        self.menu_alarm = QWidget()
        self.menu_alarm.setObjectName(u"menu_alarm")
        self.lb_robot_6 = QLabel(self.menu_alarm)
        self.lb_robot_6.setObjectName(u"lb_robot_6")
        self.lb_robot_6.setGeometry(QRect(10, 0, 71, 31))
        self.lb_robot_6.setStyleSheet(u"color: black;\n"
"font: 87 14pt \"Arial Black\" ;")
        self.stk_wid_menu.addWidget(self.menu_alarm)
        self.menu_static = QWidget()
        self.menu_static.setObjectName(u"menu_static")
        self.lb_robot_7 = QLabel(self.menu_static)
        self.lb_robot_7.setObjectName(u"lb_robot_7")
        self.lb_robot_7.setGeometry(QRect(10, 0, 71, 31))
        self.lb_robot_7.setStyleSheet(u"color: black;\n"
"font: 87 14pt \"Arial Black\" ;")
        self.stk_wid_menu.addWidget(self.menu_static)
        self.menu_operation = QWidget()
        self.menu_operation.setObjectName(u"menu_operation")
        self.lb_robot_8 = QLabel(self.menu_operation)
        self.lb_robot_8.setObjectName(u"lb_robot_8")
        self.lb_robot_8.setGeometry(QRect(10, 0, 111, 31))
        self.lb_robot_8.setStyleSheet(u"color: black;\n"
"font: 87 14pt \"Arial Black\" ;")
        self.stk_wid_menu.addWidget(self.menu_operation)
        self.stk_wid_main = QStackedWidget(self.centralwidget)
        self.stk_wid_main.setObjectName(u"stk_wid_main")
        self.stk_wid_main.setGeometry(QRect(410, 85, 1505, 990))
        self.stk_wid_main.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;")
        self.page_monitor = QWidget()
        self.page_monitor.setObjectName(u"page_monitor")
        self.stk_wid_main.addWidget(self.page_monitor)
        self.page_robot = QWidget()
        self.page_robot.setObjectName(u"page_robot")
        self.lb_monitor_17 = QLabel(self.page_robot)
        self.lb_monitor_17.setObjectName(u"lb_monitor_17")
        self.lb_monitor_17.setGeometry(QRect(40, 40, 151, 31))
        self.lb_monitor_17.setStyleSheet(u"color: black;\n"
"font: 87 14pt \"Arial Black\" ;")
        self.stk_wid_main.addWidget(self.page_robot)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.lb_monitor_4.setText(QCoreApplication.translate("MainWindow", u"iRobot Control System", None))
        self.lb_monitor_2.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.lb_monitor_3.setText(QCoreApplication.translate("MainWindow", u"Mission State", None))
        self.lb_monitor_6.setText(QCoreApplication.translate("MainWindow", u"Storage to Pick Station", None))
        self.lb_monitor_7.setText(QCoreApplication.translate("MainWindow", u"Storage to Unload Station", None))
        self.lb_monitor_8.setText(QCoreApplication.translate("MainWindow", u"Sorting to Pack Station", None))
        self.lb_monitor_22.setText(QCoreApplication.translate("MainWindow", u"Pack Station to Buffer", None))
        self.lb_monitor_26.setText(QCoreApplication.translate("MainWindow", u"Buffer to Outbound", None))
        self.lb_monitor_31.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.lb_monitor_32.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.lb_monitor_33.setText(QCoreApplication.translate("MainWindow", u"Fail", None))
        self.lb_monitor_34.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.lb_monitor_35.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.lb_monitor_36.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.lb_monitor_37.setText(QCoreApplication.translate("MainWindow", u"Executing", None))
        self.lb_monitor_38.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.lb_monitor_39.setText(QCoreApplication.translate("MainWindow", u"Pending", None))
        self.lb_monitor_40.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.lb_monitor_41.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.lb_monitor_42.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.lb_monitor_43.setText(QCoreApplication.translate("MainWindow", u"Average", None))
        self.lb_monitor_44.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.lb_monitor_45.setText(QCoreApplication.translate("MainWindow", u"2000", None))
        self.lb_monitor_46.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.lb_monitor_47.setText(QCoreApplication.translate("MainWindow", u"3333", None))
        self.lb_monitor_48.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.lb_monitor_49.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.lb_monitor_50.setText(QCoreApplication.translate("MainWindow", u"4000", None))
        self.lb_monitor_51.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.lb_monitor_52.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.lb_monitor_9.setText(QCoreApplication.translate("MainWindow", u"Task Chart", None))
        self.lb_monitor_53.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.lb_monitor_54.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.lb_monitor_55.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lb_monitor_56.setText(QCoreApplication.translate("MainWindow", u"Charging", None))
        self.lb_monitor_57.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.lb_monitor_58.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.lb_monitor_5.setText(QCoreApplication.translate("MainWindow", u"Robot", None))
        self.lb_monitor_59.setText(QCoreApplication.translate("MainWindow", u"Online", None))
        self.lb_monitor_60.setText(QCoreApplication.translate("MainWindow", u"Tasking", None))
        self.lb_monitor_61.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.lb_monitor_62.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.lb_monitor_63.setText(QCoreApplication.translate("MainWindow", u"Idle", None))
        self.lb_monitor_64.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.lb_robot_6.setText(QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.lb_robot_7.setText(QCoreApplication.translate("MainWindow", u"Static", None))
        self.lb_robot_8.setText(QCoreApplication.translate("MainWindow", u"Operation", None))
        self.lb_monitor_17.setText(QCoreApplication.translate("MainWindow", u"Page Robot", None))
    # retranslateUi

