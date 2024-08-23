# membuat list
print("--membuat list--")
listku = [1,2,3,4,5,6,7]
print(listku)

# membalik list
print("--membalik list--")
listku.reverse()
print(f"setelah dibalik {listku}\n")

# menentukan bilangan prima
print("--menentukan bilangan prima--")
for x in listku:
    if x > 1:
         if (x % 2) == 1:
             print(f"{x} adalah bilangan prima")
         else:
             print(f"{x} adalah BUKAN bilangan prima")
    else:
        continue