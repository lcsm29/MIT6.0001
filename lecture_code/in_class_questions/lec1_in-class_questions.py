#1. this won't do anything when it's ran from the editor. it'll print 'int' when it's ran from the shell.
type(7)
type("cat")
type(3.1415926535)

#this will print 2.0, not 2
print(3.0-1)

#2. you can't save value to <variable> <operator> <variable>
#x+y=2
#x*x=2
#2=x
xy=2
print("xy =",xy)

#3. 
usa_gold = 46
uk_gold = 27
romania_gold = 1

total_gold = usa_gold + uk_gold + romania_gold #total_gold is now 74
print(total_gold) #this will print 74

romania_gold += 1 #this will change romania_gold to 2
print(total_gold) #this will print 74, since total_gold remains unchanged.
