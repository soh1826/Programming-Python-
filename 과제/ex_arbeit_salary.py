h=input("일주일에 몇시간 일하는 가 : ")
h=int(h)
w=input("몇주 일하는 가 : ")
w=int(w)
s=input("시급 얼마인가 : ")
s=int(s)
sum= int(h)*int(w)*int(s)

if h>=15:
    sum+=(h/5)

print("알바비 : ", sum)
