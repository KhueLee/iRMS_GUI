import sys
import socket

from ui.ui_iRCS import *
from ui.page.page_monitor import *


class MainWindow(QMainWindow):
    def __init__(self):
        ################################################################################################################
        # Init cửa sổ
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.statusBar().hide()
        self.showFullScreen()  # Hiển thị cửa sổ full màn hình
        self.setWindowFlags(self.windowFlags() or Qt.FramelessWindowHint)  # Tắt thanh control box

        # set current widget
        self.ui.stk_wid_menu.setCurrentWidget(self.ui.menu_monitor)

        # button change view
        self.ui.btn_monitor.clicked.connect(lambda: self.ui.stk_wid_menu.setCurrentWidget(self.ui.menu_monitor))
        self.ui.btn_task.clicked.connect(lambda: self.ui.stk_wid_menu.setCurrentWidget(self.ui.menu_task))
        self.ui.btn_robot.clicked.connect(lambda: self.ui.stk_wid_menu.setCurrentWidget(self.ui.menu_robot))
        self.ui.btn_alarm.clicked.connect(lambda: self.ui.stk_wid_menu.setCurrentWidget(self.ui.menu_alarm))
        self.ui.btn_static.clicked.connect(lambda: self.ui.stk_wid_menu.setCurrentWidget(self.ui.menu_static))
        self.ui.btn_operation.clicked.connect(lambda: self.ui.stk_wid_menu.setCurrentWidget(self.ui.menu_operation))

        self.ui.btn_monitor.clicked.connect(lambda: self.ui.stk_wid_main.setCurrentWidget(self.ui.page_monitor))
        self.ui.btn_task.clicked.connect(lambda: self.ui.stk_wid_main.setCurrentWidget(self.ui.page_monitor))
        self.ui.btn_robot.clicked.connect(lambda: self.ui.stk_wid_main.setCurrentWidget(self.ui.page_robot))
        self.ui.btn_alarm.clicked.connect(lambda: self.ui.stk_wid_main.setCurrentWidget(self.ui.page_monitor))
        self.ui.btn_static.clicked.connect(lambda: self.ui.stk_wid_main.setCurrentWidget(self.ui.page_monitor))
        self.ui.btn_operation.clicked.connect(lambda: self.ui.stk_wid_main.setCurrentWidget(self.ui.page_monitor))

        #layer ui
        layer_map = LayerMap(self.ui.page_monitor)
        layer_map.show()


class DataUI:
    def __init__(self, ui_config):
        self.map_data = None
        self.robot_data = None
        self.shelf_data = None
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = ui_config["server_ip"]
        self.server_port = ui_config["server_port"]

    def init_connection(self):
        self.connection.connect((self.server_ip, self.server_port))

    def listen(self):
        pass

    def heart_beat(self):
        pass


def init_main_ui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

