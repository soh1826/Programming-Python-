def show_kind():
    kind = int(input("애니를 선택하세요. 0: 가정교사 히트맨 리본 1: 나의 히어로 아카데미아 2: 문호스트레이 독스 3: 월간순정 노자키군 4: 은혼 5: 제일복권"))
    print(Anseodang[kind])
    if kind == 0:
        goods = int(input("굿즈를 선택하세요. 0: 본고레 핀버튼, 1: 바리아 핀버튼, 2: 캬발로네 핀버튼 :")  )
    elif kind == 1:
        goods = int(input("굿즈를 선택하세요. 0: 미도리야 이즈쿠 팔찌,1: 토도로키 쇼토 팔찌, 2: 바쿠고 카츠키 팔찌 : ") ) 
    elif kind == 2:
        goods = int(input("굿즈를 선택하세요. 0: 다자이 오사무 쿠션, 1: 나카하라 츄야 쿠션, 2: 아쿠타카와 류노스케 쿠션 : "))
    elif kind == 3:
        goods = int(input("굿즈를 선택하세요. 0: 노자키 우메타로 & 사쿠라 치요 포스터, 1: 카시마 유우 & 호리 마사유키 포스터, 2: 와카마츠 히로타카 & 세오 유즈키 포스터 : "))
    elif kind == 4:
        goods = int(input("굿즈를 선택하세요. 0: 사카타 긴토키 파일, 1: 타카스기 신스케 파일 2: 오키타 소고 파일 3: 카무이 파일 : "))
    elif kind == 5:
        goods = int(input("굿즈를 선택하세요. 0: 가정교사 히트맨 리본, 1: 문호스트레이 독스 : "))
    print(show[kind][goods])

# def __init__(self, name, price):
#     self.name=name
#     self.price=price

# def sum_price():
#     sum=0
#     sum+=Anseodang.price




Anseodang = [["본고레 핀버튼", "바리아 핀버튼", "캬발로네 핀버튼"],\
    ["미도리야 이즈쿠 팔찌", "토도로키 쇼토 팔찌", "바쿠고 카츠키 팔찌"],\
    ["다자이 오사무 쿠션", "나카하라 츄야 쿠션", "아쿠타카와 류노스케 쿠션"],\
    ["노자키 우메타로 & 사쿠라 치요 포스터", "카시마 유우 & 호리 마사유키 포스터", "와카마츠 히로타카 & 세오 유즈키 포스터"],\
    ["사카타 긴토키 파일", "타카스기 신스케 파일", "오키타 소고 파일", "카무이 파일"],\
    ["가정교사 히트맨 리본", "문호스트레이 독스"]]

show = [["가정교사 히트맨 리본 : 본고레 핀버튼", "가정교사 히트맨 리본 : 바리아 핀버튼", "가정교사 히트맨 리본 : 캬발로네 핀버튼"],\
    ["나의 히어로 아카데미아 : 미도리야 이즈쿠 팔찌", "나의 히어로 아카데미아 : 토도로키 쇼토 팔찌", "나의 히어로 아카데미아 : 바쿠고 카츠키 팔찌"],\
    ["문호 스트레이 독스 : 다자이 오사무 쿠션", "문호 스트레이 독스 : 나카하라 츄야 쿠션", "문호 스트레이 독스 : 아쿠타카와 류노스케 쿠션"],\
    ["월간순정 노자키군 : 노자키 우메타로 & 사쿠라 치요 포스터","월간순정 노자키군 : 카시마 유우 & 호리 마사유키 포스터", "월간순정 노자키군 : 와카마츠 히로타카 & 세오 유즈키 포스터",],\
    ["은혼 : 사카타 긴토키 파일", "은혼 : 타카스기 신스케 파일", "은혼 : 오키타 소고 파일", "은혼 : 카무이 파일"],\
    ["제일 복권 : 가정교사 히트맨 리본", "제일 복권 : 문호스트레이 독스"]]

show_kind()