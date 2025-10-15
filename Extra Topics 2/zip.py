# zip() combines two (or more) iterables element by element — like pairing socks! 🧦

# names = ["Salman", "Nafila", "Asnif"]
# ages = [19, 18, 17]

# # zipped = zip(names, ages)
# # print(list(zipped))

# # Using inside a dictonary 

# result = {name: ages for name, ages in zip(names, ages)}
# print(result)


products = ["Apple", "Banana", "Mango"]
prices = [100, 60, 180]

discounted = {p: price * .9 for p, price in zip(products, prices)}
print(discounted)