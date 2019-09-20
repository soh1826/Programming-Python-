#p217

l=[1, 2, 3]

try:
    print(l[1])
    print(l[2])
    # print(l[4])
except IndexError as e:
    print("인덱스 에러")
    print(e)
else:
    print("성곡적으로 모든 프로그램 실행.")