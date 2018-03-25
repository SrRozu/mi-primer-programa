number_to_guess = 2

user_number = int(input("dame un numero: "))

if number_to_guess == user_number:
    print("has ganado")
else:
    int(input("dame un numero: "))
    if number_to_guess == user_number:
         print("has ganado")
    else:
        int(input("dame un numero: "))
        if number_to_guess == user_number:
            print("has ganado")
        else:
              int(input("dame un numero: "))
        if number_to_guess == user_number:
             print("has ganado")
        else:
            int(input("dame un numero: "))
        if number_to_guess == user_number:
         print("has ganado")
        else:
            print("has perdido")