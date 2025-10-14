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

f = open("marks.txt", "r")
data = f.read()
print(data)
f.close()

