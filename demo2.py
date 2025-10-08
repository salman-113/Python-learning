# try:
#     file = open("test.txt", "r")
# except FileNotFoundError:
#     print("file not found")
# finally:
#     print("this always runs")



# def divide(a, b):
#     try:
#         reslt = a / b
#     except ZeroDivisionError:
#         print("Error: cannot divide by zero")
#     except TypeError:
#         print("Error: Inputs must be numbers")
#     else:
#         print("Division successful",  reslt)
#     finally:
#         print("Execute finished")

# # divide(10, 2)
# # divide(10, 0)
# divide(10, "a")

# def outer():
#     message = "Hello"

#     def inner():
#         print(message)
        
#     return inner

# a = outer()
# a()


# def decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#     return wrapper

# @decorator
# def say_hello():
#     print("Hello!")

# say_hello()
