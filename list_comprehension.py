"""
List comprehension memberikan syntak yang lebih singkat untuk membuat sebuah list baru dari list yg sudah ada
"""

# Membuat list baru dengan element data yg mengandung karakter tertentu dari element data dari lis lama
old_list = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_list = []
print('List lama')
print(old_list)
print('\nList baru')
print(new_list)

# Syntax 1
for x in old_list:
    if 'a' in x:
        new_list.append(x)
print('\nsyntax 1 ==> for x in old_list : if "a" in x : new_list.append(x)')
print('Ambil element data dari list lama yg mengandung huruf a kemudian masukkan ke dalam list baru')
print('List baru')
print(new_list)
print('-' * 100)


old_list = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
print('List lama')
print(old_list)
# Syntax 2
new_list = [x for x in old_list if 'a' in x]
print('\nsyntax 2 ==> new_list = [x for x in old_list if "a" in x]')
print('Ambil element data dari list lama yg mengandung huruf a kemudian masukkan ke dalam list baru')
print('List baru')
print(new_list)
print('-' * 100)

# Membuat list baru dengan element data dari list lama yang tidak mengandung huruf 'a'
old_list = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_list = [x for x in old_list if 'a' not in x]
print(new_list)


















