Height = float(input("Enter your height in m^2 :"))
Weight = float(input("Enter your weight in kg :"))
BMI = Weight/Height**2
if BMI <=18.5 :
    print(f"Your'e BMI is {BMI} You're underweight ")
elif BMI > 18.5 and BMI < 25:
    print(f"Your'e BMI is {BMI} You have a normal weight ")
elif BMI > 30 and BMI < 35:
    print(f"Your'e BMI is {BMI} You are obese")
else:
    print(f"Your'e BMI is {BMI} You are clinicaly obese ")