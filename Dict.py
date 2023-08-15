user_dict = {}

while True:
    key = input("Enter a key: ")
    value = input("Enter a value: ")

    user_dict[key] = value

    more = input("Do you want to add more? (yes/no): ")
    if more.lower == "no":
        break

print(user_dict)
