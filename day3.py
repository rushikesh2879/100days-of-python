# BMI calculator
# Enter your height in meters e.g., 1.55
height = float(input("Enter height:"))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter weight:"))
bmi = weight / (height * height)
if bmi <= 18.5 :
  print(f"Your BMI is {bmi}, you are underweight.")
elif  bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese")

# Cheack the input year is LEap or Not
year = int(input("Enter the Year:"))

if year % 4 == 0:
  if year %100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else :
  print("Not leap year")
