# print("Hello World")

# for i in range(4, 8):
#     print(i)


# if True:
#     for i in range(1,6):
#         print(i)
# else:
#     for j in range(1,5):
#         print(j)


# _1 = 1
# print(_1)

# x = 1 #Small
# X = 2 #Capital
# print(X)



# x, y, z = 1,2,"salman"
# print(x,y,z)  #multiple variables

# x = y = z = 100
# print(x,y,z) # same value


# a = 10
# b = 20 
# a,b = b,a
# print(a,b) #variables swaping



# x = 10 #global

# def show ():
#     x = 5 # local
#     # print(x) #output :5

# show()
# print(x) #output :10



# a = 10 
 
# def change():
#     global a 
#     a = 20

# change()
# print(a) # #output :20 bcz its manipulated inside the function



# x = 60 
# del x 
# print(x)


# x = 10
# print(type(x))


# a = 5
# b = a
# a = 10
# print(b)


# list1 = [1,2,3]
# list2 = list1
# list1.append(4)
# print(list2)

# if True:
# print("Hi")


# x = 10      # integer variable
# name = "Salman"  # string variable
# pi = 3.14  # float variable



# x, y, z = 10, 20, 30
# print(x, y, z)


# a = b = c = 100
# print(a, b, c)


# x = 5
# y = 10
# x, y = y, x
# print(x, y)  # Output: 10 5


# x = 10  # global

# def show():
#     x = 5  # local
#     print("Inside:", x)

# show()
# print("Outside:", x)



# x = 10
# def change():
#     global x
#     x = 20
# change()
# print(x)  # Output: 20



# x = 100
# del x
# print(x)  # ❌ Error: NameError



# x = 10
# print(type(x))



# z = 2 + 3j
# print(type(z),z)  # <class 'complex'>


# for i in range(5):
#     print(i)


# student = {"name":"Salman", "age":25}
# print(student["name"], student["age"])


# s = {1,2,2,3}
# print(s)  # Output: {1,2,3}

# fs = frozenset([1,1,2,3,4])
# print(fs)



# lst = [1, 2, 3]
# lst[0] = 10      # Change item
# lst.append(4)    # Add item
# lst.remove(2)    # Remove item
# print(lst)       # [10, 3, 4]


# person = ("Salman", 22, "Male")
# print(person[0])  # Salman


# for i in range(5):
#     print(i)



# d = {"name": "Salman", "age": 22}
# d["age"] = 23        # Change value
# d["city"] = "India"  # Add new key-value
# print(d)             # {'name':'Salman','age':23,'city':'India'}


# s = {1, 2, 3}
# s.add(4)    # Add item
# s.remove(2) # Remove item
# print(s)    # {1, 3, 4}


# fs = frozenset([1, 2, 3])
# # fs.add(4)   → Error! Cannot modify
# print(fs)     # frozenset({1, 2, 3})





# # 🧮 1️⃣ Arithmetic Operators
# a = 10
# b = 3
# print("Arithmetic Operators:")
# print(a + b)   # + → koottal (addition) # output: 13
# print(a - b)   # - → kurav (subtraction) # output: 7
# print(a * b)   # * → gunam (multiplication) # output: 30
# print(a / b)   # / → bhaagam (division) # output: 3.3333333333333335
# print(a % b)   # % → remainder (balance) # output: 1
# print(a // b)  # // → floor division (integer part) # output: 3
# print(a ** b)  # ** → power (10^3) # output: 1000
# print()

# ⚖️ 2️⃣ Comparison Operators
# print("Comparison Operators:")
# print(a == b)  # == → equal aano? # output: False
# print(a != b)  # != → equal alla? # output: True
# print(a > b)   # > → valuthano? # output: True
# print(a < b)   # < → cheruthano? # output: False
# print(a >= b)  # >= → equal or valutha? # output: True
# print(a <= b)  # <= → equal or cherutha? # output: False
# print()

# # 📝 3️⃣ Assignment Operators
# print("Assignment Operators:")
# x = 5
# # x += 2  # x = x + 2
# # x -= 1  # x = x - 1
# # x *= 3  # x = x * 3
# # x /= 2  # x = x / 2
# print(x)  # output: 9.0
# print()

# # 🧠 4️⃣ Logical Operators
# print("Logical Operators:")
# p = True
# q = False
# print(p and q)  # and → randum true aanel mathi # output: False
# print(p or q)   # or → oru true aanel mathi # output: True
# print(not p)    # not → opposite aakkum # output: False
# print()

