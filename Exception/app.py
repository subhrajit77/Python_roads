# try:
#     age=int(input('Enter your age: '))
#     print(age)
# except ValueError:
#     print('Invalid input')    

try:
    age = int(input('Enter your age: '))
    income = 2000
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid input')