import socket


def send_message(udp_socket,dest_ip,dest_port):
    
        # 读取输入的数据
        send_data = input('请输入要发送的数据：')
    
        # 发送数据
        dest_addr = (dest_ip, dest_port)
        udp_socket.sendto(send_data.encode('GBK'), dest_addr)


def recv_message(udp_socket):

        # 接收数据
        recv_data = udp_socket.recvfrom(1000)
        print(recv_data)
        print("%s:%s" % (recv_data[1], recv_data[0].decode("gbk")))   


def main():
        # 创建套接字，udp用SOCK_DGRAM,tcp用SOCK_STREAM
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        #绑定端口
        udp_socket.bind(('',7890))

         # 输入对方的ip/port(端口号)
        dest_ip = input("请输入对方的ip：")
        dest_port = int(input("请输入对象的port："))
        while True:
                send_message(udp_socket,dest_ip,dest_port)
                recv_message(udp_socket)
    
        # 关闭
        udp_socket.close()
    


if __name__ == '__main__':
        main()
