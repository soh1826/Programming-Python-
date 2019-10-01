fi= open("hisstory.ama", "r", encoding="utf8")

while True:
    data = fi.readline()
    if not data:
        break
    print(data, end="")
fi.close()
