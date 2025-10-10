# class Parent:
#     def show_parent(self):
#         print("This is parent class")

# class Child(Parent):
#     def show_child(self):
#         print("This is Child class")

# c1 = Child()
# c1.show_parent()
# c1.show_child()


class Parent:
    def __init__(self):
        print("parent class constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class constructor")

obj = Child()