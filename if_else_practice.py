#simple if statement
age = 20

if age >= 18:
    print("Eligible to vote")
    
#if–else Statement
num = 7

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
#if–elif–else Statement
marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
    
#nested if statement
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Invalid username")
    
#nested if (number comparison example)
num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number")
    
#multiple conditions using logical operators
age = 22
citizen = True

if age >= 18 and citizen:
    print("Eligible for CNIC")
else:
    print("Not eligible")
    
#ternary (short if–else)
num = 10
result = "Positive" if num > 0 else "Negative"
print(result)