# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'library-management-sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1282, 676)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 248);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 100, 30))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.icons_only_widget = QWidget(self.centralwidget)
        self.icons_only_widget.setObjectName(u"icons_only_widget")
        self.icons_only_widget.setMinimumSize(QSize(60, 650))
        self.icons_only_widget.setMaximumSize(QSize(60, 650))
        self.icons_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(117, 251, 76);\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align:left;\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(117, 251, 76);\n"
"	font-weight:bold;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icons_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.user_1 = QPushButton(self.icons_only_widget)
        self.user_1.setObjectName(u"user_1")
        self.user_1.setMinimumSize(QSize(50, 50))
        self.user_1.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/icons/account_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/green_account_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.user_1.setIcon(icon)
        self.user_1.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.user_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dashboard_1 = QPushButton(self.icons_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        self.dashboard_1.setMinimumSize(QSize(40, 40))
        self.dashboard_1.setMaximumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icons/home_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/green_home_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_1.setIcon(icon1)
        self.dashboard_1.setIconSize(QSize(25, 25))
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.books_1 = QPushButton(self.icons_only_widget)
        self.books_1.setObjectName(u"books_1")
        self.books_1.setMinimumSize(QSize(40, 40))
        self.books_1.setMaximumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u":/icons/books_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/green_library_books.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.books_1.setIcon(icon2)
        self.books_1.setIconSize(QSize(25, 25))
        self.books_1.setCheckable(True)
        self.books_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.books_1)

        self.return_borrow_1 = QPushButton(self.icons_only_widget)
        self.return_borrow_1.setObjectName(u"return_borrow_1")
        self.return_borrow_1.setMinimumSize(QSize(40, 40))
        self.return_borrow_1.setMaximumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u":/icons/return_borrow_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/green_cycle_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.return_borrow_1.setIcon(icon3)
        self.return_borrow_1.setIconSize(QSize(25, 25))
        self.return_borrow_1.setCheckable(True)
        self.return_borrow_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.return_borrow_1)

        self.stats_1 = QPushButton(self.icons_only_widget)
        self.stats_1.setObjectName(u"stats_1")
        self.stats_1.setMinimumSize(QSize(40, 40))
        self.stats_1.setMaximumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(u":/icons/stats_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/green_stats_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.stats_1.setIcon(icon4)
        self.stats_1.setIconSize(QSize(25, 25))
        self.stats_1.setCheckable(True)
        self.stats_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.stats_1)

        self.settings_1 = QPushButton(self.icons_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        self.settings_1.setMinimumSize(QSize(40, 40))
        self.settings_1.setMaximumSize(QSize(40, 40))
        icon5 = QIcon()
        icon5.addFile(u":/icons/settings_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/green_settings_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_1.setIcon(icon5)
        self.settings_1.setIconSize(QSize(25, 25))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 244, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.off_1 = QPushButton(self.icons_only_widget)
        self.off_1.setObjectName(u"off_1")
        self.off_1.setMinimumSize(QSize(40, 40))
        self.off_1.setMaximumSize(QSize(40, 40))
        self.off_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon6 = QIcon()
        icon6.addFile(u":/icons/power_settings_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/green_power_settings_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.off_1.setIcon(icon6)
        self.off_1.setCheckable(True)
        self.off_1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.off_1)


        self.horizontalLayout_7.addWidget(self.icons_only_widget)

        self.icons_names_widget = QWidget(self.centralwidget)
        self.icons_names_widget.setObjectName(u"icons_names_widget")
        self.icons_names_widget.setMinimumSize(QSize(145, 650))
        self.icons_names_widget.setMaximumSize(QSize(180, 650))
        self.icons_names_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(117, 251, 76);\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align:left;\n"
"	border:none;\n"
"}\n"
"QPushButton:checked{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(117, 251, 76);\n"
"	font-weight:bold;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}")
        self.gridLayout = QGridLayout(self.icons_names_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.off_2 = QPushButton(self.icons_names_widget)
        self.off_2.setObjectName(u"off_2")
        self.off_2.setMinimumSize(QSize(120, 35))
        self.off_2.setMaximumSize(QSize(120, 35))
        font = QFont()
        font.setFamilies([u"Sitka"])
        self.off_2.setFont(font)
        self.off_2.setIcon(icon6)
        self.off_2.setCheckable(True)
        self.off_2.setAutoExclusive(True)

        self.gridLayout.addWidget(self.off_2, 3, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, -1, -1, -1)
        self.dashboard_2 = QPushButton(self.icons_names_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setMinimumSize(QSize(130, 35))
        self.dashboard_2.setMaximumSize(QSize(130, 35))
        self.dashboard_2.setFont(font)
        self.dashboard_2.setIcon(icon1)
        self.dashboard_2.setIconSize(QSize(25, 25))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.books_2 = QPushButton(self.icons_names_widget)
        self.books_2.setObjectName(u"books_2")
        self.books_2.setMinimumSize(QSize(130, 35))
        self.books_2.setMaximumSize(QSize(130, 35))
        self.books_2.setFont(font)
        self.books_2.setIcon(icon2)
        self.books_2.setIconSize(QSize(25, 25))
        self.books_2.setCheckable(True)
        self.books_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.books_2)

        self.return_borrow_2 = QPushButton(self.icons_names_widget)
        self.return_borrow_2.setObjectName(u"return_borrow_2")
        self.return_borrow_2.setMinimumSize(QSize(130, 35))
        self.return_borrow_2.setMaximumSize(QSize(130, 35))
        self.return_borrow_2.setFont(font)
        self.return_borrow_2.setIcon(icon3)
        self.return_borrow_2.setIconSize(QSize(25, 25))
        self.return_borrow_2.setCheckable(True)
        self.return_borrow_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.return_borrow_2)

        self.stats_2 = QPushButton(self.icons_names_widget)
        self.stats_2.setObjectName(u"stats_2")
        self.stats_2.setMinimumSize(QSize(130, 35))
        self.stats_2.setMaximumSize(QSize(130, 35))
        self.stats_2.setFont(font)
        self.stats_2.setIcon(icon4)
        self.stats_2.setIconSize(QSize(25, 25))
        self.stats_2.setCheckable(True)
        self.stats_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.stats_2)

        self.settings_2 = QPushButton(self.icons_names_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setMinimumSize(QSize(130, 35))
        self.settings_2.setMaximumSize(QSize(130, 35))
        self.settings_2.setFont(font)
        self.settings_2.setIcon(icon5)
        self.settings_2.setIconSize(QSize(25, 25))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 224, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.user_2 = QPushButton(self.icons_names_widget)
        self.user_2.setObjectName(u"user_2")
        self.user_2.setMinimumSize(QSize(50, 50))
        self.user_2.setMaximumSize(QSize(50, 50))
        icon7 = QIcon()
        icon7.addFile(u":/icons/account_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.user_2.setIcon(icon7)
        self.user_2.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.user_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.icons_names_widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Sitka"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.icons_names_widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        font2 = QFont()
        font2.setFamilies([u"Garamond"])
        font2.setBold(True)
        self.widget_3.setFont(font2)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 20, 621, 50))
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 80, 961, 611))
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 650))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dashboard_page1 = QWidget()
        self.dashboard_page1.setObjectName(u"dashboard_page1")
        self.label_10 = QLabel(self.dashboard_page1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 10, 273, 23))
        font3 = QFont()
        font3.setFamilies([u"Sitka"])
        font3.setPointSize(17)
        font3.setBold(True)
        self.label_10.setFont(font3)
        self.label_11 = QLabel(self.dashboard_page1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 40, 251, 25))
        font4 = QFont()
        font4.setFamilies([u"Sitka"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.label_11.setFont(font4)
        self.label_20 = QLabel(self.dashboard_page1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 70, 261, 16))
        font5 = QFont()
        font5.setFamilies([u"Sitka"])
        font5.setBold(True)
        self.label_20.setFont(font5)
        self.label_20.setStyleSheet(u"color: rgb(62, 186, 0);")
        self.dasboard_overview_widget = QWidget(self.dashboard_page1)
        self.dasboard_overview_widget.setObjectName(u"dasboard_overview_widget")
        self.dasboard_overview_widget.setGeometry(QRect(0, 100, 971, 181))
        self.dasboard_overview_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(117, 251, 76);\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	font: bold 14pt \"sitka\";\n"
"	border: none;\n"
"}\n"
"")
        self.layoutWidget2 = QWidget(self.dasboard_overview_widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(40, 19, 891, 151))
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.total_books_frame = QFrame(self.layoutWidget2)
        self.total_books_frame.setObjectName(u"total_books_frame")
        self.total_books_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.total_books_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.total_books_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 200, 26))
        self.pushButton.setMinimumSize(QSize(200, 0))
        icon8 = QIcon()
        icon8.addFile(u":/icons/books_library_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QSize(26, 26))
        self.total_books_label = QLabel(self.total_books_frame)
        self.total_books_label.setObjectName(u"total_books_label")
        self.total_books_label.setGeometry(QRect(60, 60, 101, 61))
        font6 = QFont()
        font6.setFamilies([u"Goudy Old Style"])
        font6.setPointSize(23)
        font6.setBold(True)
        self.total_books_label.setFont(font6)
        self.total_books_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(188, 0, 0);\n"
"	 border:none;\n"
"}")
        self.total_books_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.total_books_frame)

        self.available_frame = QFrame(self.layoutWidget2)
        self.available_frame.setObjectName(u"available_frame")
        self.available_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.available_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_2 = QPushButton(self.available_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 10, 200, 26))
        self.pushButton_2.setMinimumSize(QSize(200, 0))
        self.pushButton_2.setMaximumSize(QSize(200, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/icons/check_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon9)
        self.pushButton_2.setIconSize(QSize(26, 26))
        self.available_books_label = QLabel(self.available_frame)
        self.available_books_label.setObjectName(u"available_books_label")
        self.available_books_label.setGeometry(QRect(60, 60, 101, 61))
        self.available_books_label.setFont(font6)
        self.available_books_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(188, 0, 0);\n"
"	 border:none;\n"
"}")
        self.available_books_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.available_frame)

        self.borrowed_frame = QFrame(self.layoutWidget2)
        self.borrowed_frame.setObjectName(u"borrowed_frame")
        self.borrowed_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.borrowed_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_3 = QPushButton(self.borrowed_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 10, 200, 26))
        self.pushButton_3.setMinimumSize(QSize(200, 0))
        self.pushButton_3.setMaximumSize(QSize(200, 16777215))
        icon10 = QIcon()
        icon10.addFile(u":/icons/north_east_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon10)
        self.pushButton_3.setIconSize(QSize(26, 26))
        self.borrowed_books_label = QLabel(self.borrowed_frame)
        self.borrowed_books_label.setObjectName(u"borrowed_books_label")
        self.borrowed_books_label.setGeometry(QRect(60, 60, 101, 61))
        self.borrowed_books_label.setFont(font6)
        self.borrowed_books_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(188, 0, 0);\n"
"	 border:none;\n"
"}")
        self.borrowed_books_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.borrowed_frame)

        self.members_frame = QFrame(self.layoutWidget2)
        self.members_frame.setObjectName(u"members_frame")
        self.members_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.members_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_4 = QPushButton(self.members_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 10, 200, 26))
        self.pushButton_4.setMinimumSize(QSize(200, 0))
        icon11 = QIcon()
        icon11.addFile(u":/icons/members_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon11)
        self.pushButton_4.setIconSize(QSize(26, 26))
        self.total_members_label = QLabel(self.members_frame)
        self.total_members_label.setObjectName(u"total_members_label")
        self.total_members_label.setGeometry(QRect(60, 60, 101, 61))
        self.total_members_label.setFont(font6)
        self.total_members_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(188, 0, 0);\n"
"	 border:none;\n"
"}")
        self.total_members_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.members_frame)

        self.genre_dashboard_widget = QWidget(self.dashboard_page1)
        self.genre_dashboard_widget.setObjectName(u"genre_dashboard_widget")
        self.genre_dashboard_widget.setGeometry(QRect(0, 280, 961, 231))
        self.genre_dashboard_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(117, 251, 76);\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QChartView {\n"
"	background: transparent;\n"
"	border: none;\n"
"} \n"
"\n"
"QLabel{\n"
"	font: bold 11pt \"Sitka\";\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"}\n"
"")
        self.layoutWidget3 = QWidget(self.genre_dashboard_widget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(130, 10, 741, 221))
        self.horizontalLayout_17 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.trending_genres_frame = QFrame(self.layoutWidget3)
        self.trending_genres_frame.setObjectName(u"trending_genres_frame")
        self.trending_genres_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.trending_genres_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_28 = QLabel(self.trending_genres_frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(100, 10, 171, 20))
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trending_genres_bar_chart = QChartView(self.trending_genres_frame)
        self.trending_genres_bar_chart.setObjectName(u"trending_genres_bar_chart")
        self.trending_genres_bar_chart.setGeometry(QRect(10, 30, 340, 181))

        self.horizontalLayout_17.addWidget(self.trending_genres_frame)

        self.books_by_genre_frame = QFrame(self.layoutWidget3)
        self.books_by_genre_frame.setObjectName(u"books_by_genre_frame")
        self.books_by_genre_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.books_by_genre_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_29 = QLabel(self.books_by_genre_frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(100, 10, 141, 20))
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.books_by_genre_piechart = QChartView(self.books_by_genre_frame)
        self.books_by_genre_piechart.setObjectName(u"books_by_genre_piechart")
        self.books_by_genre_piechart.setGeometry(QRect(10, 30, 340, 181))

        self.horizontalLayout_17.addWidget(self.books_by_genre_frame)

        self.recent_activity_widget = QWidget(self.dashboard_page1)
        self.recent_activity_widget.setObjectName(u"recent_activity_widget")
        self.recent_activity_widget.setGeometry(QRect(-10, 510, 971, 71))
        self.recent_activity_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(117, 251, 76);\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLabel{\n"
"	font: bold 11pt \"sitka\";\n"
"	border: none;\n"
"}")
        self.recent_activity_frame = QFrame(self.recent_activity_widget)
        self.recent_activity_frame.setObjectName(u"recent_activity_frame")
        self.recent_activity_frame.setGeometry(QRect(20, 10, 951, 51))
        self.recent_activity_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.recent_activity_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_30 = QLabel(self.recent_activity_frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 10, 131, 16))
        font7 = QFont()
        font7.setFamilies([u"sitka"])
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setItalic(False)
        self.label_30.setFont(font7)
        self.stackedWidget.addWidget(self.dashboard_page1)
        self.books_page = QWidget()
        self.books_page.setObjectName(u"books_page")
        self.books_table_widget = QTableWidget(self.books_page)
        if (self.books_table_widget.columnCount() < 6):
            self.books_table_widget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.books_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.books_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.books_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.books_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.books_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.books_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.books_table_widget.setObjectName(u"books_table_widget")
        self.books_table_widget.setGeometry(QRect(-10, 230, 921, 341))
        self.books_table_widget.setFont(font)
        self.books_table_widget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: \n"
