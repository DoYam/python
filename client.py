'''
1.소켓생성
2.접속시도
3.데이터 송/수신
4.접속종료
'''
import socket
print("1.소켓생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("2.접속시도")
sock.connect(("127.0.0.1",20000))#접속할 대상의 ip (내컴퓨터 자기자신)

#접속 됐다는 전제 하에
print("5. 데이터 송/수신")
sock.sendall("Hello socket proramming".encode())
# 소켓 데이터 :문자열->바이트 형태로

print("6. 접속종료")
sock.close()