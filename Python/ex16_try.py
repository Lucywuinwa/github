from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your {filename}:")
print(txt.read())


print("Type the filename again:")
file_again = input("> ")




print(txt_again.read())


