number = 100
while number > 0:
    print("number", number)
    number = number//2  # integer divide

command = ""
while command != "quit" and command != "QUIT":
    # while command
    command = input(">> ")
    print("ECHO ", command)
