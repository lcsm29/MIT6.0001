def portion_converter (portion_saved):
    while 1:
        if portion_saved[len(portion_saved)-1] == '%':    #if user actually input '%' character, this will remove the character.
            portion_saved = float(portion_saved[0:len(portion_saved)-1])
        else:                                             #if not, proceed
            portion_saved = float(portion_saved)

        if portion_saved <= 100 and portion_saved > 1:    #if 1<portion_saved<=100, it'll assume that user entered as a percentage, and convert/return a decimal.
            portion_saved = portion_saved * 0.01
            return portion_saved
            break
        elif portion_saved <= 1 and portion_saved >= 0:   #if 0<=portion_saved<=1, it'll assume that user entered as a decimal, and return it as-is.
            return portion_saved
            break
        elif portion_saved < 0 or portion_saved > 1:      #if portion_saved is out of range, user input loop will continue.
            portion_saved = input("Let's try this again. Input should be somewhere between 0 and 100%: ")

def calculator ():
    global current_savings
    global months
    monthly_return_on_investment = current_savings * r / 12

    while current_savings < total_cost * portion_down_payment:
        months += 1
        monthly_return_on_investment = current_savings * r / 12
        current_savings = current_savings + monthly_salary * portion_saved + monthly_return_on_investment

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

portion_saved = input("How much are you going to save? Tell me either in a percentage or a decimal: ")
portion_saved = portion_converter (portion_saved)

total_cost = float(input("How much your home cost? "))

calculator()

print("It is wise to put a down payment of $", int(total_cost * portion_down_payment), "or more")
print("It'll take", int(months), "months to accumulate $", int(total_cost * portion_down_payment))
if input("Do you want somewhat more detailed calculation? Type 'yes' if you wish to: ")=="yes":
    day_calculator()
    accurate_months = days / 30.436875
    print("It'll take", accurate_months, "months or", days, "days to accumulate $", int(total_cost * portion_down_payment))
else:
    print("Bye")