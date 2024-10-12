#This is a single line comment

"""
This is a multiline comment
"""

# print

#single argument
"""print("hello world")"""

#multiple argument
"""print('You', 'are', 'a', 'boy')"""

#multiple lines
"""
print('this is the first line')
print('This is the second line')
"""
#or
"""print('a'); print('b') #not recommend"""

#printing arguments

"""
#"\n" means endline
#"\t" means tab

a = 121

b = 1249

c = 623

print(a, b, c)
print(a, b, c, sep="")
print(a, b, c, end="\n") #print no space bar
print(a, b, c, end="\t")
"""

# how ot check data type?

"""
print(type(5))
print(type(5.00))
print(type(True))
print(type('Programmingvis easy')) #single quote
print(type("Programmingvis easy")) #double quote
print(type(None)) #NoneType
"""

# str \" = "
"""
print('he says "Python is easy."') #Don't recommend
print("he says \"Python is easy.\"")
"""

# Variable

"""
x = 9
print(x)

my_name = "Khawtomkung"
print(my_name)
"""

#  input data type

"""
my_age = int(input())
print(type((my_age)))

my_name = input("enter your name :")
print(type((my_name)))

my_weight = float(input("enter your weight :"))
print(type((my_weight)))
"""

# Python as a calculator

"""
print(3 + 2) # 5
print(3 - 1) # 2
print(7 * 2) # 14
print(5 / 3) # 1.667
print(5 // 3) # 1 หารตัดเศษทิ้ง
print(5 % 2) # 1 ม้อด หารเอาแค่เศษ
print(5 ** 2) # 25 ยกกำลัง
"""

# Hierarchy of Operations

"""
()
A ** 2
* or /
+ or -
"""

# Variable Adjustment

"""
a = 3
a = a + 2 #5
print(a)

a = 10
a += 4 # a บวกไปอีก 4 = 14
print(a)

a -= 4 #10
print(a)

a /= 2 #5
print(a)

a *= 2 #25
print(a)
"""

# Comparison Operators

"""
> มากกว่า
< น้อยกว่า
>= มากกว่าเท่ากับ
<= น้อยกว่าเท่ากับ
== เท่ากับ
!= ไม่เท่ากับ
"""

# CONSTANT ASSIGNMENT
"""PI = 3.14"""

# Built-in Python Function for Numbers

"""
x = -3
#x = float(x)
print(type(x)) #float

x = -3
#x = str(x)
print(type(x)) #string

#x = int(x)
print(type(x)) #int

#x = abs(x)
print(x) #3

#print(max(10, 20, 30, 40)) #40

#print(min(10, 20, 30, 40)) #10

#print(round(3.1415925358, 3)) #3.142

print(bin(2))
"""