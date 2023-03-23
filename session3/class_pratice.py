class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def introduce(self):
        print(f"안녕하세요. 제 이름은 {self.name}이고, 나이는 {self.age}살이며, 제 키는 {self.height}")
    def yell(self):
        print("아?")

class Developer(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    def yell(self):
        print("어?")

class Designer(Person):
    keyboard = "기계식"
    def __init__(self, name, age, height, disaese):
        super().__init__(name, age, height)
        self.disaese = disaese

class ProductManager(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    def yell(self):
        print("개발자님 여기 오류있어요")
    def aging(self):
        self.age += 2
        self.height -= 5
        print("개발자를 새로 뽑아야하나...")
        Designer.keyboard = "멤브레인"


d1 = Developer("하하", 21, 187)
d2 = Designer("호호", 22, 150, "불치병")
p1 = ProductManager("히히", 22, 165)

d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
p1.introduce()
p1.yell()
p1.aging()







    

