# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'library-management-sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
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
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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
        icon = QIcon()
        icon.addFile(u":/icons/power_settings_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/green_power_settings_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.off_2.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/home_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/green_home_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/books_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/green_library_books.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/return_borrow_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/green_cycle_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/stats_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/green_stats_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/settings_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/green_settings_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/account_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.user_2.setIcon(icon6)
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


        self.gridLayout_3.addWidget(self.icons_names_widget, 0, 1, 1, 1)

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
        icon7 = QIcon()
        icon7.addFile(u":/icons/account_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icons/green_account_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.user_1.setIcon(icon7)
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
        self.dashboard_1.setIcon(icon1)
        self.dashboard_1.setIconSize(QSize(25, 25))
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.books_1 = QPushButton(self.icons_only_widget)
        self.books_1.setObjectName(u"books_1")
        self.books_1.setMinimumSize(QSize(40, 40))
        self.books_1.setMaximumSize(QSize(40, 40))
        self.books_1.setIcon(icon2)
        self.books_1.setIconSize(QSize(25, 25))
        self.books_1.setCheckable(True)
        self.books_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.books_1)

        self.return_borrow_1 = QPushButton(self.icons_only_widget)
        self.return_borrow_1.setObjectName(u"return_borrow_1")
        self.return_borrow_1.setMinimumSize(QSize(40, 40))
        self.return_borrow_1.setMaximumSize(QSize(40, 40))
        self.return_borrow_1.setIcon(icon3)
        self.return_borrow_1.setIconSize(QSize(25, 25))
        self.return_borrow_1.setCheckable(True)
        self.return_borrow_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.return_borrow_1)

        self.stats_1 = QPushButton(self.icons_only_widget)
        self.stats_1.setObjectName(u"stats_1")
        self.stats_1.setMinimumSize(QSize(40, 40))
        self.stats_1.setMaximumSize(QSize(40, 40))
        self.stats_1.setIcon(icon4)
        self.stats_1.setIconSize(QSize(25, 25))
        self.stats_1.setCheckable(True)
        self.stats_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.stats_1)

        self.settings_1 = QPushButton(self.icons_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        self.settings_1.setMinimumSize(QSize(40, 40))
        self.settings_1.setMaximumSize(QSize(40, 40))
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
        self.off_1.setIcon(icon)
        self.off_1.setCheckable(True)
        self.off_1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.off_1)


        self.gridLayout_3.addWidget(self.icons_only_widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 20, 621, 50))
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 70, 911, 581))
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 650))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dashboard_page1 = QWidget()
        self.dashboard_page1.setObjectName(u"dashboard_page1")
        self.label = QLabel(self.dashboard_page1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 90, 49, 16))
        self.stackedWidget.addWidget(self.dashboard_page1)
        self.books_page = QWidget()
        self.books_page.setObjectName(u"books_page")
        self.label_2 = QLabel(self.books_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 321, 31))
        font2 = QFont()
        font2.setFamilies([u"Sitka"])
        font2.setPointSize(17)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_7 = QLabel(self.books_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 70, 241, 21))
        font3 = QFont()
        font3.setFamilies([u"Sitka"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_7.setFont(font3)
        self.label_8 = QLabel(self.books_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 100, 521, 20))
        font4 = QFont()
        font4.setFamilies([u"Sitka"])
        font4.setBold(True)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color: rgb(62, 186, 0);")
        self.tableWidget = QTableWidget(self.books_page)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(110, 230, 611, 341))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: \n"
