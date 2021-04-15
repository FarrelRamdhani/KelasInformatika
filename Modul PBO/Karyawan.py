class Karyawan:
    jumlahKaryawan = 0

    def __init__(self, nama, gaji, umur):
        self.nama = nama
        self.gaji = gaji
        self.umur = umur
        Karyawan.jumlahKaryawan += 1

    def tampilkan_jumlah():
        return(Karyawan.jumlahKaryawan)

    def tampilkan_profil(self):
        return(self.nama, self.gaji, self.umur)

# Membuat objek pertama dari kelas Karyawan
karyawan1 = Karyawan("Sarah", 1000000, 10)
# Membuat objek kedua dari kelas Karyawan
karyawan2 = Karyawan("Budi", 2000000, 10)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("Total karyawan :", Karyawan.tampilkan_jumlah())
