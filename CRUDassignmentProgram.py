import getpass
import time
DataUMKM = {
    'ID1' : {'nama' : 'Umam Pet Shop',
            'bidang' : 'Pet Care',
            'noTelp' : '08123466723',
            'alamat' : 'Jl. Kenanga No. 4',
            'kota' : 'Malang'
    },
    'ID2' : {'nama' : 'Dian Knalpot',
            'bidang' : 'Otomotif',
            'noTelp' : '081234661029',
            'alamat' : 'Jl. Panglima Sudirman No. 93',
            'kota' : 'Surabaya'   
    },
    'ID3' :{'nama' : 'Santoso Tailor',
            'bidang' : 'Tekstil',
            'noTelp' : '0893457834566',
            'alamat' : 'Jl. Untung Suropati No. 23',
            'kota': 'Surabaya'
    },
    'ID4' :{'nama' : 'Cak Bobby Batik',
            'bidang' : 'Tekstil',
            'noTelp' : '08934574647387',
            'alamat' : 'Jl. Batik No. 102',
            'kota' : 'Yogyakarta'
    },
    'ID5' :{'nama' : 'Yanti Apem',
            'bidang' : 'Makanan',
            'noTelp' : '08567574647387',
            'alamat' : 'Jl. Sudirman No. 7',
            'kota' : 'Jakarta'
    }
}


def guestScreen():
    print('\n===== Yellow Pages UMKM Indonesia =====\n')
    mainMenu = int(input('''\n[1] Melihat Daftar UMKM 
                  \n[2] Login Admin/User
                  \n[3] Exit
                  \nSilahkan Pilih Main Menu [1-3]: '''))
    if mainMenu == 1:
        print('\n===== Data Record UMKM =====\n')
        for idUMKM, dataUMKM in DataUMKM.items():
            print(f"ID: {idUMKM}")
            print(f"Nama: {dataUMKM['nama']}")
            print(f"Bidang: {dataUMKM['bidang']}")
            print(f"Nomor Telepon: {dataUMKM['noTelp']}")
            print(f"Alamat: {dataUMKM['alamat']}")
            print(f"Kota: {dataUMKM['kota']}\n")
        print('''\n[1] Login Admin/User
                \n[2] Kembali ke menu awal
                \n[3] Exit
                \nSilahkan Pilih Main Menu [1-3]: ''')
        mauApa = int(input('\nApa yang ingin anda lakukan? '))
        if mauApa == 1:
            loginScreen()
        elif mauApa == 2:
            guestScreen()
        elif mauApa == 3:
            print('\nTerima kasih telah menggunakan aplikasi Yellow Pages UMKM Indonesia!\n')
            time.sleep(1)
            exit()

        else:
            print('\nSilahkan pilih inputan yang valid! [1-3]\n')
            guestScreen()
    elif mainMenu == 2:
        loginScreen()
    elif mainMenu == 3:
        print('\nTerima kasih telah menggunakan aplikasi Yellow Pages UMKM Indonesia!\n')
        time.sleep(1)
        exit()


def loginScreen():
    print('\n===== Menu Login Program UMKM =====\n')
    userName = input('Masukkan username anda: ').lower()
    if userName == 'admin':
        passWord = getpass.getpass('Masukkan password anda: ')
        if passWord == 'admin':
            print(f'\nHalo! Selamat datang Admin!')
            Mainmenu()
        else:
            print('Username/Password yang anda masukkan salah!')
            loginScreen()
    elif userName == 'user':
        passWord = getpass.getpass('Masukkan password anda: ')
        if passWord == 'user':
            print(f'\nHalo! Selamat datang User!')
            userMainMenu()
        else:
            print('Username/Password yang anda masukkan salah!')
            loginScreen()
    else:
        print('Username yang anda masukkan tidak ada')
        loginScreen()


