# -*- coding: utf-8 -*-

# Finger exercises on
# Introduction to Computation and Programming Using Python,
# Third Edition
# John V. Guttag, 2021
# LCCN 2020036760 | ISBN 9780262542364 (paperback)

# if you're running it on Windows, install windows-curses with the following command;
# pip install windows-curses


# chapter 1 getting started
def c01():
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
def c023():
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
def c0241():
    birthday = input("Enter your birthday in the form mm/dd/yyyy: ")
    print(f"Your were born in the year {birthday[6:10]}")


# chapter 2.5 while loops - complete the code with a while loop
def c025():
    num_x = int(input(' How many times should I print the letter X? '))
    to_print = 'X'
    while num_x:
        print(to_print, end='')
        num_x -= 1


# chapter 2.5 while loops - print the largest odd among the 10 user input integers
def c025a():
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
def c026():
    total = 2
    for odd in range(3, 1000, 2):
        for n in range(2, odd):
            if odd % n != 0 and n + 1 == odd:
                total += odd
            if odd % (n + 1) == 0:
                break
    print(f"Sum of the prime numbers >2 and <1000 is {total}")


# chapter 3.1 exhaustive enumeration - change the code so that it returns the largest rather than the smallest divisor
def c031():
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
def c031a():
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
def c031b():
    total = 2
    for odd in range(3, 1000, 2):
        for n in range(2, odd):
            if odd % n != 0 and n + 1 == odd:
                total += odd
            if odd % (n + 1) == 0:
                break
    print(f"Sum of the prime numbers >2 and <1000 is {total}")


# chapter 3.2 approximate solutions and bisection search - modify Figure 3-5 to find both negative and positive sqrt
def c032():
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
def c032a():
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
def c033():
    binary = input("Enter binary number: ")
    decimal = 0
    for n in range(len(binary)):
        decimal += int(binary[-n-1]) * 2 ** n
    print(f"binary number {binary} is {decimal} in decimal")


# chapter 3.4 Newton-Raphson - add some code to keep track of # of iterations and compare the efficiency to bisection
def c034():
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
def c0411():
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
def c0411a(str1, str2):
    def as_in():
        if str1 in str2 or str2 in str1:
            return True
        else:
            return False
    return as_in()


# chapter 4.1.1 function definitions - write a function to test is_in
def c0411b():
    def as_in_tester(first_str, second_str):
        result_as_in = c0411a(first_str, second_str)
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


# chapter 4.1.2 keyword arguments and default values - def mult, either accepts 1 int argument and print that argument
#                                                    or accepts 2 int arguments and prints the product of the two args
def c0412():
    def mult(*numbers):
        if len(numbers) == 1:
            print(numbers[0])
        if len(numbers) == 2:
            print(numbers[0] * numbers[1])

    def is_int(number):
        try:
            int(number)
            return int(number)
        except ValueError:
            return

    # this commented line doesn't work, if user gives only one input
    # first, second = input("Enter either one integer, or two integers seperated by space: ").split()
    print("Give me one or two integers.")
    first = input("Enter the first integer: ")
    second = input("Enter the second integer: ")
    first, second = is_int(first), is_int(second)
    if isinstance(first, int) and isinstance(second, int):
        mult(first, second)
    elif isinstance(first, int):
        mult(first)
    elif isinstance(second, int):
        mult(second)


