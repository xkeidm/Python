# key -> value
# 41 -> kocaeli | 34 -> istanbul

# sehirler=["kocaeli", "istanbul"]
# plakalar=[41,34]

# print(sehirler.index("kocaeli"))
# print(plakalar[sehirler.index("kocaeli")])

# plakalar = {"kocaeli":41, "istanbul":34}

# print(plakalar["istanbul"])

# print(plakalar)

# plakalar["ankara"] = 6

# print(plakalar)

users = {"isikonkun":{"age":22, 
                      "roles":["admin", "user"],
                      "email": "onkunisik@gmail.com", 
                      "adress": "ankara"}, 
         "yoelonkun":{"age":2, 
                      "roles":["user"],
                      "email": "onkunisik@gmail.com", 
                      "adress": "ankara"}}

# print(users["isikonkun"])
# print(users["isikonkun"]["age"])
# print(users["isikonkun"]["email"])
print(users["isikonkun"]["roles"][0])