"	color: rgb(66, 199, 0);\n"
"}")
        self.books_table_widget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.books_table_widget.setAlternatingRowColors(True)
        self.books_table_widget.horizontalHeader().setMinimumSectionSize(35)
        self.books_table_widget.horizontalHeader().setDefaultSectionSize(153)
        self.books_table_widget.verticalHeader().setDefaultSectionSize(37)
        self.combobox_widget = QWidget(self.books_page)
        self.combobox_widget.setObjectName(u"combobox_widget")
        self.combobox_widget.setGeometry(QRect(10, 140, 451, 91))
        self.combobox_widget.setStyleSheet(u"\n"
"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius: 7px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color: white;\n"
"	height: 35px;\n"
"	padding-left: 3px;\n"
"}")
        self.layoutWidget4 = QWidget(self.combobox_widget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(0, 20, 441, 67))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.category_label = QLabel(self.layoutWidget4)
        self.category_label.setObjectName(u"category_label")
        font8 = QFont()
        font8.setFamilies([u"Sitka"])
        font8.setPointSize(12)
        self.category_label.setFont(font8)
        self.category_label.setStyleSheet(u"")
        self.category_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.category_label)

        self.category_combo = QComboBox(self.layoutWidget4)
        self.category_combo.addItem("")
        self.category_combo.addItem("")
        self.category_combo.setObjectName(u"category_combo")
        font9 = QFont()
        font9.setFamilies([u"Sitka"])
        font9.setPointSize(8)
        self.category_combo.setFont(font9)

        self.verticalLayout_4.addWidget(self.category_combo)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.genre_label = QLabel(self.layoutWidget4)
        self.genre_label.setObjectName(u"genre_label")
        self.genre_label.setFont(font8)
        self.genre_label.setStyleSheet(u"")
        self.genre_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.genre_label)

        self.genre_combo = QComboBox(self.layoutWidget4)
        self.genre_combo.setObjectName(u"genre_combo")
        self.genre_combo.setFont(font9)

        self.verticalLayout_6.addWidget(self.genre_combo)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.available_label = QLabel(self.layoutWidget4)
        self.available_label.setObjectName(u"available_label")
        self.available_label.setFont(font8)
        self.available_label.setStyleSheet(u"")
        self.available_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.available_label)

        self.available_combo = QComboBox(self.layoutWidget4)
        self.available_combo.addItem("")
        self.available_combo.addItem("")
        self.available_combo.setObjectName(u"available_combo")
        self.available_combo.setFont(font9)

        self.verticalLayout_5.addWidget(self.available_combo)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.widget_5 = QWidget(self.books_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(480, 180, 361, 51))
        self.layoutWidget5 = QWidget(self.widget_5)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 20, 358, 28))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.books_search = QLineEdit(self.layoutWidget5)
        self.books_search.setObjectName(u"books_search")
        self.books_search.setMinimumSize(QSize(300, 25))
        self.books_search.setMaximumSize(QSize(300, 25))
        self.books_search.setFont(font)

        self.horizontalLayout_5.addWidget(self.books_search)

        self.search_button_2 = QPushButton(self.layoutWidget5)
        self.search_button_2.setObjectName(u"search_button_2")
        self.search_button_2.setMinimumSize(QSize(50, 26))
        self.search_button_2.setMaximumSize(QSize(50, 26))
        icon12 = QIcon()
        icon12.addFile(u":/icons/search_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_button_2.setIcon(icon12)
        self.search_button_2.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.search_button_2)

        self.layoutWidget6 = QWidget(self.books_page)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(0, 10, 531, 91))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout_11.addWidget(self.label_2)

        self.label_7 = QLabel(self.layoutWidget6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: rgb(62, 186, 0);")

        self.verticalLayout_11.addWidget(self.label_8)

        self.stackedWidget.addWidget(self.books_page)
        self.borrow_return_page = QWidget()
        self.borrow_return_page.setObjectName(u"borrow_return_page")
        self.label_9 = QLabel(self.borrow_return_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1, 11, 273, 23))
        self.label_9.setFont(font3)
        self.label_18 = QLabel(self.borrow_return_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 50, 204, 16))
        font10 = QFont()
        font10.setFamilies([u"Sitka"])
        font10.setPointSize(11)
        font10.setBold(True)
        self.label_18.setFont(font10)
        self.label_19 = QLabel(self.borrow_return_page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 80, 675, 16))
        self.label_19.setFont(font5)
        self.label_19.setStyleSheet(u"color: rgb(62, 186, 0);")
        self.widget_7 = QWidget(self.borrow_return_page)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(230, 100, 371, 51))
        self.layoutWidget_4 = QWidget(self.widget_7)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 20, 358, 28))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.borrow_return_search = QLineEdit(self.layoutWidget_4)
        self.borrow_return_search.setObjectName(u"borrow_return_search")
        self.borrow_return_search.setMinimumSize(QSize(300, 25))
        self.borrow_return_search.setMaximumSize(QSize(300, 25))
        self.borrow_return_search.setFont(font)

        self.horizontalLayout_9.addWidget(self.borrow_return_search)

        self.search_button_4 = QPushButton(self.layoutWidget_4)
        self.search_button_4.setObjectName(u"search_button_4")
        self.search_button_4.setMinimumSize(QSize(50, 26))
        self.search_button_4.setMaximumSize(QSize(50, 26))
        self.search_button_4.setIcon(icon12)
        self.search_button_4.setCheckable(False)

        self.horizontalLayout_9.addWidget(self.search_button_4)

        self.borrow_return_table_widget = QTableWidget(self.borrow_return_page)
        if (self.borrow_return_table_widget.columnCount() < 6):
            self.borrow_return_table_widget.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.borrow_return_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.borrow_return_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.borrow_return_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.borrow_return_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.borrow_return_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.borrow_return_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.borrow_return_table_widget.setObjectName(u"borrow_return_table_widget")
        self.borrow_return_table_widget.setGeometry(QRect(0, 160, 911, 181))
        self.borrow_return_table_widget.setFont(font)
        self.borrow_return_table_widget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: \n"
