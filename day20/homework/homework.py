name = "Tbilisi"

if name[0].isupper():
    print(name.upper())
else:
    print(name.lower())


name = input("Enter your name: ")



for i in name:
    if i.isupper():
        print(name.lower())
        break
    else:
        print(name.capitalize())
        break
    
    
animals = ["Lion","Dog","Giraffe"]

for i in animals:
    if len(i) < 5 and i == i.capitalize():
        print(i[:3])
    else:
        print(i, "is too long")


names = ["nika", "mari", "gio", "lasha"]
for i in names:
    print(i.upper())


new_list = ["Giorgi",5,True,6.5]


for i in new_list:
    if type(i) == str:
        print(i.upper()[-3:])