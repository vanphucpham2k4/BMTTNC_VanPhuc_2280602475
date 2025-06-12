import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    def start(self):
        self.connect_and_read()

    def stop(self):
        self.io_loop.stop()

    def connect_and_read(self):
        print("Connecting to server...")
        tornado.websocket.websocket_connect(
            url="ws://localhost:8888/websocket",
            callback=self.maybe_retry_connection,
            ping_interval=10,
            ping_timeout=30,
        )

    def maybe_retry_connection(self, future) -> None:
        try:
            self.connection = future.result()
            print("Connected to server")
            self.connection.read_message().add_done_callback(self.on_message)
        except Exception as e:
            print(f"Could not reconnect, retrying in 3 seconds... Error: {e}")
            self.io_loop.call_later(3, self.connect_and_read)

    def on_message(self, future):
        message = future.result()
        if message is None:
            print("Disconnected, reconnecting...")
            self.connect_and_read()
            return

        print(f"Received word from server: {message}")

        # Tiếp tục đọc tin nhắn
        self.connection.read_message().add_done_callback(self.on_message)


def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    io_loop.add_callback(client.start)
    io_loop.start()


if __name__ == "__main__":
    main()
