EX:1
name=input("Enter your name: ")
age=int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old")

#EX:2
number=int(input("Enter a number: "))
if number > 0:
    print("Postive")
elif number < 0:
    print("Nagative")
else:
    print("Zero")

#EX:3
print("Printing even numbers")
for i in range(2,52,2):
  print(f"Even no's {i}")

#EX:4
def square(number):
    return number * number

n=int(input("Enter n: "))
print(f"The square of {n} is ",square(n))

#Ex:5
def is_even(number):
    if(number%2==0):
        return True
    else:
        return False
n=int(input("Enter n: "))
print(is_even(n))


#EX:6
def count_vowel(text):
    vowel="aeiouAEIOU"
    count=0
    for char in text:
        if char in vowel:
            count+=1
    return count
user_text=input("Enter a sentense: ")
print(f"I has vowels count of ",count_vowel(user_text))

#EX:7
def fizzbuzz(n):
    for i in range(1,n+1):
        if n%3==0 and n%5==0:
            print("FIzzBuzz")
        
        elif n%5==0:
            print("buzz")
        elif n%3==0:
            print("fizz")
            
        else:
            print(i)
n=int(input("Enter n: "))
fizzbuzz(n)