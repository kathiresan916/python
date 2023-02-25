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


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a // b


print("""
Choose a type of your calculation:
1. Addtion
2. Subtraction
3. Multiplication
4. Subtraction

""")

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

