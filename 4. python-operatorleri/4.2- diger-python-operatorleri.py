# identity operator: is
x=y=[1,2,3]
z=[1,2,3]

print(x==y)
print(x==z)

print(x is y)
print(x is z) # is kullanılırken, tanımlanan objelerin aynı adresi tutup tutmadığına bakılır.

# membership operator: in

a=["apple","banana"]
print("banana" in a)

print("a" not in a)