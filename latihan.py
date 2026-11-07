def a(x):
    print(x * 2)

def b(x):
    return x * 2

hasil = b(3)
print(hasil)

def minmax(data):
    return min(data), max(data)

min_max = minmax([1, 5, 9, 7])
a, b = minmax([12, 10, 23, 7])
print(min_max)
print(a, b)

def garis(panjang=20, simbol="-"):
    print(simbol*panjang)


garis()
garis(10, "=")

def vol_balok(t,p,l = 2):
    volume = p * l * t
    return volume

print(vol_balok(10, 5, 2))
print(vol_balok(12, 10, 7))
print(vol_balok(p = 3, l = 4, t=5))
print(vol_balok(2,3))

def urutan_angka(*angka):
    print(f"nilai yang diinput {angka}")

urutan_angka()

def urutan_angka_2(**angka):
    for i, x in angka.items():
        print(i,x)