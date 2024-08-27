# menghitung jumlah angka dalam list

listku = [2,4,6,8,10]

a = sum(listku)
print(f'total isi listku = {a}')


# meremove huruf suatu kata

def remove_char(s, char):
    hasil = ""
    for i in s:
      if i != char:
        hasil += i
    return hasil

b = remove_char("Hello world","o")
print(f'hasilnya adalah = {b}')


def palindrome(c):
    x = c
    y = c[::-1]

    if x == y:
        print(True)
    else:
        print(False)

print(palindrome('madam'))
print(palindrome('hello'))


# mencari bilangan terbesar
def max_a(angka):
    z = max(angka)
    return z

b = [1,2,3,4,5,6,7]
print(max_a(b))


# merger 2 list dan mengurutkannya scr asc

def merger_a(a,b):
    c = a + b
    print(f'hasil penggabungan 2 list : {c}')
    c.sort()
    return c

list1 = [5,6,7,8]
list2 = [1,2,3,4]
print(merger_a(list1, list2))

    