# 💡 5️⃣ Bitwise Operators
# print("Bitwise Operators:")
# a = 5  # 0101
# b = 3  # 0011
# print(a & b)  # & → bitwise AND # output: 1
# print(a | b)  # | → bitwise OR # output: 7
# print(a ^ b)  # ^ → XOR # output: 6
# print(~a)     # ~ → NOT (opposite bits) # output: -6
# print(a << 1) # << → Left shift (x2) # output: 10
# print(a >> 1) # >> → Right shift (/2) # output: 2
# print()

# 🔍 6️⃣ Membership Operators
# print("Membership Operators:")
# fruits = ["apple", "banana", "cherry"]
# print("apple" in fruits)      # in → item undoo? # output: True
# print("mango" not in fruits)  # not in → item illa? # output: True
# print()

# # 🪞 7️⃣ Identity Operators
# print("Identity Operators:")
# x = [1, 2, 3]
# y = x 
# z = [1, 2, 3]
# print(x is y)     # is → same memory object aano? # output: True
# print(x is not z) # is not → different object aano? # output: True


# # Write if-else to print "Even" or "Odd"
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")


# Write if-elif-else to print "Positive", "Negative", or "Zero"
# number = 0
# if number >= 0:
#     print("Positive")
# else:
#     print("Negative")


# Write if-elif-else:
# >=90 → "Grade A", >=75 → "Grade B", >=60 → "Grade C", else → "Fail"
# marks = 85
# if marks >= 90:
#     print("Gradel A")
# elif marks >= 75:
#     print("Gradel B")
# elif marks >= 60:
#     print("Gradel C")
# else:
#     print("Fail")



# Write match-case to print:
# Monday → "Start of week"
# Friday → "End of week"
# _ → "Midweek"
# day = "Monday"
# match day:
#     case "Monday":
#         print("Start of week")
#     case "Friday":
#         print("End of week")
#     case _:
#         print("Midweek")



# # Write if-else to print "Teenager" if 13-19, else "Not a Teenager"
# age = 15
# if age >= 13 and age <= 19:
#     print("Teenager")
# else:
#     print("Not teenage") 



# if num < 20 → "Small"
# elif num <= 50 → "Medium"
# else → "Large"

# num = 50
# if num < 20:
#     print("small")
# elif num <= 50:
#     print("medium")
# else:
#     print("large")



# match-case to print:
# "Apple" → "Red"
# "Banana" → "Yellow"
# _ → "Unknown"

# fruit = "apple"
# match fruit:
#     case "apple":
#         print("red")
#     case "Banana":
#         print("yellow")
#     case _:
#         print("unknown")


# for i in range(50):
#     print(i)

# a = ["apple", "baanaana", "grapes"]
# for b in a:
#     print(b)

# a = 1

# while a <= 8:
#     print(a)
#     a +=1


# for i in range(10):
#     pass
#     print(i)


# fruits = ["apple", "banana", "cherry"]
# for item in fruits:
#     print(item)

# for i in range(len(fruits)):
#     print(i, fruits[i])

# i = 0 
# while i < len(fruits):
#     print(fruits[i])
#     i+=1




# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])   # apple
# print(fruits[-1])  # cherry (negative index → from end)
# print(fruits[0:2])  # ['apple', 'banana']
# print(fruits[:2])   # same as above
# print(fruits[1:])   # ['banana', 'cherry']
# print(fruits[:3])
 

# numbers = [10, 20, 30]
# # numbers[1] = 200
# numbers[0:2] = [100, 200]
# print(numbers)   # [10, 200, 30]


# fruits = ["apple", "banana"]
# fruits.append("cherry")
# fruits.insert(0, "orange")
# fruits.extend(numbers)
# print(fruits)   # ['apple', 'banana', 'cherry']


# num = [1, 2, 3, 4, 5]
# sqare = []
# for i in num:
#     sqare.append(i ** 2)
# print(sqare)


# sqare = [x**2 for x in [1, 2, 3, 5]]
# print(sqare)

# even = [x for x in range(20) if x % 2 == 0]
# print(even)

# nums = [1, 2, 2, 3, 4, 5, 6, 90, 8, 9, 10]
# nums.sort()
# print(nums)



# fruits = ["apple", "banana", "cherry"]
# for x in fruit:
#     print()
# new = [x.upper()for x in fruits ]
# print(new)



# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1]= "orange"
# z = tuple(y)
# print(z)

# nested = (1, 2, (3, 4),(4,5))
# print(nested[3][1]) 

# fruits = {"apple", "banana", "cherry"}
# for item in fruits:
#     print(item)


# if "apple" in fruits:
#     print("Apple is present")



# my_list = {2,2,3,3,4}
# my_list.add(6)
# print(my_list)


# fruits = {"apple", "banana", "cherry"}
# fruits.discard("mango")
# print(fruits)


# fruits = {"apple", "banana", "cherry"}
# removed = fruits.pop()
# print("Removed:", removed)




