# -*- coding: utf-8 -*-

# Finger exercises on
# Introduction to Computation and Programming Using Python,
# Third Edition
# John V. Guttag, 2021
# LCCN 2020036760 | ISBN 9780262542364 (paperback)

# chapter 1 getting started
def c1():
    import time
    import random

    dtd, speed, police = 0, 0, 0
    prob = -1.0
    while dtd < 1 or dtd > 2000:
        dtd = int(input("Enter the distance to your destination (1-2000): "))
    while speed < 1 or speed > 300:
        speed = int(input("Enter the average speed (1-300): "))
    while police < 1 or police > dtd:
        police = int(input("Enter the total number of cops on the route (1-distance): "))
    while prob < 0 or prob > 1:
        prob = float(input("Enter the probability of getting caught in decimal: "))

    print("\nThe following is a text representation of your trip.")
    print("Each dot represents one mile.")
    print("C means you encountered a cop and got caught.")
    print("E means you encountered a cop but successfully evaded.")
    enjoy = input("Press enter to enjoy your ride: ")
    while enjoy != '':
        enjoy = input("Press enter to enjoy your ride: ")

    cop_location = [0] * dtd
    for n in range(police):
        cop_location[random.randrange(dtd)] = 1

    seconds = 1 / speed
    caught = 0
    while dtd:
        dtd -= 1
        time.sleep(seconds)
        if cop_location[dtd] == 0:
            print('.', end='')
        else:
            if prob <= random.uniform(0, 1):
                print('E', end='')
            else:
                print('C', end='')
                caught += 1
    print(f"\nYou've caught by police {caught} times for speeding.")


# chapter 2.3 branching problems - print the largest odd among x,y,z
def c23():
    largest_odd, x, y, z = 0, 1, 2, 3

    if x % 2 and y % 2 and z % 2 == 0:
        print("There is no odd number.")
    else:
        if x % 2 == 1:
            largest_odd = x
        if y % 2 == 1 and y > largest_odd:
            largest_odd = y
        if z % 2 == 1 and z > largest_odd:
            largest_odd = z
    print(f"The largest odd number is {largest_odd}")


# chapter 2.4.1 input - ask users to enter their birthday in the form mm/dd/yyyy and then print yyyy
def c241():
    birthday = input("Enter your birthday in the form mm/dd/yyyy: ")
    print(f"Your were born in the year {birthday[6:10]}")


# chapter 2.5 while loops - complete the code with a while loop
def c25():
    num_x = int(input(' How many times should I print the letter X? '))
    to_print = 'X'
    while num_x:
        print(to_print, end='')
        num_x -= 1


# chapter 2.5 while loops - print the largest odd among the 10 user input integers
def c25a():
    def ordinal_num(n):
        n = int(n) + 1
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        return str(n) + suffix

    if __name__ == "__main__":
        user_input = [0] * 10
        largest_odd = 0
        for n in range(len(user_input)):  # for n in user_input: also iterates 9 times, but n is stuck at 0
            user_input[n] = int(input(f"Enter your {ordinal_num(n)} number: "))
            if user_input[n] > largest_odd and user_input[n] % 2 == 1:
                largest_odd = user_input[n]
        if largest_odd == 0:
            print("There is no odd number.")
        else:
            print(f"The largest odd number is {largest_odd}")


# chapter 2.6 for loops and range - sum of prime numbers >2 and <1000
def c26():
    total = 2
    for odd in range(3, 1000, 2):
        for n in range(2, odd):
            if odd % n != 0 and n + 1 == odd:
                total += odd
            if odd % (n + 1) == 0:
                break
    print(f"Sum of the prime numbers >2 and <1000 is {total}")


