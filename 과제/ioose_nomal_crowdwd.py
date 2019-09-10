sum=0
while True:
    in0=input("탑승객 수 : ")
    if in0=="-1":
        break
    in0=int(in0)
    out=input("하차객 수 : ")
    out=int(out)
    sum+=in0-out

print("버스 안에 있는 사람의 수 : ", sum)

if 0<=sum<=10:
    print("여유")
elif 10<=sum<=20:
    print("보통")
elif 20<=sum<=30:
    print("혼잡")