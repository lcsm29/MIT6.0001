###################
## EXAMPLE: strings 
###################
hi = "hello there"
name = "ana"
greet = hi + name  
print(greet)
greeting = hi + " " + name
print(greeting)
silly = hi + (" " + name)*3
print(silly)
print("\n")

####################
## EXAMPLE: output 
####################
x = 1
print(x)
x_str = str(x)
print("my fav number is", x, ".", "x=", x)             #is 1 . x= 1
print("my fav number is", x_str + "." + "x=" + x_str)  #is 1.x=1
print("my fav number is" + x_str + "." + "x=" + x_str) #is1.x=1
print("\n")

####################
## EXAMPLE: input
####################
text = input("Type anything... ")
print(5*text)

#modified for user friendly exception handling
while 1:
    try:
        num = int(input("Type an integer... "))
    except ValueError:
        print("Type an integer, not a float, string, etc...")
        continue
    else:
        print(5*int(num))
        break
#num = int(input("Type a number... "))
#print(5*num)
print("\n")

####################
## EXAMPLE: conditionals/branching 
####################
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
if y != 0:
    print("therefore, x / y is", x/y)
elif x < y:
    print("x is smaller")
elif x > y:
    print("y is smaller")
print("thanks!")
print("\n")


####################
## EXAMPLE: remainder 
####################
num = int(input("Enter a number. I'll tell you whether it's an even or odd number... "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")
print("\n")

####################
## EXAMPLE: while loops 
## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that. 
## Hint: use a counter
####################
counter=0
n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while n != "left" and n != "Left":
    counter+=1
    if counter < 2:
        n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
    if counter >= 2:
        n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
print("\nYou got out of the Lost Forest!\n\o/")
print("\n")


#n = 0
#while n < 5:
#    print(n)
#    n = n+1


####################
## EXAMPLE: for loops
####################
for n in range(5):
    if n<=3:
        print(n)
    elif n==4:            #looking for improvement.
        print(n, "\n")    #opted for this format because this only gives me a single empty line in the end,

'''
for n in range(5):        
    print(n)
    if n==4:              #while this format gives me two empty lines in the end
        print("\n")
'''

mysum = 0
for i in range(10):
    mysum += i
print(mysum, "\n")        #45, because it stops at 10-1

mysum = 0
for i in range(7, 10):    #7+8+9=24
    mysum += i
print(mysum, "\n")

mysum = 0
for i in range(5, 11, 2): #range(starting_point, end_point+1, steps)
    mysum += i
    if mysum == 5:
        break             #break kicks in first
        mysum += 1        #this line is not registered
print(mysum, "\n")



####################
## EXAMPLE: perfect squares
####################
#ans = 0
#neg_flag = False
#x = int(input("Enter an integer: "))
#if x < 0:
#    neg_flag = True
#while ans**2 < x:
#    ans = ans + 1
#if ans**2 == x:
#    print("Square root of", x, "is", ans)
#else:
#    print(x, "is not a perfect square")
#    if neg_flag:
#        print("Just checking... did you mean", -x, "?")


####################
## TEST YOURSELF!
## Modify the perfect squares example to print 
## imaginary perfect sqrts if given a negative num.
####################
sqrt = 0
posi_conversion=0
neg_flag = False
user_input = int(input("Enter an integer: "))
if user_input < 0:
    neg_flag = True
    posi_conversion = 0 - user_input
else:
    posi_conversion=user_input
while sqrt**2 < posi_conversion:
    sqrt += 1
if sqrt**2 == user_input and neg_flag==False:
    print("Square root of", user_input, "is", sqrt)
elif sqrt**2 == posi_conversion and neg_flag==True:
    string_user_input=str(user_input)
    string_sqrt=str(sqrt)
    print("Square root of " + string_user_input + " is " + string_sqrt + "i")
else:
    print(user_input, "is not a perfect square")
    
