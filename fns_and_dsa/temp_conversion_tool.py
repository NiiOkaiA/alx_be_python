FARENHEIT_TO_CELCIUS_FACTOR=5/9
CELCIUS_TO_FARENHEIT_FACTOR=9/5



def convert_to_celcius(farenheit):
    celcius=FARENHEIT_TO_CELCIUS_FACTOR*farenheit
    print(f"{farenheit} farenheit is {celcius} celcius")


def convert_to_farenheit(celcius):
    farenheit=CELCIUS_TO_FARENHEIT_FACTOR*celcius
    print(f"{celcius} celcius is {farenheit} farenheit")


number=int(input("Enter the temprature to convert:"))

celfar=input("Is this temprature in Celcius or Farenheit (C/F):")

if celfar=='C':
    convert_to_farenheit(number)


if celfar=='F':
    farenheit_to_celcius(number)

    
