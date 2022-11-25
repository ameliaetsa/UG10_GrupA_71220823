nama = input("Masukkan nama mahasiswa : ")
nim = (input("Masukkan NIM-nya : "))

if nim[0:2] == "71" and nim[2:4] >= "20" and nim[2:4] <= "22":
    print(nama, "merupakan mahasiswa informatika angkatan 20 hingga 22")
else : 
    print(nama, "bukan merupakan mahasiswa informatika angkatan 20 hingga 22")