# InClass Problems

#1 A
"""
print("Hello, World!")
"""

#2 B
"""
n = int(input())
k = int(input())

print(n * (3 ** k))
"""

#3 C

#4 D

#5 E
"""
s = input()
n = len(s) // 2 - 1

print(s[n:n+3])
"""

#6 F
"""
s = input()
print(s.count("f"))
"""

# Day 1

#1
#2
#3
#4
#5

# Day 2

#1 A
#2 B
#3 C
#4 D

#5 E
##if "f" in s and "ba" + "na" * 2(* in)

# 1

"""n = int(input())
m = int(input())
 
if n <= m :
   print(n)
else :
    print(m)"""

# 2

"""x = int(input())

if 0 <= x <= 40 :
  print("Emerging")
elif 41 <= x <= 80 :
  print("Developing")
else :
  print("Achieved")"""

#3

"""n = int(input())

x = int(n / 2)
print(x)"""

#4

"""n = int(input())
n = n // 10

print(n)"""

#5

"""m = int(input())

h = m // 60
m = m - (h * 60)

print(h)
print(m)"""

#6

"""s = str(input())
print(len(s))
n = int((len(s) - 1) / 2)

print(s[n-1] + s[n] + s[n+1])"""

#if 10,000 baht

"""age = int(input("Age :"))
if age >= 16 :
    incom_per_month = int(input("Incom per month :"))
    deposit = int(input("Deposit :"))
    if incom_per_month < 70000 or deposit <500000 :
        print("10000 Baht!!")
    else :
        print("No 10,000 baht")
else :
    print("No 10,000 baht")
"""
#BMI

"""weight = float(input("Weight :"))
height = int(input("Height :")) / 100
BMI = weight / height ** 2

if BMI > 30 :
    print("อ้วนระดับ 2")
elif BMI >= 25 :
    print("อ้วนระดับ 1")
elif BMI >= 23 :
    print("น้ำหนักเกิน")
elif BMI >= 18.5 :
    print("สมส่วน")
else :
    print("ต่ำกว่าเกณฑ์")"""

#7

"""s = str(input())
n = len(s)
x = 0

for i in s :
    if i == "f" :
        x += 1
print(x)"""

#day2 - 1

"""T = int(input())

if T > 35 :
    print("CANCEL SCHOOL")
elif T > 30 :
    print("CANCEL TWO CLASSES")
else :
    print("NORMAL CLASSES")"""

#day2 - 2

"""a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c :
    if b >= c :
        print(a + b)
    else :
        print(a + c)
elif b >= a and b >= c :
    if a >= c :
        print(b + a)
    else :
        print(b + c)
elif c >= a and c >= b :
    if a >= b :
        print(c + a)
    else :
        print(c + b)"""

#day2 - 3

"""n = int(input())
while n > 0 :
    print(n)
    n -= 1"""
