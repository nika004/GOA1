num1 = int(input("პირველი რიცხვი: "))
num2 = int(input("მეორე რიცხვი: "))
num3 = int(input("მესამე რიცხვი: "))

def sum_three_numbers(num1, num2, num3):
    return num1 + num2 + num3

def user_info(name, age):
    print(name, "is", age,"წლის") 

def square(num):
    return num ** 2

print("ჯამი:", sum_three_numbers(num1, num2, num3))
print(user_info("Nika", 15))
print("კვადრატი:", square(6))