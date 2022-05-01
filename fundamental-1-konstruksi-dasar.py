# Konstruksi dasar Python
# Sequential: Eksekusi berurutan
print('Hello World!')
print('Tanggal 10 juni 2020')
print('-' * 10)

# Percabangan: Eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('Jalan lain')
    
# Perulangan
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1): #jumlah perulangan = 5 - 1 = 4
    print(f'Halo anak #{index_anak}')