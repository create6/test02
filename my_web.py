"""


"""
import socket
import threading
from code_day14_MiniWeb.my_framework import application

class WebServer(object):

    def __init__(self):
        # 创建http_server_socket套接字
        http_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 地址的复用
        http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定地址端口   bind()
        http_server_socket.bind(("", 8082))

        # 设置为被动监听状态  listen()
        http_server_socket.listen(128)

        self.http_server_socket = http_server_socket

    def handle_client(self, new_socket):
        """为一次请求进行服务"""

        # 接收客户端的请求报文
        recv_data = new_socket.recv(4096)
        recv_data = recv_data.decode("utf-8")
        print("接收到的请求报文如下：")
        print(recv_data)

        # 在请求报文中把 请求行中的资源路径  拿出来
        request_line = recv_data.split("\r\n")[0]  # 获取请求行
        file_path = request_line.split(" ")[1]

        if file_path == "/":
            file_path = "/index.html"

        # 响应给客户端页面内容（发送响应报文 hello world）
        #
        response_line = "HTTP/1.1 200 OK\r\n"
        #response_header = "Content-Type: text/html;charset=utf-8\r\nServer: python12/1.0\r\n"
        response_header = "Server: python12/1.0\r\n"
        response_split = "\r\n"

        # 静态资源的请求
        # 因为html文件中都包含有动态资源的请求，所以我们把.html的请求也看成动态资源的请求
        # 即如果 file_name不是以.html结尾的
        if not file_path.endswith('.html'):

            try:
                with open("static" + file_path, "rb") as f:
                    response_body = f.read()
            except:
                with open("框架代码/static/404.html", "rb") as f:
                    response_body = f.read()

        # 动态资源请求响应  .html
        else:
            # 拆包 application函数返回的参数
            status ,headers , response_body =application(file_path)
            # 响应首行
            response_line ="HTTP/1.1%s\r\n"%status
            # 响应头
            # response_header = "Content-Type: text/html;charset=utf-8\r\n"  #格式要可调
            for i in headers:  # headers是列表, i是("Server", "python12/2.0\r\n")
                response_header = i[0] + ":" + i[1] + "\r\n"
            # 响应体
            response_body =response_body.encode('utf-8')





# 响应体部分（不含response_body）内容拼接
        response_data = response_line + response_header + response_split
        new_socket.send(response_data.encode("utf-8") + response_body)

        # 关闭新套接字
        new_socket.close()


    def run(self):

        while True:
            # 等待客户端的连接 accept()
            new_socket, id_port = self.http_server_socket.accept()

            # 把 一个请求 看成一个任务
            # handle_client(new_socket)
            t1 = threading.Thread(target=self.handle_client, args=(new_socket, ))
            t1.start()


        # 关闭http_server_socket套接字
        http_server_socket.close()


if __name__ == "__main__":
    # 写面向对象代码： 创建一个对象，通过调用对象的某个方法来执行代码
    web_server = WebServer()
    web_server.run()
    #
    # application('/index.html')
    # application('/xx.html')
