import sys


# print(sys.argv)
# print("Hello", sys.argv[0])

# if len(sys.argv)<2:
#     print("Too few arguments")
# elif len(sys.argv)> 2:
#     print("Too many arguments")
# else:
#     print("Hello", sys.argv[1])


if len(sys.argv)<2:
    sys.exit("Too few arguments")
# elif len(sys.argv)> 2:
#     sys.exit("Too many arguments")

print("Hello", sys.argv[1])

for arg in sys.argv[1:]:
    print("Hello", arg)