'''Part A: House Hunting
You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and
decide that you want to start saving to buy a house. As housing prices are very high in the Bay Area,
you realize you are going to have to save for several years before you can afford to make the down
payment on a house. In Part A, we are going to determine how long it will take you to save enough
money to make the down payment given the following assumptions:
1. Call the cost of your dream home ​ total_cost​ .
2. Call the portion of the cost needed for a down payment ​ portion_down_payment​ . For
simplicity, assume that portion_down_payment = 0.25 (25%).
3. Call the amount that you have saved thus far ​ current_savings​ . You start with a current
savings of $0.
4. Assume that you invest your current savings wisely, with an annual return of ​ r ​ (in other words,
at the end of each month, you receive an additional ​ current_savings*r/12​ funds to put into
your savings – the 12 is because ​ r ​ is an annual rate). Assume that your investments earn a
return of r = 0.04 (4%).
5. Assume your annual salary is ​ annual_salary​ .
6. Assume you are going to dedicate a certain amount of your salary each month to saving for
the down payment. Call that ​ portion_saved​ . This variable should be in decimal form (i.e. 0.1
for 10%).
7. At the end of each month, your savings will be increased by the return on your investment,
plus a percentage of your ​ monthly salary ​ (annual salary / 12).
Write a program to calculate how many months it will take you to save up enough money for a down
payment. You will want your main variables to be floats, so you should cast user inputs to floats.
1Your program should ask the user to enter the following variables:
1. The starting annual salary (annual_salary)
2. The portion of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
Hints
To help you get started, here is a rough outline of the stages you should probably follow in writing your
code:
● Retrieve user input. Look at input() if you need help with getting user input. For this problem set,
you can assume that users will enter valid input (e.g. they won’t enter a string when you expect
an int)
● Initialize some state variables. You should decide what information you need. Be careful about
values that represent annual amounts and those that represent monthly amounts.
Try different inputs and see how long it takes to save for a down payment. ​ Please make your
program print results in the format shown in the test cases below.
Test Case 1
>>>
Enter your annual salary:​ 120000
Enter the percent of your salary to save, as a decimal: ​ . 10
Enter the cost of your dream home:​ 1000000
Number of months:​ 183
>>>
Test Case 2
>>>
Enter your annual salary:​ 80000
Enter the percent of your salary to save, as a decimal: ​ . 15
Enter the cost of your dream home:​ 500000
Number of months:​ 105
>>>'''
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
            portion_saved = input("Let's try this again. Input somewhere between 0% and 100% ")

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