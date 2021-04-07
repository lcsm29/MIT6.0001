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
        for n in range(len(user_input)):  # for n in user_input: also iterates from 0 to 9, but n is stuck at 0
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
                print(odd)
                total += odd
            if odd % (n + 1) == 0:
                break
    print(total)


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
def c31b():
    total = 2
    for odd in range(3, 1000, 2):
        for n in range(2, odd):
            if odd % n != 0 and n + 1 == odd:
                print(odd)
                total += odd
            if odd % (n + 1) == 0:
                break
    print(total)


chapter_call = input("Enter the chapter name (e.g. c23 means chapter 2.3, c31a means second exercise on chapter 3.1): ")
if chapter_call in locals().keys() and callable(locals()[chapter_call]):
    locals()[chapter_call]()
else:
    print("No such function exists")
