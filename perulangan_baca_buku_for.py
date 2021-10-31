"""
Perulangan dengan for
"""
print('Ibu memerintahkan Budi untuk membaca semua bukunya')
print('Budi menjawab, "Iya Bu"')
jumlah_semua_buku = 10
print(f'jumlah semua buku Budi adalah {jumlah_semua_buku}')
jumlah_buku_dibaca = 0
print(f'jumlah buku yang sudah dibaca Budi adalah {jumlah_buku_dibaca}')
print('Budi mulai membaca buku')

for i in range(1, jumlah_semua_buku + 1):
    print(f'Budi sudah membaca buku ke-{i}')

print('Budi sudah membaca semua bukunya')


