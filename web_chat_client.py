from flask import Flask 
from flask import render_template
from flask_socketio import SocketIO 

app = Flask(__name__) #플라슽크 인스턴스 생성
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

#connected라는 이벤트를 받을거야
@socketio.on("connected")
def connect_handler():
    socketio.emit("response", {"nickname" : "서버" , "message" : "새로운 유저 입장"})  #response라는 이름의 소켓으로 뒤에 값을 보낸다

@socketio.on("chat")
def event_handler(json):
    json["nickname"]= json["nickname"].encode("latin1").decode("utf-8")
    json["message"]= json["message"].encode("latin1").decode("utf-8")

    socketio.emit("response",{"nickname":json["nickname"], "message":json["message"]})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=15000, debug=True)  #소켓 사용할거라서 


