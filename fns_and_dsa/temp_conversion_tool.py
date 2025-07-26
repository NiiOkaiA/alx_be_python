FAHRENHEIT_TO_CELCIUS_FACTOR= 5/9
CELCIUS_TO_FAHRENHEIT_FACTOR= 9/5



def convert_to_celcius(fahrenheit):
    celcius=FAHRENHEIT_TO_CELCIUS_FACTOR*fahrenheit
    print(f"{fahrenheit} fahrenheit is {celcius} celcius")


def convert_to_farenheit(celcius):
    fahrenheit=CELCIUS_TO_FAHRENHEIT_FACTOR*celcius
    print(f"{celcius} celcius is {fahrenheit} fahrenheit")


number=int(input("Enter the temprature to convert:"))

celfar=input("Is this temprature in Celcius or Fahrenheit (C/F):")

if celfar=='C':
    convert_to_fahrenheit(number)


if celfar=='F':
    convert_to_celcius(number)

    
