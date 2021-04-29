class Siswa:
    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #Decorator
    @property
    def nis(self):
        pass

    #Get
    @nis.getter
    def nis(self):
        return self.__nis

    #Set
    @nis.setter
    def nis(self, nis):
        self.__nis = nis

fais = Siswa(15973, "Supreme Leader", "XI MIPA 5")

print(fais.nis)
fais.nis = 123456
print(fais.nis)
