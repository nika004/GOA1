word = input("შეიყვანეთ სიტყვა: ")

lower = word.lower()
upper = word.upper()
capitalized = word.capitalize() 

print("პატარა ასო:", lower)
print("დიდი ასო:", upper)
print("პირველი ასო დიდი, დანარჩენი პატარა:", capitalized)


word2 = input("პირველი წინადადება: ")
word3 = input("მეორე წინადადება: ")
word4 = input("მესამე წინადადება: ")

print("lower ", word2.lower())
print("upper ", word3.upper())
print("capitalize ", word4.capitalize())


my_name = "Nika"
user_name = input("შეიყვანეთ თქვენი სახელი: ")

if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names.")


word5 = "hello world!"


word6 = word5.capitalize()

print(word6)



#lower ყველას გარდაქმნის პატარად
text = "HELLO"
print(text.lower())

# upper ყველა ასოს გარდაქმნის დიდ ფორმად დიდად
text = "hello"
print(text.upper()) 

#capitalize პირველი ასო დიდია, დანარჩენი — პატარა
text = "nika"
print(text.capitalize())  
