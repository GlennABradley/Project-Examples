height = float(input("enter your height in inches: "))
weight = float(input("enter your weight in lbs: "))

bmi =  weight / height ** 2 * 703
bmi = round(bmi, 1)

result = ""
if bmi < 16.0:
    result = "Severely Underweight"
elif bmi < 18.4:
    result = "Underweight"
elif bmi < 24.9:
    result = "Normal"
elif bmi < 29.9:
    result = "Overweight"
elif bmi < 34.9:
    result = "Moderately Obese"
elif bmi < 39.9:
    result = "Severely Obese"
else:
    result = "Morbidly Obese"

print(f"Your BMI of {bmi} makes you {result}")