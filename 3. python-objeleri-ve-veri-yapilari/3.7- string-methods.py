message="benim adım ışık"

# message=message.upper()

# print(message)

# print(message.lower())

# print(message.title())

# print(message.capitalize())

# message=message.strip() #kullanıcının girdiği baş ve sondaki boş karakterleri bu şekilde silebilirsin
# message=message.split() #cümleyi parçalara ayırır. dizi şekilde kullanabilirsin daha sonrasında, print(message[2])
# split'i .split('.') olarak da ayarlayabilirsin

# ayrı olarak gelen bilgileri tekrar birleştir. message=' '.join(message)

# index = message.find("ışık")
# print(index)   -> negatif olursa cümle içerisinde kelime geçmiyor, sayı çıkarsa başladığı index yazdırılır.

# isFound = message.startswith("b")
# print(isFound)

# isFound = message.endswith("k")
# print(isFound)

# message = message.replace("ışık","yoel").replace(" ", ".")
# print(message)

message = message.center(100,"*")
print(message)