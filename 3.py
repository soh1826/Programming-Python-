#굿즈 주문 앱 - 애니 종류를 보여주고 그 애니의 여러 굿즈들을 주문 받는 앱입니다.
import sys

class Anseodong:

    def __init__(self, name, price, kind):
        self.name=name
        self.price=price
        self.kind=kind

    def __str__(self):#주문 목록
        return "애니 : "+self.name+"\t종류: "+self.kind+"\t가격: "+str(self.price)+"원"

class Gahiri(Anseodong):#애니 종류 가히리 관련 굿즈
    _goods=["본고레 핀버튼", "바리아 핀버튼", "캬발로네 핀버튼", "본고레 포스터", "바리아 포스터", "캬발로네 포스터", "본고레 스트랩", "바리아 스트랩", "아르꼬발레노 스트랩", "본고레 스티커", "바리아 스티커", "아르꼬발레노 스티커"]

    def __init__(self, name, price, kind):
        super().__init__(name, price, kind)
        self.goods=0
    
    def set_goods(self):#굿즈 선택하기
        self.goods=input("굿즈를 선택하십시오.(0: 본고레 핀버튼 1: 바리아 핀버튼 2: 캬발로네 핀버튼 3: 본고레 포스터 4: 바리아 포스터 5: 캬발로네 포스터 6: 본고레 스트랩 7:바리아 스트랩 8: 아르꼬발레노 스트랩 9:본고레 스티커 10: 바리아 스티커 11: 아르꼬발레노 스티커) : ")
        if self.goods=="":#만약 엔터를 치면 바로 종료.
            sys.exit()
        else:#엔터가 아니면 입력받은 값을 넣어주는 것.
            self.gooods = int(self.goods)
    
    def __str__(self):#주문 목록에 선택한 굿즈도 같이 출력함.
        return super().__str__()+"\t굿즈: "+Gahiri._goods[int(self.goods)]
    
    def order(self):
        self.set_goods()


class Hiroaka(Anseodong):#히로아카 관련 굿즈 
    _goods=["미도리야 이즈쿠 팔찌", "토도로키 쇼토 팔찌", "바쿠고 카츠키 팔찌", "미도리야 이즈쿠 쿠션", "토도로키 쇼토 쿠션", "바쿠고 카츠키 쿠션", "UA 스티커", "빌런 연합 스티커"]

    def __init__(self, name, price, kind):
        super().__init__(name, price, kind)
        self.goods=0
    
    def set_goods(self):#굿즈 선택하는 것.
        self.goods=input("굿즈를 선택하십시오.(0: 미도리야 이즈쿠 팔찌 1: 토도로키 쇼토 팔찌 2: 바쿠고 카츠키 팔찌 3: 미도리야 이즈쿠 쿠션 4: 토도로키 쿠션 5: 바쿠고 카츠키 쿠션 6: UA 스티커 7: 빌런 연합 스티커) : ")
        if self.goods=="":#만약 엔터를 치면 바로 종료됨.
            sys.exit()
        else:#아니면 입력받은 굿즈를 넣어줌.
            self.gooods = int(self.goods)
    
    def __str__(self):#선택한 굿즈를 주문 목록에과 같이 출력함
        return super().__str__()+"\t굿즈: "+Gahiri._goods[int(self.goods)]
    
    def order(self):
        self.set_goods()

class Cuji(Anseodong):#제일복권을 선택했을 때
    _cuji=["가정교사 히트맨 리본", "문호스트레이 독스"]
    _cuji1=["Last one : 본고레 대형 쿠션", "A : 사와다 츠나요시&리본 쿠션", "B : 고쿠데라 하야토&야마모토 타케시 쿠션", "C : 히바리 쿄야&로쿠도 무크로 쿠션", "D : 본고레 담요", "E : 바리아 담요", "F : 핀버튼"]
    _cuji2=["Last one : 데드애플 대형 쿠션", "A : 다자이 오사무&나카하라 츄야 쿠션", "B : 나카지마 아츠시&아쿠타카와 류노스케 쿠션", "C : 무장탐정사 담요", "D : 포트마피아 담요", "E : 암흑시대 담요 ", "F : 핀버튼"]

    def __init__(self, name, price, kind):
        super().__init__(name, price, kind)
        self.cuji=0
    
    def set_cuji(self):#뽑고 싶은 제일복권을 선택
        self.cuji=input("뽑고 싶은 제일 복권을 선택하십시오.(0: 가정교사 히트맨 리본, 1: 문호스트레이 독스) : ")
        if self.cuji=="":#엔터를 치면 종료
            sys.exit()
        else:#아니면 입력받은 것을 넣어줌.
            self.cuji=int(self.cuji)
    
    def __str_cuji(self):
        if self.cuji==0:#0번을 선택했을 시 CUJI1에 담긴 리스트에서 한가지 랜덤으로 선택
            random.choice(cuji1)
        elif self.cuji==1:#1번을 선택했을 시 CUJI2에 담긴 리스트에서 한가지 랜덤으로 선택
            random.choice(cuji2)
    
    def __str__(self):#랜덤으로 뽑은 제일복권을 경우에 따라 출력합니다.
        if self.cuji==0:
            return super().__str__+"\t선택한 제일복권 : "+Cuji._cuji1[self.cuji]
        elif self.cuji==1:
            return super().__str__+"\t선택한 제일복권 : "+Cuji._cuji2[self.cuji]
    
    def order(self):
        super().order()
        self.set_cuji()


