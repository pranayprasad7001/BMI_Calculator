print("BMI Calculator:\n")
# Taking your height and weight as input and type casting it into float
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# Calculating their BMI & limiting it decimal digit upto 1.
bmi = round((weight / (height ** 2)), 1)
print("\nYour Body Mass Index (BMI) is: " + str(bmi))
