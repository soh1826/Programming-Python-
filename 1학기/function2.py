# def input(s):
#     print(s)

# input("현재의 input() 함수는 사용자 정의 함수 입니다.")

# import random

# n=random.randint(1, 6)
# print("결과 : ", n)
# n=random.randint(1, 6)
# print("결과 : ", n)
# n=random.randint(1, 6)
# print("결과 : ", n)


#star함수 정의

# def star():
#     print("*****")

# star()
# star()
# star()

# def rolling_dice(pip, repeat):
#     for r in range(1, repeat+1):
#         n=random.randint(1, pip)
#         print(pip,"면 주사위 굴린 결과 ", r, " : ", n)

# rolling_dice(6, 1)
# rolling_dice(6, 2)
# rolling_dice(12, 0)
# rolling_dice(20, -3)

#가변인수
# print("-------가변인수-------")
# print("♡")
# print("♡", "♪")
# print("♡", "♪", "♣")
# print("♡", "♪", "♣", "♠")
# print("♡", "♪", "♣", "♠", "★")

# def p(*args):
#     string=""
#     for a in args:
#         string +=a
#     print(string)
# p("♡")
# p("♡", "♪")
# p("♡", "♪", "♣")
# p("♡", "♪", "♣", "♠")
# p("♡", "♪", "♣", "♠", "★")

#안녕 함수

# def 안녕(*args):
#     for a in args:
#         print("안녕, ", a)

# def p(space, space_num, *args):
#         string =args[0]
#         for i in range(1, len(args)):
#                 string +=(space * space_num)+args[i]
#         print(string)
# p(",",3,"▼", "♪")

#115쪽 혼자해보기
# def star(word, *args):
#         for i in args:
#                 print(word*i)

# star("♬", 3)
# star("♥", 1, 2, 3)

#p.116 ㅣ워드 인자 사용한 함수

# def fn(a, b, c, d, e):
#         print(a, b, c, d, e)

# fn(1, 2, 3, 4, 5)
# fn(10, 20, 30, 40, 50)
# fn(5, 6, 7, 8, 9)
# fn(a=1, b=2, c=3, d=4, e=5)
# fn(e=5, d=4, c=3, b=2, a=1)
# fn(1, 2, c=3, e=5, d=4)

#p.118

# def star(mark, repeat, space, space_repeat, line):
#         for i in range(1, line):
#                 string = (mark*repeat)
#                 for j in range(2, repeat):
#                         string +=(space+space_repeat)+(mark*repeat)
#                 print(string)

# star("*", 2, "+", 3, 5)
# print("---------------------------")
# star(mark="*", repeat=2, space="+", space_repeat=3, line=5)

# def star2(mark, repeat, space, space_repeat, line):
#         string = (mark*repeat)+(space+space_repeat)+(mark*repeat)
#         for n in range(line):
#                 print(string)

# star2("※", 3, "_", 2, 3)
# print("---------------------------")
# star2(mark="※", repeat=3, space="_", space_repeat=2, line=3)

#p119

# def hello(msg="안녕하세요"):
#         print(msg+".")

# hello("오랜만이에요")
# hello("강은서")
# hello()

# def hello2(name="무명", msg="안녕하세요"):
#         print(name+"님, "+msg+".")

# hello2("곽가연", "오랜만이에요")
# hello()

# def hello3(name, msg="안녕하세요"):
#         print(name+"님, "+msg+".")

# hello3("김봄이", "오랜만이에요")
# hello3("김소현")
# hello3() name을 넣어주어야 한다.

# def fn2(a, b=[]):
#         b.append(a)
#         print(b)

# fn2(3)
# fn2(5)
# fn2(10)

#p123
# def gugudan(a):
#         for i in range (2, 9+1):
#                 print("{} X {} = {}".format(a, i, a*i))
#         print("-------------------")

# gugudan(3)
# gugudan(2)

#p125
# def sum(*numbers):
#         sum_value=0
#         for number in numbers:
#                 sum_value +=number
#         return sum_value
# result=sum(1, 3)
# print("1+3=", result)
# print("1+3+5+7=", sum(1, 3, 5, 7))

#p126

# def min(*numbers):
#         min_value=numbers[0]
#         for number in numbers:
#                 if min_value<number:
#                         min_value=number
#         return min_value

# print("min(1, 3) =", min(1, 3))
# print("min(0,3, -11) =", min(0, 3, -11))

# def multi_num(multi, start, end):
#         result=[]
#         for n in range(start, end):
#                 if n % multi==0:
#                         result.append(n)
#         return result
# print("multi_num(17, 1, 200)=", multi_num(17, 1, 200))
# print("multi_num(3, 1, 200)=", multi_num(3, 1, 200))

def min_max(*args):
        min=args[0]
        max=args[0]
        for arg in args:
                if min>arg:
                        min=arg
                if max<arg:
                        max=arg
                
        return min, max
print("min_max(52, -3, 23, 89, -21)")
min_value, max_value=min_max(52, -3, 23, 89, -21)
print("최솟값 : ", min_value, "최댓값 : ", max_value)