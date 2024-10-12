# string

"""
s = "string"

print(s[0]) # [location]
"""

# String slicing

"""
#start:stop:step
s = "Hello! long string"

print(s[1:2])
print(s[1:15:4])
print(s[10:2:-2])
print(s[:]) #all
print(s[::-1]) #back
"""

# F string (มีตัวแปลอยู่ข้างใน)

"""
num = 10
num_mul_ten = num * 10

print(f"My number is {num}")
print(f"My number is {num} multioly by 10 got {num_mul_ten}")
"""

# * str

"""
a = "apple "

print(a * 4)
print("banana " * 4)
print(("orange " * 3) + (a * 3))
"""

# \' f"{}" 

"""
txt = "can\'t"
age = 16
name = "sam"

if age < 15:
    txt = "can"
else:
    txt = "can\'t"

print(f"{name} {txt} join our below 15 club!!")
"""

# split()

"""
s = "a b c d e f g"

print(s.split())

s = "a!b!c!d!e!f!g"

print(s.split("! "))
"""

# in operation + not in

"""
s = "abc"

print("a" in "abc") #True
print("ac" in "abc") #False

s = input()

if "d" in s:
    print("we have d in inputed text")

if "a" not in s:
    print("we not have a in inputed text")
"""

# len - length

"""
s = "fgsdvxfgdcbhjhkmbfdgvjkh"

print(len(s))
"""

# count

"""
s = "fffxxxxxxxxxxxxxx"

print(s.count("f")) #3
"""

# condition

"""
s = "string longgggg"

if len(s) > 10:
    if "s" in s:
        print("This in long enough and contains \'s\'")
"""

# basic password checker
# 12-20 long password
# contains ! and * in password
"""
password = input()

if len(password) >= 12 and len(password) <= 20:
    if "!" in password and "*" in password:
        print("password is secure")
    else:
        print("your password not contains \'!\' and \'*\'")
else:
    print("your password is not 12-20 long")
"""

# loops

#use debug
"""
s = "string"

for i in s:
    print(s)

for i in s:
    print(i)
#same
for i in range(len(s)):
    print(s[i])

for i in range(len(s)):
    print(i, s[i])
#same
for i, v in enumerate(s): #เป็นการดึงตำแหน่ง และค่าของมันออกมาเป็นคู่ๆ
    print(i, v)
"""

# strip()

"""
s = "   sarn toi   "
print(s.strip()) #default = space bar

s = "!!!sarn toi!!!"
print(s.strip("!"))
"""

# replace

"""
s = "srt sdrgjy srtFZDTRGJHsrt"

print(s.replace("srt", "ada"))
"""

# remove

"""
s = "aikreuhgikreal"

print(s.replace("a", ""))
"""

# chr() ord()

"""
#chr num to letter
#ord letter to num

print(chr(65)) #A 65-90(A-Z)

print(chr(65)) #chr(65) = A
print(ord("A")) #ord("A") = 65

password = "A"
print(ord(password))

password = "A"
step = 3

o = ord(password)

print(chr(o + step)) #A -> D
"""

"""
password = "Khawfang132"
step = 3

encryted_password = ""
for letter in password:
    letter_ord = ord(letter)
    encryted_letter = chr(letter_ord + step)
    encryted_password += encryted_letter

print(encryted_password)
"""