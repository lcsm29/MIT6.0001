# version 0.11.210525 - cleaned it up a bit

def portion_converter(portion_saved):
    while 1:
        if '%' in portion_saved:
            portion_saved = portion_saved.strip('%')
        portion_saved = float(portion_saved)
        if 1 < portion_saved <= 100:
             portion_saved *= 0.01
        if portion_saved < 0 or portion_saved > 1:
            portion_saved = input("Let's try this again. It should be somewhere between 0 and 100%: ")
            continue
        else:
            return portion_saved

def calculator():
    global current_savings
    global months
    monthly_return_on_investment = current_savings * r / 12
    while current_savings < total_cost * portion_down_payment:
        months += 1
        monthly_return_on_investment = current_savings * r / 12
        current_savings = current_savings + monthly_salary * portion_saved + monthly_return_on_investment

def day_calculator():
    global current_savings
    global months
    global days
    days = months * 30.436875
    daily_contribution_equivalent = monthly_salary * portion_saved / 30.436875
    while current_savings > total_cost * portion_down_payment:
        days -= 1
        daily_return_on_investment = current_savings * r / 365.2425
        current_savings = current_savings - daily_contribution_equivalent - daily_return_on_investment

months, days = 0.0, 0.0
current_savings = 0
portion_down_payment = 0.25
r = 0.04

monthly_salary = float(input("What is your annual salary? ")) / 12
portion_saved = portion_converter(input("How much are you going to save? Tell me either in a percentage or a decimal: "))
total_cost = float(input("How much your home cost? "))

calculator()

print(f"It is wise to put a down payment of ${int(total_cost * portion_down_payment)} or more for ${int(total_cost)} home")
print(f"It'll take approx. {int(months)} months to accumulate ${int(total_cost * portion_down_payment)}")
if input("Do you want somewhat more detailed calculation [y/N]? ").lower().startswith('y'):
    day_calculator()
    accurate_months = days / 30.436875
    print(f"It'll take {accurate_months} months or {days} days to accumulate ${int(total_cost * portion_down_payment)}")
else:
    print("Bye")