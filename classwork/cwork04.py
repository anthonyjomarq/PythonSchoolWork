# In class work
# Date: 9/28/21

# Enter value 1 (a number) and store in variable x
x = int(input("Enter number 1: "))

# Enter value 2 (a number) and store in variable y
y = int(input("Enter number 2: "))

# Enter value 3 (a string) and store in variable z
z = input("Enter an operator: ")

#prints the sum of x and y if the value of z is +
print("The value of z is ", z)
if z == '+' :
    print(x+y)
if z == '-' :
    print(x - y)
if z == '*' :
    print(x * y)
if z == '/' :
    print(x / y)
else:
    print("The string is not a +, -, * or / operator")
