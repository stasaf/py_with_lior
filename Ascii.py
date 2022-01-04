
#Ascii
while True:
    user_input = input("Enter key to print (Enter 'q' to quit):\n")
    print("user input was:", user_input)
    print("the value of", user_input, "in ASCII is:", str(ord(user_input)), "\n\n\n")

    if user_input == "q":
        print("Ending program.....bye \n\n\n")
        break