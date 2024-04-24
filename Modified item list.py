itery = ["books", "food", "clothes"]
print(itery)
a = input("Which item do you want to get? ").lower().strip()
items = {"books": 650, "food": 100, "clothes": 700}


def printMoni(item): print(f"The price of {item} is {items[item]} rupees")


def money():
    if a == "books":
        printMoni(a)
    elif a == "food":
        printMoni(a)
    elif a == "clothes":
        printMoni(a)
    elif a == new_items:
        printMoni(new_items)


money()

y = int(input("If you are an employee\nWhat is the password? "))
if y == 2048:
    new_items = input("Names of the new items to be added: ").strip()
    amount = input("What is the amount of the item: ")
    itery.append(new_items)
    items[new_items] = amount
    a = input("Which item do you want to get? ").lower().strip()
    money()
else:
    print("Thank for enquiring about the items.")
