# class Student:
#     def __init__(self, name, age):
#         self.name = name  # public variable
#         self.__age = age  # private variable (using__)

#     # getter method
#     def get_age(self):
#         return self.__age
    
#     # setter method 
#     def set_age(self, age):
#         if age > 0:
#             self.__age = f"age is modified with {age}"
#         else:
#             print("Invalid age")

# # create object
# s = Student("Alex", 21)

# print(s.name)        # ✅ accessible
# # print(s.__age)     # ❌ Error: can't access directly

# print(s.get_age())   # ✅ Access via getter

# s.set_age(2)         # ✅ Modify via setter
# print(s.get_age())


        