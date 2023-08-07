﻿# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass


from PySide6.QtWidgets import QMessageBox, QFileDialog, QVBoxLayout, QMenu, QAbstractItemView, QDialog
from PySide6.QtGui import QAction, QStandardItemModel, QStandardItem, QIcon
from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, Qt, QSize,QTimer, QThread


from app.app_utilities import AppUtilitiesClass

from layers.appDataLay.fuzz import ThreadObj_App_fuzz

from subUi.signalFuzz.dialog_fuzzSetting import Dialog_fuzzSetting
from subUi.signalFuzz.ui_groupbox_signalFuzz import Ui_GroupBox_signalFuzz
from subUi.signalFuzz.dialog_selectSignal import Dialog_selectSignal
from subUi.queryDB.dialog_querysniffdb import Dialog_querySniffDB

class GroupBox_signalFuzz(QtWidgets.QDialog):
    def __init__(self, mainWin, threadObj_ioPort, parent=None):
        super().__init__(parent)
        self.ui = Ui_GroupBox_signalFuzz()
        self.ui.setupUi(self)

        self.mainWin = mainWin

        self.threadObj_ioPort = threadObj_ioPort

        self.timerisCreated_send = False

        # 设置发送信号列表表格被选整行
        self.ui.tableView_sendSignalList.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.model_tableView_sendSignalList = QStandardItemModel()
        self.model_tableView_sendSignalList_currentRow = 0

        # 设置发送信号列表表格的右键菜单
        self.ui.tableView_sendSignalList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView_sendSignalList.customContextMenuRequested.connect(self.tableView_sendSignalList_show_context_menu)
        self.tableView_sendSignalList_context_menu = QMenu(self)  # 创建右键菜单        
        delete_action = QAction("delete", self)  # 添加动作到菜单
        delete_action.triggered.connect(self.tableView_sendSignalList_delete_Rows)      # 连接删除信号
        self.tableView_sendSignalList_context_menu.addAction(delete_action)  


        # 连接信号
        

        # 设置发送信号列表的表头
        self.setTableTitle_tableView_sendSignalList()

        # 创建并显示信号库查询UI
        self.create_querySignalSubUi()

        # fuzz信号发送线程管理
        self.threadObj_fuzz = None
        self.thread_fuzz = None

        # 配置 fuzz信号发送线程
        self.thread_cfg_threadObj_fuzz()

    def thread_cfg_threadObj_fuzz(self):


        if self.threadObj_fuzz is not None:
            return

        # 创建线程
        self.thread_fuzz = QThread(self)
        self.threadObj_fuzz = ThreadObj_App_fuzz()
        self.threadObj_fuzz.moveToThread(self.thread_fuzz)
        self.thread_fuzz.finished.connect(self.thread_fuzz.deleteLater)
        self.thread_fuzz.finished.connect(self.threadObj_fuzz.deleteLater)

        # 信号连接
        self.threadObj_fuzz.base_connect(self.mainWin) # 基本信号连接
        self.signal_sendFuzzSignalData.connect(self.threadObj_fuzz.fuzz_slot)
        self.threadObj_fuzz.signal_fuzzData.connect(self.threadObj_ioPort.devices_sendByteArrays_slot)
        self.destroyed.connect(self.thread_fuzz.quit)

        self.thread_fuzz.start()

    # 显示发送信号列表表格的右键菜单
    @Slot(int)
    def tableView_sendSignalList_show_context_menu(self, pos):
        # 在指定位置显示菜单
        self.tableView_sendSignalList_context_menu.exec_(self.ui.tableView_sendSignalList.mapToGlobal(pos))

    # 递归删除发送信号列表表格选中的表项
    @Slot()
    def tableView_sendSignalList_delete_Rows(self):
        # 获取选中的行索引
        selectedIndexes = self.ui.tableView_sendSignalList.selectionModel().selectedRows()
        # 获取选中行的行号
        selectedRows = [index.row() for index in selectedIndexes]

        if len(selectedRows) > 0 :
            self.ui.tableView_sendSignalList.model().removeRow(selectedRows[0])
            self.model_tableView_sendSignalList_currentRow = self.model_tableView_sendSignalList_currentRow - 1
            self.tableView_sendSignalList_delete_Rows()


    # 设置 tableView_sendSignalList 表头
    @Slot()
    def setTableTitle_tableView_sendSignalList(self):
        headers = ["name","signal_name","frame_id","start_bit","len","byte_order","UB"]
        self.model_tableView_sendSignalList.setHorizontalHeaderLabels(headers)
        self.ui.tableView_sendSignalList.setModel(self.model_tableView_sendSignalList)


    # 创建并显示信号库查询UI
    @Slot()
    def create_querySignalSubUi(self):

        # 创建子UI
        list_dbName = ["fuzzFuncDB"]
        self.subUi_querySignal = Dialog_querySniffDB(mainWin=self.mainWin, list_dbName=list_dbName)
        self.subUi_querySignal.ui.pushButton_dbcDecode.setVisible(False)
        self.subUi_querySignal.ui.pushButton_outputcsv.setVisible(False)

        # 连接信号
        self.subUi_querySignal.singal_tipsPrint.connect(self.singal_tipsPrint)

        # 添加并显示 子 UI
        self.subUi_subWinHand_querySignal = self.ui.mdiArea_querySignal.addSubWindow(self.subUi_querySignal)
        self.subUi_subWinHand_querySignal.setWindowState(self.subUi_querySignal.windowState() | Qt.WindowMaximized) # 将子UI最大化
        self.subUi_subWinHand_querySignal.setWindowFlags(self.subUi_subWinHand_querySignal.windowFlags() | Qt.WindowStaysOnTopHint)

        self.subUi_querySignal.show()

    # 向发送信号列表添加信号
    @Slot(dict)
    def add_sendSignal_slot(self, data_dict):
     
        if self.model_tableView_sendSignalList_currentRow > 2000 :
            self.model_tableView_sendSignalList_currentRow = 0
            self.model_tableView_sendSignalList.clear()
            self.setTableTitle_tableView_sendSignalList()

        item = QStandardItem(data_dict["name"])
        self.model_tableView_sendSignalList.setItem(self.model_tableView_sendSignalList_currentRow, 0, item)
        item = QStandardItem(data_dict["signal_name"])
        self.model_tableView_sendSignalList.setItem(self.model_tableView_sendSignalList_currentRow, 1, item)
        item = QStandardItem(data_dict["frame_id"])
        self.model_tableView_sendSignalList.setItem(self.model_tableView_sendSignalList_currentRow, 2, item)
        item = QStandardItem(data_dict["start_bit"])
        self.model_tableView_sendSignalList.setItem(self.model_tableView_sendSignalList_currentRow, 3, item)
        item = QStandardItem(data_dict["len"])
        self.model_tableView_sendSignalList.setItem(self.model_tableView_sendSignalList_currentRow, 4, item)
        item = QStandardItem(data_dict["byte_order"])
        self.model_tableView_sendSignalList.setItem(self.model_tableView_sendSignalList_currentRow, 5, item)
        item = QStandardItem(data_dict["UB"])
        self.model_tableView_sendSignalList.setItem(self.model_tableView_sendSignalList_currentRow, 6, item)


        self.ui.tableView_sendSignalList.setModel(self.model_tableView_sendSignalList)


        self.model_tableView_sendSignalList_currentRow = self.model_tableView_sendSignalList_currentRow + 1
        

    # 向功能库添加信息信号
    @Slot(dict)
    def add_newSignal_slot(self, data_dict):
        # 获取从数据库选择的信号
        print("data_dict", data_dict)

        # 把获取的信号写进数据库
        db = AppUtilitiesClass.sqlDB_connect("fuzzFuncDB")
        AppUtilitiesClass.sqlDB_insert_fuzzFuncData(db, "fuzzFuncTable", data_dict)
        AppUtilitiesClass.sqlDB_disconnect(db)

        # 刷新显示
        self.subUi_querySignal.get_sniffDB_tableNames()
        self.subUi_querySignal.ui.comboBox_swtable.setCurrentText("fuzzFuncTable")

    @Slot()
    def on_pushButton_addNewSignal_clicked(self):
        # 创建对话框
        list_dbName = ["dbcDataDB"]  
        dialog = Dialog_querySniffDB(mainWin=self.mainWin, list_dbName=list_dbName)
        # 对话框属性设置
        # 设置表格的右键菜单
        action_add = QAction("add signal", dialog)
        dialog.tableView_sniffdb_context_menu.addAction(action_add)

        # 对话框信号连接
        action_add.triggered.connect(dialog.get_selectAndEditRowData_slot)
        dialog.signal_get_selectAndEditRowData_result.connect(self.add_newSignal_slot)
        
        dialog.exec()
    
    @Slot()
    def on_pushButton_addSendSignal_clicked(self):
        # 获取选择的信号数据
        data_list = self.subUi_querySignal.get_seleteRowsData_slot()
        for data_dict in data_list:
            if data_dict is not None:
                # 添加到发送信号列表并进行显示
                self.add_sendSignal_slot(data_dict)

    @Slot()
    def on_pushButton_clearSendSignalList_clicked(self):
        # 创建消息对话框
        msg_box = QMessageBox()
        msg_box.setText(self.tr(f"Confirm to clear the transmission signal list?"))
        msg_box.setWindowTitle("Tips")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton(self.tr("OK"), QMessageBox.AcceptRole)
        msg_box.addButton(self.tr("Cancel"), QMessageBox.RejectRole)
        icon = QIcon()
        icon.addFile(u":/icons/zeekr", QSize(), QIcon.Normal, QIcon.Off)
        msg_box.setWindowIcon(icon)

        # 弹出对话框并等待用户操作
        response = msg_box.exec()
        if response == 0:
            self.model_tableView_sendSignalList_currentRow = 0
            self.model_tableView_sendSignalList.clear()
            self.setTableTitle_tableView_sendSignalList()
            self.singal_tipsPrint.emit(self.tr(f"Clear the transmission signal list successfully!"))

    # 发送，信号列表当中的信号
    @Slot()
    def on_pushButton_sendFuzzSignal_clicked(self):
        # 获取信号列表当中是信号
        list_fuzzSigs = []

        row_count = self.ui.tableView_sendSignalList.model().rowCount()
    
        for row in range(row_count):
            row_data = {}
            header_view = self.ui.tableView_sendSignalList.horizontalHeader()
            for column in range(self.ui.tableView_sendSignalList.model().columnCount()):
                item = self.ui.tableView_sendSignalList.model().item(row, column)
                key = self.ui.tableView_sendSignalList.model().headerData(column, header_view.orientation())
                if item is not None:
                    row_data[key] = item.text()
                else:
                    row_data[key] = item.text()
            
            list_fuzzSigs.append(row_data)
        
        print("list_fuzzSigs", list_fuzzSigs)

        # 发送fuzz数据
        self.signal_sendFuzzSignalData.emit(list_fuzzSigs)

        
    @Slot()
    def on_checkBox_timerSend_stateChanged(self):
        if self.ui.checkBox_timerSend.isChecked() :
            if self.timerisCreated_send == False:
                self.timerisCreated_send = True
                self.timer_send=QTimer() 
                self.timer_send.timeout.connect(self.on_pushButton_sendFuzzSignal_clicked)
                self.destroyed.connect(lambda:(
                    self.timer_send.stop(),
                    self.timer_send.deleteLater()
                ))

            interValue = self.ui.spinBox_portTimeValue.value()
            self.timer_send.setInterval(interValue)  
            self.timer_send.start()
        else:
            self.timer_send.stop()


    # Fuzz 设置
    @Slot()
    def on_pushButton_fuzzSetting_clicked(self):
        dialog = Dialog_fuzzSetting(self)
        if dialog.exec_() == QDialog.Accepted:
            # 获取设置
            pass
        pass


    # 输出提示信息信号
    singal_tipsPrint = Signal(str)

    # 信号，通知发送fuzz信号数据
    signal_sendFuzzSignalData = Signal(list)
