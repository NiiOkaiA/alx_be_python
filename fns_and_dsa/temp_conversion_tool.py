FAHRENHEIT_TO_CELSIUS_FACTOR= 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR= 9/5



def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit} fahrenheit is {celsius} celsius")


def celsius_to_farenheit(celcius):
    fahrenheit=(celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    print(f"{celcius} celsius is {fahrenheit} fahrenheit")


number=int(input("Enter the temperature to convert:"))

if  type(number) in (int,float):
    print("Invalid temperature. Please enter a numeric value.")
celfar=input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if celfar=='C':
    celsius_to_fahrenheit(number)


if celfar=='F':
    fahrenheit_to_celsius(number)

    
