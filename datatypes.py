#creating Strings

s1 = "Artificial Intelligence"
s2 = 'Python'
s3 = """This is
a multiline
string"""

print(s1)
print(s2)
print(s3)

#string Length
text = "Python"
print(len(text))

#indexing
word = "Python"
print(word[0])    
print(word[-1])   

#slicing
word = "Artificial"
print(word[0:4])    
print(word[5:])     
print(word[:6])    
print(word[::-1])

#string Concatenation
a = "Artificial"
b = " Intelligence"
print(a + b)

#membership Operators
sentence = "Artificial Intelligence"

print("AI" in sentence)
print("ML" not in sentence)

#string Comparison
print("AI" == "ai")
print("Python" > "Java")

#string Modifiers
text = "python programming"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

#removing whitespaces
text = "   AI   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#replace and find
text = "AI is powerful"

print(text.replace("powerful", "useful"))
print(text.find("AI"))
