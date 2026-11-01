while True:
    try:
        number = int(input("Enter a Number: "))
        if number % 2 == 0:
            print("You have Entered an EVEN Number")
        else:
            print("You have Entered an ODD Number")
        break
    except ValueError:
        print("You have Entered a worng input")