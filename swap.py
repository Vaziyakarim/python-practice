a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Before swap a " + str(a) + " and b "  +str(b))
a=a+b
b=a-b
a=a-b
print("After swap a " + str(a) + " and b "  +str(b))