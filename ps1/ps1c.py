# Problem Set 1, ps1c.py
# Version: 0.11.210526 (some touch-ups)
# Name: lcsm29
# Collaborators: None
# Time spent (hh:mm): 00:07 (time spent for previous versions excluded)

def bisection():
    rate_min, rate_max, mid = 0, 10000, 5000
    rate_tolerance, savings_tolerance = 1, 100
    search_counter = 0
    if calculator(rate_max) < required:
        print("It is not possible to pay the down payment in three years.")
        return
    elif calculator(1) >= required:
        mid = 1
    else:
        while abs(calculator(mid) - required) >= savings_tolerance and rate_max - rate_min >= rate_tolerance:
            search_counter += 1
            if calculator(mid) >= required:
                rate_max = mid
            else:
                rate_min = mid
            mid = (rate_min + rate_max) / 2

    print(f"Best savings rate: {0.01*mid:.2f}%")
    print(f"Steps in bisection search:​ {search_counter}")


def calculator(mid):
    local_monthly_salary = monthly_salary
    local_mid = mid * 0.0001
    current_savings, monthly_return, months = (0, )*3

    for months in range(36):
        months += 1
        monthly_return = current_savings * r / 12
        current_savings = current_savings + local_monthly_salary * local_mid + monthly_return
        if months % 6 == 0:
            local_monthly_salary += local_monthly_salary * semi_annual_raise
    return current_savings


def make_float(query):
    while 1:
        tmp = input(f"{query}: ").strip('%')
        try:
            if float(tmp) > 0:
                return float(tmp)
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == '__main__':
    semi_annual_raise = 0.07
    r = 0.04
    home_cost = 1_000_000
    portion_down_payment = 0.25
    required = home_cost * portion_down_payment

    q = 'Enter starting salary'
    monthly_salary = make_float(q) / 12
    bisection()