def userMainMenu():
    print('\n===== Yellow Pages UMKM Indonesia =====\n')
    mainMenu = int(input('''\n[1] Daftar UMKM 
                  \n[2] Menambahkan Data UMKM 
                  \n[3] Exit 
                  \nSilahkan Pilih Main Menu [1-3]: '''))
    
    if mainMenu == 1:
        userLihatData()
        
    elif mainMenu == 2:
        userTambahData()

    elif mainMenu == 3:
        print('\nTerima kasih User telah menggunakan aplikasi Yellow Pages UMKM Indonesia!\n')
        guestScreen()

    else:
        print('\nPilihan tidak valid. Silahkan pilih menu [1-3]: ')
        userMainMenu()


def Mainmenu():
    print('\n===== Yellow Pages UMKM Indonesia =====\n')
    mainMenu = int(input('''\n[1] Daftar UMKM 
                  \n[2] Menambahkan Data UMKM 
                  \n[3] Menghapus Data UMKM
                  \n[4] Edit Data UMKM
                  \n[5] Exit 
                  \nSilahkan Pilih Main Menu [1-5]: '''))
    
    if mainMenu == 1:
        lihatData()
        
    elif mainMenu == 2:
        tambahData()

    elif mainMenu == 3:
        hapusData()
    
    elif mainMenu == 4:
        editData()

    elif mainMenu == 5:
        print('\nTerima kasih Admin telah menggunakan aplikasi Yellow Pages UMKM Indonesia!\n')
        guestScreen()

    else:
        print('\nPilihan tidak valid. Silahkan pilih menu [1-5]: ')


def cariData():
    print('\n===== Menu Cari Data UMKM =====\n')
    # Mencari data berdasarkan nama yang dicari
    apaYangdicari = input('Anda ingin mencari UMKM berdasarkan kategori apa? (Nama, Bidang, atau Kota): ').capitalize()
    if apaYangdicari == 'Nama':
        namaYangDicari = input('Masukkan nama UMKM yang anda cari: ').title()

    # Membuat dictionary untuk menyimpan hasil pencarian
        hasilPencarian = {}

        for idUMKM, dataUMKM in DataUMKM.items():
            if dataUMKM['nama'] == namaYangDicari:
                hasilPencarian[idUMKM] = dataUMKM

        # Menampilkan hasil pencarian
        if hasilPencarian:
            print("Hasil Pencarian:\n")
            for idUMKM, dataUMKM in hasilPencarian.items():
                print(f"ID: {idUMKM}")
                print(f"Nama: {dataUMKM['nama']}")
                print(f"Bidang: {dataUMKM['bidang']}")
                print(f"Nomor Telepon: {dataUMKM['noTelp']}")
                print(f"Alamat: {dataUMKM['alamat']}")
                print(f"Kota: {dataUMKM['kota']}\n")
            cariDataLagi()
        else:
            print("Data tidak ditemukan.")
            cariData()

    elif apaYangdicari == 'Bidang':
        # Input bidang yang ingin dicari
        bidangYangDicari = input('Masukkan bidang UMKM yang ingin Anda cari: ').title()

        # Membuat dictionary untuk menyimpan hasil pencarian
        hasilPencarian = {}

        # Iterasi melalui DataUMKM
        for idUMKM, dataUMKM in DataUMKM.items():
            if dataUMKM['bidang'] == bidangYangDicari:
                hasilPencarian[idUMKM] = dataUMKM

        # Menampilkan hasil pencarian
        if hasilPencarian:
            print("Hasil Pencarian:\n")
            for idUMKM, dataUMKM in hasilPencarian.items():
                print(f"ID: {idUMKM}")
                print(f"Nama: {dataUMKM['nama']}")
                print(f"Bidang: {dataUMKM['bidang']}")
                print(f"Nomor Telepon: {dataUMKM['noTelp']}")
                print(f"Alamat: {dataUMKM['alamat']}")
                print(f"Kota: {dataUMKM['kota']}\n")
            cariDataLagi()
        else:
            print("Data tidak ditemukan.")
            cariData()

    elif apaYangdicari == 'Kota':
        # Input kota yang ingin dicari
        bidangYangDicari = input('Masukkan Kota UMKM yang ingin Anda cari: ').title()

        # Membuat dictionary untuk menyimpan hasil pencarian
        hasilPencarian = {}

        # Iterasi melalui DataUMKM
        for idUMKM, dataUMKM in DataUMKM.items():
            if dataUMKM['kota'] == bidangYangDicari:
                hasilPencarian[idUMKM] = dataUMKM

        # Menampilkan hasil pencarian
        if hasilPencarian:
            print("Hasil Pencarian:\n")
            for idUMKM, dataUMKM in hasilPencarian.items():
                print(f"ID: {idUMKM}")
                print(f"Nama: {dataUMKM['nama']}")
                print(f"Bidang: {dataUMKM['bidang']}")
                print(f"Nomor Telepon: {dataUMKM['noTelp']}")
                print(f"Alamat: {dataUMKM['alamat']}")
                print(f"Kota: {dataUMKM['kota']}\n")
            cariDataLagi()
        else:
            print("Data tidak ditemukan.")
            cariData()
    else:
        print('Pilihan tidak valid. Silahkan pilih kategori yang ingin dicari: (Nama, Bidang, atau Kota)')
        cariData()



