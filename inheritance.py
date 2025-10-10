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



# 1. Single Inheritance

# class Parent:
#     def show_parent(self):
#         print("This is parent class")

# class Child(Parent):
#     def show_child(self):
#         print("This is child class")           

# c = Child()
# c.show_parent()
# c.show_child()


# 2. Multilevel Inheritance
# Child → Parent → Grandparent (chain-like)

# class GrandParent:
#     def show_gp(self):
#         print("This is GrandParent Class")

# class Parent(GrandParent):
#     def show_parent(self):
#         print("This is Parent Class")

# class Child(Parent):
#     def show_child(self):
#         print("This is Child class")     

# c = Child()
# c.show_gp()
# c.show_parent()
# c.show_child()



# 3. Multiple Inheritance
# Child inherits from many parents.

# class Father:
#     def feature1(self):
#         print("Fuature from Father")

# class Mother:
#     def feature2(self):
#         print("Feature from Mother")

# class Child(Father, Mother):
#     def feature3(self):
#         print("Feature from Child")

# c = Child()
# c.feature1()
# c.feature2()
# c.feature3()



# 4. Hierarchical Inheritance
# Many children inherit from one parent.

# class Parent:
#     def show_parent(self):
#         print("This is parent Class")

# class Child1(Parent):
#     def show_child1(self):
#         print("This is Child 1")

# class Child2(Parent):
#     def show_child2(self):
#         print("This is Child 2")

# c1 = Child1()
# c2 = Child2()

# c1.show_parent()
# c2.show_parent()



# 5. Hybrid Inheritance
# A mix of multiple and multilevel inheritance.

# class A:
#    def methodA(self):
#       print("A class") 

# class B(A):
#    def methodB(self):
#       print("B class")

# class C(A):
#    def methodC(self):
#       print("C class")

# class D(B, C):  # Hybrid: inherits from both B and C (which inherit from A)
#    def methodD(self):
#       print("D class")

# obj = D()
# obj.methodA()
# obj.methodB()
# obj.methodC()
# obj.methodD()
# print(D.mro())
# print(D.__mro__) # used to chek order when there are multiple paths