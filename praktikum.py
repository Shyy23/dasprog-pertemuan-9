"""
Nama : Syahrul Hidayatulloh
NIM : 2603364
Kelas : 1C
"""

# Latihan 1 no 1 Fibonacci
def fibonacci(jumlah_deret):
    list_deret = []
    a, b = 0, 1
    
    while jumlah_deret > 0:
        list_deret.append(a)
        a, b = b, a + b  # Update nilai a dan b secara bersamaan
        jumlah_deret -= 1

    for i in list_deret:
        print(i, end=" ")


# Latihan 1 no 2 Volume Tabung
def volume_tabung(r, t):
    volume = (22 * r ** 2 * t) / 7
    print(f"Volume Tabung adalah: {volume:.2f}cm")


# Latihan 1 no 3 Total dan Rata-Rata
list_angka = []

def hitung_total_dan_rata(*angka):
    total = sum(angka)
    rata_rata = total / len(angka) if len(angka) > 0 else 0 
    return total, rata_rata

# # Input User
# jumlah_angka = int(input('Masukkan jumlah angka yang mau diinput: '))

# for i in range(jumlah_angka):
#     list_angka.append(int(input(f"Masukkan Angka ke-{i+1} : ")))

# # Memanggil fungsi (unpack 2 nilai return)
# total_nilai, rata_rata_nilai = hitung_total_dan_rata(*list_angka)

# print(f"Total     : {total_nilai}")
# print(f"Rata-rata : {rata_rata_nilai:.2f}")




# Latihan 2 Login (password)

def login():
    password_benar = "Latihan"
    batas_salah = 3

    print("Selamat datang di sistem login")
    while batas_salah > 0:
        input_password = input("Masukkan Password: ")
        
        if input_password == password_benar:
            print("Login berhasil! Selamat datang.")
            break
        else:
            batas_salah -= 1
            if batas_salah > 0:
                print(f"Password salah! Kesempatan tersisa: {batas_salah}\n")
            else:
                print("Kesempatan habis. Anda keluar dari menu login.")

# Jalankan fungsi login
# login()

# Latihan 3 selisih waktu
def hitung_inputan_detik_waktu():
    jam = int(input("Masukkan Jam: "))
    menit = int(input("Masukkan Menit: "))
    detik = int(input("Masukkan Detik: "))

    total = (jam * 3600) + (menit * 60) + detik
    return  total

def hitung_selisih_waktu():

    print("--- Input Waktu Mulai ---")
    total_mulai = hitung_inputan_detik_waktu()

    print("\n--- Input Waktu Selesai ---")
    total_selesai = hitung_inputan_detik_waktu()

    selisih_detik = total_selesai - total_mulai

    if selisih_detik < 0:
        selisih_detik += 24 * 3600

    jam = selisih_detik // 3600
    sisa_detik = selisih_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60

    print("\n--- Hitung Selisih ---")
    print(f"Output: {jam} jam - {menit} menit - {detik} detik")

# Jalankan fungsi
hitung_selisih_waktu()