# chapter 4.2 specification - write a function which uses bisection and satisfies the specification below.
# Assumes x and epsilon int or float, base an int,
#         x > 1, epsilon > 0 & power > = 1
# Returns float y such that base**y is within epsilon of x.
def c042():
    def log(x, base, epsilon):
        low = 0
        high = max(1, x)
        ans = (high + low) / 2
        while abs(base ** ans - x) >= epsilon:
            if base ** ans < x:
                low = ans
            else:
                high = ans
            ans = (high + low) / 2
        return ans

    def is_int_or_float(user_input):
        try:
            int(user_input)
            return int(user_input)
        except ValueError:
            try:
                float(user_input)
                return float(user_input)
            except ValueError:
                return

    def type_converter(number):
        if type(number) == int:
            return int(number)
        else:
            return float(number)

    x = input("Enter x: ")
    while is_int_or_float(x) is None or is_int_or_float(x) <= 1:
        if is_int_or_float(x) is None:
            print("x should be either int or float.")
        elif is_int_or_float(x) <= 1:
            print("x should be greater than 1.")
        x = input("Enter x (>1, and either int or float): ")

    epsilon = input("Enter epsilon: ")
    while is_int_or_float(epsilon) is None or is_int_or_float(x) <= 0:
        if is_int_or_float(epsilon) is None:
            print("epsilon should be either int or float.")
        elif is_int_or_float(epsilon) <= 0:
            print("epsilon should be greater than 1.")
        epsilon = input("Enter epsilon (>0, and either int or float): ")

    base = input("Enter base: ")
    while is_int_or_float(base) is None or type(is_int_or_float(base)) == float or is_int_or_float(base) <= 1:
        if is_int_or_float(epsilon) is None or type(is_int_or_float(base)) is float:
            print("base should be an integer.")
        elif is_int_or_float(base) <= 1:
            print("base should be positive integer not equal to 1")
        base = input("Enter base (positive int, not 1): ")

    x, epsilon, base = type_converter(x), type_converter(epsilon), type_converter(base)
    y = log(x, base, epsilon)
    print(f"y within epsilon {epsilon} is {y}.")


# chapter 5.2 ranges and iterables - expression that evaluates to the mean of a tuple of numbers, using function sum
def c052():
    import random
    tuple = ()
    for num in range(10):
        tuple += (random.uniform(0, 1_000_000), )
    expression = sum(list(tuple))/len(tuple)
    print(f"the mean of the following tuple of numbers is {expression}\n{tuple}")


# chapter 5.3 lists and mutability - what does the following code print?
def c053():
    L = [1, 2, 3]
    L.append(L)
    print(L)
    print(L[-1])
    print(L is L[-1])


# chapter 5.3.2 list comprehension - write a list comprehension that generates all non-primes between 2 and 100
def c0532():
    nonprimes = [x for x in range(2, 101) if not all(x % y != 0 for y in range(2, x))]
    print(f"method 1\n"
          f"non-primes {nonprimes}\n")


# chapter 5.4 higher-order operations on lists - implement a function satisfying the specs
def c054():
    def f(L1, L2):
        """
        L1, L2 lists of same length of numbers
        returns the sum of raising each element in L1
        to the power of the element at the same index in L2
        For example, f([1,2], [2,3]) returns 9
        """
        sum = 0
        for num in range(len(L1)):
            sum += L1[num] ** L2[num]
        return sum
    L1 = [1, 2, 3]
    L2 = [9, 8, 2]
    print(f(L1, L2))


# chapter 6 recursion and global variables - write a recursive function that computes the harmonic sum of an integer (n > 0)
def c06():
    integer = 0
    while integer <= 0:
        try:
            temp_input = input(f"\nEnter an integer (n > 0): ")
            integer = int(temp_input)
        except ValueError:
            print("You have to enter an integer. Try again.\n")
            continue
        if integer <= 0:
            print("You have to enter a positive integer. Try Again.\n")
    
    def harmonic_sum(number):
        if number < 2:
            return 1
        else:
            return 1 / number + (harmonic_sum(number - 1))
    print(f"Harmonic sum of {integer} is {harmonic_sum(integer)}")


# chapter 6.1 Fibonacci numbers - when the implementation of fib in Fig. 6-3 is used to compute fib(5),
# how many times does it compute the value of fib(2) on the way to compute fib(5)?
''' Fig6-3
def fib(n):
    """Assumes n int >= 0
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def test_fib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
'''
def c061():
    counter = 0
    def fib(n):
        """Assumes n int >= 0
        Returns Fibonacci of n"""
        nonlocal counter
        if n == 2:
            counter += 1
        if n == 0 or n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    print(f"fib(2) was calculated {counter} times when computing fib(5)")


