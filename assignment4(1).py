# 3 Write a Python program to append text to a file and display the text.
f = open("myfile1.txt",'r')
print(f.read())
f.close()
print("---------------------------------------------------")

# 4 Write a Python program to read first n lines of a file.
f = open("myfile1.txt",'r')
print(f.readline())
f.close()
print("---------------------------------------------------")

# 5 Write a Python program to read last n lines of a file.
f = open("myfile1.txt",'r')
print(f.readlines(2))
f.close()
print("--------------------------------------------------")

# 6 Write a Python program to read a file line by line and store it into a list.
f = open("myfile1.txt",'r')
print(f.readlines())
f.close()
print("--------------------------------------------------")

# 7 Write a Python program to read a file line by line store it into a variable.
f = open("myfile1.txt",'r')
name=(f.readlines())
f.close()
print("---------------------------------------------------")

# 8 Write a python program to find the longest words.
f = open("myfile1.txt",'r')
name=(f.readlines())
print(name)
f.close()
