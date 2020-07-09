import socket


def main():
    #1 创建套接字
    tcp_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2 链接服务器
    #tcp_socket.connect(("192.168.200.0",6000))
    server_ip = input('请输入服务器的ip:')
    server_port = int(input('请输入服务器的端口号(port):'))
    server_addr = (server_ip,server_port)
    tcp_socket.connect(server_addr)
    

    
    #3 收发数据
    while True:
        send_data = input('输入要发送的内容(推出输入q)：')
        tcp_socket.send(send_data.encode('gbk'))

        if send_data == 'q':
            break
    
    #4 关闭套接字
    tcp_socket.close()


if __name__ =="__main__":
    main()
