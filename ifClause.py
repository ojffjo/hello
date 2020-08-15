# if clause
name = "Jiab"
weight_kg = 50
height_m = 1.62

bmi = weight_kg / (height_m ** 2)
print(bmi)

if bmi < 25:
    print("Hi, Jiab, you are in a good shape.")
elif bmi == 25:
    print("Hi, Jiab, you are almost there.")
else:
    print("Hi, Jiab, you are overweight should diet quickly.")

# Function
def bmiCal(w, h, n):
    calBmi = (0.45 * w) / (h ** 2)
    print(calBmi)
    if calBmi < 25:
        print(f"Hi, {n}, you are in a good shape.")
    else:
        print(f"Hi, {n}, you are overweight should diet quickly.")


bmiCal(160, 1.63, 'Tim')
bmiCal(112, 1.62, 'J')
print("This is out of bmiCal function.")