class Person(object):
    def __init__(self, name, idNumber):
        self.name = name
        self.idNumber = idNumber

    def display(self):
        print(self.name)
        print(self.idNumber)

class Employee(Person):
    def __init__(self, name, idNumber, salary, post):
        Person.__init__(self, name, idNumber)
        self.salary = salary
        self.post = post

a = Employee("Rachess", 19216811, 60000000, "Supreme Leader")
a.display()
