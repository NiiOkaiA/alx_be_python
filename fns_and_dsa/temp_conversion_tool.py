FAHRENHEIT_TO_CELSIUS_FACTOR= 5/9
CELCIUS_TO_FAHRENHEIT_FACTOR= 9/5



def convert_to_celsius(fahrenheit):
    celsius=FAHRENHEIT_TO_CELSIUS_FACTOR*fahrenheit
    print(f"{fahrenheit} fahrenheit is {celsius} celsius")


def convert_to_farenheit(celcius):
    fahrenheit=CELSIUS_TO_FAHRENHEIT_FACTOR*celsius
    print(f"{celcius} celsius is {fahrenheit} fahrenheit")


number=int(input("Enter the temprature to convert:"))

celfar=input("Is this temprature in Celsius or Fahrenheit (C/F):")

if celfar=='C':
    convert_to_fahrenheit(number)


if celfar=='F':
    convert_to_celsius(number)

    
