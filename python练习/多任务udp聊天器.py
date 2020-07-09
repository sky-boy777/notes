#coding:utf-8

import socket
import threading

def recv_msg(udp_socket):
    '''接收数据并显示'''
    while True:
       
       recv_data = udp_socket.recvfrom(1000)
       print("%s:%s" % (recv_data[1], recv_data[0].decode("gbk")))  
       
        

def send_msg(udp_socket, dest_ip, dest_port):
    '''发送数据'''
    while True:
        send_data = input('输入要发送的数据：')
        udp_socket.sendto(send_data.encode('gbk'), (dest_ip, dest_port))


def main():
    '''完成udp聊天的整体控制'''
    #1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #2. 绑定本地信息
    udp_socket.bind(("",7890))

    #3.获取对方ip和端口
    dest_ip = input('请输入对方的ip:')
    dest_port = int(input('请输入对方的port(端口)：'))

    #4. 创建两个线程，去执行相应的功能
    #接收
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    #发送
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

    t_recv.start()
    t_send.start()

if __name__ == "__main__":
    main()
