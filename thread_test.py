#쓰레드 = 일꾼
import time
import threading

def order():
    for i in range(5):
        print("주문받기 {}".format(i))
        time.sleep(1)

def send():
    for i in range(5):
        print("우편발송 {}".format(i))
        time.sleep(0.5)

# order()
# send()   
#쓰레드 1개

th1 = threading.Thread(target = order)
th2 = threading.Thread(target = send)

th1.daemon = True
th2.daemon = True

th1.start()
th2.start()
#쓰레드 2개로 구동 메인쓰레드는 따로 전체적으로 한 개