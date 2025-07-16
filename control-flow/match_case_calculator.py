num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

operation=input("choose the operation(+,-,*,/):")

if operation =="+":
    result= num1+num2
elif operation=="-":
    result=num1-num2
elif operation=="*":
    result=num1*num2
elif operation=="/" :
    if num2==0:
        print("no division by 0")
        exit()
    result=num1/num2
else:
    print("choose something from the list")
    exit()

print ("The result is",result)
