'''
서버
1.소켓생성
2.바인딩
3.접속대기
4.접속수락
5.데이터 송/수신
6.접속종료
'''
import socket
print("1.소켓생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 123.123.123.123 IP버전4를 사용한 인터넷 주소 체계를 쓴다는 내용
# SOCK_DGRAM - UDP
# SOCK_STREAM - TCP

print("2.바인딩")
#운영체제에 이 IP와 이 PORT쓸거라고 말 하는거
#소켓은 운영체제의 허락을 받는 개념
sock.bind(("",20000))
#튜플형태로 주소(서버는 필요 없어 어차피내컴퓨터)랑 포트번호 넘겨

print("3.접속대기")
sock.listen()

print("4.접속수락")
c_sock , addr = sock.accept()
 #접속된 클라이언트의 소켓(새롭게 만들어진소켓)이랑 주소가 리턴
 #리슨하고있는 소켓에 클라이언트의 요청이 오면 접속시켜서 새로운 소켓 생성

print("5.데이터 송/수신")
#수신
receive_data = c_sock.recv(1024)
print("수신된 데이터 : {}".format(receive_data))

print("6.접속종료")
c_sock.close()
sock.close()
#접속 종료를 꼭 해야해
