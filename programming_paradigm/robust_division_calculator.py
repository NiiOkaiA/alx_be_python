


#ValueError - inappropriate value passed to a function
#TypeError  - when an operation is tried with incompatible data types

def safe_divide(numerator,denominator):
    try:
       num= float(numerator)
       den= float(denominator)

       result=num/den
       return f"The result of the division is {float(result)}"

    except ValueError:
        return f"Error: Please enter numeric values only."
    
        
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."

    
    
