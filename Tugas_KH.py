def hitung_jarak_terkoreksi():
    print("hitung jarak terkoreksi!")
    print()
    print('diketahui')
    
    #memasukkan data
    suhu = float(input("masukkan suhu(C): "))
    tekanan = float(input("masukkan tekanan(hPa): "))
    tinggi = float(input("masukkan tinggi(m): "))

    #menghitung nilai KA dan L
    KA = (279.67 - (79.535 * tekanan)/(273.15 + suhu)) * (10**-6)
    jarak_terkoreksi = tinggi * (1 + KA)

    print()
    print('jawab')
    print("KA: ", KA)
    print("L: ", jarak_terkoreksi)

hitung_jarak_terkoreksi()