def userCariData():
    print('\n===== Menu Cari Data UMKM =====\n')
    # Mencari data berdasarkan nama yang dicari
    apaYangdicari = input('Anda ingin mencari UMKM berdasarkan kategori apa? (Nama, Bidang, atau Kota): ').capitalize()
    if apaYangdicari == 'Nama':
        namaYangDicari = input('Masukkan nama UMKM yang anda cari: ').title()

    # Membuat dictionary untuk menyimpan hasil pencarian
        hasilPencarian = {}

        for idUMKM, dataUMKM in DataUMKM.items():
            if dataUMKM['nama'] == namaYangDicari:
                hasilPencarian[idUMKM] = dataUMKM

        # Menampilkan hasil pencarian
        if hasilPencarian:
            print("Hasil Pencarian:\n")
            for idUMKM, dataUMKM in hasilPencarian.items():
                print(f"ID: {idUMKM}")
                print(f"Nama: {dataUMKM['nama']}")
                print(f"Bidang: {dataUMKM['bidang']}")
                print(f"Nomor Telepon: {dataUMKM['noTelp']}")
                print(f"Alamat: {dataUMKM['alamat']}")
                print(f"Kota: {dataUMKM['kota']}\n")
            userCariDataLagi()
        else:
            print("Data tidak ditemukan.")
            userCariData()

    elif apaYangdicari == 'Bidang':
        # Input bidang yang ingin dicari
        bidangYangDicari = input('Masukkan bidang UMKM yang ingin Anda cari: ').title()

        # Membuat dictionary untuk menyimpan hasil pencarian
        hasilPencarian = {}

        # Iterasi melalui DataUMKM
        for idUMKM, dataUMKM in DataUMKM.items():
            if dataUMKM['bidang'] == bidangYangDicari:
                hasilPencarian[idUMKM] = dataUMKM

        # Menampilkan hasil pencarian
        if hasilPencarian:
            print("Hasil Pencarian:\n")
            for idUMKM, dataUMKM in hasilPencarian.items():
                print(f"ID: {idUMKM}")
                print(f"Nama: {dataUMKM['nama']}")
                print(f"Bidang: {dataUMKM['bidang']}")
                print(f"Nomor Telepon: {dataUMKM['noTelp']}")
                print(f"Alamat: {dataUMKM['alamat']}")
                print(f"Kota: {dataUMKM['kota']}\n")
            userCariDataLagi()
        else:
            print("Data tidak ditemukan.")
            userCariData()

    elif apaYangdicari == 'Kota':
        # Input kota yang ingin dicari
        bidangYangDicari = input('Masukkan Kota UMKM yang ingin Anda cari: ').title()

        # Membuat dictionary untuk menyimpan hasil pencarian
        hasilPencarian = {}

        # Iterasi melalui DataUMKM
        for idUMKM, dataUMKM in DataUMKM.items():
            if dataUMKM['kota'] == bidangYangDicari:
                hasilPencarian[idUMKM] = dataUMKM

        # Menampilkan hasil pencarian
        if hasilPencarian:
            print("Hasil Pencarian:\n")
            for idUMKM, dataUMKM in hasilPencarian.items():
                print(f"ID: {idUMKM}")
                print(f"Nama: {dataUMKM['nama']}")
                print(f"Bidang: {dataUMKM['bidang']}")
                print(f"Nomor Telepon: {dataUMKM['noTelp']}")
                print(f"Alamat: {dataUMKM['alamat']}")
                print(f"Kota: {dataUMKM['kota']}\n")
            userCariDataLagi()
        else:
            print("Data tidak ditemukan.")
            userCariData()
    else:
        print('Pilihan tidak valid. Silahkan pilih kategori yang ingin dicari: (Nama, Bidang, atau Kota)')
        userCariData()


