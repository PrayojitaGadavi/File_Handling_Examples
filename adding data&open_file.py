files = open("first.txt", "a")

files.write("\n This one more adding data in file")

files.close()

f = open("first.txt", "r")

print(f.read())