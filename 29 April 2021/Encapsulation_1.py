#Encapsulation 1
class Hero:
    jumlah = 0

    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    #Get
    def getName(self):
        return(self.__name)

    def getHealth(self):
        return(self.__health)

    #Set
    def getAttack(self, attserang):
        self.__health -= attserang

#Init Object
lina = Hero("Lina", 10)

#Print Private
print(lina.getName())
print(lina.getHealth())

#Attacked
lina.getAttack(5)
print(lina.getHealth())
