# menjumlahkan bilangan 1 hingga n

def sum_to(n):
    listku = list(range(1,n+1))
    print(listku)
    hasil = sum(listku)

    return hasil

print(f"hasil : {sum_to(5)}")


# menghitung angka dengan frekuensi kemunculan paling banyak
def duplicate(s):
    print(s)

    # mengambil tiap isi list dan menghitungnya dalam dict
    hitung = {}
    for i in s:
      hitung[i] = s.count(i)
    print(f"frekuensi list : {hitung}")

    # ambil frekuensi paling banyak
    maxi = max(hitung.values())
    print(f'frekuensi terbanyak : {maxi}')

print(duplicate([1,2,4,2]))


# menggabungkan 2 string scr bergantian

# menggabungkan 2 string secara bergantian

def mergerqu(s1, s2):
  # mengambil string terpendek antara s1 dan s2
  min_string = min(len(s1), len(s2))
  print(f'panjang string terpendek : {min_string}')

  hasil = ""

  # mencampurkan 2 string sebanyak jumlah string terpedek
  for i in range(min_string):
    hasil += s1[i] + s2[i]

  # jika salah satu string lebih panjang dr yg lain, sisa huruf akan ditempatkan di akhir
  hasil += s1[min_string:] + s2[min_string:]

  return hasil

a1 = "abcde"
a2 = "1234"
a = mergerqu(a1, a2)
print(f"hasil pencampuran kata {a1} dan {a2} : {a}")

# menemukan bilangan genap

def genap(c):
    genaplist = []
    for i in c:
        if i % 2 == 0:
            genaplist.append(i)
        else:
            continue
    print(genaplist)

listku = genap([1,2,4,5,6])


# mencari nilai minimum dalam list

def mini(x):
    s = min(x)
    return s

angka = mini([9,7,1,4,0])
print(angka)


    