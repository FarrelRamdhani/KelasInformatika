from Siswa import siswaDatabase

#Display dan Testing Class

#Init
siswa1 = siswaDatabase()
siswa2 = siswaDatabase()
siswa3 = siswaDatabase()
siswa4 = siswaDatabase()
siswa5 = siswaDatabase()

#Memasukkan data profil (contoh siswa 5 tidak ada identitas)
siswa1.profilSiswa("Alexey", "XI 5", 1)
siswa2.profilSiswa("Al Marooosh", "XI 9", 8)
siswa3.profilSiswa("Badroon", "XI IIS", 27)
siswa4.profilSiswa("Halmo", "X 1", 33)

#Memasukkan data nilai (contoh siswa 2 dan 5 tidak ada nilai)
siswa1.nilaiSiswa(81, 98, 88, 90)
siswa3.nilaiSiswa(88, 79, 63, 81)
siswa4.nilaiSiswa(100, 91, 89, 94)

#Display Seluruh Data Profil
print(siswa1.displayProfilSiswa())
print(siswa2.displayProfilSiswa())
print(siswa3.displayProfilSiswa())
print(siswa4.displayProfilSiswa())
print(siswa5.displayProfilSiswa())

#Display Seluruh Nilai Siswa
print(siswa1.displayNilaiSiswa())
print(siswa2.displayNilaiSiswa())
print(siswa3.displayNilaiSiswa())
print(siswa4.displayNilaiSiswa())
print(siswa5.displayNilaiSiswa())

#Display Jumlah Siswa
print(siswaDatabase.jumlahSiswa())
