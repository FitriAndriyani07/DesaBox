import csv
import datetime
import os
import sys
filesoal= 'kuesioner.csv'
filejawab= 'hasilvoting.csv'
fileSaran= 'saran.csv'
fileBerita= 'berita.csv'
filecsv= 'loginPass.csv'
x = datetime.datetime.now()
tanggal= x.strftime("%A, %d-%b-%Y")


def clear():
    os.system('cls')


def selesai():
    sys.exit()


def backtoMenuWarga():
    print("\n")
    input("Tekan ENTER untuk kembali...")
    menuWarga()


def backtoMenuWellcome():
    print("\n")
    input("Tekan ENTER untuk kembali...")
    menuWellcome()


def backtoMenuAdmin():
    print("\n")
    input("Tekan ENTER untuk kembali...")
    menuAdmin()


def logout() :
    clear()
    menuWellcome()


def buatAkun() :
    clear()
    penampung= []
    bio= dict()
 
    namaKolom= ['Nama    ', 'NIK     ', 'Password']

    nama    = input('Nama     = ')
    nik     = input('NIK      = ')
    password= input('Password = ')

    with open(filecsv, 'r') as file:
        reader= csv.DictReader(file, delimiter=',')
        for data in reader:
            penampung.append(data)
            
    bio['Nama    ']= nama
    bio['NIK     ']= nik
    bio['Password']= password

    penampung.append(bio)

    with open(filecsv, 'w', newline='') as file:
        penulis= csv.DictWriter(file, delimiter=',', fieldnames= namaKolom)
        penulis.writeheader()
        penulis.writerows(penampung)

    if password != '128432':
        menuWarga()
    elif password == '128432':
        menuAdmin()
    


def login() :
    clear()
    print('===LOG IN===')
    nama    = input('nama    = ')
    password= input('password= ')

    dataDiri= []

    with open(filecsv, 'r') as file:
        pembaca= csv.DictReader(file, delimiter=',')
        for data in pembaca:
            dataDiri.append(data)

    for sel in dataDiri:
        if nama==sel['Nama    ']:
            sandi= sel['Password']
            if password == sandi:
                if sandi == '128432' :
                    menuAdmin()
                else:
                    menuWarga()
    print('Akun belum terdaftar!')
    backtoMenuWellcome()



iniPass= []

