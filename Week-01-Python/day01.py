# 1st problem

# string 
a = 'hello world'
rev = ''

for i in a :
    rev = i+rev
print(rev)

# ---------------------------------------------


# 2nd problem

# conditional statements

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = input("Enter symbol: ")

if c == "+":
    print( a + b)

elif c == "-":
    print( a - b)

elif c == "*":
    print( a * b) 

elif c == "/":
    if b != 0:
        print( a / b)
    else:
        print("Cannot divide by zero")

elif c == "//":
    if b != 0:
        print( a // b)
    else:
        print("Cannot divide by zero")

elif c == "%":
    if b != 0:
        print( a % b)
    else:
        print("Cannot divide by zero")

elif c == "**":
    print( a ** b)

else:
    print("Invalid symbol")

# ----------------------------------------------

# 3rd problem


# prime numbers

num = int(input("number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

# ------------------------------------

# 4th problem

# sum of digits
#  1234 => 1+2+3+4 = 10

num = int(input("number: "))
tot = 0
for i in range(num):
    dig = num % 10
    tot += dig
    num = num // 10
print("Sum of dig:", tot)

# -------------------------------------

# 5th problem

# type of data

# Integer
a = 10
print(a)
print(type(a))

# Float
b = 10.5
print(b)
print(type(b))

# Complex
c = 5 + 3j
print(c)
print(type(c))
