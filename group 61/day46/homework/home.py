# 1)Prompt the user to enter a number. If the input is not a number, display an error message. use error handling

# 2)Create a list and try to access an index that does not exist. Handle IndexError.

# 3)Try adding an integer to a string and catch the TypeError.

# 4)დაასრულეთ საკლასო დავალება ვისაც არ დაგისრულებიათ

# 5) აუცილებლად გადახედეთ თავიდან ჩანაწერს და რესურსებში ჩაგდებულ სქრინს გადახედეთ სადაც განმარტებულია, თითოეული ერორი როდის ვარდება

num = input("Enter a number: ")
try:
    num = int(num)
    print("You entered the number:", num)
except ValueError:
    print("Error")

lst = [1, 2, 3]

try:
    print(lst[5])
except IndexError:
    print("Error") 

num2 = 10
try:
    print(num2 + " years")
except TypeError:
    print("Error")

