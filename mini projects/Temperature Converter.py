# Temperature converter
# _______________________

'''
Fahrenheit to Celsius   : C = (F - 32)*5/9 
Fahrenheight to kelvin  : K = (F - 32)*(5/9) + 273.15
Celsius to Fahrenheit   : F = (9/5)*C + 32
Celsius to kelvin       : K = C + 273.15
kelvin to celsius       : C = K - 273.15
kelvin to fahrenheit    : F = (K - 273.15)*9/5 + 32
'''

Temp_converter_chart = ''' Choose an option :
1.Fahrenheit to Celsius
2.Fahrenheight to kelvin
3.Celsius to Fahrenheit
4.Celsius to kelvin
5.kelvin to celsius
6.kelvin to fahrenheit
'''
print(Temp_converter_chart)

user_inp = int(input("Enter you choice : "))
C=K=F  = float(input("Enter temperatur : "))

if user_inp == 1:
    C = (F - 32)*5/9
    print(C)
elif user_inp == 2:
    K = (F - 32) * (5/9) + 273.15
    print(K)
elif user_inp == 3:
    F = (9/5)*C + 32
    print(F) 
elif user_inp == 4:
    K = C + 273.15
    print(K)
elif user_inp == 5:
    C = K - 273.15
    print(C)
elif user_inp == 6:
    F = (K - 273.15)*9/5 + 32
    print(F)
else:
    print("Invalid input! ⚠️")
