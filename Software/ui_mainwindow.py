# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QMainWindow, QMdiArea,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QTabWidget,
    QTextBrowser, QTextEdit, QToolBar, QWidget)
import rc_resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1680, 960)
        icon = QIcon()
        icon.addFile(u":/icons/zeekr.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.action_Connect = QAction(MainWindow)
        self.action_Connect.setObjectName(u"action_Connect")
        icon1 = QIcon()
        icon1.addFile(u":/icons/connect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Connect.setIcon(icon1)
        self.action_Disconnect = QAction(MainWindow)
        self.action_Disconnect.setObjectName(u"action_Disconnect")
        icon2 = QIcon()
        icon2.addFile(u":/icons/disconnect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Disconnect.setIcon(icon2)
        self.action_connectParamSet = QAction(MainWindow)
        self.action_connectParamSet.setObjectName(u"action_connectParamSet")
        icon3 = QIcon()
        icon3.addFile(u":/icons/ConnectParamSet.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_connectParamSet.setIcon(icon3)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        icon4 = QIcon()
        icon4.addFile(u":/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_about.setIcon(icon4)
        self.action_rawDis = QAction(MainWindow)
        self.action_rawDis.setObjectName(u"action_rawDis")
        self.action_rawDis.setCheckable(True)
        icon5 = QIcon()
        icon5.addFile(u":/icons/basicData.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_rawDis.setIcon(icon5)
        self.action_sniff = QAction(MainWindow)
        self.action_sniff.setObjectName(u"action_sniff")
        self.action_sniff.setCheckable(True)
        icon6 = QIcon()
        icon6.addFile(u":/icons/dataSniff.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_sniff.setIcon(icon6)
        self.action_historyQuery = QAction(MainWindow)
        self.action_historyQuery.setObjectName(u"action_historyQuery")
        icon7 = QIcon()
        icon7.addFile(u":/icons/dataQuery.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_historyQuery.setIcon(icon7)
        self.action_signalFuzz = QAction(MainWindow)
        self.action_signalFuzz.setObjectName(u"action_signalFuzz")
        self.action_signalFuzz.setCheckable(True)
        icon8 = QIcon()
        icon8.addFile(u":/icons/dbcDeocde.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_signalFuzz.setIcon(icon8)
        self.action_send_data = QAction(MainWindow)
        self.action_send_data.setObjectName(u"action_send_data")
        icon9 = QIcon()
        icon9.addFile(u":/icons/send.png", QSize(), QIcon.Normal, QIcon.On)
        self.action_send_data.setIcon(icon9)
        self.action_dbcDecode = QAction(MainWindow)
        self.action_dbcDecode.setObjectName(u"action_dbcDecode")
        icon10 = QIcon()
        icon10.addFile(u":/icons/fileDecode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_dbcDecode.setIcon(icon10)
        self.action_addFlexRayDB = QAction(MainWindow)
        self.action_addFlexRayDB.setObjectName(u"action_addFlexRayDB")
        self.action_addFlexRayDB.setIcon(icon10)
        self.action_addLinDB = QAction(MainWindow)
        self.action_addLinDB.setObjectName(u"action_addLinDB")
        self.action_addLinDB.setIcon(icon10)
        self.action_addEthernetDB = QAction(MainWindow)
        self.action_addEthernetDB.setObjectName(u"action_addEthernetDB")
        self.action_addEthernetDB.setIcon(icon10)
        self.action_helpDoc = QAction(MainWindow)
        self.action_helpDoc.setObjectName(u"action_helpDoc")
        icon11 = QIcon()
        icon11.addFile(u":/icons/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_helpDoc.setIcon(icon11)
        self.action_swLanguage = QAction(MainWindow)
        self.action_swLanguage.setObjectName(u"action_swLanguage")
        self.action_swLanguage.setCheckable(True)
        icon12 = QIcon()
        icon12.addFile(u":/icons/swLanguage.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_swLanguage.setIcon(icon12)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setChildrenCollapsible(True)
        self.mdiArea_main = QMdiArea(self.splitter)
        self.mdiArea_main.setObjectName(u"mdiArea_main")
        self.mdiArea_main.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea_main.sizePolicy().hasHeightForWidth())
        self.mdiArea_main.setSizePolicy(sizePolicy)
        self.mdiArea_main.setMinimumSize(QSize(1280, 600))
        self.mdiArea_main.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        brush = QBrush(QColor(240, 245, 251, 255))
        brush.setStyle(Qt.SolidPattern)
        self.mdiArea_main.setBackground(brush)
        self.mdiArea_main.setViewMode(QMdiArea.TabbedView)
        self.mdiArea_main.setDocumentMode(True)
        self.mdiArea_main.setTabsClosable(True)
        self.mdiArea_main.setTabsMovable(True)
        self.mdiArea_main.setTabShape(QTabWidget.Rounded)
        self.mdiArea_main.setTabPosition(QTabWidget.North)
        self.splitter.addWidget(self.mdiArea_main)
        self.tabWidget_info = QTabWidget(self.splitter)
        self.tabWidget_info.setObjectName(u"tabWidget_info")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_clearAppPrint = QPushButton(self.tab_3)
        self.pushButton_clearAppPrint.setObjectName(u"pushButton_clearAppPrint")

        self.horizontalLayout.addWidget(self.pushButton_clearAppPrint)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textBrowser_appPrint = QTextBrowser(self.groupBox)
        self.textBrowser_appPrint.setObjectName(u"textBrowser_appPrint")
        self.textBrowser_appPrint.setFrameShape(QFrame.NoFrame)
        self.textBrowser_appPrint.setFrameShadow(QFrame.Sunken)
        self.textBrowser_appPrint.setLineWidth(1)
        self.textBrowser_appPrint.setLineWrapMode(QTextEdit.WidgetWidth)
        self.textBrowser_appPrint.setOverwriteMode(False)

        self.gridLayout_2.addWidget(self.textBrowser_appPrint, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)

        self.tabWidget_info.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_info.addTab(self.tab_4, "")
        self.splitter.addWidget(self.tabWidget_info)
        self.splitter_2.addWidget(self.splitter)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1680, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menu_4)
        self.menu_5.setObjectName(u"menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setOrientation(Qt.Horizontal)
        self.mainToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_Connect)
        self.menu.addAction(self.action_Disconnect)
        self.menu.addAction(self.action_connectParamSet)
        self.menu.addSeparator()
        self.menu_2.addAction(self.action_swLanguage)
        self.menu_2.addAction(self.action_helpDoc)
        self.menu_2.addAction(self.action_about)
        self.menu_3.addAction(self.action_rawDis)
        self.menu_3.addAction(self.action_sniff)
        self.menu_3.addAction(self.action_signalFuzz)
        self.menu_3.addAction(self.action_send_data)
        self.menu_4.addAction(self.menu_5.menuAction())
        self.menu_4.addAction(self.action_historyQuery)
        self.menu_5.addAction(self.action_dbcDecode)
        self.menu_5.addAction(self.action_addFlexRayDB)
        self.menu_5.addAction(self.action_addLinDB)
        self.menu_5.addAction(self.action_addEthernetDB)
        self.mainToolBar.addAction(self.action_Connect)
        self.mainToolBar.addAction(self.action_Disconnect)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.action_sniff)
        self.mainToolBar.addAction(self.action_signalFuzz)
        self.mainToolBar.addAction(self.action_send_data)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.action_dbcDecode)
        self.mainToolBar.addAction(self.action_historyQuery)

        self.retranslateUi(MainWindow)

        self.tabWidget_info.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoSuite v1 Designed by ZEEKR ZERO", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(QCoreApplication.translate("MainWindow", u"AutoSuite v1.0 ", None))
#endif // QT_CONFIG(statustip)
        self.action_Connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(tooltip)
        self.action_Connect.setToolTip(QCoreApplication.translate("MainWindow", u"Connect", None))
#endif // QT_CONFIG(tooltip)
        self.action_Disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
#if QT_CONFIG(tooltip)
        self.action_Disconnect.setToolTip(QCoreApplication.translate("MainWindow", u"Disconnect", None))
#endif // QT_CONFIG(tooltip)
        self.action_connectParamSet.setText(QCoreApplication.translate("MainWindow", u"Set device parameters", None))
#if QT_CONFIG(tooltip)
        self.action_connectParamSet.setToolTip(QCoreApplication.translate("MainWindow", u"Set device parameters", None))
#endif // QT_CONFIG(tooltip)
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About us", None))
#if QT_CONFIG(tooltip)
        self.action_about.setToolTip(QCoreApplication.translate("MainWindow", u"About us", None))
#endif // QT_CONFIG(tooltip)
        self.action_rawDis.setText(QCoreApplication.translate("MainWindow", u"Byte stream", None))
#if QT_CONFIG(tooltip)
        self.action_rawDis.setToolTip(QCoreApplication.translate("MainWindow", u"Byte stream", None))
#endif // QT_CONFIG(tooltip)
        self.action_sniff.setText(QCoreApplication.translate("MainWindow", u"Sniffing", None))
#if QT_CONFIG(tooltip)
        self.action_sniff.setToolTip(QCoreApplication.translate("MainWindow", u"Sniffing", None))
#endif // QT_CONFIG(tooltip)
        self.action_historyQuery.setText(QCoreApplication.translate("MainWindow", u"Data query", None))
#if QT_CONFIG(tooltip)
        self.action_historyQuery.setToolTip(QCoreApplication.translate("MainWindow", u"Data query", None))
#endif // QT_CONFIG(tooltip)
        self.action_signalFuzz.setText(QCoreApplication.translate("MainWindow", u"Signal FUZZ", None))
#if QT_CONFIG(tooltip)
        self.action_signalFuzz.setToolTip(QCoreApplication.translate("MainWindow", u"Signal FUZZ", None))
#endif // QT_CONFIG(tooltip)
        self.action_send_data.setText(QCoreApplication.translate("MainWindow", u"Send data", None))
#if QT_CONFIG(tooltip)
        self.action_send_data.setToolTip(QCoreApplication.translate("MainWindow", u"Send bus data", None))
#endif // QT_CONFIG(tooltip)
        self.action_dbcDecode.setText(QCoreApplication.translate("MainWindow", u"CAN database", None))
#if QT_CONFIG(tooltip)
        self.action_dbcDecode.setToolTip(QCoreApplication.translate("MainWindow", u"Import CAN database", None))
#endif // QT_CONFIG(tooltip)
        self.action_addFlexRayDB.setText(QCoreApplication.translate("MainWindow", u"FlexRay database", None))
#if QT_CONFIG(tooltip)
        self.action_addFlexRayDB.setToolTip(QCoreApplication.translate("MainWindow", u"Import the FlexRay database", None))
#endif // QT_CONFIG(tooltip)
        self.action_addLinDB.setText(QCoreApplication.translate("MainWindow", u"LIN database", None))
#if QT_CONFIG(tooltip)
        self.action_addLinDB.setToolTip(QCoreApplication.translate("MainWindow", u"LIN database", None))
#endif // QT_CONFIG(tooltip)
        self.action_addEthernetDB.setText(QCoreApplication.translate("MainWindow", u"Ethernet database", None))
#if QT_CONFIG(tooltip)
        self.action_addEthernetDB.setToolTip(QCoreApplication.translate("MainWindow", u"Ethernet database", None))
#endif // QT_CONFIG(tooltip)
        self.action_helpDoc.setText(QCoreApplication.translate("MainWindow", u"Contact us", None))
#if QT_CONFIG(tooltip)
        self.action_helpDoc.setToolTip(QCoreApplication.translate("MainWindow", u"Contact us", None))
#endif // QT_CONFIG(tooltip)
        self.action_swLanguage.setText(QCoreApplication.translate("MainWindow", u"Language", None))
#if QT_CONFIG(tooltip)
        self.action_swLanguage.setToolTip(QCoreApplication.translate("MainWindow", u"Language", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clearAppPrint.setText(QCoreApplication.translate("MainWindow", u"Clear tips", None))
        self.groupBox.setTitle("")
        self.tabWidget_info.setTabText(self.tabWidget_info.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tips", None))
        self.tabWidget_info.setTabText(self.tabWidget_info.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Terminal", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Device", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"Functions", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"Import database", None))
        self.mainToolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

