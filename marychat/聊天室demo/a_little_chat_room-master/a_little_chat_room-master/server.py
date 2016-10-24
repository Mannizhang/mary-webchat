from tornado import websocket, web, ioloop


class MainHandler(web.RequestHandler):
    def get(self):
        self.render("client.html")

application = tornado.web.Application


#添加了user元组
users = []


class SocketHandler(websocket.WebSocketHandler):
    def open(self):
        users.append(self)
        print("连接成功")

    def on_connection_close(self):
        print("关闭了")

    def on_message(self, message):
        print(message)
        for ws in users:
            ws.write_message(message)

    def on_finish(self):
        print("finish")

    def on_close(self):
        print("连接关闭")
        users.remove(self)

class registerHandler(websocket.WebSocketHandler):
    def post(self): self:<__main__.registerHandler object at 0x10fd723c8>




application = web.Application([
    (r"/", MainHandler),
    (r"/ws", SocketHandler),
])

if __name__ == "__main__":
    application.listen(9999)
    ioloop.IOLoop.instance().start()
