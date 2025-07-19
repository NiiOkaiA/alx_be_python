num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if num2==0:
        print("Cannot divide by 0")
        exit()
operation=input("Choose the operation (+, -, *, /):")



match operation:
        case "+":
             result=num1+num2
             print("The result is",result)
        case "-":
             result=num1-num2
             print("The result is",result)
        case "*":
             result=num1*num2
             print("The result is",result)
        case "/":
             result=num1/num2
             print("The result is",result)


'''
if operation =="+":
    result= num1+num2
elif operation=="-":
    result=num1-num2
elif operation=="*":
    result=num1*num2
elif operation=="/" :
    if num2==0:
        print("cannot divide by 0")
        exit()
    result=num1/num2
else:
    print("choose something from the list")
    exit()

print ("The result is",result)
'''
 
