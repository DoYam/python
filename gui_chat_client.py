import tkinter #파이썬 기본 라이브러리
import socket
from threading import Thread

IP = ""
PORT=0
#connect함수 :버튼 누르면 호출
def connect(event=None): 
    global IP, PORT
    connect_string = input_string.get()  #input_string에 주소값 존재, 그 값을 구해와
    addr = connect_string.split(":")
    IP = addr[0]
    PORT = int(addr[1])
    w_connect.destroy() #접속대상 창 닫기
    
#send_message함수  :샌드버튼 누르면 호출
def send_message(event=None):
    msg = input_msg.get() #인풋메세지로 받은 채팅 메세지를 겟하고
    sock.send(msg.encode())#인코딩해서 소켓으로 전송
    input_msg.set("")#인풋 메세지 초기화
    if input_msg == "/bye":
        sock.close()
        window.quit()
    pass

def recv_message(sock):
    while True:
        msg = sock.recv(1024)
        chat_list.insert(tkinter.END, msg.decode())
        chat_list.see(tkinter.END) 



w_connect = tkinter.Tk()
w_connect.title("접속대상")  
#라벨
tkinter.Label(w_connect, text = "접속대상").grid(row=0, column=0)
input_string = tkinter.StringVar(value = "127.0.0.1 : 8765")
#엔트리
input_addr = tkinter.Entry(w_connect, textvariable = input_string, width =20)
input_addr.grid(row=0, column=1)
#버튼
c_button = tkinter.Button(w_connect, text="접속하기", command = connect)
c_button.grid(row=0, column=2, padx=5, pady=5)

#창의 크기
width = 330
height = 45

#화면의 가로세로길이(해상도)
screen_width = w_connect.winfo_screenwidth()
screen_height = w_connect.winfo_screenheight()
#창을 정가운데 뜨게 하고 싶어
x= int((screen_width/2)-(width/2))
y= int((screen_height/2)-(height/2))
w_connect.geometry("{}x{}+{}+{}".format(width, height,x,y))
w_connect.mainloop()

#채팅 입력창 만들기
window = tkinter.Tk()
window.title("클라이언트")
#채팅이 보여질 창 만들기
frame = tkinter.Frame(window) #프레임 생성
scroll = tkinter.Scrollbar(frame)#스크롤 만들기, 프레임에 속한다
scroll.pack(side =tkinter.RIGHT, fill = tkinter.Y)
#창 생성
#tkinter의 리스트박스프레임에 속하고, 높이, 너비,y축 스크롤로 set한다
chat_list = tkinter.Listbox(frame, height =15, width = 50, yscrollcommand=scroll.set)
chat_list.pack(side = tkinter.LEFT, fill = tkinter.BOTH, padx=5, pady=5)
frame.pack()  #프레임 안에 챗리스트와 스크롤을 팩한다

input_msg = tkinter.StringVar() #티킨터 스트링 입력변수
#엔트리
inputbox = tkinter.Entry(window, textvariable = input_msg) #메세지를 입력창(엔트리)에 연결
inputbox.bind("<Return>", send_message)
#side = 정렬, fill = 화면에 꽉 채우겠다, expand= 리사이즈로 늘어났을 떄 확장한다
inputbox.pack(side = tkinter.LEFT, fill = tkinter.BOTH, expand = tkinter.YES, padx=5,pady=5)
#버튼
send_button = tkinter.Button(window, text="전송", command = send_message)
send_button.pack(side = tkinter.RIGHT, fill = tkinter.X, padx=5, pady=5)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))

th = Thread(target = recv_message ,args = (sock, ))
th.daemon = True
th.start()


window.mainloop()

