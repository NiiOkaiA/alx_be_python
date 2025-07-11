monthly_income= int(input("enter your monthly income: "))
monthly_expenses= int (input("enter total monthly expenses: "))
monthly_savings= monthly_income-monthly_expenses

projected_savings= monthly_savings * 12 + (monthly_savings*12*0.05)

print("monthly savings", monthly_savings)
print("projected annual savings",projected_savings)
