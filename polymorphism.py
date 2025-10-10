# “Poly” = many, “Morph” = forms
# ➡️ Polymorphism means one thing behaving in many forms.


# Example 1: Polymorphism with Functions and Objects

# class Dog:
#     def speak(self):
#         return "Woof !"
    
# class Cat:
#     def speak(self):
#         return "Meow !"

# # same method name, different behavior    
# animals = [Dog(), Cat()]

# for animal in animals:
#     print(animal.speak())
# Here, both classes have speak() — same name, different results → Polymorphism




# Example 2: Polymorphism with Inheritance (Method Overriding)

# class Bird:
#     def fly(self):
#         print("Birds can fly")

# class Penguin(Bird):
#     def fly(self):  # overriding
#         print("Penguins cannot fly")

# p1 = Bird()
# p2 = Penguin()

# p1.fly()
# p2.fly()
# fly() behaves differently for each class — that’s runtime polymorphism.