# chapter 3.1 exhaustive enumeration - change the code so that it returns the largest rather than the smallest divisor
def c31():
    x = int(input('Enter an integer greater than 2: '))
    smallest_divisor = None
    for guess in range(2, x):
        if x % guess == 0:
            smallest_divisor = guess
            break
    if smallest_divisor is not None:
        print(f"Smallest divisor of {x} is {smallest_divisor}")
        print(f"Largest divisor of {x} is {int(x / smallest_divisor)}")
    else:
        print(f"{x} is a prime number")


# chapter 3.1 exhaustive enumeration - take an integer input and print root and pwr(1<pwr<6) (root**pwr == user_input)
def c31a():
    import math
    user_input = int(input("Enter an integer: "))
    found = None
    for root in range(int(math.sqrt(user_input)) + 1):
        for pwr in range(2, 6):
            if root ** pwr == user_input:
                found = 1
                print(f"{root} to the power {pwr} = {user_input}")
                if pwr % 2 == 0 and not user_input == 0:
                    print(f"{-root} to the power {pwr} = {user_input}")
    if found is None:
        print("No such pair of integers exists (1<pwr<6)")


# chapter 3.1 exhaustive enumeration - print the sum of the prime numbers >2 and <1000.
# the following is okay for 1,000 or 10,000 but getting slow for 100,000
def c31b():
    total = 2
    for odd in range(3, 1000, 2):
        for n in range(2, odd):
            if odd % n != 0 and n + 1 == odd:
                total += odd
            if odd % (n + 1) == 0:
                break
    print(f"Sum of the prime numbers >2 and <1000 is {total}")


# chapter 3.2 approximate solutions and bisection search - modify Figure 3-5 to find both negative and positive sqrt
def c32():
    x = int(input("Enter an integer greater than 2: "))
    neg = False
    if x < 0:
        neg, x = True, -x
    epsilon = 0.01
    num_guesses, low = 0, 0
    high = max(1, x)
    ans = (high + low) / 2
    while abs(ans ** 2 - x) >= epsilon:
        print(f"low = {low}, high = {high}, ans = {ans}")
        num_guesses += 1
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    print(f"number of guesses = {num_guesses}")
    if not neg:
        print(f"{ans} is close to square root of {x}")
    else:
        print(f"{ans} and {-ans} are close to square root of {x}")


# chapter 3.2 approximate solutions and bisection search - egg drop, 102 stories, under 7 searches
def c32a():
    max_safe_floor = int(input("Egg would survive the drop, up to floor # (1-102): "))
    epsilon = 0.5
    num_guesses, low, high = 0, 1, 102
    mid = (high + low) / 2
    while abs(mid - max_safe_floor) >= epsilon:
        print(f"low = {low}, high = {high}, mid = {mid}")
        num_guesses += 1
        if mid < max_safe_floor:
            low = mid
        else:
            high = mid
        mid = (high + low) / 2
    print(f"number of guesses = {num_guesses}\n"
          f"maximum survivable floor = {round(mid)} ")


# chapter 3.3 a few words about using floats - decimal equivalent of the binary number 10011
def c33():
    binary = input("Enter binary number: ")
    decimal = 0
    for n in range(len(binary)):
        decimal += int(binary[-n-1]) * 2 ** n
    print(f"binary number {binary} is {decimal} in decimal")


# chapter 3.4 Newton-Raphson - add some code to keep track of # of iterations and compare the efficiency to bisection
def c34():
    from time import perf_counter_ns
    # Newton-Raphson
    k = 123456789
    epsilon = 0.01
    guess = k / 2
    newton_raphson_counter = 0
    newton_start = perf_counter_ns()
    while abs(guess ** 2 - k) >= epsilon:
        guess = guess - (((guess ** 2) - k) / (2 * guess))
        newton_raphson_counter += 1
    newton_elapsed = perf_counter_ns() - newton_start

    # Bisection
    num_guesses, low = 0, 0
    high = max(1, k)
    ans = (high + low) / 2
    bisection_start = perf_counter_ns()
    while abs(ans ** 2 - k) >= epsilon:
        num_guesses += 1
        if ans ** 2 < k:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    bisection_elapsed = perf_counter_ns() - bisection_start

    # Results
    print(f"\nSquare root of {k} is about;\n"
          f"Newton-Raphson: {guess}.\n"
          f"bisection search: {ans}.\n")
    print(f"Number of iterations;\n"
          f"Newton-Raphson: {newton_raphson_counter}\n"
          f"bisection search: {num_guesses}\n")
    print(f"Time elapsed in nanoseconds;\n"
          f"Newton-Raphson: {newton_elapsed}\n"
          f"bisection search: {bisection_elapsed}")


