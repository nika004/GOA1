# ```1)შექმენით ახალი სია, რომელიც შეიცავს 1-დან 10-მდე რიცხვების კვადრატებს.

# 2) მოცემული სიიდან [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] შეარჩიეთ მხოლოდ ლუწი რიცხვები.

# 3)მოცემული სტრიქონების სიიდან ["apple", "banana", "cherry", "date"] შექმენით ახალი სია, სადაც ყველა სიტყვა დიდი ასოებით იქნება დაწერილი.

# 4)მოცემული სიიდან ["cat", "dog", "elephant", "mouse"] შექმენით ახალი სია, რომელიც შეიცავს თითოეული სიტყვის სიგრძეს.

# 5)მოცემული სიიდან [5, 12, 8, 20, 3, 15] შექმენით ახალი სია, რომელიც შეიცავს მხოლოდ 10-ზე მეტ რიცხვებს.

# 6)მოცემული სიის [1, 2, 3, 4] თითოეული ელემენტი გაამრავლეთ 5-ზე.

# 7)მოცემული სიიდან ["hello", "world", "python", "programming", "list"] აირჩიეთ მხოლოდ ის სიტყვები, რომლებიც იწყება ასო 'p'-ით.

# 8)1-დან 10-მდე რიცხვებისთვის შექმენით სია, სადაც ლუწი რიცხვებისთვის ჩაიწერება 'Even', ხოლო კენტი რიცხვებისთვის 'Odd'.

# 9)აუცილებლად გადახედეთ ჩანაწერს და დაიწყეთ ჯგუფურ სამუშაოზეც მუშაობა

list=[1,2,3,4,5,6,7,8,9,10]

list1=[]
for i in list:
    list1.append(i **2)

print(list1)

list2=[]
for i in list:
    if i % 2 ==0:
        list2.append(i)

fruits=["apple", "banana", "cherry", "date"]
fruits2=[]
for i in fruits:
    fruits2.append(i.upper())
print(fruits2)

live=["cat", "dog", "elephant", "mouse"]
live2=[]
for i in live:
    live2.append(len(i))
print(live2)


list3=[5, 12, 8, 20, 3, 15]
list4=[]
for i in list3:
    if i > 10:
        list4.append(i)

print(list4)


num=[1, 2, 3, 4]
num1=[]
for i in num:
    num1.append(i*5)


word=["hello", "world", "python", "programming", "list"]
word1=[]
for i in word:
    if i.startswith("p"):
        word1.append(i)

for i in list:
    if i % 2==0:
        print("even")
    else:
        print("odd")