from PySide2.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsLineItem
from PySide2.QtGui import QColor, QPen
from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QPainter
from websocketIO.WebSocketListener import *


class LayerMap(QWidget):
    radius = 3

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ws_listener = WebSocketListener()  # Đối tượng WebSocketListener
        self.map_data = None
        self.robot_data = {}  # Bộ nhớ đệm dữ liệu robot

        # Khởi tạo Scene và View
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(0, 0, 1505, 990)

        # Kích hoạt kéo thả và zoom
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.view.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        # Lấy bản đồ
        self.get_map()

        # Cập nhật robot mỗi 33ms (~30Hz)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_robots)
        self.timer.start(33)

    def get_map(self):
        """Lấy dữ liệu bản đồ từ API và hiển thị."""
        import requests
        if self.map_data is None:
            url = "http://127.0.0.1:8080/map/get_map"
            try:
                response = requests.get(url, timeout=1)
                response.raise_for_status()
                data = response.json()
                if data["message"] == "OK":
                    self.map_data = data
                    self.print_map()
                else:
                    print("Error: Invalid response")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching map data: {e}")

    def print_map(self):
        """Hiển thị các node và đường nối trên bản đồ."""
        self.scene.clear()
        self.nodes = self.map_data["nodes"]
        width = self.map_data["max_x"] - self.map_data["min_x"]
        height = self.map_data["max_y"] - self.map_data["min_y"]
        self.map_res = max(width / 1455, height / 940)

        node_positions = {}

        # Vẽ các node
        for node in self.nodes.values():
            x = (node["coordinate"]["x"] - self.map_data["min_x"]) // self.map_res
            y = (node["coordinate"]["y"] - self.map_data["min_y"]) // self.map_res
            node_positions[node["id"]] = (x, y)

            color = "#ffaa00" if node["type"] == 1 else "#0766AD" if node["type"] == 3 else "#C7C8CC"
            ellipse = QGraphicsEllipseItem(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
            ellipse.setPen(Qt.NoPen)
            ellipse.setBrush(QColor(color))
            ellipse.setZValue(1)
            self.scene.addItem(ellipse)

        # Vẽ các đường nối (edges)
        for node in self.nodes.values():
            start_pos = node_positions[node["id"]]
            for connected_id in node["edges"]:
                if connected_id["destination"] in node_positions:
                    end_pos = node_positions[connected_id["destination"]]
                    line = QGraphicsLineItem(start_pos[0], start_pos[1], end_pos[0], end_pos[1])
                    line.setPen(QPen(QColor("#888888"), 1))
                    line.setZValue(-1)
                    self.scene.addItem(line)

    def update_robots(self):
        """Cập nhật robot trên bản đồ từ WebSocketListener."""
        robots = self.ws_listener.get_robot_data()

        # Xóa các robot cũ trước khi vẽ lại
        for item in self.scene.items():
            if isinstance(item, QGraphicsEllipseItem) and item.data(0) == "robot":
                self.scene.removeItem(item)

        # Vẽ robot mới
        for robot_id, robot in robots.items():
            x = (robot["x"] - self.map_data["min_x"]) // self.map_res
            y = (robot["y"] - self.map_data["min_y"]) // self.map_res

            color = "#00ff00"  # Màu robot (mặc định xanh lá)

            ellipse = QGraphicsEllipseItem(x - self.radius * 3, y - self.radius * 3, self.radius * 6, self.radius * 6)
            ellipse.setPen(Qt.NoPen)
            ellipse.setBrush(QColor(color))
            ellipse.setZValue(2)
            ellipse.setData(0, "robot")
            ellipse.setToolTip(f"Robot ID: {robot_id}\nTheta: {robot['theta']:.2f}")  # Hiển thị thông tin
            self.scene.addItem(ellipse)

    def wheelEvent(self, event):
        """Xử lý phóng to/thu nhỏ bằng con lăn chuột."""
        zoom_factor = 1.15
        if event.angleDelta().y() > 0:
            self.view.scale(zoom_factor, zoom_factor)
        else:
            self.view.scale(1 / zoom_factor, 1 / zoom_factor)
