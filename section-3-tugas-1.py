print('Ibu memberi perintah, "Beli 1 Botol Susu"')
print('Anak menjawab, "OK"')
print('Anak pergi ke toko')

susu_ada = True
telur_ada = True
anak_pulang = "Anak pulang ke rumah"
menyerahkan_hasil = "Menyerahkan hasil belanjanya kepada Ibu"
if susu_ada == True:
    print('Anak mengecek harganya, cukup')
    if telur_ada == True:
        print('Anak membeli satu botol susu')
        print(anak_pulang)
        print(menyerahkan_hasil)
    else:
        print('Anak membeli 6 botol susu')
        print(anak_pulang)
        print(menyerahkan_hasil)
else:
    print('Anak tidak jadi membeli susu')
    print(anak_pulang)
    print(menyerahkan_hasil)