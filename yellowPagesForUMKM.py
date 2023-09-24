import getpass
import time
# Dictionary untuk data UMKM
DataUMKM = {
    'ID1' : {'nama' : 'Umam Pet Shop',
            'bidang' : 'Pet',
            'noTelp' : '08123466723',
            'alamat' : 'Jl. Kenanga No. 4',
            'kota' : 'Malang'
    },
    'ID2' : {'nama' : 'Haryo Knalpot',
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
    'ID4' :{'nama' : 'Yanto Hoodie',
            'bidang' : 'Tekstil',
            'noTelp' : '08934574647387',
            'alamat' : 'Jl. Batik No. 102',
            'kota' : 'Yogyakarta'
    },
    'ID5' :{'nama' : 'Dinda Apem',
            'bidang' : 'Makanan',
            'noTelp' : '08567574647387',
            'alamat' : 'Jl. Sudirman No. 7',
            'kota' : 'Jakarta'
    }
}


def guestScreen(): # Menu guest apabila tidak login ke user atau admin
    print('\n===== Yellow Pages UMKM Indonesia =====\n')
    mainMenu = input('''\n[1] Melihat Daftar UMKM 
                  \n[2] Login Admin/User
                  \n[3] Exit
                  \nSilahkan Pilih Main Menu [1-3]: ''')
    if mainMenu == '1':
        print('\n\t\t\t\t===== Data Record UMKM =====\n')
        printDataUMKM()
        print('''\n[1] Login Admin/User
                \n[2] Kembali ke menu awal
                \n[3] Exit
                \nSilahkan Pilih Main Menu [1-3]: ''')
        mauApa = input('\nApa yang ingin anda lakukan? ')
        if mauApa == '1':
            loginScreen()
        elif mauApa == '2':
            guestScreen()
        elif mauApa == '3':
            print('\nTerima kasih telah menggunakan aplikasi Yellow Pages UMKM Indonesia!\n')
            time.sleep(1)
            exit()

        else:
            print('\nSilahkan pilih inputan yang valid! [1-3]\n')
            time.sleep(0.5)
            guestScreen()
    elif mainMenu == '2':
        loginScreen()
    elif mainMenu == '3':
        print('\nTerima kasih telah menggunakan aplikasi Yellow Pages UMKM Indonesia!\n')
        time.sleep(1)
        exit()
    else:
        print('\nSilahkan pilih inputan yang valid! [1-3]\n')
        guestScreen()

def cekAjuan(): # fungsi yang digunakan admin untuk mengecek ajuan dari user
    print('\n===== Data Ajuan Tambah Data UMKM =====\n')
    if len(ajuanUser) > 0:
        print(f'Hai admin! Ada {len(ajuanUser)} ajuan user untuk tambah data nih.\nSilahkan review satu persatu untuk disimpan ke database ya!\n')
        time.sleep(1)
        yangDihapusSetelahValidasi = []  # Membuat daftar kunci yang akan dihapus
        for idUMKM, dataUMKM in ajuanUser.items():
            print(f"ID: {idUMKM}")
            print(f"Nama: {dataUMKM['nama']}")
            print(f"Bidang: {dataUMKM['bidang']}")
            print(f"Nomor Telepon: {dataUMKM['noTelp']}")
            print(f"Alamat: {dataUMKM['alamat']}")
            print(f"Kota: {dataUMKM['kota']}\n")
            validasi = input('Apakah admin menyetujui ajuan tambah data ini?\nApabila "Y", akan disimpan dalam database\nApabila N berarti ajuan tidak diterima. (Y/N): ').upper()
            if validasi == 'Y':
                DataUMKM.update({idUMKM:dataUMKM})
                print(f'\nBaik! Data dengan ID: {idUMKM} telah ditambahkan pada database DataUMKM!\n')
                yangDihapusSetelahValidasi.append(idUMKM)  # Menambahkan kunci ke daftar untuk dihapus
            elif validasi == 'N':
                print(f'\nBaik! Ajuan user dengan ID: {idUMKM} tidak disetujui!\n')
                pass
            else:
                print('\nTolong masukkan inputan yang valid! (Y/N)')
                cekAjuan()

        for key in yangDihapusSetelahValidasi:
            del ajuanUser[key]
        clearDictGa() 
    else:
        print('Hai admin! Masih belum ada data Ajuan atau admin sudah memproses semua data Ajuan Tambah Data dari User nih.\nSilahkan cek secara berkala ya! ')
        time.sleep(1)
        Mainmenu()

def clearDictGa(): # fungsi Untuk admin menghapus ajuan dari user
    clearDictga = input('\nTerima kasih admin telah memproses ajuan user!\nApakah anda mau menghapus semua ajuan user? (Y/N): ').upper()
    if clearDictga == 'Y':
        print('\nBaik! Semua ajuan user telah dihapus')
        ajuanUser.clear()
        time.sleep(0.75)
        Mainmenu()
    elif clearDictga == 'N':
        print('\nBaik. Semua ajuan user tidak dihapus')
        time.sleep(0.75)
        Mainmenu()
    else:
        print('Tolong masukkan inputan yang valid! (Y/N)')
        clearDictGa()
        

def loginScreen(): # fungsi login screen untuk admin atau user
    print('\n===== Menu Login Program UMKM =====\n')
    userName = input('Masukkan username anda: ').lower()
    if userName == 'admin':
        passWord = getpass.getpass('Masukkan password anda: ')
        if passWord == 'admin':
            print(f'\nHalo! Selamat datang Admin!')
            time.sleep(1)
            Mainmenu()
        else:
            print('Username/Password yang anda masukkan salah!')
            loginScreen()
    elif userName == 'user':
        passWord = getpass.getpass('Masukkan password anda: ')
        if passWord == 'user':
            print(f'\nHalo! Selamat datang User!')
            time.sleep(1)
            userMainMenu()
        else:
            print('Username/Password yang anda masukkan salah!')
            loginScreen()
    else:
        print('Username yang anda masukkan tidak ada')
        time.sleep(0.75)
        loginScreen()


def userMainMenu(): # Main menu untuk user
    print('\n===== Yellow Pages UMKM Indonesia =====\n')
    mainMenu = input('''\n[1] Daftar UMKM 
                  \n[2] Menambahkan Data UMKM 
                  \n[3] Cek Ajuan UMKM Kamu 
                  \n[4] Logout 
                  \nSilahkan Pilih Main Menu [1-3]: ''')
    
    if mainMenu == '1':
        userLihatData()
        
    elif mainMenu == '2':
        userTambahData()

    elif mainMenu == '3':
        userMauEditAjuan()

    elif mainMenu == '4':
        print('\nTerima kasih User telah menggunakan aplikasi Yellow Pages UMKM Indonesia!\n')
        time.sleep(1)
        guestScreen()

    else:
        print('\nPilihan tidak valid. Silahkan pilih menu [1-3]: ')
        userMainMenu()


def Mainmenu(): # Main menu untuk admin
    print('\n===== Yellow Pages UMKM Indonesia =====\n')
    mainMenu = input('''\n[1] Daftar UMKM 
                  \n[2] Menambahkan Data UMKM 
                  \n[3] Menghapus Data UMKM
                  \n[4] Edit Data UMKM
                  \n[5] Cek Ajuan Tambah Data User
                  \n[6] Logout 
                  \nSilahkan Pilih Main Menu [1-6]: ''')
    
    if mainMenu == '1':
        lihatData()
        
    elif mainMenu == '2':
        tambahData()

    elif mainMenu == '3':
        hapusData()
    
    elif mainMenu == '4':
        editData()

    elif mainMenu == '5':
        cekAjuan()
    
    elif mainMenu == '6':
        print('\nTerima kasih Admin telah menggunakan aplikasi Yellow Pages UMKM Indonesia!\n')
        time.sleep(1)
        guestScreen()

    else:
        print('\nPilihan tidak valid. Silahkan pilih menu [1-6]: ')


def cariData(): # Fungsi untuk admin mencari data yang ada dalam data UMKM
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
            time.sleep(0.5)
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
            time.sleep(0.5)
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
            time.sleep(0.5)
            cariData()
    else:
        print('Pilihan tidak valid. Silahkan pilih kategori yang ingin dicari: (Nama, Bidang, atau Kota)')
        cariData()



def userCariData(): # Fungsi untuk user mencari data yang ada dalam data UMKM
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
            time.sleep(0.5)
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
            time.sleep(0.5)
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
            time.sleep(0.5)
            userCariData()
    else:
        print('Pilihan tidak valid. Silahkan pilih kategori yang ingin dicari: (Nama, Bidang, atau Kota)')
        userCariData()


def subMenuDaftarUMKM(): # Submenu digunakan untuk admin yang selesai melakukan read dalam program agar tidak langsung ke MainMenu
    pilihMenu = input('''\nApa yang ingin anda lakukan? 
                          \n[1] Menambahkan Data UMKM 
                        \n[2] Menghapus Data UMKM
                        \n[3] Edit Data UMKM
                        \n[4] Kembali ke Menu 
                        \nSilahkan Pilih Main Menu [1-4]: ''')
    if pilihMenu == '1':
        tambahData()
    elif pilihMenu == '2':
        hapusData()
    elif pilihMenu == '3':
        editData()
    elif pilihMenu == '4':
        print('Baik kamu akan diarahkan kembali ke Main Menu')
        time.sleep(0.5)
        Mainmenu()
    else:
        print('Masukkan No Menu yang valid! [1-4]')
        subMenuDaftarUMKM()


def userSubMenuDaftarUMKM(): # Submenu digunakan untuk user yang selesai melakukan read dalam program agar tidak langsung ke MainMenu
    pilihMenu = input('''\nApa yang ingin anda lakukan? 
                          \n[1] Menambahkan Data UMKM 
                        \n[2] Cek Ajuan Kamu 
                        \n[3] Kembali ke Menu 
                        \nSilahkan Pilih Main Menu [1-2]: ''')
    if pilihMenu == '1':
        userTambahData()
    elif pilihMenu == '2':
        cekAjuan()
    elif pilihMenu == '3':
        userMainMenu()
    else:
        print('Masukkan No Menu yang valid! [1-2]')
        userSubMenuDaftarUMKM()


def printDataUMKM():
    # Menampilkan header kolom
    print("{:<12} {:<20} {:<18} {:<23} {:<30} {:<15}".format("ID UMKM", "Nama UMKM", "Bidang UMKM", "No. Telepon UMKM", "Alamat UMKM", "Kota UMKM"))

    # Meloop dan mencetak data Record UMKM
    for idUMKM, dataUMKM in DataUMKM.items():
        print("{:<12} {:<20} {:<18} {:<23} {:<30} {:<15}".format(idUMKM, dataUMKM['nama'], dataUMKM['bidang'], dataUMKM['noTelp'], dataUMKM['alamat'], dataUMKM['kota']))


def printAjuanUMKMUser():
    # Berfungsi untuk mencetak Data Record UMKM di menu user
    print("{:<12} {:<20} {:<18} {:<23} {:<30} {:<15}".format("ID UMKM", "Nama UMKM", "Bidang UMKM", "No. Telepon UMKM", "Alamat UMKM", "Kota UMKM"))

    # Meloop dan mencetak data Record UMKM
    for idUMKM, dataUMKM in ajuanUser.items():
        print("{:<12} {:<20} {:<18} {:<23} {:<30} {:<15}".format(idUMKM, dataUMKM['nama'], dataUMKM['bidang'], dataUMKM['noTelp'], dataUMKM['alamat'], dataUMKM['kota']))


def userMauEditAjuan(): # fungsi untuk user edit ajuannya
    if len(ajuanUser): # untuk mengecek apakah len ajuan user berisi None atau tidak. Apabila ada isinya akan lanjut ke if. Apabila isinya None akan langsung ke else
        printAjuanUMKMUser()
        apaygMaudilakukanUser = input('\nApakah anda mau edit data ajuan anda? (Y/N): ').upper()
        if apaygMaudilakukanUser == 'Y':
            idUpdate = input('Masukkan ID yang ingin diedit (angkanya saja): ')
            if idUpdate.isdigit():
                idUpdate = f'ID{idUpdate}'
            else:
                print('\nMasukkan ID yang valid\n')
                userMauEditAjuan()

            if idUpdate in ajuanUser:
                UMKMID = idUpdate
                UMKMData = ajuanUser.get(UMKMID)

                if UMKMData:
                    print(f'\nID: {UMKMID}')
                    for key, value in UMKMData.items():
                        print(f'{key}: {value}')

                    lanjutEdit = input('\nApakah anda ingin mengedit data ini? (Y/N): ').upper()
                    if lanjutEdit == 'Y':
                        valueYangdiEdit = input('Masukkan nama field yang ingin diedit (Nama/Bidang/No.Telp/Alamat/Kota): ').lower()
                        if valueYangdiEdit in ['nama', 'bidang', 'no.telp', 'alamat', 'kota']:
                            if valueYangdiEdit == 'no.telp':
                                valueBaru = input(f'Masukkan nilai baru untuk {valueYangdiEdit}: ')
                                if valueBaru.isdigit() and len(valueBaru) >= 9:
                                    validasi = input('\nApakah anda yakin untuk mengedit data ini? (Y/N): ').upper()
                                    if validasi == 'Y':
                                        UMKMData[valueYangdiEdit] = valueBaru
                                        print(f'\nData dengan {idUpdate} telah berhasil diupdate!\n')
                                        print(f'ID: {UMKMID}')
                                        for key, value in UMKMData.items():
                                            print(f'{key}: {value}')
                                        userEditAjuanLagi()
                                    elif validasi == 'N':
                                        print('Baik! Data anda tidak jadi tersimpan \n')
                                        userEditAjuanLagi()
                                else:
                                    print('Masukkan No. Telepon yang valid\n')
                                    userMauEditAjuan()
                            else:
                                valueBaru = input(f'Masukkan nilai baru untuk {valueYangdiEdit}: ').title()
                                validasi = input('\nApakah anda yakin untuk mengedit data ini? (Y/N): ').upper()
                                if validasi == 'Y':
                                    UMKMData[valueYangdiEdit] = valueBaru
                                    print(f'\nData dengan {idUpdate} telah berhasil diupdate!\n')
                                    print(f'ID: {UMKMID}')
                                    for key, value in UMKMData.items():
                                        print(f'{key}: {value}')
                                    userEditAjuanLagi()
                                elif validasi == 'N':
                                    userEditAjuanLagi()
                        else:
                            print(f'\n{valueYangdiEdit} tidak ada dalam database!')
                    elif lanjutEdit == 'N':
                        userSubMenuDaftarUMKM()
                else:
                    print('\nData tidak ditemukan.')
                    time.sleep(0.5)
                    userMauEditAjuan()
            else:
                print(f'\nID dengan nomor {idUpdate} tidak ada dalam database')
                userMauEditAjuan()
        elif apaygMaudilakukanUser == 'N':
            userSubMenuDaftarUMKM()
        else:
            print('\nMasukkan inputan yang valid! (Y/N)')
            userMauEditAjuan()
    else:
        print('\nAnda belum mengajukan untuk tambah data ke admin!\nSilahkan ajukan data terlebih dahulu')
        time.sleep(0.75)
        userMainMenu()



def lihatData():
    # Berfungsi untuk melihatkan data dan memberi pilihan admin apakah ingin mencari data atau tidak
    print('\n\t\t\t\t===== Data Record UMKM =====\n')
    printDataUMKM()
    mauCariUMKM = input('\nApakah anda ingin mencari UMKM? (Y/N): ').upper()
    if mauCariUMKM == 'Y':
        cariData()
    elif mauCariUMKM == 'N':
        subMenuDaftarUMKM()
    else:
        print('Pilihan tidak valid! Silahkan input (Y/N)')
        lihatData()


def userLihatData():
    # Berfungsi untuk melihatkan data dan memberi pilihan user apakah ingin mencari data atau tidak
    print('\n\t\t\t\t===== Data Record UMKM =====\n')
    printDataUMKM()
    mauCariUMKM = input('\nApakah anda ingin mencari UMKM? (Y/N): ').upper()
    if mauCariUMKM == 'Y':
        userCariData()
    elif mauCariUMKM == 'N':
        userSubMenuDaftarUMKM()
    else:
        print('Pilihan tidak valid! Silahkan input (Y/N)')
        userLihatData()

             
def tambahData(): # fungsi untuk admin tambah data
    print('\n===== Menu Tambah Data UMKM =====\n')
    idUMKM = len(DataUMKM) +1 # Auto Increment ID UMKM
    namaUMKM = input('Masukkan nama UMKM: ').title()
    bidangUMKM = input('Masukkan bidang UMKM: ').title()
    teleponUMKM = input('Masukkan No. Telepon UMKM: ')

    if teleponUMKM.isdigit() and len(teleponUMKM) >= 9: # Memeriksa inputan user apakah digit dan no telfon sudah sesuai
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
            print('\n\t\t\t\t===== Data Record UMKM =====\n')
            printDataUMKM()
            print(f'\nData dengan Nama UMKM {namaUMKM}, dengan bidang {bidangUMKM} berhasil disimpan dengan ID: {idUMKM}\n')
            time.sleep(0.75)
            # Memberi pilihan user apakah ingin menambah data lagi atau tidak
            TambahDataLagi() 

        elif validasi == 'N': # Tidak menambahkan data apabila user input 'N'
            # Memberi pilihan user apakah ingin menambah data lagi atau tidak
            TambahDataLagi()
    else:
        print('\nMasukkan No. Telepon yang valid\n')
        tambahData()

ajuanUser = {} # dictionary kosong untuk menyimpan ajuan user untuk divalidasi admin

def userTambahData():
    print('\n===== Menu Tambah Data UMKM =====\n')
    idUMKM = len(DataUMKM) + len(ajuanUser) +1 # Auto Increment ID UMKM
    namaUMKM = input('Masukkan nama UMKM: ').title()
    bidangUMKM = input('Masukkan bidang UMKM: ').title()
    teleponUMKM = input('Masukkan No. Telepon UMKM: ')

    if teleponUMKM.isdigit() and len(teleponUMKM) >= 9: # Memeriksa inputan user apakah digit dan no telfon sudah sesuai
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
            ajuanUser.update(UMKMBaru)
            printAjuanUMKMUser()
            print(f'\nData dengan Nama UMKM {namaUMKM}, dengan bidang {bidangUMKM} berhasil disimpan dalam Ajuan dengan ID: {idUMKM}.\nTunggu Validasi admin untuk menambahkan data anda pada database ya!')
            time.sleep(0.75)
            # Memberi pilihan user apakah ingin menambah data lagi atau tidak
            userTambahDataLagi() 

        elif validasi == 'N': # Tidak menambahkan data apabila user input 'N'
            # Memberi pilihan user apakah ingin menambah data lagi atau tidak
            userTambahDataLagi()
        else:
            print('Masukkan inputan yang valid! (Y/N)')
    else:
        print('\nMasukkan No. Telepon yang valid\n')
        userTambahData()


def hapusData(): # Fungsi untuk admin menghapus data UMKM
    print('\n\t\t\t\t===== Menu Hapus Data UMKM =====\n')
    printDataUMKM()
    idHapus = input('Masukkan ID yang ingin dihapus (angkanya saja): ')
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
            time.sleep(0.75)
            hapusDataLagi()

        elif validasi == 'N': # Apabila user input 'N' maka user akan diarahkan kembali ke menu sebelumnya
            hapusDataLagi()
        else:
            print('Masukkan inputan yang valid! (Y/N)')
            hapusData()
    else:
        print(f'ID dengan nomor {idHapus} tidak ada dalam database')
        hapusData()


def editData(): # fungsi untuk admin edit data UMKM
    print('\n\t\t\t\t===== Menu Edit Data UMKM =====\n')
    printDataUMKM() # Menunjukkan data record UMKM pada user agar user tahu pasti ID berapa yang mau diedit
    idUpdate = input('Masukkan ID yang ingin diedit (angkanya saja): ')
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

                    # Melakukan pemeriksaan pada inputan user apabila input no.telp harus digit dan diatas 9 digit
                    if valueYangdiEdit == 'no.telp': 
                        valueBaru = input(f'Masukkan nilai baru untuk {valueYangdiEdit}: ')
                        if valueBaru.isdigit() and len(valueBaru) >= 9:
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
            time.sleep(0.5)
            editData()
    else:
        print(f'ID dengan nomor {idUpdate} tidak ada dalam database')
        editData()


def cariDataLagi(): # fungsi untuk validasi admin mau cari data lagi atau tidak
    mauLagi = input('\nApakah anda ingin mencari data yang lain? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Cari Data UMKM\n')
        time.sleep(0.75)
        cariData()
    elif mauLagi == 'N':
        subMenuDaftarUMKM()
    else:
        print('Masukkan inputan yang valid!')


def userCariDataLagi(): # fungsi untuk validasi admin mau cari data lagi atau tidak
    mauLagi = input('\nApakah anda ingin mencari data yang lain? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Cari Data UMKM\n')
        time.sleep(0.75)
        userCariData()
    elif mauLagi == 'N':
        userSubMenuDaftarUMKM()
    else:
        print('Masukkan inputan yang valid!')
        userCariData()


def TambahDataLagi(): # fungsi untuk validasi admin mau tambah data lagi atau tidak
    mauLagi = input('\nApakah anda ingin menambah data lagi? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Tambah Data UMKM')
        time.sleep(0.75)
        tambahData()
    elif mauLagi == 'N':
        print('\nBaik! Kamu akan diarahkan kembali ke Main Menu!\n')
        time.sleep(0.75)
        Mainmenu()
    else:
        print('Masukkan inputan yang valid! (Y/N)')
        time.sleep(0.75)
        TambahDataLagi()


def userTambahDataLagi(): # fungsi untuk validasi user mau tambah data lagi atau tidak
    mauLagi = input('\nApakah anda ingin menambah data lagi? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Tambah Data UMKM')
        time.sleep(0.75)
        userTambahData()
    elif mauLagi == 'N':
        print('\nBaik! Kamu akan diarahkan kembali ke Main Menu!\n')
        time.sleep(0.75)
        userMainMenu()
    else:
        print('Masukkan inputan yang valid!')
        time.sleep(0.75)
        userTambahDataLagi()


def hapusDataLagi(): # fungsi untuk validasi admin mau hapus data lagi atau tidak
    mauLagi = input('\nApakah anda ingin menghapus data yang lain? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Hapus Data UMKM')
        time.sleep(0.75)
        hapusData()
    elif mauLagi == 'N':
        print('\nBaik! Kamu akan diarahkan kembali ke Main Menu!\n')
        time.sleep(0.75)
        Mainmenu()
    else:
        print('Masukkan inputan yang valid!')


def editDataLagi(): # fungsi untuk validasi admin mau edit data lagi atau tidak
    mauLagi = input('\nApakah anda ingin mengedit data yang lain? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Edit Data UMKM')
        time.sleep(0.75)
        editData()
    elif mauLagi == 'N':
        print('\nBaik! Kamu akan diarahkan kembali ke Main Menu!\n')
        time.sleep(0.75)
        Mainmenu()
    else:
        print('Masukkan inputan yang valid!')

def userEditAjuanLagi(): # fungsi untuk validasi user mau edit ajuan data lagi atau tidak
    mauLagi = input('\nApakah anda ingin mengedit data yang lain? (Y/N): ').upper()
    if mauLagi == 'Y':
        print('\nBaik! Anda akan diarahkan ke menu Edit Ajuan UMKM')
        time.sleep(0.75)
        userMauEditAjuan()
    elif mauLagi == 'N':
        print('\nBaik! Kamu akan diarahkan kembali ke Main Menu!\n')
        time.sleep(0.75)
        userMainMenu()
    else:
        print('Masukkan inputan yang valid!')

while True:
    guestScreen()
    