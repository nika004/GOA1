data = [] #შევქმენით ლისთი 


def register(): #შევქმენით დროებითი ცვლადი register და მომხმარებეკს შემოვაყვანინეთ სახელი და პაროლი
    username = input("Enter your username:")
    password = input("Create a new password:")
    #აქ შევქმენით დიქშენერი სადაც გასაღები name i da password i გვაქ რომლებსაც მნიშვნელობად აქვთ მომხმარებლის შემოყვანილი მონაცემი -username,password
    current_user = {
        "name":username,
        "password":password
    }
    if len(data) == 0: #აქ შევამოწმეთ თუ ჩვენ მიერ შექმნილი DATA სიის ელემენტების რაოდენობა ნოლს უდრიდა და თუ იყო TRUE ჭეშმარიტია დაპრინტავ და "Registration successfull!" და DATA სიაში ჩაამატებდა დიქშენერის
        print("Registration successfull!")
        data.append(current_user)
    
    elif len(data) > 0: #აქ შევამოწმეთ თუ ჩვენ მიერ data სიის ელემენტების რაოდენობა ნოლხე მეტი იყო თუ არა თუ იყო ჭეშმარიტი გადავიდოდა if elsზე და შეამოწმებდა თუ data სიაში უკვე იყო მომხმარებლის მიერ შემოყვანილი მონაცემი და თუ იყო თავიდან შემოვაყვანინებდით მონაცემს და მომხმარებლის პირველი შემოყვანილი მონაცემი ჩაენაცვლებოდა ახალი შემოყვანილი მონაცემით და დაემატებოდა data სიაში
        for i in data:
            if i["name"] == current_user["name"]:
                print("username already exists!")
                username = input("Enter another username again: ")
                current_user["name"] = username
                data.append(current_user)
                break
            else:#აქ გამოვიყენეთ else რომ თუ არ იყო მომხმაებლის მიერ შემომოყვანილი მონაცემი data სიაში და data სიაში აიტვირთებოდა მონაცემი და დაპრინთავდა "Registration successfull!"
                print("Registration successfull!")
                data.append(current_user)
                break




    username1 = input("Enter your username:")
    password1 = input("Enter your password:")

    current_user1 = {
        "name":username,
        "password":password
    }
    if len(data) > 0:
        for i in data:
            if i["name"] == username1 and i["password"]==password1:
                print("Login successfull!")
                data.append(username1)
                break

            else:
                print("Login failed")
                username2=input("Enter your Username again!")
                password2=input("Enter your password again!")
                current_user1["name"]==username2
                current_user1["password"]==password2
                data.append(current_user1)
                break
    return data

        
print(register())




