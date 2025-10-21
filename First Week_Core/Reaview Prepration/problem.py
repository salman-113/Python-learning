# 1. Reverse string
# Problem: Reverse "hello" without slicing

# s = "HELLO"
# rev = ""
# for i in s:
#     rev = i + rev

# print(rev)


# 2. Count Vowels
# Problem: Count vowels in "programming".

# s = "Programming"
# vowels = "aeiou"
# count = 0
# for i in s:
#     if i in vowels:
#         count += 1

# print("Vowel Count:", count)


# 3. Even or Odd
# Problem: Check if number is even or odd.

# num = 8 
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")


# 4. Sum of List
# Problem: Find sum of [1,2,3,4] without sum().

# nums = [1, 2, 3, 4, 5]
# total = 0 
# for n in nums:
#     total += n
# print(total)


# 5. Print Numbers with Break & Continue
# Problem: Print 1–20, skip multiples of 3, stop if number is 15.

# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     if i == 15:
#         break
#     print(i, end="/")


# 6. Access Nested Dictionary
# Problem: From

# student = {"name": "Ali", "marks": {"math": 80, "science": 90}}

# print(student["marks"]["science"])


# 7. Word Frequency
# Problem: Count words in "this is is a test".

# text = "I am am Muhammed Salman Faris"
# words = text.split()
# freq = {}
# for w in words:
#     freq[w] = freq.get(w, 0) +1
# print(freq)
# print(words)


# Find Largest Number
# Problem: Find largest in [3,6,2,8].

# nums = [3, 5, 7, 89, 447, 462]
# largest = nums[0]
# for n in nums:
#     if n > largest:
#         largest = n
# print("Largest:", largest)


# 9. Palindrome Check
# Problem: Check if "madam" is palindrome.

# s = "MALAYALAM"
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")
    

# 10. Factorial using Loop
# Problem: Find factorial of 5

# num = 5
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print("Factorial:", fact)