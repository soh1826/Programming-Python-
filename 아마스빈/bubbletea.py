from drink import Drink

class Bubbletea(Drink): #Drink를 상속하는 버블티
    _pearls = ["타피오카", "코코", "젤리", "알로에"]

    def __init__(self, name, price):
        super().__init__(name, price)
        self.pearl = 0

    def set_pearl(self):
        self.pearl = input("펄을 선택하세요.(0:타피오카, 1:코코, 2:젤리, 3:알로에)")
        if self.pearl == "":
            self.pearl = 0
        else:
            self.pearl = int(self.pearl)

    def __str__(self):
        return super().__str__() + "\t펄: "+Bubbletea._pearls[self.pearl] #상속받은 부모를 부르는 문장

    def order(self): #상속 받은 것에서 중복된 것이 있다면 부모 걸 불러오는 게 더 이득!
        super().order()
        self.set_pearl()