"	color: rgb(66, 199, 0);\n"
"}")
        self.borrow_return_table_widget.setMidLineWidth(1)
        self.borrow_return_table_widget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.borrow_return_table_widget.setAlternatingRowColors(True)
        self.borrow_return_table_widget.horizontalHeader().setMinimumSectionSize(35)
        self.borrow_return_table_widget.horizontalHeader().setDefaultSectionSize(151)
        self.borrow_return_table_widget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.selected_book_frame = QFrame(self.borrow_return_page)
        self.selected_book_frame.setObjectName(u"selected_book_frame")
        self.selected_book_frame.setGeometry(QRect(150, 350, 621, 231))
        self.selected_book_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(117, 251, 76);\n"
"	border: 10px rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QWidget{\n"
"	background-color: rgb(117, 251, 76);\n"
"}\n"
"\n"
"QLabel{\n"
"	font: 12pt \"sitka\";\n"
"	color: black;\n"
"}\n"
"\n"
"QLabel#selected_book_label {\n"
"	font: bold 14pt \"sitka\";\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	font-family: \"Sitka\";\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: black;\n"
"	color: rgb(117, 251, 76);\n"
"}\n"
"QPushButton:pressed {\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color: black;\n"
"	color: rgb(117, 251, 76);\n"
"}\n"
"")
        self.selected_book_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.selected_book_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.selected_book_heading = QLabel(self.selected_book_frame)
        self.selected_book_heading.setObjectName(u"selected_book_heading")
        self.selected_book_heading.setGeometry(QRect(210, 10, 141, 20))
        self.selected_book_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_2 = QWidget(self.selected_book_frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(50, 30, 551, 191))
        self.layoutWidget7 = QWidget(self.widget_2)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(80, 10, 448, 130))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.id_label_2 = QLabel(self.layoutWidget7)
        self.id_label_2.setObjectName(u"id_label_2")

        self.verticalLayout_8.addWidget(self.id_label_2)

        self.title_label_2 = QLabel(self.layoutWidget7)
        self.title_label_2.setObjectName(u"title_label_2")

        self.verticalLayout_8.addWidget(self.title_label_2)

        self.author_label_2 = QLabel(self.layoutWidget7)
        self.author_label_2.setObjectName(u"author_label_2")

        self.verticalLayout_8.addWidget(self.author_label_2)

        self.genre_label_3 = QLabel(self.layoutWidget7)
        self.genre_label_3.setObjectName(u"genre_label_3")

        self.verticalLayout_8.addWidget(self.genre_label_3)

        self.year_label_2 = QLabel(self.layoutWidget7)
        self.year_label_2.setObjectName(u"year_label_2")

        self.verticalLayout_8.addWidget(self.year_label_2)

        self.status_label_2 = QLabel(self.layoutWidget7)
        self.status_label_2.setObjectName(u"status_label_2")

        self.verticalLayout_8.addWidget(self.status_label_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_3 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.selected_id_label = QLabel(self.layoutWidget7)
        self.selected_id_label.setObjectName(u"selected_id_label")
        self.selected_id_label.setMinimumSize(QSize(300, 16))
        self.selected_id_label.setMaximumSize(QSize(300, 16))

        self.verticalLayout_9.addWidget(self.selected_id_label)

        self.selected_title_label = QLabel(self.layoutWidget7)
        self.selected_title_label.setObjectName(u"selected_title_label")
        self.selected_title_label.setMinimumSize(QSize(300, 16))
        self.selected_title_label.setMaximumSize(QSize(300, 16))

        self.verticalLayout_9.addWidget(self.selected_title_label)

        self.selected_author_label = QLabel(self.layoutWidget7)
        self.selected_author_label.setObjectName(u"selected_author_label")
        self.selected_author_label.setMinimumSize(QSize(300, 16))
        self.selected_author_label.setMaximumSize(QSize(300, 16))

        self.verticalLayout_9.addWidget(self.selected_author_label)

        self.selected_genre_label = QLabel(self.layoutWidget7)
        self.selected_genre_label.setObjectName(u"selected_genre_label")
        self.selected_genre_label.setMinimumSize(QSize(300, 16))
        self.selected_genre_label.setMaximumSize(QSize(300, 16))

        self.verticalLayout_9.addWidget(self.selected_genre_label)

        self.selected_year_label = QLabel(self.layoutWidget7)
        self.selected_year_label.setObjectName(u"selected_year_label")
        self.selected_year_label.setMinimumSize(QSize(300, 16))
        self.selected_year_label.setMaximumSize(QSize(300, 16))

        self.verticalLayout_9.addWidget(self.selected_year_label)

        self.selected_status_label = QLabel(self.layoutWidget7)
        self.selected_status_label.setObjectName(u"selected_status_label")
        self.selected_status_label.setMinimumSize(QSize(300, 16))
        self.selected_status_label.setMaximumSize(QSize(300, 16))

        self.verticalLayout_9.addWidget(self.selected_status_label)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        self.layoutWidget8 = QWidget(self.widget_2)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(150, 150, 222, 32))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.borrow_button = QPushButton(self.layoutWidget8)
        self.borrow_button.setObjectName(u"borrow_button")
        self.borrow_button.setMinimumSize(QSize(50, 30))
        self.borrow_button.setCheckable(False)
        self.borrow_button.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.borrow_button)

        self.horizontalSpacer_4 = QSpacerItem(88, 27, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.return_button = QPushButton(self.layoutWidget8)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setMinimumSize(QSize(50, 30))
        self.return_button.setCheckable(False)
        self.return_button.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.return_button)

        self.stackedWidget.addWidget(self.borrow_return_page)
        self.stats_page = QWidget()
        self.stats_page.setObjectName(u"stats_page")
        self.label_5 = QLabel(self.stats_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 170, 49, 16))
        self.stackedWidget.addWidget(self.stats_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_6 = QLabel(self.settings_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 80, 49, 16))
        self.stackedWidget.addWidget(self.settings_page)
        self.layoutWidget9 = QWidget(self.widget_3)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(49, 20, 831, 42))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_button = QPushButton(self.layoutWidget9)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setMinimumSize(QSize(60, 40))
        self.menu_button.setMaximumSize(QSize(60, 40))
        self.menu_button.setStyleSheet(u"border: none;")
        icon13 = QIcon()
        icon13.addFile(u":/icons/menu_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_button.setIcon(icon13)
        self.menu_button.setIconSize(QSize(30, 30))
        self.menu_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.menu_button)

        self.horizontalSpacer = QSpacerItem(38, 37, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_search = QLineEdit(self.layoutWidget9)
        self.main_search.setObjectName(u"main_search")
        self.main_search.setMinimumSize(QSize(250, 25))
        self.main_search.setMaximumSize(QSize(250, 25))
        self.main_search.setFont(font)

        self.horizontalLayout.addWidget(self.main_search)

        self.search_button = QPushButton(self.layoutWidget9)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(50, 26))
        self.search_button.setMaximumSize(QSize(50, 26))
        self.search_button.setIcon(icon12)
        self.search_button.setCheckable(False)

        self.horizontalLayout.addWidget(self.search_button)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.user_3 = QPushButton(self.layoutWidget9)
        self.user_3.setObjectName(u"user_3")
        self.user_3.setMinimumSize(QSize(60, 40))
        self.user_3.setMaximumSize(QSize(60, 40))
        self.user_3.setStyleSheet(u"border: none;")
        self.user_3.setIcon(icon7)
        self.user_3.setIconSize(QSize(30, 30))
        self.user_3.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.user_3)


        self.horizontalLayout_7.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_button.toggled.connect(self.icons_only_widget.setHidden)
        self.menu_button.toggled.connect(self.icons_names_widget.setVisible)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.stats_1.toggled.connect(self.stats_2.setChecked)
        self.return_borrow_1.toggled.connect(self.return_borrow_2.setChecked)
        self.books_1.toggled.connect(self.books_2.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.books_2.toggled.connect(self.books_1.setChecked)
        self.return_borrow_2.toggled.connect(self.return_borrow_1.setChecked)
        self.stats_2.toggled.connect(self.stats_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.off_1.toggled.connect(MainWindow.close)
        self.off_2.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.user_1.setText("")
        self.dashboard_1.setText("")
        self.books_1.setText("")
        self.return_borrow_1.setText("")
        self.stats_1.setText("")
        self.settings_1.setText("")
        self.off_1.setText("")
        self.off_2.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.books_2.setText(QCoreApplication.translate("MainWindow", u"Books", None))
        self.return_borrow_2.setText(QCoreApplication.translate("MainWindow", u"Borrow/Return", None))
        self.stats_2.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.user_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"E-Library", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Welcome to E-Library ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Overview of the Library", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Total Books", None))
        self.total_books_label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Available", None))
        self.available_books_label.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Borrowed", None))
        self.borrowed_books_label.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Members", None))
        self.total_members_label.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Trending Genres", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Books by Genre", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Recent Activity", None))
        ___qtablewidgetitem = self.books_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None))
        ___qtablewidgetitem1 = self.books_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        ___qtablewidgetitem2 = self.books_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        ___qtablewidgetitem3 = self.books_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        ___qtablewidgetitem4 = self.books_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        ___qtablewidgetitem5 = self.books_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.category_label.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.category_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Fiction", None))
        self.category_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Non-Fiction", None))

        self.category_combo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Category", None))
        self.genre_label.setText(QCoreApplication.translate("MainWindow", u"Genre ", None))
        self.genre_combo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Genre", None))
        self.available_label.setText(QCoreApplication.translate("MainWindow", u"Available", None))
        self.available_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Available", None))
        self.available_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Borrowed", None))

        self.books_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Book...", None))
        self.search_button_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to E-Library ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Books Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Here on this page, you can search for the books available inside our library", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Welcome to E-Library ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Borrow and Returns Page", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Here on this page, you can borrow books available in our library and return ones you have finished using", None))
        self.borrow_return_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Book...", None))
        self.search_button_4.setText("")
        ___qtablewidgetitem6 = self.borrow_return_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"id", None))
        ___qtablewidgetitem7 = self.borrow_return_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        ___qtablewidgetitem8 = self.borrow_return_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        ___qtablewidgetitem9 = self.borrow_return_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        ___qtablewidgetitem10 = self.borrow_return_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        ___qtablewidgetitem11 = self.borrow_return_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.selected_book_heading.setText(QCoreApplication.translate("MainWindow", u"Selected Book", None))
        self.id_label_2.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.title_label_2.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.author_label_2.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.genre_label_3.setText(QCoreApplication.translate("MainWindow", u"Genre:", None))
        self.year_label_2.setText(QCoreApplication.translate("MainWindow", u"Year:", None))
        self.status_label_2.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.selected_id_label.setText("")
        self.selected_title_label.setText("")
        self.selected_author_label.setText("")
        self.selected_genre_label.setText("")
        self.selected_year_label.setText("")
        self.selected_status_label.setText("")
        self.borrow_button.setText(QCoreApplication.translate("MainWindow", u"Borrow", None))
        self.return_button.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"stats", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.menu_button.setText("")
        self.main_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"What's on your mind?...", None))
        self.search_button.setText("")
        self.user_3.setText("")
    # retranslateUi

