#ask a user for input

name = input("What is your name?")

#Remove whitespace from a str and capitalizing

name = name.strip().title()

#Split's name into first and last name
first, last = name.split(" ")

#print the output
# print("Hello", name)

#format string

print(f"Hello, {first}")