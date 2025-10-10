# class Parent:
#     def show_parent(self):
#         print("This is parent class")

# class Child(Parent):
#     def show_child(self):
#         print("This is Child class")

# c1 = Child()
# c1.show_parent()
# c1.show_child()


# class Parent:
#     def __init__(self):
#         print("parent class constructor")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child class constructor")

# obj = Child()



# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speake(self):
#         return "Geniric animal sound"     # ➡️ Animal is the parent (base) class
#                                           # ➡️ It has a method speake() (common for all animals).

# class Dog(Animal):
#     def speake(self):
#         return "woof !"

# class Cat(Animal):
#     def speake(self):
#         return "Meow !"    # ➡️ Both Dog and Cat override the parent method speake()
#                            # ➡️ This is called method overriding — a part of polymorphism.

# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# print(dog.name)
# print(dog.speake())
# print(cat.name)
# print(cat.speake())


# ➡️ Each object calls its own version of the method: