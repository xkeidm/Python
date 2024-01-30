# ”Bmw, Mercedes, Opel, Mazda” elemanlarına sahip bir liste oluşturunuz.
arabalar=["BMW", "Mercedes", "Opel", "Mazda"]

# Liste Kaç elemanlıdır ?
print(len(arabalar))

# Listenin ilk ve son elemanı nedir ?
print(arabalar[0])
print(arabalar[3])
print(arabalar[-1])

# Mazda değerini Toyota ile değiştirin.
arabalar[-1]="Toyota"
print(arabalar)

# Mercedes listenin bir elemanı mıdır ?
print("Mercedes" in arabalar)

# Listenin -2 indeksindeki değer nedir ?
print(arabalar[-2])

# Listenin ilk 3 elemanını alın.
print(arabalar[0:3])
print(arabalar[:3])

# Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:]=["Toyota", "Renault"]
print(arabalar)

# Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
print(arabalar + ["Audi", "Nissan"])

# Listenin son elemanını silin.
del arabalar[-1]
print(arabalar)

# Liste elemanlarını tersten yazdırınız.
print(arabalar[::-1])

# Aşağıdaki verileri bir liste içinde saklayınız.
    # studentA: Yiğit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan 1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["yiğit", "bilgi", 2010, [70,60,70]]
studentB = ["sena", "bilgi", 1999, [80,80,70]]
studentC = ["ahmet", "bilgi", 1998, [80,70,90]]

# Liste elemanlarını ekrana yazdırınız.

print(studentA[0])
print(studentB[1])
print(studentC[3])
print(studentC[3][1])

print(f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}")