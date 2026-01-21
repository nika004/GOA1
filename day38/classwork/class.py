# 1)შექმენით dictionary სადაც შენახული იქნება შენი სახელი, ასაკი და ქალაქი.

# შემდეგ ამოიღეთ კონკრეტული მნიშვნელობა და შეინახე ცვლადში.

# ასევე შეცვალეთ რომელიმე მნიშვნელობა რაც გექნება dictionary ში.

# წაშალე ერთი ელემენტი.

# for ციკლის მეშვეობით გამოიტანე თითოეული key და value (არ ამიხსნია ჯერ და მაინტერესებს თუ იზამთ :)) )


# ასევე გამოიტანეთ მხოლოდ value ები

info={
    "name":"nika",
    "age":"16",
    "city":"tbilisi"
}

# name=info.get("name")
# info.update("name":"info")
# info["name"] = "info"
# info1=info.pop("age")

# print(info)



for i in info.items():
    print(i)

for i in info.values():
    print(i)