

months = 0.0
current_savings​ = 0
portion_down_payment = 0.25
r = 0.04
monthly_return_on_investment = current_savings*r/12

def portion_converter (portion_saved):
    while 1:
        if portion_saved[len(portion_saved)-1] == '%':
            portion_saved = 0.01 * float(portion_saved[0:len(portion_saved)-1])
        else:
            portion_saved = 0.01 * float(portion_saved)

        if portion_saved < 0 or portion_saved > 1:
            portion_saved = input("Let's try this again. Input somewhere between 0% and 100% ")
        else:
            break

def months calculator ():
    months = 0.0
    while current_savings < total_cost * portion_down_payment:
        months += 1
        current_savings = current_savings + monthly_salary*portion_saved + monthly_return_on_investment
    return months

annual_salary​ = float(input("What is your annual salary? "))
monthly_salary = annual_salary/12

portion_saved = input("How much are you going to save? Tell me in percentage. ")


total_cost = float(input("How much your home cost? "))

print("Your down payment would be $", total_cost * portion_down_payment)
print("It'll take", months, " to accumulate $", total_cost * portion_down_payment)