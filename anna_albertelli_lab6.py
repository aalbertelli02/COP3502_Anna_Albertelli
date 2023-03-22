# Takes a string of ints and shifts each int up by 3
def encode(password):
    encoded_pswrd = ""
    for num in password:
        if int(num) < 7:  # If num + 3 does not reach 10
            new_value = int(num) + 3
        elif int(num) >= 7:  # If num + 3 is greater than or equal to 10
            new_value = (int(num) + 3) % 10
        encoded_pswrd += str(new_value)
    return encoded_pswrd


# Takes a string of ints and shifts each int back by 3
def decode(password):
    decode_password = ""
    for num in password:  # iterates through each number in encoded password
        decode_int = (int(num) - 3) % 10  # subtracts 3 to each integer digit, returns a value 0-9 b/c of % 10
        decode_password += str(decode_int)
    return decode_password


# Prints menu options
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def main():
    keep_going = True
    # Runs as long as the user does not select menu choice #3
    while keep_going == True:
        print_menu()
        print()
        menu_choice = int(input("Please enter an option: "))
        if menu_choice == 1:
            pswrd_to_encode = input("Please enter your password to encode: ")
            encoded_pswrd = encode(pswrd_to_encode)
            print("Your password has been encoded and stored!")
            print()
        elif menu_choice == 2:
            print(f"The encoded password is {encoded_pswrd}, and the original password is {decode(encoded_pswrd)}.")
            print()
        elif menu_choice == 3:
            keep_going = False


if __name__ == ("__main__"):
    main()