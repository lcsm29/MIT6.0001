# Finger exercises on
# Introduction to Computation and Programming Using Python,
# Revised and Expanded Edition
# John V. Guttag, 2013
# ISBN 978-0-262-52500-8 (pbk. : alk. paper)

# p. 6
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

# p. 16
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


# p. 20
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