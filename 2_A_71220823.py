print("="*4, "Selamat datang di Toko Andi Tersenyum, selamat belanja!", "="*4)
total = int(input("Total belanja :Rp "))

#diskon
ss = int(total*(2/100))
sl = int(total*(5/100))
sst = int(total*(10/100))
print(total-sl)


if total >= 100000  and total <= 500000 : 
    print("Biaya yang harus dibayar setelah diskon adalah : Rp.", total-ss)
elif total >= 500000 and total <= 1000000 :
    print("Biaya yang harus dibayar setelah diskon adalah : Rp.", total-sl)
elif total >= 1000000 :
    print("Biaya yang harus dibayar setelah diskon adalah Rp.", total-sst)
else :
    print("Tidak ada diskon! Maka yang Anda bayarkan adalah : Rp.", total)