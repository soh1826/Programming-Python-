#아마스빈 주문 앱           1.음료 이름 // 2. 컵 사이즈 // 3. 얼음량 // 4. 당도 // 5. 펄
#Drink <- Coffee    // <- 상속받는다.
#      <- Bubbletea // <- 상속받는다.
#Order
#  메뉴 보여주자.
#  음료 주문하자.
#  주문한 음료 보여주자.
#  총 금액 계산하자.
from order import Order

o = Order()
o.order_drink()

#아메리카노 = Coffee("아메리카노", 1800)
#아메리카노.oder() #oder로 묶어준것. 아메리카노.set_cup() 아메리카노.set_ice() 아메리카노.set_sugar으로 나눌 수도 있다.
#print(아메리카노)   #이름 : 아메리카노\t가격 : 1800원
#타로밀크티 = Bubbletea("타로밀크티", 3500)
#타로밀크티.order() #타로밀크티.set_cup() 타로밀크티.set_ice() 타로밀크티.set_sugar() 타로밀크티.set_pearl()로 나눌 수 있다.
#print(타로밀크티)