def perform_operation(num1, num2, operation):
    if operation=="add":
        return num1+num2

    elif operation=="subtract":
        return num1-num2

    elif operation=="multiply":
        return num1*num2

    elif operation=="divide":
        if num2 == 0:
             print("cannot divide by 0")
             exit()
           
        else:
             return num1/num2
           
        


    
    '''
    match operation:
        case 'add':
            return num1+num2

        case 'subtract':
            return num1-num2

        case 'multiply':
            return num1*num2

        case 'divide':
            if (num2!=0):
                      return num1/num2
            else:
                print("cannot divide by 0")
'''

    

