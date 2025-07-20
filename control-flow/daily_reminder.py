task=input("Enter your task:")

priority=input("Priority (high/medium/low):")

time_bound=input("Is it time-bound?  (yes/no):")


match priority:
    case "high":
        if time_bound=="yes":
             print(f"{task} is a {priority} task that requires your attention today.")
           #  print(task, "is a",priority,"priority task that requires your attention today")
       
       # else :
           #  print(f"{task} is a {priority} task. Consider completing it when you have time.")
    case _:
         print(f"{task} is a {priority} task. Consider completing it when you have time.")
       
        
  # case "low":
   #      if time_bound=="no"
    #     print(task, "is a",priority,"priority task. Consider completing it when you have time")

#match priority:
 #   case "high":
  #        print(task, "is a",priority,"priority task that requires your attention today")
   
