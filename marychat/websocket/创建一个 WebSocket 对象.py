WebSocket WebSocket
  in DOMString url,
  in optional DOMString protocols
);

WebSocket WebSocket(
  in DOMString url,
  in optional DOMString[] protocols
);

#url
# 表示要连接的URL。这个URL应该为响应WebSocket的地址。
#protocols 可选
#可以是一个单个的协议名字字符串或者包含多个协议名字字符串的数组。
# 这些字符串用来表示子协议，这样做可以让一个服务器实现多种WebSocket子协议（
# 例如你可能希望通过制定不同的协议来处理不同类型的交互）。
# 如果没有制定这个参数，它会默认设为一个空字符串。
#构造器方法可能抛出以下异常：

#SECURITY_ERR
#试图连接的端口被屏蔽。