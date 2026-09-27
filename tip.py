bill = float(input("Bill amount: "))
tip_percent = float(input("Tip percentage: "))
people = int(input("Number of people: "))

tip = bill * tip_percent / 100
total = bill + tip
each = total / people

print("Each person pays:", round(each, 2))
