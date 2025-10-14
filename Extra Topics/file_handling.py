# File handling
#its used to read and write data to files

# f = open("demo2.txt", "w")
# f.write("This is my first file.\n")
# f.write("iam salmn")
# f.close()
# print(f)


# f = open("marks.txt", "w")
# f.write("Name: Salman\nScore: 95")
# f.close()

# f2 = open("marks.txt", "r" )
# data = f2.read()
# print(data)
# f2.close()

# f1 = open("marks.txt", "a")
# f1.write("I am writing new thing for study\n")
# f1.close()

# 1️⃣ Write to a file (creates new file or overwrites existing one)

# f = open("myfile.txt", "w")
# f.write("Hello! This is my first file.\n")
# f.write("I am learning file handling in Pyhton.\n")
# f.close()

# # 2️⃣ Read the file content

f1 = open("myfile.txt", "r")
# data = f1.read()
# print(data)
# f1.close()

# # 3️⃣ Append more data to the file

# f2 = open("myfile.txt", "a")
# f2.write("This is now i added for append learnig\n")
# f2.close()


# 4️⃣ Use 'with open()' for safe reading

# with open("myfile.txt", "r") as f:
#     for line in f:
#         print(line.strip())


# line1 = f1.readline()
# print(line1.strip())
# f1.close()

# lines = f1.readlines()
# f1.close()
# print(lines)

# for line in lines:
#     print(line.strip())