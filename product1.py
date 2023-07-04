import math
import sys
import random
import datetime

Neg_Score = - 1
Min_Score = 25
Max_Score = 100
Average_Score = 50

# User Input
def get_user_input(prompt, data_type=float, min_value=None, max_value=None):
    while True:
        try:
            value = data_type(input(prompt))
            if min_value is not None and value < min_value:
                raise ValueError("Value must be greater or equal to {}".format(min_value))
            if max_value is not None and value > max_value:
                raise ValueError("Value must be less or equal to {}".format(max_value))
            return value
        except ValueError as e:
            print("Error: {}".format(e))

max_lendingA = 50000
max_lendingB = 100000
client_lending_rate = ()
BOE_interest_rate = 4.75 # %
BNK_interest_rate = round(random.uniform(3.0,8.9))
print("\033[32mBank lending rate is {}%\033[0m".format(BNK_interest_rate))
if BNK_interest_rate > BOE_interest_rate:
    client_lending_rate = max_lendingB
else:
    client_lending_rate = max_lendingA
print("Maximum borrow figure for retail clients:", client_lending_rate)

# Client Loan Request
client_requested_amount = 0
while not (1 <= client_requested_amount <= client_lending_rate):
    try:
        client_requested_amount = int(input(f"How much are you looking to borrow between 1 and {client_lending_rate}? "))
        if not (1 <= client_requested_amount <= client_lending_rate):
            print(f"\033[31mInvalid. Please enter a borrow amount between 1 and {client_lending_rate}.\033[0m")
    except ValueError:
        print("\033[31mInvalid input. Please enter a valid integer value.\033[0m")

# Score Start
score = 0

# Income
while True:
    try:
        client_income = int(input("What was your income for the year 2021 - 2022? "))
        if client_income <= 0:
            raise ValueError("\033[31mIncome must be a positive number\33[0m")      # Red
        break
    except ValueError as e:
        print("\033[31mInvalid input. {}\033[0m".format(e))     # Red
if client_income >= client_requested_amount/ 3:
    score += 35
elif client_income < client_requested_amount / 3:
    score -= 10

# Assets
client_assets = None
while client_assets is None:
    try:
        client_assets = int(input("What is the total value of your current assets (in GBP)? "))
    except ValueError:
        print("\033[31mInvalid input. Please enter a valid value.\033[m")       # Red
if client_assets >= client_requested_amount/ 0.10:
    score += 35
elif client_requested_amount/0.05 <= client_assets <= client_requested_amount/ 0.09:
    score += 0
elif client_assets < client_requested_amount/ 0.04:
    score -= 10

# Employed
def ask_employed_questions():
    global score  # Use scoring system of the entire programme
    job = None
    while not job:
        job = input("What is your current or most recent job position? ")
        if not job:
            print("\033[31mPlease enter your current or most recent job position\033[m")        # Red

    experience = None
    while experience is None:
        try:
            experience = int(input("In months, how long have you been working in your current or most recent job? "))
        except ValueError:
            print("\033[31mPlease enter your current or most recent job position in months\033[m")

    if experience == 24 or experience == 36 or 24 <= experience <= 36:
        score += 20
    elif experience == 18 or experience == 23 or 18 <= experience <= 23:
        score += 15
    elif experience == 12 or experience == 17 or 12 <= experience <= 17:
        score += 10
    elif experience <= 11:
        score -= 5

# Unemployed
def ask_unemployed_questions():
    global score
    job = None
    while job is None:
        try:
            job = int(input("How long have you been unemployed for in months? "))
        except ValueError:
            print("\033[31mPlease enter how long you have been unemployed for in months\033[m")

    if job <= 3:
        score -= 20
    elif job == 4 or job == 6 or 4 <= job <= 6:
        score -= 23
    elif job == 7 or job == 12 or 7 <= job <= 12:
        score -= 25
    elif job >= 13:
        score -= 30

# Student
def ask_student_questions():
    student = None
    while not student:
        student = input("What is your current level of education?\n"
                        " 1. Undergraduate\n"
                        " 2. Postgraduate\n ")
        if student == "Undergraduate" or student == "undergraduate":
            ask_undergrad_ucasid()
            break
        elif not student:
            print("\033[31mPlease enter your current level of education\033[m")     # Red
def ask_undergrad_ucasid():
    global score
    UCAS_ID = "UCAS2023" and "ucas2023"
    id = None
    while not id:
        id = input("Enter your UCAS ID: ")
        if id == UCAS_ID:
            score += 10
            ask_undergrad_email()
            break
        elif not id:
            print("\033[31mPlease enter a valid UCAS ID\033[m")
def ask_undergrad_email():
    global score
    student_email = "@.com"
    email = None
    while not email:
        email = input("Enter your student email address: ")
        if email == student_email:

            score += 10
            break
        elif not email:
            print("\033[31mPlease enter a valid student email address\033[m")

client_occupation = None
while not client_occupation:
    client_occupation = input("What is your employment status? Select Option: \n"
                          " 1. Employed\n"
                          " 2. Unemployed\n"
                          " 3. Student\n")

if client_occupation.strip() == "Student" or client_occupation.strip() == "student":
    ask_student_questions()
elif client_occupation.strip() == "Employed" or client_occupation.strip() == "employed":
    ask_employed_questions()
elif client_occupation.strip() == "Unemployed" or client_occupation.strip() == "unemployed":
    ask_unemployed_questions()
elif not client_occupation:
    print("\033[31mPlease enter a valid occupation\033[m")

print("Your eligibility score is", score)

print("What does your score mean? \n"
                "1 - 10 (You are not eligible)\n"
                "11 - 20 (Further details required, please contact customer support and quote reference number #0981B\n"
                "21 - 30 (You meet the minumum requiremnts, a member of the team will be in contact shortly for further details\n"
                "31 and above (Congratulations, you are eligible for an instant transfer of funds")
