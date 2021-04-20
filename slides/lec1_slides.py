a=13
b=4.23
c=7.0001
d=3

#this formatting works as intended on IDLE, or python 3.8.6 comes with Ubuntu 20.10.
#however it returns not very pretty results on python 2.7.18.
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

print("a*a =", a*a)
print("a**d =", a**d)
print("a/d =", a/d)
print("a%d =", a%d)
print("((a+b)/c)/2 =", ((a+b)/c)/2)

print("float(a) =", float(a))
print("int(b) =", int(b))

#this formatting works as intended on python 2.7.18, but produces SyntaxError on python3
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print("a =", a)?
"""
print "a =", a
print "b =", b
print "c =", c
print "d =", d

print "a*a =", a*a
print "a**d =", a**d
print "a/d =", a/d
print "a%d =", a%d
print "((a+b)/c)/2 =", ((a+b)/c)/2

print "float(a) =", float(a)
print "int(b) =", int(b)
"""
