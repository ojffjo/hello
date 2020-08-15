course = "Python for Beginer"
print(course[0:5])

name = input("What is your name? ")
weight_lbs = input('What is your weight (lbs)? ')
weight_kg = float(weight_lbs) * 0.45
weight = str(weight_kg)
print(name + ", you weigh " + weight + " Kg.")
height_m = input('How tall are you (m)? ')
height = float(height_m)
bmi = weight_kg / (height ** 2)
print(f"Your BMI is {bmi}")
print("Your BMI is " "%.2f" % bmi)
