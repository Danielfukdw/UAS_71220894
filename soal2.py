print ("==== Selamat Datang di XXV")
tgl= input ("Masukan Tanggal Hari ini:",)
print ("==== Berikut genre film yang tersedia ====")
print ("1. Horror")
print ("2. Action")
genre =int(input("Silahkan pilih mau nonton film bergenre apa:"))
# def bioskop (genre):
if genre ==(1):
        print ("==== Berikut pilihan film Horror yang sedang tayang ====")
        print ("1. The Devil's Right")
        print ("2. Pengabdi setan")
        film = int(input("Silahkan pilih mau nonton film apa:", ))
elif genre ==(2):
        print ("==== Berikut pilihan film Action yang sedang tayang ====")
        print ("1. Black Panther: Wakanda Forever")
        print ("2. Avatar: The Way of Water")
        film = int(input("Silahkan pilih mau nonton film apa:", ))
else : 
        print ("Pilihan yang anda pilih tidak tersedia di bioskop ini")
jumlah =int(input("Mau memesan tiket sebanyak:", ))
price = 25000
total =price *jumlah
print ("Total yang harus dibayar adalah: Rp.",total)


# if film ==(1):
#     jumlah =int(input("Mau memesan tiket sebanyak:", ))
#     print ("Total yang harus dibayar adalah: Rp.",tiket)
# def film (film):
#     if