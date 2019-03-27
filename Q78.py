person = {}
for i in range(3):
    name = input("name:")
    age = int(input("age:"))
    person.update({name:age})
maxage = 0
for value in person.values():
    maxage = max(maxage, value)
for key,value in person.items():
    if value == maxage:
        print(key)
