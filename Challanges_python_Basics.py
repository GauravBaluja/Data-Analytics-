# CHALLANGE 1
#Programming Challenge: Celsius to Fahrenheit

Celcius = ""
Celcius = int(input("Enter temp in Celcius: "))
def temp(Celcius):

    F = round(1.8*Celcius +32,1)    # F is Farenheight & C is Celcuis
    return F

print("The Fahrenheit equivalent of " + str(Celcius) + " degrees Celsius is ", temp(Celcius))
