korean = int(input("국어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
english =int(input("영어 점수 입력 : "))
java =int(input("자바 점수 입력 : "))
python = int(input("파이썬 점수 입력 : "))
jsp=int(input("JSP 점수 입력 : "))

score=korean+math+english+java+python+jsp
print("총합 : ", score)

a=score/6
print("평균 : ", a)
if a>=90:
    print("용돈 100000원")
elif a>=80:
    print("용돈 80000원")
elif a>=70:
    print("용돈 70000원")
elif a>=60:
    print("용돈 60000원")
else:
    print("용돈 50000원")