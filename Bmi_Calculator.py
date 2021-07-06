print("BMI Calculator:\n")
# Taking your height and weight as input and type casting it into float
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# Calculating their BMI & rounding off the result.
bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

