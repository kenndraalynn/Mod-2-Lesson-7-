
userweather = input("What is the temperature? (in Fahrenheit) ")

def weatherchange(userweather):
    celsiustemp = ((userweather - 32) * (5/9))
    return celsiustemp  

try:
    celsiusoutput = float(userweather)
except:
    print("Invalid, please use numerical values")
else:
    print(round(weatherchange(celsiusoutput)))
finally:
    print("Thank you for your input!")
    







