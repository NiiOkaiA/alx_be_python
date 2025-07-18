task=input("Enter your task:")

priority=input("Priority (high/medium/low):")

time=input("Is it time-bound?  (yes/no:)")


match time:
    case "yes":
        print(task, "is a",priority,"priority task that requires your attention today")
    case "no":
         print(task, "is a",priority,"priority task. Consider completing it when you have time")
