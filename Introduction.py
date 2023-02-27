# Bold Text
# print("\033[1mWelcome, Kathiresan Selvaraj!\033[0m")
"""
Tamil=100
Engligh=100
Maths=100
Science=100
Social=100

print (Tamil + Engligh + Maths + Science + Social)

Linebyline = """ """This is my First Python

Thanks,
Kathiresan Selvaraj""""""""

s
print(Linebyline)

word = "    Kathiresan Selvaraj "
print(word.strip().upper().lower())

word = "Kathiresan Selvara"
print(word.split("S"))

word = "Hello World"
print("Hell" in word)
a1 = "Kathiresan"
a2 = " Selvaraj"
print(a1 + a2)

fruits = ["Apple", "Orange", "Banana", "Dragon Fruit"]
fruits.append("Jackfruit")
fruits.sort()
print(fruits)

"""

"""
My_Data = {
    "Name": "Kathiresan Selvaraj",
    "Age": "27",
    "Weight": "45"
}
print(My_Data.get("Age"))
"""

"""
loan = 1100000.00
if loan > 100000.00:
    print("Your Eligible for loan")
elif loan == 100000.00:
    print("Apply for Loan")
else:
    print("You're Not Eligible for Loan")
"""

"""
def addition():
    a = 10
    b = 10
    print(a + b)

addition()
addition()

"""

"""
def addition(a, b):
    print(a + b)

def subtraction(a, b):
    print(a - b)

addition(10, 10)
subtraction(10, 20)

def name(name):
    print("Hi, " + name)

name("Kathiresan Selvaraj")

"""
"""
name = 'Kathiresan Selvaraj'
for letters in name:
    print(letters)
"""

"""
fruits = "Apple", "Orange", "Kiwi", "Banana", "Pomo"
for fruit in fruits:
    print(fruit)
"""

"""
for i in "Kathiresan Selvaraj":
    if i == 'e':
        print("e is entered")
        break
    else:
        print("e is not entered")

"""

"""
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("Finished")

"""
"""
name = input("Type your Name:")
print("My Name is, " + name)
"""

"""
a = int(input("Enter your First Value:"))
b = int(input("Enter your Second Value:"))
print(a + b)

a = float(input("Enter your First Value:"))
b = float(input("Enter your Second Value:"))
print(a + b)
"""

"""
a = int(input("Enter first value:"))
b = int(input("Enter Second Value:"))
print("your result addition is:", a + b)
print("your result subtraction is:", a - b)
print("your result multiplication is:", a * b)
print("your result division is:", a / b)

"""

"""
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a // b

"""

"""
print(Choose a type of your calculation:
1. Addtion
2. Subtraction
3. Multiplication
4. Subtraction)
"""

""" 

choice = int(input("Enter your Choice:"))
a = int(input("Enter your First Value:"))
b = int(input("Enter your Second Value:"))

if choice == 1:
    print(addition(a, b))
elif choice == 2:
    print(subtraction(a, b))
elif choice == 3:
    print(multiplication(a, b))
elif choice == 4:
    print(division(a, b))
else:
    print("Enter correct Choice")

"""

"""
def multiply_or_add(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

num1 = int(input("Enter Number1:"))
num2 = int(input("Enter Number2:"))

result = multiply_or_add(num1, num2)
print("The result is:", result)

"""

"""
numbers = int(input("Enter Your Number:"))
print("Printing current and Previous number sum in a range", numbers)

previous_numbers = 0

for current_number in range(1, numbers+1):
    sum_of_numbers = current_number + previous_numbers
    print("Current Number is:", current_number, "Previous Number is:", previous_numbers, "Sum is:", sum_of_numbers)
    previous_numbers = current_number

"""

"""
while n <= 10:
    print("Current Numer is:", n, "Previous Number is:", n-1, "Sum:", n-1+n)
    n += 1
    break
"""
"""
string = "pynative"
print("Original String is:", string)
print("Printing only even index chars")
print("p")
print("n")
print("t")
print("v")

"""
"""
input_str = input("Original String is:")
even_chars = ""
for i in range(0, len(input_str), 2):
    even_chars += input_str[i]
print("Printing only even index Chars:")
"""

"""
word = input("Enter a String:")
print("Original String is:", word)

size = len(word)
print("Printing only Even Index Chars")

for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])
"""
"""
word = input("Enter a String:")
print("Original String is:", word)
x = list(word)
for i in x[0::2]:
    print(i)
"""

"""
def remove_chars(string, n):
    return string[n:]


string1 = "Kathiresan"
n1 = 4
print(remove_chars(string1, n1))

string2 = "Kathiresan"
n2 = 2l
print(remove_chars(string2, n2))

"""

def remove_chars(word, n):
    print("Original String:", word)
    x = word[n:]
    return x

print("Removing Character from a String:")
print(remove_chars("Kathiresan", 4))
print(remove_chars("Kathireasn", 2))











