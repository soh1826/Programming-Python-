from coffee import Coffee
from bubbletea import Bubbletea

class Order:
    _menus = [Coffee("아메리카노", 1800), Bubbletea("딸기요거트", 3500)]

    def __init__(self):
        self.order_menu = []
        self.order = None #자바에서 NULL과 같은 의미 - 딱히 넣을 값이 없을 때 사용.
    
    def show_menu(self):
        print("0: 아메리카노 1800원, 1: 딸기요거트 3500원")
    
    def sum_price(self):
        sum = 0
        for drink in self.order_menu:
            sum += drink.price
            
        return sum
    
    def order_drink(self):
        #반복▼
        while True:
            #   메뉴 보여주자
            self.show_menu()
            #   주문 받자.
            #   음료 선택하자.
            self.order = input("음료를 선택하세요: ")
            #       음료 객체 생성하자
            #0 -> Coffee("아메리카노", 1800)
            #1 -> Bubbletea("딸기요거트", 3500)
            if self.order == "":    #메뉴 선택안하고 그냥 엔터치면 주문 끝
                break
            if int(self.order)==0:
                drink=Coffee("아메리카노", 1800)
            elif int(self.order)==1:
                drink=Bubbletea("딸기 버블티", 2300)
            # drink = Order._menus[int(self.order)]
            #       음료 옵션 정하자.
            drink.order()
            #   주문한 음료 리스트에 추가하자.
            self.order_menu.append(drink)
            #반복▲
            #주문한 음료 출력하자.
            for drink in self.order_menu:
                print(drink)
            #   금액 합계 구하자.
            print("총금액: "+str(self.sum_price())+"원")

                  
o = Order()
o.order_drink()

#아메리카노 = Coffee("아메리카노", 1800)
#아메리카노.oder() #oder로 묶어준것. 아메리카노.set_cup() 아메리카노.set_ice() 아메리카노.set_sugar으로 나눌 수도 있다.
#print(아메리카노)   #이름 : 아메리카노\t가격 : 1800원
#타로밀크티 = Bubbletea("타로밀크티", 3500)
#타로밀크티.order() #타로밀크티.set_cup() 타로밀크티.set_ice() 타로밀크티.set_sugar() 타로밀크티.set_pearl()로 나눌 수 있다.
#print(타로밀크티)