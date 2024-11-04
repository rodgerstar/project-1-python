# error handling

x = input("Enter first number: ")
y = input("Enter second number: ")
z = input("Enter third number: ")

try:
    x_num = int(x)
    y_num = int(y)
    z_num = int(z)
    print(x_num * y_num * z_num)
except:
    print("Please enter valid numbers")


