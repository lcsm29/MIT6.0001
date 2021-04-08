def portion_converter (before_conversion): #changed the names of variables to reuse this functions twice
    while 1:
        if before_conversion[len(before_conversion)-1] == '%':
            percent_removed = float(before_conversion[0:len(before_conversion)-1])
        else:                                           
            percent_removed = float(before_conversion)

        if percent_removed <= 100 and percent_removed > 1:
            return percent_removed * 0.01
            break
        elif percent_removed <= 1 and percent_removed >= 0:
            return percent_removed
            break
        elif percent_removed < 0 or percent_removed > 1:
            before_conversion = input("Let's try this again. Input should be somewhere between 0 and 100%: ")

def calculator ():
    global current_savings
    global months
    global monthly_salary
    global semi_annual_raise
    monthly_return_on_investment = current_savings * r / 12

    while current_savings < total_cost * portion_down_payment:
        months += 1
#        if (months%6 == 0):  #this location gives me one less month on test case 2 and 3 (but not on 1)
#            monthly_salary += monthly_salary * semi_annual_raise
        monthly_return_on_investment = current_savings * r / 12
        current_savings = current_savings + monthly_salary * portion_saved + monthly_return_on_investment        
        if (months%6 == 0):  #while this location doesn't. this location assumes raise happens at month #7, #13, ... while the above location assumes month #6, #12.
            monthly_salary += monthly_salary * semi_annual_raise

def day_calculator (): #it starts off from the previous calculation to reduce the total number of loop executions. it's not working very well, but i'll leave it for now
    global current_savings
    global months
    global days
    days = months * 30.436875
    daily_contribution_equivalent = monthly_salary * portion_saved / 30.436875

    while current_savings > total_cost * portion_down_payment:
        days -= 1
        daily_return_on_investment = current_savings * r / 365.2425
        current_savings = current_savings - daily_contribution_equivalent - daily_return_on_investment

months = 0.0
days = 0.0
portion_down_payment = 0.25
current_savings = 0
r = 0.04

annual_salary = float(input("What is your annual salary? "))
monthly_salary = annual_salary/12

before_conversion = input("How much are you going to save? Tell me either in a percentage or a decimal: ")
portion_saved = portion_converter (before_conversion)

total_cost = float(input("How much your home cost? "))

before_conversion = input("How much raise are you expecting per every half year? Tell me either in a percentage or a decimal: ")
semi_annual_raise = portion_converter (before_conversion)

calculator()

print("It is wise to put a down payment of $", int(total_cost * portion_down_payment), "or more")
print("It'll take", int(months), "months to accumulate $", int(total_cost * portion_down_payment))
if input("Do you want somewhat more detailed calculation? Type 'yes' if you wish to: ")=="yes":
    day_calculator()
    accurate_months = days / 30.436875
    print("It'll take", accurate_months, "months or", days, "days to accumulate $", int(total_cost * portion_down_payment))
else:
    print("Bye")