def subMenuDaftarUMKM(): 
    # Submenu digunakan untuk user yang selesai melakukan read dalam program agar tidak langsung ke MainMenu
    pilihMenu = int(input('''\nApa yang ingin anda lakukan? 
                          \n[1] Menambahkan Data UMKM 
                        \n[2] Menghapus Data UMKM
                        \n[3] Edit Data UMKM
                        \n[4] Kembali ke Menu 
                        \nSilahkan Pilih Main Menu [1-4]: '''))
    if pilihMenu == 1:
        tambahData()
    elif pilihMenu == 2:
        hapusData()
    elif pilihMenu == 3:
        editData()
    elif pilihMenu == 4:
        Mainmenu()
    else:
        print('Masukkan No Menu yang valid! [1-4]')


def userSubMenuDaftarUMKM(): 
    # Submenu digunakan untuk user yang selesai melakukan read dalam program agar tidak langsung ke MainMenu
    pilihMenu = int(input('''\nApa yang ingin anda lakukan? 
                          \n[1] Menambahkan Data UMKM 
                        \n[2] Kembali ke Menu 
                        \nSilahkan Pilih Main Menu [1-2]: '''))
    if pilihMenu == 1:
        userTambahData()
    elif pilihMenu == 2:
        userMainMenu()
    else:
        print('Masukkan No Menu yang valid! [1-4]')


def printDataUMKM():
    # Berfungsi untuk mencetak Data Record UMKM
    print('\n===== Data Record UMKM =====\n')
    for idUMKM, dataUMKM in DataUMKM.items():
        print(f"ID: {idUMKM}")
        print(f"Nama: {dataUMKM['nama']}")
        print(f"Bidang: {dataUMKM['bidang']}")
        print(f"Nomor Telepon: {dataUMKM['noTelp']}")
        print(f"Alamat: {dataUMKM['alamat']}")
        print(f"Kota: {dataUMKM['kota']}\n")

def lihatData():
    # Berfungsi untuk melihatkan data dan memberi pilihan user apakah ingin mencari data atau tidak
    printDataUMKM()
    mauCariUMKM = input('Apakah anda ingin mencari UMKM? (Y/N): ').upper()
    if mauCariUMKM == 'Y':
        cariData()
    elif mauCariUMKM == 'N':
        subMenuDaftarUMKM()
    else:
        print('Pilihan tidak valid! Silahkan input (Y/N)')
        lihatData()



def userLihatData():
    # Berfungsi untuk melihatkan data dan memberi pilihan user apakah ingin mencari data atau tidak
    printDataUMKM()
    mauCariUMKM = input('Apakah anda ingin mencari UMKM? (Y/N): ').upper()
    if mauCariUMKM == 'Y':
        userCariData()
    elif mauCariUMKM == 'N':
        userSubMenuDaftarUMKM()
    else:
        print('Pilihan tidak valid! Silahkan input (Y/N)')
        userLihatData()

             
