from order import Order
from file_manager2 import FileManager

# 주문내역 불러오고 출력하자.
file_manager = FileManager("history.bin")
history = file_manager.load()
# if history == []:
#     print("주문내역이 없습니다.")
# else:
sum=0

for h in history:
    print(h)
    sum+=h.price
print("합계 : "+str(sum)+"원")
# 지금 주문하자
o = Order()
o.order_drink()

# 주문내역 저장
file_manager.save(history+o.order_menu)



