import asyncio
import websockets
import json
import threading
import time


class WebSocketListener:
    def __init__(self, uri="ws://127.0.0.1:8080/ws/robots"):
        self.uri = uri
        self.robot_data = {}  # Bộ nhớ đệm dữ liệu robot
        self.ws_running = True  # Cờ điều khiển WebSocket
        self.thread = threading.Thread(target=self.run_websocket_loop, daemon=True)
        self.thread.start()  # Bắt đầu luồng WebSocket

    def run_websocket_loop(self):
        """Tạo event loop riêng cho WebSocket."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.listen_robot_data())

    async def listen_robot_data(self):
        """Lắng nghe WebSocket và cập nhật dữ liệu robot."""
        while self.ws_running:
            try:
                print("🔄 Kết nối WebSocket...")
                async with websockets.connect(self.uri) as websocket:
                    print("✅ WebSocket đã kết nối!")
                    while self.ws_running:
                        message = await websocket.recv()
                        data = json.loads(message)
                        self.robot_data = data  # Lưu dữ liệu vào bộ nhớ
            except (websockets.exceptions.ConnectionClosed, ConnectionError) as e:
                print(f"⚠️ WebSocket lỗi: {e}, thử kết nối lại sau 5 giây...")
                await asyncio.sleep(5)

    def get_robot_data(self):
        """Trả về dữ liệu robot hiện tại."""
        return self.robot_data

    def stop(self):
        """Dừng WebSocket khi thoát chương trình."""
        self.ws_running = False
