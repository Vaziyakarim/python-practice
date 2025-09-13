#Handling errors
try:
    age=int(input("Age:"))
    income=20000
    risk=income/age
    print(f'your age is {age}')
except ZeroDivisionError:
    print("Age cannt be 0")
except ValueError:
    print("Invalid value")
