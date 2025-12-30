#simple function (no prameters, no return)
def greet():
    print("Welcome to Python Functions")

greet()

#function with parameters
def add(a,b):
    print("Sum =", a + b)

add(5, 3)

#function with return value
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print("Result =", result)

#function with default parameters
def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(2, 3))

#function with keyword arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Ali")

#function with variable-length arguments (*args)
def total(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(total(10, 20, 30))

#function with keyword Variable-Length Arguments (**kwargs)
def info(**details):
    for key, value in details.items():
        print(key, ":", value)

info(name="Ali", course="AI", age=21)

#recursive function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

#lambda (anonymous) function
square = lambda x: x * x
print(square(6))

#function inside function (nested function)
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()

#function using list
def max_value(lst):
    return max(lst)

numbers = [10, 25, 5, 40]
print(max_value(numbers))

#function with return vs print
def show():
    print("This is print")

def give():
    return "This is return"

show()
print(give())

#built-in function usage
nums = [1, 2, 3, 4]

print(len(nums))
print(sum(nums))
print(max(nums))

#mini practice program (all-in-one)
def calculator(a, b):
    return a + b, a - b, a * b, a / b

add, sub, mul, div = calculator(10, 5)

print(add)
print(sub)
print(mul)
print(div)