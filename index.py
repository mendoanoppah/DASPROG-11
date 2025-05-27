# fungsi reverse_per_kata: mereverse setiap kata dalam kalimat
def reverse_per_kata(kalimat):
    kataList = kalimat.split()
    hasil = " ".join([kata[::-1] for kata in kataList])
    return hasil

# fungsi urutkan_kalimat: mengurutkan kata berdasarkan indeks list
def urutkan_kalimat(kalimat, urutan):
    kataList = kalimat.split()
    hasil = []

    for posisi in urutan:
        index = posisi - 1
        if 0 <= index < len(kataList):
            hasil.append(kataList[index])
        else:
            hasil.append("salah")
    
    return " ".join(hasil)

# fungsi ganti_vokal: mengganti huruf vokal dengan simbol tertentu
def ganti_vokal(kalimat, opsi):
    vokal_kecil = {"a": "4", "i": "1", "u": "|_|", "e": "3", "o": "0"}
    vokal_kapital = {"A": "4", "I": "1", "U": "|_|", "E": "3", "O": "0"}

    hasil = ""
    for huruf in kalimat:
        if opsi == 1 and huruf in vokal_kecil:
            hasil += vokal_kecil[huruf]
        elif opsi == 2 and huruf in vokal_kapital:
            hasil += vokal_kapital[huruf]
        else:
            hasil += huruf

    return hasil

print("REVERSE:")
print(reverse_per_kata("AKU CINTA KAMU"))  

print("\nURUTAN KALIMAT sesuai INDEX:")
print(urutkan_kalimat("HARI INI SEDANG BELAJAR PYTHON", [5, 1, 4, 3, 2]))  

print("\nGANTI VOKAL:")
print(ganti_vokal("Aku Cinta Kamu", 1))  
print(ganti_vokal("Aku Cinta Kamu", 2))  