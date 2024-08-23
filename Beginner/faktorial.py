# menentukan faktorial dari sebuah angka
angka = int(input("masukan angka = "))
faktorial = 1 # inisisasi angka faktorial awal

for x in range(1, angka+1):
    #print("x adalah ", x)
    faktorial *= x # perkalian faktorial dan peampungan angka terjadi
    print(faktorial)

print(f"hasil !{angka} = {faktorial}")