# Chapter 7.2 using predefined packages - write a function that meets the specification
def c072():
    def shopping_days(year):
        """year a number >= 1941
           returns the number of days between U.S. Thanksgiving and Christmas in year"""
        return 24 + 30 - find_thanksgiving(year)
    def find_thanksgiving(year):
        month = cal.monthcalendar(year, 11)
        if month[0][cal.THURSDAY] != 0:
            thanksgiving = month[3][cal.THURSDAY]
        else:
            thanksgiving = month[4][cal.THURSDAY]
        return thanksgiving
    import calendar as cal
    year = int(input("Enter the year (>= 1941): "))
    print(f"The number of days between Thanksgiving and Christmas in {year} is {shopping_days(year)}")


# Chapter 7.2 using predefined packages - calculate shopping days for Canadian Thanksgiving (second Monday on Oct, since 1958)
def c072a():
    def shopping_days(year):
        return 24 + 30 + 31 - find_thanksgiving(year)
    def find_thanksgiving(year):
        month = cal.monthcalendar(year, 10)
        if month[0][cal.MONDAY] != 0:
            thanksgiving = month[1][cal.MONDAY]
        else:
            thanksgiving = month[2][cal.MONDAY]
        return thanksgiving
    import calendar as cal
    year = int(input("Enter the year (> 1957): "))
    print(f"The number of days between Canadian Thanksgiving and Christmas in {year} is {shopping_days(year)}")


# Chapter 7.3 files - store the first 10 Fibonnaci sequence to a file fib_file (each number on a separate line), and print the content of file
def c073():
    def fib(num, file_name):
        known_fibs = [0, 1]
        for _ in range(num):
            next_fib = known_fibs[0] + known_fibs[1]
            known_fibs[0] = known_fibs[1]
            known_fibs[1] = next_fib
            file_name.write(str(known_fibs[0]) + '\n')
        return known_fibs[0]
    with open('fib_file', 'w') as file_name:
        fib(10, file_name)
    with open('fib_file', 'r') as file_name:
        for line in file_name:
            print(line, end='')

# Chapter 9.1 handling exceptions - implement sum_digits() that meets the specs with try-except
def c091():
    def sum_digits(s):
        """ Assumes s is a string
        Returns the sum of the decimal digits in s
        For example, if s is 'a2b3c' it returns 5"""
        digits = []
        for _, c in enumerate(s):
            try:
                digits.append(int(c))
            except ValueError:
                continue
        return sum(digits)
    print(sum_digits(input("Enter a string: ")))


# Chapter 9.2 exceptions as a control flow mechanism - implement find_an_eval() that satisfies the spec
def c092():
    def find_an_even(L):
        """ Assumes L is a list of integers
        Returns the first even number in L
        Raises ValueError if L does not contain an even number"""
        for elem in L:
            if elem != 0 and elem % 2 == 0:
                return elem
        raise ValueError('L does not contain an even number')
    selector = {'L1': [1, 3, 9, 0, 8, 4, 7], 'L2': [3, 0, 1, 5, 9, 5, 9], 'L3': [-1, 0, 3, -4, 8, 2, 7]}
    while 1:    
        selected = input('L1: [1, 3, 9, 0, 8, 4, 7]\
        \nL2: [3, 0, 1, 5, 9, 5, 9]\
        \nL3: [-1, 0, 3, -4, 8, 2, 7]\
        \nEnter a list you want to test the find_an_even() (enter quit to exit): ').upper()
        if selected in ('L1', 'L2', 'L3'):
            print(f"find_an_even({selected}): {find_an_even(selector[selected])}")
        if selected.lower().startswith('q'):
            break


