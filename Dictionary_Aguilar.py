# Laboratory Activity # 3
# Name: Aengracia Aguilar
# Course and Year: BSCOE 2-2

# this is to print the MENU

print("Menu:")
print("1. -> Add an Item")
print("2. -> Search")
print("3. -> Exit (y/n?)")

# this is to create a dictionary
contactdictionary = {}

# this is to utilize the elif method
while True:
    choices = int(input("What do you want to do? (1-3): "))
    if choices == 1:
        fullname = input("Full name: ")
        age = int(input("Age: "))
        address = input("Address: ")
        phonenumber = int(input("Phone number: "))
        contactdictionary[fullname]={"Age":age,"Address":address,"Phone number":phonenumber}
        print("SAVED!")
    elif choices == 2:
        fullname = input("Full name: ")
        if fullname in contactdictionary.keys():
            for item in contactdictionary[fullname].items():
                print(item[0],":",item[1])
        else:
            print("Full name is not found!")
    elif choices == 3:
        choice2 = input("Exit? ")
        if choice2 == "y":
            break
        else:
            print("Invalid choice!")
