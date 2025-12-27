#arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)


#relational/comparison Operators
x = 5
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


#logical Operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)


#assignment Operators
x = 5
print(x)

x += 2
print(x)

x -= 1
print(x)

x *= 3
print(x)

x /= 2
print(x)

x %= 2
print(x)


#bitwise Operators

a = 5      # 101
b = 3      # 011

print(a & b)   # AND
print(a | b)   # OR
print(a ^ b)   # XOR
print(~a)      # NOT
print(a << 1)  # Left Shift
print(a >> 1)  # Right Shift


#membership Operators

text = "Artificial Intelligence"
print("AI" in text)
print("ML" not in text)


#identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)


#ternary (Conditional) Operator
age = 18
result = "Eligible" if age >= 18 else "Not Eligible"
print(result)


#operator Precedence Example

result = 10 + 5 * 2
print(result)   # Multiplication first