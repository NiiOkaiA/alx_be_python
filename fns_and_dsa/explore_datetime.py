from datetime import datetime
from datetime import timedelta

#now=datetime.now()
#print(now)



def display_current_datetime():
    current_date=datetime.now()
    print(current_date)
    return current_date

now=display_current_datetime()
   # display_current_datetime()

#  nonlocal current_date
def calculate_future_date():    
  future_date =now+timedelta(days=int(input("number of days")))  
  print(future_date)




calculate_future_date()
