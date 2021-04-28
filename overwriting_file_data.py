import fileinput

files = open("one.txt", "w")

files.write("This will overriding all data")

files.close()

files = open("one.txt", "r")

print(files.read())