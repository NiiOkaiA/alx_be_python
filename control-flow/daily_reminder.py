Task=input("Enter your task:")

Priority=input("Priority (high/medium/low):")

Time_Bound=input("Is it time-bound?  (yes/no):")


match priority:
    case "yes":
        print(task, "is a",priority,"priority task that requires your attention today")
    case "no":
         print(task, "is a",priority,"priority task. Consider completing it when you have time")


'''match priority:
    case "high":
          print(task, "is a",priority,"priority task that requires your attention today")'''
