# lomani
def encode(password): # encode a string and set each digit in string + 3
    string = "" # initialize string
    for i in password: # loop through each digit of password
        if int(i) + 3 > 9: # check if the sum is greater than 9
            string = string + str((8 - int(i) + 3)) # add 3 up to 9 and then start again at 0
        else: # if the sum is not greater than 9
            string = string + str((int(i) + 3)) # add 3 to digit
    return string

def decode(password):
    result = ''  # Initialize an empty string to store the decoded message
    for digit in password:  # Iterate through each character in the message
        new_digit = str((int(digit) - 3) % 10)  # Convert the character to integer, subtract 3, and take the modulo 10
        result += new_digit  # Append the decoded digit to the result string
    return result  # Return the decoded message

def main():
    quit = False # initialize variable to check if user has quit
    while quit == False: # loop until user has selected option 3
        print("Menu" # print menu
              "\n-------------"
              "\n1. Encode"
              "\n2. Decode"
              "\n3. Quit\n")
        user_option = input("Please enter your option: ") # retrieve user option
        if user_option == "1": # if user selects option 1
            password = input("Please enter your password to encode: ") # retrieve and initial password with user input
            password = encode(password) # encode password and update it to the variable
            print("Your password has been encoded and stored!\n") # print message
        if user_option == "2": # if user selects option 2
            decoded_password = decode(password) # decode password and initialize it with the variable
            print(f"The encoded password is {password}, and the original password is {decoded_password}.\n") # print message
        if user_option == "3": # if user selects option 3
            quit = True # quit loop

if __name__ == "__main__":
    main()