# A = {1, 2, 3, 4}
# B = {3, 4}
# print(A.issuperset(B))



# X = {10, 20}
# # Y = {30, 40}
# # print(X.union(Y)) 

# d = X.copy()
# print(d)



# _Me = {
#     "name": "Salman",
#     "age": 21,
#     "city": "Kozhikode"
# }
# print(_me["name"])
# print(me.get("age"))



# _Me = {
#     "name": "Salman",
#     "age": 21,
#     "city": "Kozhikode"
# }
# # _Me["age"] = 45
# # _Me.update({"age":56,"city":"malpppuram"})
# # print(_Me)


# _Me = {
#     "name": "Salman",
#     "age": 21,
#     "city": "Kozhikode"
# }

# _Me["grade"]= "A"
# _Me.update({"email":"salman@gmail.com"})
# print(_Me)


# _Me = {
#     "name": "Salman",
#     "age": 21,
#     "city": "Kozhikode"
# }
# # _Me.pop("name")
# _Me.popitem()
# print(_Me)


# _Me = {
#     "name": "Salman",
#     "age": 21,
#     "city": "Kozhikode"
# }

# # for key in _Me:
# #     print(key)
# # for value in _Me.values():
# #     print(value)

# # for key, value in _Me.items():
# #     print(key,":", value)



# A = {}
# for x in range(5):
#     A[x] = x + 1
# print(A) # it is a normal way 


#using comprehension

# A = {x: x*x for x in range(5)}
# print(A)

# A = {x: x*x for x in range(5) if x % 2 == 0}
# print(A)



# a = {"name": "salman"}
# a.setdefault("age", 9)
# print(a)

# s = "PythonProgramming"
# print(s[::2])


# s = "Python"
# s_new = "J" + s[1:]
# print(s_new)     


# first = "Hello"
# second = "World"
# result = first + " " + second
# print(result)  # Hello World



# name = "Salman"
# greeting = f"Hello, {name}!"
# print(greeting)


# name = "salman"
# age = 18
# greeting = f"hello. {name} , {age}"
# print(greeting)


# my_str =  "Salman"
# print(my_str[2:])


# My_str = "salman"
# new_str = "Muhammed" + " " + My_str + " " + "Faris"
# print(new_str)

# my_name = "sakman"
# new_name = my_name.replace("k" ,"l")
# print(new_name)



# name = " hello salman "

# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.strip())
# print(name.split())
# print("-".join(name))
# print(name.find("s"))
# print(name.count("a"))
# print(name.startswith(" "))
# print("salman".isalpha())
# print("123".isdigit())
# print(" ".isspace())




# def greet ():
#     print("hellloooo")
# greet()



# def greet_user(name):
#     print("Hello", name)

# greet_user("salman")  

# def add(a, b):
#     print(a + b)

# add(500,9000)


# def show_names(*name):
#     print("Names = ", name)

# show_names("salman", "nafila", " asnif")  



# def total_sum(*nums):
#     print(sum(nums))

# total_sum(10, 20, 50)
# total_sum(10, 20, 50)




# def info(name, age):
#     print("Name:", name)
#     print("Age:", age)

# info(name="salman", age=20)



# def stdnt_details(**info):
#     print("Student info:", info)

# stdnt_details(name="Salman", age=18, place= "Kozhikkode")


# def demo(*arg, **kwargs):
#     print("Positional args:", arg)
#     print("Keyword args:", kwargs)

# demo(1,2,3, name="salman", age=35)

# def demo (**kwarg):
#     for i, k in kwarg.items():
#         print(f"{i}:{k}")

# demo(salman="pizza", nafila="momos")



# def factorial(n):
#     if n == 0: # base case
#         return 1
#     else:
#         return n * factorial(n-1) # recurcive call

# print(factorial(5))



# a = lambda a, b : a + b
# print(a(6,5))

# square = lambda x : x*x
# print(square(2))



# nums = [1, 2, 3, 4, 5]

# square = list(map(lambda x : x*x, nums))
# print(square)

# even = list(filter(lambda x : x % 2 == 0, nums))
# print(even)



# import my_modules

# my_modules.greet("salman")


# import math

# print(math.sqrt(16))



# from math import sqrt, pi
# print(sqrt(16))
# print(pi)


# import math as m
# print(m.sqrt(12))


# from random import randint, choice
# print(randint(1, 108980))
# print(choice([1,2,3,4,5]))

# import datetime
# now = datetime.datetime.now()
# print(now)


# import os
# print("current", os.getcwd())


# import sys
# print("python version:", sys.api_version)



# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divided bt zero!")

# try:
#     num = int("abc")
# except:
#     print("sotmhtonog went wroneg")

try:
    num = int("abc")
except ValueError:
    print("Invalid imput")
else:
    print(num)
