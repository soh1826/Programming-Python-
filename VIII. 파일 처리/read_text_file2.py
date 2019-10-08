fi= open("hisstory.ama", "r", encoding="utf8")
sum = 0
while True:
    data = fi.readline()
    if not data:
        break
    # print(data, end="")
    l=data.split()
    sum += int(l[1])
print("총금액 : "+str(sum))
fi.close()
