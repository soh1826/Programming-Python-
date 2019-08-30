class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def eat(self, food):
        print(self.name+"가 "+food+"을 먹습니다.")

    def __str__(self):
        return self.name+"는 "+str(self.age)+"살입니다."

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary=salary

    def work(self):
        print("일을 합니다.")

    def gst_salary(self):
        print("급료를 받습니다.")
        return self.salary

e=Employee("송골매", 25, 2500)
print(e)
e.eat("밥")
e.work()
r=e.gst_salary()
print("급료는 "+str(r)+"만 원 입니다.")