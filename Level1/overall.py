#print("Hello world")

#this is a comment

""" this
    is
    a
    comment
"""
#print("This is single argument print") 
#print("This", "is", "multiple", "argument", "print")

#print(type(True))

print("\"rimuru\"") #แสดงผลออกมามีฟันหนูครอบข้อความ, '""'

#print(type(None))

"""x = 9
print(x)"""

"""การตั้งชื่อตัวแปร"""

"""my_age = int(input("Input your age : "))
print(my_age)"""

#print(10 ** 3)

#x = 10

"""
x = x + 5
x += 5
"""

"""x *= 10
print(x)

x /= 3

x //= 3

print(x)"""

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

"""_______________________________________________________________________________________"""

#6

"""s = str(input())
print(len(s))
n = int((len(s) - 1) / 2)

print(s[n-1] + s[n] + s[n+1])"""

#if elif else

"""x = int(input())
if x > 5 :
    print("x is more positive Number 5")
elif x == 0 :
    print("x is zeso Number")
else :
    print("x is nagative number")"""

"""x = int(input())
if x > 0 : print("x is positive Number")
elif x == 0 : print("x = 0")"""

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

#for loop

#print(list(range(10))) #stop
#print(list(range(2, 10))) #start, stop
#print(list(range(2, 10, 2))) #start, stop, step
#print(list(range(2, 100, 2)))

"""for number in range(1, 100, 2) :
    print(number)"""

"""x = int(input())
sum = 0
for number in range(1, x + 1, 2) :
    sum += number
print(sum)"""

#while loop

"""number = 0
while number < 5 :
    print(number)
    number += 1"""

"""target = int(input())
number = 1
sum = 0
while number <= target :
    sum += number
    number += 1
print(sum)"""

"""for number in range (10) :
    if number == 3 :
        continue
    if number == 5 :
        pass
    if number == 7 :
        break #stop
    print(number)"""

#day2 - 4

"""number = int(input())

if number % 7 ==  0 :
    if number % 11 != 0:
        print("YES")
    elif number % 11 == 0:
        print("NO")
elif number % 7 != 0 :
    print("NO")"""

#prime number จำนวนเฉพาะ

"""x = int(input())
is_prime_number = True
if x == 1 :
    is_prime_number = False
for number in range (2, x) :
    if x % number == 0 :
        is_prime_number = False
        break
print(is_prime_number)"""

#สูตรคูณ

"""for x in range(2, 13) :
    for y in range(1, 13) :
        print(x, "x", y, "=", x * y)"""

#day2 - 5

"""n = int(input())
sum = n * (n + 1) // 2
for _ in range(n - 1) :
    number = int(input())
    sum -= number
print(sum)"""

"""_______________________________________________________________________________________"""

#day3 - 1

"""a = int(input())
b = int(input())

x = a + b
y = str(a)
z = str(b)

print((y + z), x)"""

#string

"""s = "Hello!" # H=-6, e=-5, l=-4, l=-3, o=-2, !=-1

print(s[0:3]) #print(s[-6]) เริ่ม0ถึง2 ไม่เอา3 #print(s[::-1]) เริ่มแบบถอยหลัง
"""
#s string

"""num = 10
num_mul_ten = num * 10

print(f"My number is {num}")

print(f"My number is {num} multiply by 10 {num_mul_ten}")

print(f"My number is %d" % (num))"""

"""txt = "can\'t"
age = 16
name = "sam"

if age < 15 :
    txt = "can"
else :
    txt = "can\'t"
"""
#split()

"""s = "a b c d e f g"

print(s.split())

s = "a!b!c!d!e!f!g"

print(s.split("0"))"""

#In operation
"""
s = "abc"

print("a" in "abc")
print("ac" in "abc")
#ac ab false
#ac bc false

s = input()

if "d" in s :
    print("We have d in inputted text")
else :
    print("We don't have d in inputted text")"""

#len - length

"""s = "iunbionzdriughpoirhggjhxnyopjohjiny"

print(len(s))

#เฉลยโจทย์ในคลาส ค่ากลาง

#s = "abcxyzabc"
#print xyz
#slicing s[a, a+3]

s = "abcxyzabc"
length = len(s)

print(length)

a = length // 2 - 1

print(a)
print(s[a:a+3])"""

# count

"""s = "respectfffffulness"
print(s.count("f"))"""

# condition

"""s = "string long looooong"

if len(s) > 10 :
    if "s" in s :
        print("this is long enough and contains \'s\'")

#basic passpord
#12-20 long password
#! and * in password

password = input()"""

#day3 - 2

"""s = str(input())
n = int(len(s))
ans = "YES"

for i in range(n) :
    n -= 1
    if s[-n - 1] != s[n] :
        ans = "NO"
print(ans)"""

"""_______________________________________________________________________________________"""

# map

"""a = input().split()

print(a)
print(list(map(int, a)))"""

# if

"""ist = [1, 2, 5, 2, 7, 4]

ist.sort(reverse=True)

print(ist)

ist.sort()

print(ist)"""

# extend to another list

"""ist_a = [1, 4, 5]
ist_b = [2, 3, 6, 7]

ist_a.extend(ist_b)

print(ist_a)"""

# count

"""ist = [1, 4, 6, 3, 2, 3, 2, 5, 6]
s = "asdfffds"
print(ist.count(3))
print(s.count("f"))"""

#

"""ist_a = [1, 2, 3, 4, 5]
ist_b = ist_a.copy()

print(ist_b)

ist_b[0] = 5

print(ist_b)"""

# condition

"""ist = [1, 2, 3, 4, 5]"""

# if len(){function}, in, count()

"""if len(ist) > 2 :
"""

# 7

"""n = int(input())
ist = list(map(int, input().split()))
cnt = int(input())

print(ist[cnt])"""

# 8

"""n = int(input())
ist = list(map(int, input().split()))

print(*ist[::2])"""

# Tuple

"""t = (123, 834, 20)

t[0] = 2"""

"""variables = (3, 2, 8)
variables = list(variables)

print(type(variables))"""

"""variables = (3, 2, 8)

t = ()

t_2 = ("saraoitn", 23, False)

print(type(variables), type(t), type(t_2))

for i in variables :
    if i >= 3 :
        print(i)"""

# dictionary key-value

# day4 - 1

"""n = int(input())
ist = list(map(int, input().split()))
x = int(input())

for i in range(n) :
    print(ist[i] + x, end = " ")"""

# day4 - 2

"""n = int(input())
ist = list(map(int, input().split()))
data = []

for i in range(n) :
    if ist[i] % 2 == 0 :
        data.append(ist[i])

print(*data)"""

#day4 - 3

"""n = int(input())
ist_a = list(map(int, input().split()))
ist_b = list(map(int, input().split()))

for i in range(n) :
    print(ist_a[i], ist_b[i], end = " ")"""

#day4 - 4

"""n = int(input())
ist = list(map(int, input().split()))
ist.sort()

if ist[0] * ist[1] <= ist[n-1] * ist[n-2] :
    print(ist[n-1] * ist[n-2])
else :
    print(ist[1] * ist[0])"""


#day4 - 5

"""n = int(input())
st = set(list(map(int, input().split())))

print(len(st))"""

#day3 - 3

"""s = input()
n = len(s)

x = int(n/2)

print(s[x:n:], end = "")
print(s[0:x:])"""

#day3 - 5
#1)
"""txt = input()
for i in txt :
    if i!='x':
        print(i, end = "")"""
#2)
"""txt = input()

x = txt.split("x")
for i in x :
    print(i, end = "")"""
