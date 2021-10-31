"""
Perulangan dengan while dan if
"""
print('Ibu memerintahkan Budi untuk membaca semua bukunya')
print('Budi menjawab, "Iya Bu"')
jumlah_semua_buku = 10
print(f'jumlah semua buku Budi adalah {jumlah_semua_buku}')
jumlah_buku_dibaca = 0
print(f'jumlah buku yang sudah dibaca Budi adalah {jumlah_buku_dibaca}')
jumlah_buku_dibaca_dan_faham = 0
print(f'jumlah buku yg sudah dibaca dan difahami adalah {jumlah_buku_dibaca_dan_faham}')
print('Budi mulai membaca buku')

while jumlah_buku_dibaca < jumlah_semua_buku * 2 :
    jumlah_buku_dibaca = jumlah_buku_dibaca + 1
    if jumlah_buku_dibaca_dan_faham == 9 :
        print(f'Buku ke {jumlah_buku_dibaca_dan_faham + 1} belum faham')
    else:
        jumlah_buku_dibaca_dan_faham = jumlah_buku_dibaca_dan_faham + 1
        print(f'Buku ke- {jumlah_buku_dibaca_dan_faham} sudah dibaca dan difahami')

print(f'Jumlah buku yang sudah dibaca dan difahami {jumlah_buku_dibaca_dan_faham}')
if jumlah_buku_dibaca_dan_faham == jumlah_semua_buku :
    print('Semua buku sudah dibaca dan difahami Budi')
else:
    print(f'Tidak semua buku bisa difahami Budi, Budi hanya bisa memahami {jumlah_buku_dibaca_dan_faham} buku')





print('Budi sudah membaca semua bukunya')



