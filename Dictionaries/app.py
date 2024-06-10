customer = {
    "name" : "John Doe",
    "age" : 30,
    "is_verified" : True
}
print(customer["name"],  customer["age"])

customer["name"] = "Jack Smith"
customer["birthday"] = "Jan 1 1980"
print(customer["name"]) 
print(customer["birthday"])


phone = input("Phone :")
digits_mapping = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    
    
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, " !") + " "
print(output)    