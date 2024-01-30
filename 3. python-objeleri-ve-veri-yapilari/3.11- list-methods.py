numbers=[1,10,5,16,4,9,10]
letters=["a","g","s","b","y","a","s"]

print(min(numbers))
print(max(numbers))
print(max(letters)+" "+min(letters))

print(numbers[3:6])

numbers.append(51) #ekledi
print(numbers)

numbers.insert(3,78)
print(numbers)

numbers.insert(-1,69)
print(numbers)

numbers.pop() # içine bişi yazılmazsa en sondakini siler. içine array number yazarak silmek istediğin konumu silebilirsin
print(numbers)

numbers.remove(1)
print(numbers)

numbers.sort()
print(numbers)

letters.sort()
print(letters)

numbers.reverse()
print(numbers)

letters.reverse()
print(letters)

print(letters.count("a"))

