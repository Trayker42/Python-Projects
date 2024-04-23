#Code to get the price of a given item

itery = ["Books", "Food", "Clothes"]
print(itery)

a = input("Which item do you want to get? ")
b = a.lower()

items = {"Books": 650,
          "Food": 100,
          "Clothes": 700}

if b == "books":
    x = items["Books"]
    print(f"The price of {a} is {x} rupees")
elif b == "food":
    x = items["Food"]
    print(f"The price of {a} is {x} rupees")
elif b == "clothes":
    x = items["Clothes"]
    print(f"The price of {a} is {x} rupees")
