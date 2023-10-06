# BMI - Body Mass Index calculator
# --------------------------------

'''
Conditions
-----------
       BMI < 18.5    : Underweight
18.5 <= BMI <= 24.9    : Normal weight
24.9 < BMI <= 29.9    : Over weight
  30 < BMI <= 34.9    : Obessed
       BMI  > 35      : Extremely Obessed 
'''

'''
Formula for BMI
----------------
BMI = Weight(in Kilogram)/height*height(in meter)    
'''
 
weight = float(input("Enter your weight (in Kg) : "))
height = float(input("Enter your weight (in meters) : "))
BMI = weight/(height*height)

if BMI <= 18.5:
    print("Underweight")

elif BMI > 18.5 and BMI <= 24.9:
    print("Normal Weight")

elif BMI > 24.9 and BMI <= 29.9:
    print("Over weight")

elif BMI > 29.9 and BMI <= 34.9:
    print("Obessed")

elif BMI > 35:
    print("Extremely Obessed")

else:
    print("Invalid Details")
