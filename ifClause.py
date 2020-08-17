# if clause
# name = "Jiab"
# weight_kg = 50
# height_m = 1.62
#
# bmi = weight_kg / (height_m ** 2)
# print(bmi)
#
# if bmi < 25:
#     print("Hi, Jiab, you are in a good shape.")
# elif bmi == 25:
#     print("Hi, Jiab, you are almost there.")
# else:
#     print("Hi, Jiab, you are overweight should diet quickly.")
#
# # Function
# def bmiCal(w, h, n):
#     calBmi = (0.45 * w) / (h ** 2)
#     print(calBmi)
#     if calBmi < 25:
#         print(f"Hi, {n}, you are in a good shape.")
#     else:
#         print(f"Hi, {n}, you are overweight should diet quickly.")
#
#
# bmiCal(160, 1.63, 'Tim')
# bmiCal(112, 1.62, 'J')
# print("This is out of bmiCal function.")

name = input("What is your name? ")
weight_lbs = input('What is your weight (lbs)? ')
weight_kg = float(weight_lbs) * 0.45
weight = str(weight_kg)
print(name + ", you weigh " + weight + " Kg.")  # Didn't use formatted string
height_m = input('How tall are you (m)? ')
height = float(height_m)
bmi = weight_kg / (height ** 2)
print(bmi)
print()
print('\n')
print(f"Your BMI is {bmi:.2f}")  # New formatted string
print("Your BMI is %.2f" % bmi)  # Old formatted string

if bmi < 18.5:
    print(f'Hi, {name}, you are Underweight.')

elif 18.5 <= bmi <= 24.9:
    print('')
    print(f'Hi, {name}, you are in a good shape.')

elif 25 <= bmi <= 29.9:
    print(f'Hi, {name}, you are Overweight.')

else:
    print(f'Hi, {name}, you are Obese.')

