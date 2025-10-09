# oops concept learning 

# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def start(self):
#         print(f"{self.color} {self.brand} car is starting......")

# car1 = Car("Toyota", "Red")
# car2 = Car("BMW", "Black")
# car1.start() 
# car2.start()
# print(type(car1))




# class Student:
#     def __init__(self,book):
#         self.book = book

#     def study(self):
#         print(f"The student is studying {self.book}")

# s1 = Student("Textbook")
# s1.study()
# s1.study()




class Developer:
    def __init__(self,name,stack):
        self.name = name
        self.stack = stack

    def Display(self):
        print(f"The {self.name} is a {self.stack} Developer")

dev = Developer("Salman", "Python Full-stack") 
dev.Display()       