def tambahsaran() :
    clear()
    namaKolom = ['Tanggal', 'Nama', 'Saran']

    nama     = input('Nama penulis = ')
    saran    = input('Saran penulis= ')
    print('Tanggapan anda berhasil terkirim!')

    databaru= dict()     
    penampung= []  

    databaru['Tanggal'] = tanggal
    databaru['Nama'] = nama
    databaru['Saran'] = saran

    with open(fileSaran, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for data in reader:
            penampung.append(data)

    penampung.append(databaru)

    with open(fileSaran, 'w', newline='') as csvFile:
        writer= csv.DictWriter(csvFile, delimiter=',', fieldnames=namaKolom)  
        writer.writeheader()
        writer.writerows(penampung)
    backtoMenuWarga()



def bacasaran() :
    clear()
    with open(fileSaran, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for data in reader:
            for key, value in data.items() :
                print("{} = {}".format(key, value))
            print()
    backtoMenuAdmin()



def tambahberita() :
    clear()
        
    namaKolom = ['Tanggal   ', 'Judul     ', 'Isi Berita']

    judul= input('Judul berita= ')
    isi  = input('Isi berita  = ')
    print('Berita berhasil terkirim!')

    databaru= dict()     
    penampung= []  

    databaru['Tanggal   '] = tanggal
    databaru['Judul     '] = judul
    databaru['Isi Berita'] = isi

    penampung.append(databaru)

    with open(fileBerita, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for data in reader:
            penampung.append(data)

    with open(fileBerita, 'w', newline='') as csvFile:
        writer= csv.DictWriter(csvFile, delimiter=',', fieldnames=namaKolom)  
        writer.writeheader()
        writer.writerows(penampung)
    backtoMenuAdmin()



def editberita() :
    clear()
    namaKolom = ['Tanggal   ', 'Judul     ', 'Isi Berita']
    sunting= input('Judul yang ingin disunting= ')
    penampung= []

    with open(fileBerita, 'r') as berita:
        reader= csv.DictReader(berita, delimiter=',')
        for data in reader:
            penampung.append(data)
        
    for data in penampung:
        if data['Judul     '] == sunting:
            for key, value in data.items() :
                print("{} = {}".format(key, value))
            print()

            judulbaru= input('Masukan judul baru= ')
            isibaru  = input('Tulis isi berita  = ')
            print('Berita berhasil diperbaharui!\n')
            data.update({'Judul     ': judulbaru})
            data.update({'Isi Berita': isibaru})

            for key, value in data.items() :
                print("{} = {}".format(key, value))
            print()

            with open(fileBerita, 'w', newline='') as file:
                penulis= csv.DictWriter(file, delimiter=',', fieldnames= namaKolom)
                penulis.writeheader()
                penulis.writerows(penampung)
    backtoMenuAdmin()



def bacaberitawarga() :
    clear()
    with open(fileBerita, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for data in reader:
            for key, value in data.items() :
                print("{} = {}".format(key, value))
            print()

    backtoMenuWarga()



def bacaberitaadmin() :
    clear()
    with open(fileBerita, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for data in reader:
            for key, value in data.items() :
                print("{} = {}".format(key, value))
            print()

    backtoMenuAdmin()




def kirimQ() :
    clear()
    hasil=[]
    with open(filejawab, 'w', newline='') as file:
        penulis= csv.writer(file, delimiter=',')
        penulis.writerows(hasil)
        
    penampung= []
    kuesioner= dict()
    header= ['Apa pendapat anda tentang    ', 'Pilih salah satu jawaban dari']
    soal= '\n' + input('Tulis pertanyaan anda= ') + '\n'
    pilihan= '\na. Sangat setuju\nb. Setuju\nc. Kurang setuju\nd. Tidak setuju'

    kuesioner['Apa pendapat anda tentang    ']= soal
    kuesioner['Pilih salah satu jawaban dari']= pilihan

    penampung.append(kuesioner)

    with open(filesoal, 'w', newline='') as soal :
        penulis= csv.DictWriter(soal, delimiter=',', fieldnames=header)
        penulis.writeheader()
        penulis.writerows(penampung)
    
    print('\nKuesioner berhasil terkirim!')
    backtoMenuAdmin()



def bacaQ() :
    with open(filesoal, 'r') as soal:
        pembaca= csv.DictReader(soal, delimiter=',')
        for data in pembaca:
            for key, value in data.items() :
                print("{} = {}".format(key, value))
            print()


def voteAdmin():
    clear()
    bacaQ()

    penampung= []

    jumlaha = []
    jumlahb = []
    jumlahc = []
    jumlahd = []
    with open(filejawab, 'r') as file:
        scanner= csv.reader(file, delimiter=',')
        for sel in scanner:
            penampung.append(sel)

    for data in penampung:
        if data== ['a']:
            jumlaha.append(1)
        elif data== ['b']:
            jumlahb.append(1)
        elif data== ['c']:
            jumlahc.append(1)
        elif data== ['d']:
            jumlahd.append(1)

    print('=======Hasil Kuesioner=======')
    print('     Sangat setuju= ', len(jumlaha))
    print('     Setuju       = ', len(jumlahb))
    print('     Kurang setuju= ', len(jumlahc))
    print('     Tidak setuju = ', len(jumlahd))
    print('=============================')
    backtoMenuAdmin()

def voteUser():
    clear()
    bacaQ()
    masukan= input('Jawab= ')

    penampung= []

    with open(filejawab, 'a', newline='') as file:
        penulis= csv.writer(file, delimiter=',')
        penulis.writerow(masukan)

    jumlaha = []
    jumlahb = []
    jumlahc = []
    jumlahd = []
    with open(filejawab, 'r') as file:
        scanner= csv.reader(file, delimiter=',')
        for sel in scanner:
            penampung.append(sel)

    for data in penampung:
        if data== ['a']:
            jumlaha.append(1)
        elif data== ['b']:
            jumlahb.append(1)
        elif data== ['c']:
            jumlahc.append(1)
        elif data== ['d']:
            jumlahd.append(1)
        
    print('\n=======Hasil Kuesioner=======')
    print('     Sangat setuju= ', len(jumlaha))
    print('     Setuju       = ', len(jumlahb))
    print('     Kurang setuju= ', len(jumlahc))
    print('     Tidak setuju = ', len(jumlahd))
    print('~Terimakasih atas masukannya~')
    print('=============================')
    
    backtoMenuWarga()






def menuWarga():
    clear()
    while True:
        print('::::::DESA BOX::::::')
        print('    *MENU WARGA*     \n')
        print('[1] Kotak Saran')
        print('[2] Berita Hari Ini')
        print('[3] Kuesioner')
        print('[4] Log out')
        print('[5] Keluar dari menu')
        print('::::::::::::::::::::\n')
        menu= input('Pilih Menu= ')

        if menu == '1':
            tambahsaran()
        elif menu == '2':
            bacaberitawarga()
        elif menu == '3':
            voteUser()
        elif menu == '4':
            logout()
        elif menu == '5':
            clear()
            selesai()
        else:
            clear()
        print('Input yang anda masukan salah!')
        continue



def menuAdmin() :
    clear()
    while True:
        print('::::::DESA BOX::::::')
        print('    *MENU ADMIN*     \n')
        print('[1] Kotak Saran')
        print('--------------------')
        print('[2] Berita Hari Ini')
        print('[3] Tulis Berita')
        print('[4] Sunting Berita')
        print('--------------------')
        print('[5] Buat Kuesioner')
        print('[6] Hasil Kuesioner')
        print('--------------------')
        print('[7] Log out')
        print('[8] Keluar dari menu')
        print('::::::::::::::::::::\n')
        menu= input('Pilih Menu= ')

        if menu == '1':
            bacasaran()
        elif menu == '2':
            bacaberitaadmin()
        elif menu == '3':
            tambahberita()
        elif menu == '4':
            editberita()
        elif menu == '5':
            kirimQ()
        elif menu == '6':
            voteAdmin()
        elif menu == '7':
            logout()
        elif menu == '8':
            clear()
            selesai()
        else:
            clear()
        print('\nInput yang anda masukan salah!')
        continue
        


def menuWellcome() :
    clear()
    while True:
        print('::::::DESA BOX::::::')
        print('  ~Selamat Datang~\n')
        print('[1] Login')
        print('[2] Buat Akun Baru')
        print('[3] Keluar')
        print('::::::::::::::::::::\n')
        menu= input('Pilih Menu= ')
        
        if menu == '1' :
            login()
        elif menu == '2' :
            buatAkun()
        elif menu == '3' :
            clear()
            selesai()
        else:
            clear()
        print('\nInput yang anda masukan salah!')
        continue

menuWellcome()