# chapter 4.1.1 function definitions - modify the Fig. 4-3 to print sum of sqrt(25), 3sqrt(-8), 4sqrt(16). 0.001 epsilon
def c411():
    def find_root(x, power, epsilon):
        # Find interval containing answer
        if x < 0 and power % 2 == 0:
            return None  # Negative number has no even-powered roots
        low = min(-1, x)
        high = max(1, x)
        # Use bisection search
        ans = (high + low) / 2
        while abs(ans**power - x) >= epsilon:
            if ans**power < x:
                low = ans
            else:
                high = ans
            ans = (high + low) / 2
        return ans
    print(f"{find_root(25, 2, 0.001) + find_root(-8, 3, 0.001) + find_root(16, 4, 0.001)}")


# chapter 4.1.1 function definitions - write a function as_in.
# take two string args and return True if either string occurs anywhere in the other.
def c411a(str1, str2):
    def as_in():
        if str1 in str2 or str2 in str1:
            return True
        else:
            return False
    return as_in()


# chapter 4.1.1 function definitions - write a function to test is_in
def c411b():
    def as_in_tester(first_str, second_str):
        result_as_in = c411a(first_str, second_str)
        matched = False
        longer_str, shorter_str = '', ''
        if len(first_str) == len(second_str):
            # if both string have same length, compare two strings right up
            for n in range(len(first_str)):
                print('head on comparo')
                if first_str[n] is not second_str[n]:
                    break
                elif first_str[n] == second_str[n] and n + 1 == len(first_str):
                    matched = True
        else:
            # if not, determine the longer one
            if len(first_str) > len(second_str):
                longer_str = first_str
                shorter_str = second_str
            else:
                longer_str = second_str
                shorter_str = first_str
            # and mark the entry_point
            entry_point = []
            for n in range(len(longer_str)):
                if shorter_str[0] == longer_str[n] and len(shorter_str) + n <= len(longer_str):
                    entry_point.append(1)
                else:
                    entry_point.append(0)
            # and compare shorter string to longer string, starting from each entry points
            for n in range(len(longer_str)):
                if entry_point[n] == 0:
                    continue
                else:
                    for x in range(len(shorter_str)):
                        if shorter_str[x] is not longer_str[n + x]:
                            break
                        elif shorter_str[x] == longer_str[n + x] and x + 1 == len(shorter_str):
                            matched = True
        # result printer
        if matched == result_as_in:
            print(f"The result of as_in function is {result_as_in}. It is correct.")
        else:
            print(f"The result of as_in function is {result_as_in}. It is incorrect.")
    first_str = input("Enter the first string you want to test: ")
    second_str = input("Enter the second string you want to test: ")
    as_in_tester(first_str, second_str)


# chapter caller
chapter_call = input("Chapter Selector\n-------------------------------------------\n"
                     "Command Examples"
                     "First exercise on Chapter 2.3 = c23\n"
                     "Third exercise on Chapter 4.1.1 = c411b\n"
                     "The last chapter on this code = <enter>\n-------------------------------------------\n"
                     "Enter the chapter name [default: the last chapter]: ")
if chapter_call in locals().keys() and callable(locals()[chapter_call]):
    locals()[chapter_call]()
elif chapter_call == '':
    last_chapter = dir()[-2]
    locals()[last_chapter]()
else:
    print("No such function exists")
