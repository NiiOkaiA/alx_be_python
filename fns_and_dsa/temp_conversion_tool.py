FAHRENHEIT_TO_CELSIUS_FACTOR= 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR= 9/5



def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit} fahrenheit is {celsius} celsius")


def celsius_to_farenheit(celcius):
    fahrenheit=(celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    print(f"{celcius} celsius is {fahrenheit} fahrenheit")


number=int(input("Enter the temprature to convert:"))

celfar=input("Is this temprature in Celsius or Fahrenheit (C/F):")

if celfar=='C':
    celsius_to_fahrenheit(number)


if celfar=='F':
    fahrenheit_to_celsius(number)

    
