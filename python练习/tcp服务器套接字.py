import socket


def main():
    # 1 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2 绑定本地端口
    tcp_server_socket.bind(('',7893))
    
    # 3 让默认的套接字由主动变为被动listen
    tcp_server_socket.listen(128)
    
    while True:
        print('等待请求.....')
    
        # 4 等待客户端的链接 accept
        new_client_socket, client_addr = tcp_server_socket.accept()
        print('收到来自%s的请求:'%str(client_addr))

        while True:

            # 接受客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print('收到的请求：'+recv_data.decode('gbk'))

            
             # 回送一部分数据给客户端
            if recv_data:
                new_client_socket.send('完成请求'.encode('gbk'))
            else:
                 break
        # 5 关闭套接字
        new_client_socket.close()
        print()
    tcp_server_socket.close()
    
if __name__ == '__main__':
    main()
