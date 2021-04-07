# -*- coding: utf-8 -*-

# Finger exercises on
# Introduction to Computation and Programming Using Python,
# Third Edition
# John V. Guttag, 2021
# LCCN 2020036760 | ISBN 9780262542364 (paperback)

# chapter 1
'''
import time
import random

dtd, speed, police = 0, 0, 0
prob = -1.0
while dtd < 1 or dtd > 2000:
    dtd = int(input("Enter the distance to your destination (1-2000): "))
while speed < 1 or speed > 300:
    speed = int(input("Enter the average speed (1-300): "))
while police < 1 or police > dtd:
    police = int(input("Enter the number of police officers you would encounter during the trip (1-distance): "))
while prob < 0 or prob > 1:
    prob = float(input("Enter the probability of getting caught in decimal: "))

print("\nThe following is a text representation of your trip.")
print("Each dot represents one mile.")
print("C means you encountered a cop and got caught.")
print("E means you encountered a cop but successfully evaded.")
print("Times run approximately 3,600 times faster in this program.")
print("Hence, one second in this program is about equal to one hour in real time.")
enjoy = input("Press enter to enjoy your ride: ")
while enjoy != '':
    enjoy = input("Press enter to enjoy your ride: ")

cop_location = [0] * dtd
for n in range(police):
    cop_location[random.randrange(dtd)] = 1

start_time = time.time()
seconds = 1 / speed
caught = 0
while dtd:
    dtd -= 1
    time.sleep(seconds)
    if cop_location[1999 - dtd] == 0:
        print('.', end='')
    else:
        if prob <= random.uniform(0, 1):
            print('E', end='')
        else:
            print('C', end='')
            caught += 1
print(f"You've caught by police {caught} times for speeding.")
'''

# chapter 2.3 - print the largest odd among x,y,z
'''
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
'''

# p. 20 (on revised and expanded edition) - print the largest odd among the 10 user input integers
'''
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
'''

# chapter 2.4.1 - ask users to enter their birthday in the form mm/dd/yyyy and then print yyyy
'''
birthday = input("Enter your birthday in the form mm/dd/yyyy: ")
print(f"Your were born in the year {birthday[6:10]}")
'''

# chapter 2.5
'''
num_x = int( input(' How many times should I print the letter X? '))
to_print = 'X'
while num_x:
    print(to_print, end='')
    num_x -= 1
'''