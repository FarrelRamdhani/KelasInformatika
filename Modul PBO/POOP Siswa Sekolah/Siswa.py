class siswaDatabase:
    countSiswa = 0

    def __init__(self):
        siswaDatabase.countSiswa += 1

    def profilSiswa(self, nama, kelas, absen):
        self.nama = nama
        self.kelas = kelas
        self.absen = absen

    def nilaiSiswa(self, mtk, fis, kim, bio):
        self.nilaiMatematika = mtk
        self.nilaiFisika = fis
        self.nilaiKimia = kim
        self.nilaiBiologi = bio

    def displayProfilSiswa(self):
        try:
            return(self.nama, self.kelas, self.absen)
        except:
            return("", "", 0)

    def displayNilaiSiswa(self):
        try:
            return(self.nilaiMatematika, self.nilaiFisika, self.nilaiKimia, self.nilaiBiologi)
        except:
            return(0, 0, 0, 0)

    def jumlahSiswa():
        return(siswaDatabase.countSiswa)
