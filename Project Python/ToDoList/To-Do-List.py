# to-do list

def main():
  #list penampung tugas
  tugas = []

  #menu
  while True:
    print("\n--Welcome to nana's to-do list!--\nSilahkan pilih menu dibawah ini:")
    print("1. Tambahkan Tugas")
    print("2. Lihat Tugas")
    print("3. Tandai Tugas Sebagai Selesai")
    print("4. Keluar")
    
    #terima input user
    masukan = input("menu yang dipilih: ")
    
    #memproses input
    # input 1
    print()
    if masukan == '1':
      jum_tugas = int(input("berapa banyak tugas yg ingin ditambahkan? : "))

      #tambahkan ke list tugas
      for i in range(jum_tugas):
        x = input("masukan tugas: ")
        #tugas baru ditandai sebagai selesai=false
        tugas.append({'tugas': x, 'selesai': False})
        print("tugas berhasil ditambahkan!")

    # input 2
    elif masukan == '2':
      print()
      print("---List Tugas Anda---")
      for index, aksi in enumerate(tugas):
        if aksi['selesai']:
          status = "Selesai"
        else:
          status = "Belum selesai"
        #cetak tugas
        print(f"{index + 1}. {aksi['tugas']} - {status}")

    # input 3
    elif masukan == "3":
      print()
      #mengambil nomor tugas yg ingin ditandai selesai
      angka_done = int(input("tugas nomor berapa yg ingin ditandai sebagai 'selesai'?: ")) - 1

      #mengubah status tugas menjadi selesai=true
      if angka_done < len(tugas):
        tugas[angka_done]['selesai'] = True
        print("tugas berhasil ditandai sebagai selesai!")
      else:
        print('nomor tidak ditemukan')

    # input 4
    elif masukan == '4':
      z = input('anda yakin ingin keluar? (y/n): ')
    
      if z == 'y':
        print('okay, bye!')
        break
      else:
        pass

if __name__ == "__main__":
  main()