def tambahData():
    print('\n===== Menu Tambah Data UMKM =====\n')
    idUMKM = len(DataUMKM) +1 # Auto Increment ID UMKM
    namaUMKM = input('Masukkan nama UMKM: ').title()
    bidangUMKM = input('Masukkan bidang UMKM: ').title()
    teleponUMKM = input('Masukkan No. Telepon UMKM: ')

    if teleponUMKM.isdigit() and len(teleponUMKM) >= 12: # Memeriksa inputan user apakah digit dan no telfon sudah sesuai
        alamatUMKM = input('Masukkan Alamat UMKM: ').title()
        kotaUMKM =  input('Masukkan Kota UMKM: ').title()
        UMKMBaru = {
        f'ID{str(idUMKM)}' : {'nama' : namaUMKM,
                'bidang' : bidangUMKM,
                'noTelp' : teleponUMKM,
                'alamat' : alamatUMKM,
                'kota' : kotaUMKM
        }
        }
        print(f"\nID: {idUMKM}")
        print(f"Nama: {namaUMKM}")
        print(f"Bidang: {bidangUMKM}")
        print(f"Nomor Telepon: {teleponUMKM}")
        print(f"Alamat: {alamatUMKM}")
        print(f"Kota: {kotaUMKM}\n")

        # Memberikan validasi kepada user apa benar data ini yang ingin ditambahkan
        validasi = input('Apakah anda yakin dengan data ini? (Y/N): ').upper()
        if validasi == 'Y': # Menambahkan data apabila user input 'Y'
            DataUMKM.update(UMKMBaru)
            printDataUMKM()
            print(f'Data dengan Nama UMKM {namaUMKM}, dengan bidang {bidangUMKM} berhasil disimpan dengan ID: {idUMKM}\n')

            # Memberi pilihan user apakah ingin menambah data lagi atau tidak
            TambahDataLagi() 

        elif validasi == 'N': # Tidak menambahkan data apabila user input 'N'
            # Memberi pilihan user apakah ingin menambah data lagi atau tidak
            TambahDataLagi()
    else:
        print('\nMasukkan No. Telepon yang valid\n')
        tambahData()


def userTambahData():
    userTempDict = {}
    print('\n===== Menu Tambah Data UMKM =====\n')
    idUMKM = len(DataUMKM) +1 # Auto Increment ID UMKM
    namaUMKM = input('Masukkan nama UMKM: ').title()
    bidangUMKM = input('Masukkan bidang UMKM: ').title()
    teleponUMKM = input('Masukkan No. Telepon UMKM: ')

    if teleponUMKM.isdigit() and len(teleponUMKM) >= 12: # Memeriksa inputan user apakah digit dan no telfon sudah sesuai
        alamatUMKM = input('Masukkan Alamat UMKM: ').title()
        kotaUMKM =  input('Masukkan Kota UMKM: ').title()
        UMKMBaru = {
        f'ID{str(idUMKM)}' : {'nama' : namaUMKM,
                'bidang' : bidangUMKM,
                'noTelp' : teleponUMKM,
                'alamat' : alamatUMKM,
                'kota' : kotaUMKM
        }
        }
        print(f"\nID: {idUMKM}")
        print(f"Nama: {namaUMKM}")
        print(f"Bidang: {bidangUMKM}")
        print(f"Nomor Telepon: {teleponUMKM}")
        print(f"Alamat: {alamatUMKM}")
        print(f"Kota: {kotaUMKM}\n")

        # Memberikan validasi kepada user apa benar data ini yang ingin ditambahkan
        validasi = input('Apakah anda yakin dengan data ini? (Y/N): ').upper()
        if validasi == 'Y': # Menambahkan data apabila user input 'Y'
            DataUMKM.update(userTempDict)
            printDataUMKM()
            print(f'Data dengan Nama UMKM {namaUMKM}, dengan bidang {bidangUMKM} berhasil disimpan dengan ID: {idUMKM}\n')

            # Memberi pilihan user apakah ingin menambah data lagi atau tidak
            userTambahDataLagi() 

        elif validasi == 'N': # Tidak menambahkan data apabila user input 'N'
            # Memberi pilihan user apakah ingin menambah data lagi atau tidak
            userTambahDataLagi()
    else:
        print('\nMasukkan No. Telepon yang valid\n')
        userTambahData()


