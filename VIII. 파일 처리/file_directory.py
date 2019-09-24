import os

data=os.listdir("c:/Users")

for d in data:
    print(d)
    print("is Directory?:"+str(os.path.isdir(d)))
    print("is file?: "+str(os.path.isfile(d)))