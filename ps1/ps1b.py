# Problem Set 1, ps1b.py
# Version: 0.12.210526 (rewritten)
# Name: lcsm29
# Collaborators: None
# Time spent (hh:mm): 00:23 (time spent for previous versions excluded)
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


def make_decimal(num, query):
    if 1 < num <= 100:
        return num * 0.01
    elif 0 <= num <= 1:
        return num
    else:
        print("Invalid input. Please try again.")
        n = num
        while n < 0 or n > 100:
            n = make_float(query)
        return make_decimal(n, query)


def calculator(ms, ps, hc, sar, pdp, r):
    months, accumulated = 0, 0
    while accumulated < hc * pdp:
        months += 1
        accumulated += ms * ps + accumulated * r / 12
        if months % 6 == 0:
            ms += ms * sar
    return months, accumulated


if __name__ == '__main__':
    portion_down_payment = 0.25
    r = 0.04

    q = 'Enter your annual salary'
    mo_salary = make_float(q) / 12
    q = 'Enter the percent of your salary to save'
    portion_saved = make_decimal(make_float(q), q)
    q = 'Enter the cost of your dream home'
    home_cost = make_float(q)
    q = 'Enter the expected semi annual raise'
    semi_annual_raise = make_decimal(make_float(q), q)
    result = calculator(mo_salary, portion_saved, home_cost, semi_annual_raise, portion_down_payment, r)
    print(f"Number of months: {result[0]} (months to accumulate ${result[1]:,.2f})")
