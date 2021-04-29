class Siswa:
    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    def getNis(self):
        return self.__nis

    def setNis(self, nis):
        self.__nis = nis

fais = Siswa(15973, "Supreme Leader", "XI MIPA 5")

print(fais.getNis())
fais.setNis(10000)
print(fais.getNis())
