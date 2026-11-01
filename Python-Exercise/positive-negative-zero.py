while True:
    try:
        number = int(input("Enter a Number: "))
        if number == 0:
            print("The Entered Number is ZERO")
        elif number > 0:
            print("The Entered Number is POSITIVE")
        else:
            print('The Entered Number is NEGATIVE')
        break
    except ValueError:
        print("You have Entered a wrong input")