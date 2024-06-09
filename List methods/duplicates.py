numbers = [2, 2, 4 ,5 ,5, 8, 8, 9 , 14,]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)        