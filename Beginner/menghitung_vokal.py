# menghitung huruf vokal dalam kata/kalimat

# menentukan input
kata = input("masukan kata/kalimat yg akan dicek = ")
 # kecilkan semua huruf jika ada kapital
kata1 = kata.lower()

# proses
vokal = 'aiueo'
hitung = []

v = vokal.split()

for x in kata1:
    for y in v:
        if (x in y) == 1:
            print(x)
            hitung.append(x)

print(hitung)
print("jumlah huruf vokalnya adalah : ", len(hitung))