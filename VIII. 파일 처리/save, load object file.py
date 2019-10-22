import pickle

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self):
        return("이름: "+self.name+"\n나이: "+str(self.age))

per1 = Person("정유경", 18)
# print(per1)

f= open("object.bin", "wb")
pickle.dump(per1, f)
f.close()
