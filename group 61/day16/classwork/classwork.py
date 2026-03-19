num = 1
while num <= 20:
    print(num)
    num = num + 1

pin1 = "1234"
pin2 = input("შეიყვანეთ პინ კოდი: ")

while pin2 != pin1:
    print("პინ კოდი არასწორია სცადეთ თავიდან")
    pin2 = input("შეიყვანეთ პინ კოდი: ")

print("პინ კოდი სწორია!")


for num in range(1, 21):
    if num % 2 == 0:
        print(num)

for num in range(1, 31):
    if num % 2 != 0:
        print(num)

num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num = num + 1

