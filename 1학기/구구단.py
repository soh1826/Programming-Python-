for dan in range(2, 9+1):
    for i in range(1, 9+1):
        if i%2==0:
            continue
        print("{} X {} = {}".format(dan, i, dan*i))
    print("-----------------")


array=[]
for i in range(1, 10, 2):
    array.append(i)
print(array)

array2={i for i in range(1, 10, 2)}
print(array2)
array3={i*i for i in range(1, 10, 2)}
print(array3)

array4={i*i for i in range(1, 10, 2) if i*i > 30}
print(array4)