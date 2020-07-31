import sys

if len(sys.argv) != 2:
    print("Enter your name, please")
    sys.exit()

print("Hello, " + sys.argv[1] + "!")
