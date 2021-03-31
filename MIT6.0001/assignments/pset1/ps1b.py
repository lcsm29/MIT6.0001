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

'''Part B: Saving, with a raise
Background
In Part A, we unrealistically assumed that your salary didn’t change. But you are an MIT graduate, and
clearly you are going to be worth more to your company over time! So we are going to build on your
solution to Part A by factoring in a raise every six months.

In ​ ps1b.py​ , copy your solution to Part A (as we are going to reuse much of that machinery). Modify
your program to include the following

1. Have the user input a semi-annual salary raise ​ semi_annual_raise​ (as a decimal percentage)
2. After the 6​ th​ month, increase your salary by that percentage. Do the same after the 12 th
month, the 18​ th ​ month, and so on.

Write a program to calculate how many months it will take you save up enough money for a down
payment. LIke before, assume that your investments earn a return of ​ r ​ = 0.04 (or 4%) and the
required down payment percentage is 0.25 (or 25%). Have the user enter the following variables:

1. The starting annual salary (annual_salary)
2. The percentage of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
4. The semi­annual salary raise (semi_annual_raise)

Hints
To help you get started, here is a rough outline of the stages you should probably follow in writing your 
code:
● Retrieve user input.
● Initialize some state variables. You should decide what information you need. Be sure to be
careful about values that represent annual amounts and those that represent monthly amounts.
● Be careful about when you increase your salary – this should only happen ​ after​ the 6​ th​ , 12 th
​ , 18 th month, and so on.
Try different inputs and see how quickly or slowly you can save enough for a down payment. Please
make your program print results in the format shown in the test cases below.

Test Case 1
>>>
Enter your starting annual salary:​ 120000
Enter the percent of your salary to save, as a decimal: ​ . 05
Enter the cost of your dream home: ​ 500000
Enter the semi­annual raise, as a decimal:​ .03
Number of months:​ 142
>>>

Test Case 2
>>>
Enter your starting annual salary:​ 80000
Enter the percent of your salary to save, as a decimal: ​ . 1
Enter the cost of your dream home: ​ 800000
Enter the semi­annual raise, as a decimal:​ .03
Number of months:​ 159
>>>

Test Case 3
>>>
Enter your starting annual salary:​ 75000
Enter the percent of your salary to save, as a decimal: ​ . 05
Enter the cost of your dream home:​ 1500000
Enter the semi­annual raise, as a decimal:​ .05
Number of months:​ 261
>>>'''