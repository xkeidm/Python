# ogrenciler= {
#     "120":{
#         "ad":"Ali",
#         "soyad":"Yilmaz",
#         "telefon:":"123"
#     },
#     "125":{
#         "ad":"Can",
#         "soyad":"Yilmaz",
#         "telefon:":"456"
#     },
#     "128":{
#         "ad":"Volkan",
#         "soyad":"Yilmaz",
#         "telefon:":"789"
#     }
# }

# 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

ogrenciler={}

number=input("ogrenci no: ")
name=input("ogrenci adı: ")
surname=input("ogrenci soyad: ")
phone=input("ogrenci telefon: ")

# ogrenciler[number] = {
#     "ad":name,
#     "soyad":surname,
#     "telefon":phone
# }

ogrenciler.update({ # update çoklu bir şekilde kullanılabilir, sonuna ',' eklenerek.
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

print(ogrenciler)
