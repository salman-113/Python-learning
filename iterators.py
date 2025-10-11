# numbers = [1, 2, 3]

# it = iter(numbers)

# print(next(it))


# class MyNumbers:
#     def __init__(self, limit):
#         self.limit = limit
#         self.num = 0  # start from 0

#     def __iter__(self):
#         return self   # returns the iterator object itself
    
#     def __next__(self):
#         if self.num < self.limit:
#             current = self.num
#             self.num += 1
#             return current
#         else:
#             raise StopIteration  # no more items
        
# numbers = MyNumbers(11)
# for i in numbers:
#     print(i)