"	color: rgb(66, 199, 0);\n"
"}")
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
        self.widget1 = QWidget(self.combobox_widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 20, 441, 67))
        self.horizontalLayout_4 = QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.category_label = QLabel(self.widget1)
        self.category_label.setObjectName(u"category_label")
        font5 = QFont()
        font5.setFamilies([u"Sitka"])
        font5.setPointSize(12)
        self.category_label.setFont(font5)
        self.category_label.setStyleSheet(u"")
        self.category_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.category_label)

        self.category_combo = QComboBox(self.widget1)
        self.category_combo.addItem("")
        self.category_combo.addItem("")
        self.category_combo.setObjectName(u"category_combo")
        font6 = QFont()
        font6.setFamilies([u"Sitka"])
        font6.setPointSize(8)
        self.category_combo.setFont(font6)

        self.verticalLayout_4.addWidget(self.category_combo)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.genre_label = QLabel(self.widget1)
        self.genre_label.setObjectName(u"genre_label")
        self.genre_label.setFont(font5)
        self.genre_label.setStyleSheet(u"")
        self.genre_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.genre_label)

        self.genre_combo = QComboBox(self.widget1)
        self.genre_combo.setObjectName(u"genre_combo")
        self.genre_combo.setFont(font6)

        self.verticalLayout_6.addWidget(self.genre_combo)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.available_label = QLabel(self.widget1)
        self.available_label.setObjectName(u"available_label")
        self.available_label.setFont(font5)
        self.available_label.setStyleSheet(u"")
        self.available_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.available_label)

        self.available_combo = QComboBox(self.widget1)
        self.available_combo.addItem("")
        self.available_combo.addItem("")
        self.available_combo.setObjectName(u"available_combo")
        self.available_combo.setFont(font6)

        self.verticalLayout_5.addWidget(self.available_combo)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.widget_5 = QWidget(self.books_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(480, 180, 361, 51))
        self.layoutWidget2 = QWidget(self.widget_5)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 358, 28))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.search_entry_2 = QLineEdit(self.layoutWidget2)
        self.search_entry_2.setObjectName(u"search_entry_2")
        self.search_entry_2.setMinimumSize(QSize(300, 25))
        self.search_entry_2.setMaximumSize(QSize(300, 25))
        self.search_entry_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.search_entry_2)

        self.search_button_2 = QPushButton(self.layoutWidget2)
        self.search_button_2.setObjectName(u"search_button_2")
        self.search_button_2.setMinimumSize(QSize(50, 26))
        self.search_button_2.setMaximumSize(QSize(50, 26))
        icon8 = QIcon()
        icon8.addFile(u":/icons/search_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_button_2.setIcon(icon8)
        self.search_button_2.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.search_button_2)

        self.stackedWidget.addWidget(self.books_page)
        self.borrow_return_page = QWidget()
        self.borrow_return_page.setObjectName(u"borrow_return_page")
        self.label_4 = QLabel(self.borrow_return_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 160, 49, 16))
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
        self.layoutWidget3 = QWidget(self.widget_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(49, 20, 831, 42))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_button = QPushButton(self.layoutWidget3)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setMinimumSize(QSize(60, 40))
        self.menu_button.setMaximumSize(QSize(60, 40))
        self.menu_button.setStyleSheet(u"border: none;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/menu_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_button.setIcon(icon9)
        self.menu_button.setIconSize(QSize(30, 30))
        self.menu_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.menu_button)

        self.horizontalSpacer = QSpacerItem(38, 37, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_entry = QLineEdit(self.layoutWidget3)
        self.search_entry.setObjectName(u"search_entry")
        self.search_entry.setMinimumSize(QSize(250, 25))
        self.search_entry.setMaximumSize(QSize(250, 25))
        self.search_entry.setFont(font)

        self.horizontalLayout.addWidget(self.search_entry)

        self.search_button = QPushButton(self.layoutWidget3)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(50, 26))
        self.search_button.setMaximumSize(QSize(50, 26))
        self.search_button.setIcon(icon8)
        self.search_button.setCheckable(False)

        self.horizontalLayout.addWidget(self.search_button)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.user_3 = QPushButton(self.layoutWidget3)
        self.user_3.setObjectName(u"user_3")
        self.user_3.setMinimumSize(QSize(60, 40))
        self.user_3.setMaximumSize(QSize(60, 40))
        self.user_3.setStyleSheet(u"border: none;")
        self.user_3.setIcon(icon6)
        self.user_3.setIconSize(QSize(30, 30))
        self.user_3.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.user_3)


        self.gridLayout_3.addWidget(self.widget_3, 0, 2, 1, 1)

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

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.off_2.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.books_2.setText(QCoreApplication.translate("MainWindow", u"Books", None))
        self.return_borrow_2.setText(QCoreApplication.translate("MainWindow", u"Borrow/Return", None))
        self.stats_2.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.user_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"E-Library", None))
        self.user_1.setText("")
        self.dashboard_1.setText("")
        self.books_1.setText("")
        self.return_borrow_1.setText("")
        self.stats_1.setText("")
        self.settings_1.setText("")
        self.off_1.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"dasboard", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to E-Library ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Books Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Here on this page, you can search for the books available inside our library", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
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

        self.search_entry_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Book...", None))
        self.search_button_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"borrow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"stats", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.menu_button.setText("")
        self.search_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"What's on your mind?...", None))
        self.search_button.setText("")
        self.user_3.setText("")
    # retranslateUi