lastUMKMID = 0  # Inisialisasi ID terakhir dengan 0 untuk auto decrement
if DataUMKM:
    lastUMKMID = max(int(key[2:]) for key in DataUMKM.keys())

def hapusData():
    print('\n===== Menu Hapus Data UMKM =====\n')
    printDataUMKM()
    idHapus = input('Masukkan ID yang ingin dihapus: ')
    if idHapus.isdigit(): # Memeriksa apakah ID yang dimasukkan oleh user adalah digit atau tidak
        idHapus = f'ID{idHapus}'
    else:
        print('Masukkan ID yang valid\n')
        hapusData()

    if idHapus in DataUMKM: # Memeriksa apakah ID yang diinput user ada didalam database
        UMKMID = idHapus
        # Menggunakan key untuk mengakses value dari database
        UMKMData = DataUMKM.get(UMKMID)
        # Memeriksa apakah UMKMData tidak None (artinya, ID yang diminta ada dalam database)
        if UMKMData:
        # Menampilkan key dan value ID yang diinput oleh user
            print(f'\nID: {UMKMID}')
            for key, value in UMKMData.items():
                print(f'{key}: {value}')

        # Memberikan validasi pada user apa benar ini data yang ingin dihapus
        validasi = input('\nApakah anda yakin untuk menghapus data ini? (Y/N): ').upper() 
        if validasi == 'Y': # Apabila user input 'Y' maka akan dihapus datanya
            DataUMKM.pop(idHapus)
            print(f'\nData dengan ID {idHapus} telah berhasil dihapus!')
            hapusDataLagi()

        elif validasi == 'N': # Apabila user input 'N' maka user akan diarahkan kembali ke menu sebelumnya
            hapusDataLagi()
    else:
        print(f'ID dengan nomor {idHapus} tidak ada dalam database')


