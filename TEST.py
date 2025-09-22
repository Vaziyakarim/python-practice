#simple calculator 
def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /,'**'): ")
    
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '**':
        print("Result:", a ** b)    
    elif op == '/':
        print("Result:", a / b)
    else:
        print("Invalid operator!")

calculator()

#Number Gueesing Game
import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Correct!")
else:
    print(f"Wrong! The number was {number}.")

#Simple quiz
question = "What is the capital of France? "
answer = "Paris"

user_answer = input(question)

if user_answer.strip().capitalize() == answer:
    print("Correct!")
else:
    print("Wrong!")

Rock paper scissors
import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("Enter rock, paper, or scissors: ").lower()

if user == computer:
    print("Tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose! Computer chose", computer)

Simple Alarm,
import time

alarm_time = input("Set alarm time (HH:MM): ")

while True:
    current_time = time.strftime("%H:%M")
    if current_time == alarm_time:
        print("Wake up!")
        break
    time.sleep(30)

#Password generator
import random
import string

try:
    length = int(input("Enter password length: "))
    if length <= 0:
        raise ValueError("Password length must be positive.")

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password:", password)

except ValueError as e:
    print("Error:", e)
