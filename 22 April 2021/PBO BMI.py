class pasien:
    jumlahPasien = 0

    def __init__(self, nama, berat, tinggi):
        self.nama = nama
        self.berat = berat
        self.tinggi = tinggi
        pasien.jumlahPasien += 1

    def bmi(self):
        bmi = self.berat/(self.tinggi**2)
        print("BMI = ", bmi)
        if bmi < 18.5:
            print("Kekurangan berat badan.")
        elif bmi > 18.5 and bmi <=24.9:
            print("Berat badan ideal.")
        elif bmi > 24.9 and bmi <= 29.9:
            print("Berat badan berlebih.")
        else:
            print("Obesitas.")

    def beratIdeal(self):
        ideal = (self.tinggi*100 - 100) - (10/100 * (self.tinggi*100 - 100))
        print("BB Ideal = ", ideal)
        print("---------------------")

pasien1 = pasien("Sergei", 110, 1.7)
pasien2 = pasien("Simov", 62, 1.65)

pasien1.bmi()
pasien1.beratIdeal()

pasien2.bmi()
pasien2.beratIdeal()

print("Jumlah pasien : ", pasien.jumlahPasien)