# Chapter 10.1 abstract data types and classes - add a method union() satisfying the specification
class Int_set(object):
    """ An Int_set is a set of integers """
    #Information about the implementation (not the abstraction):
      #Value of a set is represented by a list of ints, self._vals.
      #Each int in a set occurs in self._vals exactly once.

    def __init__(self):
        """ Create an empty set of integers """
        self._vals = []

    def insert(self, e):
        """ Assumes e is an integer and inserts e into self """
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        """ Assumes e is an integer
            Returns True if e is in self, and False otherwise """
        return e in self._vals

    def remove(self, e):
        """ Assumes e is an integer and removes e from self
            Raises ValueError if e is not in self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def get_members(self):
        """ Returns a list containing the elements of self._
            Nothing can be assumed about the order of the elements """
        return self._vals[:]
    
    def union(self, other):
        """ other is an Int_set
            mutates self so that it contains exactly the elemnts in self
            plus the elements in other. """
        for element in other.get_members():
            self._vals.append(element)

    def __str__(self):
        """ Returns a string representation of self """
        if self._vals == []:
            return '{}'
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'
    
    def __add__(self, other):
        """ other is an Int_set. when operator + is used on two Int_set object,
            it returns new Int_set which contains every element of self and other """
        new_set = Int_set()
        new_set._vals = self._vals + other._vals
        return new_set


def c101():
    def take_input(option):
        while True:
            nums = input(f'Enter a set of integers for {option} Int_set, separated by blank space (e.g. 2 7 4): ')
            try:
                [int(n) for n in nums.split()]
                break
            except:
                print('Invalid input. Only numbers (and space/tab/enter) are allowed. Try again.')
        return nums
    union_original, union_other = Int_set(), Int_set()
    for n in take_input('original').split(): union_original.insert(int(n))
    for n in take_input('other').split(): union_other.insert(int(n))
    print(f'self._vals (original Int_set) before union: {union_original.get_members()}')
    print(f'self._vals (other Int_set): {union_other.get_members()}')
    union_original.union(union_other)
    print(f'self._vals (original Int_set) after union: {union_original.get_members()}')


# Chapter 10.1.1 magic methods and hashable types - replace the union method you added to Int_set 
# by a method that allows clients of Int_set to use the + operator to denote set union.
def c1011():
    ori, oth = Int_set(), Int_set()
    for i in range(10):
        if i % 2 == 0:
            oth.insert(i)
        else:
            ori.insert(i)
    print(f'testing __add__ method of Int_set\n'
          f'ori: {ori.get_members()}\n'
          f'oth: {oth.get_members()}\n'
          f'ori + oth: {(ori + oth).get_members()}')


# 10.2 inheritance - implement a subclass of Person as per specs
class Person(object):
    def __init__(self, name):
        """ Assumes name a string. Create a person """
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except:
            self._last_name = name
        self.birthday = None
        
    def get_name(self):
        """Returns self's full name"""
        return self._name
    
    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name
    
    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate"""
        self._birthday = birthdate
        
    def get_age(self):
        """Returns self's current age in days"""
        import datetime
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days
    
    def __lt__(self, other):
        """Assume other a Person
           Returns True if self precedes other in alphabetical
           order, and False otherwise. Comparison is based on last
           names, but if these are the same full names are
           compared."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name
    
    def __str__(self):
        """Returns self's name"""
        return self._name

class Politician(Person):
    """ A politician is a person that can belong to a political party """
    
    def __init__(self, name, party = None):
        """ name and party are strings """
        Person.__init__(self, name)
        self._party = party
    
    def get_party(self):
        """ returns the party to which self belongs """
        return self._party
    
    def might_agree(self, other):
        """ returns True if self and other belong to the same party
            or at least one of then does not belong to a party """
        return self._party == other.get_party()

def c102():
    def take_input(option):
        name, party = input(
            f'Enter a name and party ({option}), '
            f'separated by comma (e.g. Person, Party): ').split(',')
        return name, party
    original, other = take_input('original'), take_input('other')
    ori = Politician(original[0], original[1].replace(' ', ''))
    oth = Politician(other[0], other[1].replace(' ', ''))
    print(f'Original Name: {ori.get_name()}, Original Party: {ori.get_party()}\n'
          f'Other Name: {oth.get_name()}, Other Party: {oth.get_party()}\n'
          f'might_agree(): {ori.might_agree(oth)}')


# Chapter 10.2.1 multiple levels of inheritance - what is the value of the following expression?
# isinstance('ab', str) == isinstance(str, str)
def c1021():
    print(isinstance('ab', str) == isinstance(str, str))


