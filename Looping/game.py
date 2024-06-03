secret_number =9
guess_count=0
guess_limit =3

while guess_count<guess_limit :
    guess= int(input("Enter guess : "))
    guess_count += 1 
    if guess==secret_number:
        print("You won!")
        break
    else:
        print(f"Try again and u have {guess_limit -1} times left")

if guess_count == 3:
    print("game over")          