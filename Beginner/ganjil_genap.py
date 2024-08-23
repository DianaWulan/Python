# menghitung jumlah bilangan ganjil dan genap

angka = list(range(1,6))
print(angka)

# 
ganjil = []
genap = []
x = 0

# pisahkan yg ganjil dan genap
for x in angka:
    if x % 2 == 0:
      print(x)
      genap.append(x)
    else:
       ganjil.append(x)

# hasil
print("ganjil = ", ganjil)
print("jumlah angka ganjil = ", len(ganjil))
print("genap = ", genap)
print("jumlah angka ganjil = ", len(genap))