# Chapter 10.3.1 generators - add to grades a generator that meets the specification
class MIT_person(Person):
    
    _next_id_num = 0 #identification number
    
    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1
        
    def get_id_num(self):
        return self._id_num
    
    def __lt__(self, other):
        return self._id_num < other._id_num

class Student(MIT_person):
    pass

class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year

    def get_class(self):
        return self._year
    
class Grad(Student):
    pass

class Transfer_student(Student):

    def __init__(self, name, from_school):
        MIT_person.__init__(self, name)
        self._from_school = from_school

    def get_old_school(self):
        return self._from_school

class Grades(object):

    def __init__(self):
        """Create empty grade book"""
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self._students:
            raise ValueError('Duplicate student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False

    def add_grade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def get_grades(self, student):
        """Return a list of grades for student"""
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')
    ''' older version (non-generator) 
    def get_students(self):
        """Return a sorted list of the students in the grade book"""
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        return self._students[:]
    '''
    def get_students(self): #new version from later in chapter
        """ Return the students in the grade book one at a time
            in alphabetical order """
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for s in self._students:
            yield s
    
    def get_students_above(self, grade):
        """ Return the students a mean grade > g one at a time """
        for s in self._students:
            if sum(self.get_grades(s)) / len(self.get_grades(s)) > grade:
                yield s

def grade_report(course):
    """Assumes course is of type Grades"""
    report = ''
    for s in course.get_students():
        tot = 0.0
        num_grades = 0
        for g in course.get_grades(s):
            tot += g
            num_grades += 1
        try:
            average = tot/num_grades
            report = f"{report}\n{s}'s mean grade is {average}"
        except ZeroDivisionError:
            report = f"{report}\n{s} has no grades"
    return report

def c1031():
    import random
    students = [
        Grad('Al'), Grad('Aram'), Grad('Bernie'), Grad('Dembe'), 
        Grad('Harold'), Grad('Liz'), Grad('Meera'), Grad('Ray'), Grad('Tom')]
    gr = Grades()
    for s in students:
        gr.add_student(s)
        for _ in range(20):
            gr.add_grade(s, random.random() * 5)
        print(f'{s} (Grade {sum(gr.get_grades(s)) / len(gr.get_grades(s)):.02f}), ', end='')
    print()
    for g in range(1, 10):
        print(f'Grade above {g/2}: ', end='')
        for s in gr.get_students_above(g/2):
            print(f'{s} ', end='')
        print()



# old chapter caller
def old_chapter_selector():
    chapter_list = [chapter for chapter in globals().keys() if chapter.startswith('c') and len(chapter) < 7]
    chapter_call = ''
    while chapter_call not in chapter_list and chapter_call != 'l':
        chapter_call = input("Chapter Selector\n-------------------------------------------\n"
                            "First exercise on Chapter 10.2: c102\n"
                            "Third exercise on Chapter 4.1.1: c0411b\n"
                            "type 'l' to see the chapter list\n-------------------------------------------\n"
                            "Enter the chapter name: ")
        if chapter_call == 'l':
            chapter_call = ''
            print('\nA list of finger exercises: ', end='')
            for i, chapter in enumerate(chapter_list):
                if not i == len(chapter_list) - 2:
                    print(f'{chapter}, ' if not chapter[1].isalpha() else '', end='')
                else:
                    print(f'{chapter}' if not chapter[1].isalpha() else '')
    if chapter_call in globals() and callable(globals()[chapter_call]):
        globals()[chapter_call]()
    else:
        print("No such function exists")


def get_menu():
    menu = ['Home', 
        'Chapter 1', 
        'Chapter 2', 
        'Chapter 3', 
        'Chapter 4', 
        'Chapter 5', 
        'Chapter 6',
        'Chapter 7',
        'Chapter 9',
        'Chapter 10',
        'Old Selector',
        'Exit'
    ]
    return menu


def get_chapters():
    chapters = [['Chapter 1'],
        ['Chapter 2.3', 'Chapter 2.4.1', 'Chapter 2.5 - First', 'Chapter 2.5 - Second', 'Chapter 2.6'],
        ['Chapter 3.1 - First', 'Chapter 3.1 - Second', 'Chapter 3.1 - Third', 'Chapter 3.2 - First', 'Chapter 3.2 - Second', 'Chapter 3.3', 'Chapter 3.4'],
        ['Chapter 4.1.1 - First', 'Chapter 4.1.1 - Second', 'Chapter 4.1.1 - Third', 'Chapter 4.1.2', 'Chapter 4.2'],
        ['Chapter 5.2', 'Chapter 5.3', 'Chapter 5.3.2', 'Chapter 5.4'],
        ['Chapter 6', 'Chapter 6.1'],
        ['Chapter 7.2 - First', 'Chapter 7.2 - Second', 'Chapter 7.3'],
        ['Chapter 9.1', 'Chapter 9.2'],
        ['Chapter 10.1', 'Chapter 10.1.1','Chapter 10.2', 'Chapter 10.2.1', 'Chapter 10.3.1'],
    ]
    return chapters


def chapter_selector():  # from nikhilkumarsingh/python-curses-tut
    def print_menu(stdscr, selected_row_idx, content):
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        for idx, row in enumerate(content):
            x = width // 2 - len(row) // 2
            y = height // 2 - len(content) // 2 + idx
            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

    def print_center(stdscr, text):
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        x = width // 2 - len(text) // 2
        y = height // 2
        stdscr.addstr(y, x, text)
        stdscr.refresh()

    def selector(stdscr):
        curses.curs_set(0)  # turn off cursor blinking
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # color scheme for selected row
        current_row = 0  # specify the current selected row

        print_menu(stdscr, current_row, get_menu())  # print the menu

        while True:
            key = stdscr.getch()
            stdscr.keypad(True)  # KEY_UP/LEFT/DOWN/RIGHT not working for unknown reason
            if key in [curses.KEY_UP, 450, curses.KEY_LEFT, 452] and current_row > 0:
                current_row -= 1
            elif key in [curses.KEY_DOWN, 456, curses.KEY_RIGHT, 454] and current_row < len(get_menu())-1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                print_center(stdscr, "You selected '{}'".format(get_menu()[current_row]))
                if current_row == 1:
                    stdscr.getch()
                    curses.endwin()
                    return [['Chapter 1'], 0]
                elif 1 < current_row < len(get_menu()) - 2:
                    submenu = get_chapters()[current_row - 1]
                    current_row = 0
                    print_menu(stdscr, current_row, submenu)
                    while True:
                        key = stdscr.getch()
                        stdscr.keypad(True)  # KEY_UP/LEFT/DOWN/RIGHT not working for unknown reason
                        if key in [curses.KEY_UP, 450, curses.KEY_LEFT, 452] and current_row > 0:
                            current_row -= 1
                        elif key in [curses.KEY_DOWN, 456, curses.KEY_RIGHT, 454] and current_row < len(submenu)-1:
                            current_row += 1
                        elif key == curses.KEY_ENTER or key in [10, 13]:
                            print_center(stdscr, "You selected '{}'".format(submenu[current_row]))
                            stdscr.getch()
                            curses.endwin()
                            return submenu, current_row
                        print_menu(stdscr, current_row, submenu)
                else:
                    return [['Old Selector', 0]]
            print_menu(stdscr, current_row, get_menu())
    selected_chapter = curses.wrapper(selector)
    return selected_chapter


if __name__ == '__main__':
    def flatten(lst):
        flat = []
        for e in lst:
            if type(e) == list:
                flat += flatten(e)
            else:
                flat.append(e)
        return flat
    
    try:
        import curses
        funcs = [fname for fname in dir() if fname.startswith('c')]
        selected_chapter = chapter_selector()
        if selected_chapter == [['Old Selector', 0]]:
            old_chapter_selector()
        else:
            selected = selected_chapter[0][selected_chapter[1]]
            print(selected)
            locals()[funcs[flatten(get_chapters()).index(selected)]]()
    except ModuleNotFoundError:
        # if you're running this on Windows,
        # and seeing either ModuleNotFoundError or old chapter selector,
        # install windows-curses with the following command;
        # pip install windows-curses
        old_chapter_selector()