class Order:
    _menus=[Gahiri("가정교사 히트맨 리본", 5000, "핀버튼"),Gahiri("가정교사 히트맨 리본", 5000, "핀버튼"),Gahiri("가정교사 히트맨 리본", 5000, "핀버튼"), Gahiri("가정교사 히트맨 리본", 8000, "포스터"), Gahiri("가정교사 히트맨 리본", 8000, "포스터"),Gahiri("가정교사 히트맨 리본", 8000, "포스터"),Gahiri("가정교사 히트맨 리본", 7000, "스트랩"), Gahiri("가정교사 히트맨 리본", 7000, "스트랩"),Gahiri("가정교사 히트맨 리본", 7000, "스트랩"),Gahiri("가정교사 히트맨 리본", 4000, "스티커"),  Gahiri("가정교사 히트맨 리본", 4000, "스티커"),Gahiri("가정교사 히트맨 리본", 4000, "스티커"),Hiroaka("나의 히어로 아카데미아", 9000, "팔찌"), Hiroaka("나의 히어로 아카데미아", 9000, "팔찌"),Hiroaka("나의 히어로 아카데미아", 9000, "팔찌"),Hiroaka("나의 히어로 아카데미아", 15000, "쿠션"), Hiroaka("나의 히어로 아카데미아", 15000, "쿠션"),Hiroaka("나의 히어로 아카데미아", 15000, "쿠션"), Hiroaka("나의 히어로 아카데미아", 4000, "스티커"), Hiroaka("나의 히어로 아카데미아", 4000, "스티커")]
    _menus1=[Cuji("가정교사 히트맨 리본", 12000, "제일복권"), Cuji("문호스트레이 독스", 12000, "제일복권")]
    def __init__(self):
        self.order_menu=[]
        self.order_menu1=[]
        self.order=None#딱히 넣을 값이 없어서 사용했습니다.
    
    def show_menu(self):#메뉴를 보여줄 역할을 할겁니다.
        print("0: 가정교사 히트맨 리본 1: 나의 히어로 아카데미아 2: 제일복권")

    def sum_price(self):#값을 계산합니다.
        sum=0
        if self.order==2:#제일복권을 선택했을 시 _muens1에서
            for anseodong in self.order_menu1:
                sum+=anseodong.price
        else:#제일복권이 아닌 것을 선택했을 시 _menus에서
            for anseodong in self.order_menu:
                sum+=anseodong.price
            
        return sum
        
    def order_anseodong(self):
        while True:
            self.show_menu()#메뉴를 보여줍니다.
            self.order=input("애니를 선택하십시오. : ")
            if self.order=="":#엔터를 치면 종료합니다.
                break
            if self.order==2:#제일복권을 선택했을 시
                anseodong=Order._menus1[int(self.order)]#뽑을 제일복권을 정합니다.
                anseodong.order()#주문한 굿즈를 리스트에 추가합니다.
            else:#나머지 애니를 선택했을 시.
                anseodong=Order._menus[int(self.order)]#굿즈를 정합니다.
                anseodong.order()#주문한 굿즈를 리스트에 추가합니다.
            self.order_menu.append(anseodong) #주문 목록을 보여줍니다.
            self.order_menu1.append(anseodong) #주문 목록을 보여줍니다.
            for anseodong in self.order_menu:#
                print(anseodong)
            print("총금액: "+str(self.sum_price()+2500)+"원")

o=Order()
o.order_anseodong()