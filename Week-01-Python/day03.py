
# SETS   

set_a={1, 2, 3, 4, 5}

set_a.add(6)           # adding element     
set_a.remove(3)           # removing element
print(set_a) 

b={4, 5, 6, 7, 8}
print(set_a.union(b))      # union of two sets
print(set_a.intersection(b)) # intersection of two sets
print(set_a.difference(b))   # difference of two sets
print(set_a.symmetric_difference(b)) # symmetric difference of two sets


c={1, 2, 3, 4, 5}
print("c = " , c)

c.discard(3)  # discard element
print(c)


numbers = {10, 20, 30, 40} #clearing all elements from the set
numbers.clear()

print(numbers)


numbers_1 = {10, 20, 30} #copying all elements from the set

new_numbers = numbers_1.copy()

print(new_numbers)

 



# ---------------------------------------------------------------------------------------





# dictionary

products = {
    "bat": 1500,
    "shoes": 2500,
    "ball": 500,
    "racket": 1800
}

filtered_prod={}

for prod,cost in products.items():
    if cost>1000 and cost<=2000:
        filtered_prod[prod]=cost


print("Filtered Products:", filtered_prod)



# ----------------------------------------

# Sort a dictionary by values

# Sort the dictionary in ascending order based on its values.

a={"apple": 50, "banana": 20, "orange": 40}

# Output: {"banana": 20, "orange": 40, "apple": 50}

# sorted_a = dict(sorted(a.items(), key=lambda x: x[1]))
# print(sorted_a)

items=list(a.items())
print("Items:", items)
for i in range(len(items)):
    for j in range(i+1, len(items)):
        if items[i][1] < items[j][1]:
            items[i], items[j] = items[j], items[i]
print("Sorted Items:", items)

# ----------------------------------------
# Strings

# length of string without using len() function

str="hello word"
c=0
for i in range(len(str)):
    if str[i]!= ' ':
        c+=1
print("Length of string:", c)

# ----------------------------------------
#  finding vowels in a string
str = "hello word"
vowels = 0
cons = 0

for ch in str:
    if ch in 'aeiouAEIOU':
        vowels += 1
    elif ch.isalpha():
        cons += 1

print("Vowels:", vowels)
print("Cononants:", cons)


# -------------------------------------------------------------

# err0r_handling

try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))

    result=a/b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("No errors occurred.")



try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Invalid input")

finally:
    print("Program execution completed")



