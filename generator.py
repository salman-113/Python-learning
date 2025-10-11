def numbers(limit):
    num = 0
    while num < limit:
        yield num
        num += 1

for n in numbers(5):
    print(n)