x=int(input())

if x<=30:
    print(2000)
else:
    if x%10 !=0:
        print(((x-30)//10)*1000+2000+1000)
    else:
        print(((x-30)//10)*1000+2000)
