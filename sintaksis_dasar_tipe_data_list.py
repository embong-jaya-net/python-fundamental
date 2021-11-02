"""
Sintaksis Dasar Tipe Data List
"""
daftar_buku = ['buku1','buku2','buku3','buku4']

# print daftar_buku
print('\nPrint variable daftar_buku')
print(daftar_buku)

# print daftar buku dengan for
print('\nPrint isi variable daftar_buku dengan for in')
for buku in daftar_buku :
    print(buku)

print('\nPrint variable daftar_buku dengan for in range')
for i in range(0,len(daftar_buku)) :
    print(daftar_buku[i])


print('\nPrint variable daftar_buku dengan indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[-1])
print(daftar_buku[-2])
print(daftar_buku[-4])

# Menambahkan element ke dalam list data dengan append
daftar_buku.append('buku5')
print('\nPrint variable daftar_buku yang sudah ditambah element datanya')
print(daftar_buku)

# Mengganti nilai dari element list data
daftar_buku[0] = 'buku6'
print('\nPrint variable daftar_buku yang element pertamanya sudah di ganti menjadi buku6')
print(daftar_buku)

# Mengambil salah satu element data pada list dengan pop
daftar_buku.pop(0)
print('\nPrint variable daftar_buku yang element pertamanya sudah diambil')
print(daftar_buku)

# Perintah pop jikda tidak memberikan nilai indeks maka otomatis akan mengambil element data terakhir pada list
daftar_buku = ['buku1','buku2','buku3','buku4']
daftar_buku.pop()
print('\nPrint variable daftar_buku yang sudah diambil datanya dengan perintah pop tanpa memberikan indeks pada pop')
print(daftar_buku)

# Nilai emelent yg diambil dengan pop dapat disimpan ke dalam variable
daftar_buku = ['buku1','buku2','buku3','buku4']
x = daftar_buku.pop(1)
print('\nPrint variable yang nilainya adalah nilai element pd list yg sudah diambil dengan pop')
print(x)

# Nilai (isi) dari variable list dapat dihapus dengan perintah clear
daftar_buku = ['buku1','buku2','buku3','buku4']
daftar_buku.clear()
print('\nPrint variable daftar_buku yang isiya sudah dihapus')
print(daftar_buku)