def editData():
    print('\n===== Menu Edit Data UMKM =====\n')
    printDataUMKM() # Menunjukkan data record UMKM pada user agar user tahu pasti ID berapa yang mau diedit
    idUpdate = input('Masukkan ID yang ingin diedit: ')
    if idUpdate.isdigit(): # Memeriksa apakah inputan user digit atau bukan agar ID bisa ditemukan
        idUpdate = f'ID{idUpdate}'
    else:
        print('Masukkan ID yang valid\n')
        editData()
    if idUpdate in DataUMKM: # Memeriksa apakah ID yang diinput user ada didalam database
        UMKMID = idUpdate # Menyimpan inputan user kedalam variabel UMKMID
        UMKMData = DataUMKM.get(UMKMID) # Mengambil ID inputan user dari dalam database UMKMData
        # Memeriksa apakah UMKMData tidak None (artinya, ID yang diminta ada dalam database)
        if UMKMData:
        # Mencetak value yang sesuai dengan ID inputan user
            print(f'\nID: {UMKMID}')
            for key, value in UMKMData.items():
                print(f'{key}: {value}')
            # Konfirmasi user apa benar ini data yang mau diedit
            lanjutEdit = input('\nApakah anda ingin mengedit data ini? (Y/N): ').upper()
            if lanjutEdit == 'Y':

                # Memberikan user pilihan untuk mengedit key apa yang terdapat dalam database
                valueYangdiEdit = input('Masukkan nama field yang ingin diedit (Nama/Bidang/No.Telp/Alamat/Kota): ').lower()
                if valueYangdiEdit in ['nama', 'bidang', 'no.telp', 'alamat', 'kota']:

                    # Melakukan pemeriksaan pada inputan user apabila input no.telp harus digit dan diatas 12 digit
                    if valueYangdiEdit == 'no.telp': 
                        valueBaru = input(f'Masukkan nilai baru untuk {valueYangdiEdit}: ')
                        if valueBaru.isdigit() and len(valueBaru) >= 12:
                            validasi = input('\nApakah anda yakin untuk mengedit data ini? (Y/N): ').upper() # Memberikan validasi kepada user
                            
                            if validasi == 'Y':
                                # Apabila input user 'Y' maka akan disimpan dan ditanya apakah mau melakukan edit data lagi
                                UMKMData[valueYangdiEdit] = valueBaru 
                                print(f'\nData dengan {idUpdate} telah berhasil diupdate!\n')
                                print(f'ID: {UMKMID}')
                                for key, value in UMKMData.items():
                                    print(f'{key}: {value}')
                                editDataLagi()
                            
                            elif validasi == 'N':
                            # Apabila input user 'N' maka akan ditanya apakah mau melakukan edit data lagi atau tidak. Apabila tidak maka akan diarahkan ke main menu
                                print('Baik! Data anda tidak jadi tersimpan \n')
                                editDataLagi()
                        else:
                            print('Masukkan No. Telepon yang valid\n')
                            editData()
                    else:
                        # Untuk inputan user selain no.telp
                        valueBaru = input(f'Masukkan nilai baru untuk {valueYangdiEdit}: ').title()
                        validasi = input('\nApakah anda yakin untuk mengedit data ini? (Y/N): ').upper()

                        if validasi == 'N':
                            editDataLagi()

                        elif validasi == 'Y':
                            UMKMData[valueYangdiEdit] = valueBaru
                            print(f'\nData dengan {idUpdate} telah berhasil diupdate!\n')
                            print(f'ID: {UMKMID}')
                            for key, value in UMKMData.items():
                                print(f'{key}: {value}')
                            editDataLagi()
                else:
                    print(f'{valueYangdiEdit} tidak ada dalam database!')
                    editData()
            elif lanjutEdit == 'N':
                subMenuDaftarUMKM()
        else:
            print('\nData tidak ditemukan.')
    else:
        print(f'ID dengan nomor {idUpdate} tidak ada dalam database')
        editData()


def cariDataLagi():
    mauLagi = input('\nApakah anda ingin mencari data yang lain? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Cari Data UMKM\n')
        cariData()
    elif mauLagi == 'N':
        subMenuDaftarUMKM()
    else:
        print('Masukkan inputan yang valid!')


def userCariDataLagi():
    mauLagi = input('\nApakah anda ingin mencari data yang lain? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Cari Data UMKM\n')
        userCariData()
    elif mauLagi == 'N':
        userSubMenuDaftarUMKM()
    else:
        print('Masukkan inputan yang valid!')


def TambahDataLagi():
    mauLagi = input('\nApakah anda ingin menambah data lagi? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Tambah Data UMKM')
        tambahData()
    elif mauLagi == 'N':
        print('\nBaik! Kamu akan diarahkan kembali ke Main Menu!\n')
        Mainmenu()
    else:
        print('Masukkan inputan yang valid!')


def userTambahDataLagi():
    mauLagi = input('\nApakah anda ingin menambah data lagi? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Tambah Data UMKM')
        userTambahData()
    elif mauLagi == 'N':
        print('\nBaik! Kamu akan diarahkan kembali ke Main Menu!\n')
        userMainMenu()
    else:
        print('Masukkan inputan yang valid!')


def hapusDataLagi():
    mauLagi = input('\nApakah anda ingin menghapus data yang lain? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Hapus Data UMKM')
        hapusData()
    elif mauLagi == 'N':
        print('\nBaik! Kamu akan diarahkan kembali ke Main Menu!\n')
        Mainmenu()
    else:
        print('Masukkan inputan yang valid!')


def editDataLagi():
    mauLagi = input('\nApakah anda ingin mengedit data yang lain? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Edit Data UMKM')
        editData()
    elif mauLagi == 'N':
        print('\nBaik! Kamu akan diarahkan kembali ke Main Menu!\n')
        Mainmenu()
    else:
        print('Masukkan inputan yang valid!')

while True:
    guestScreen()
    