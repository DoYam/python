class CarMixin:
    def ready(self):
        print("믹스인 레디")
    def start(self):
        print("{}가  {}속도로 달립니다".format(self.name, self.speed))
    
class Performance:
    def __init__(self, name, speed):
        self.name= name
        self.speed = speed
        self.ready()  #카믹인 클래스의 함순데 믹스인 된 순간 쓸 수 있게 됨

class SuperCar(CarMixin, Performance): #클래스 믹스인
    def show_info(self):
        print("{}는 {}속도의 성능입니다".format(self.name, self.speed))
    def start(self):  #카믹인의 start함수가 무효화 = 오버라이딩
        super().start()  #카믹인의 start함수 사용 가능 super메소드(부모 클래스 호출)
        print("스타트")

s = SuperCar("람보르", 300)
s.show_info()
s.start()
