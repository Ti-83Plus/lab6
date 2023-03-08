#Name: Josh Gallardo
#lab6.py

"""
The password encoder should take in an 8-digit password in string format containing only integers. 
After passing the password into the encoder, the encoder stores the encoded password to a new 
variable, with each digit being shifted up by 3 numbers.
"""

def encoder(user_pwd):

    my_dict = {"0":3, "1":4, "2":5, "3":6, "4":7, "5":8, "6":9, "7":0, "8":1, "9":2 }

    result = ""
    for index in user_pwd:
        my_array = my_dict[index]
        result = result + str(my_array) 
    return(result)


# Geoffrey Clark's decoder
def decoder(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        unshifted_digit = str((int(digit)-3) % 10)
        decoded_password += unshifted_digit
    return decoded_password


def menu():

    integer_list = []
    while(True):
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit ")
        print()
        print("Please enter an option:")
        user_choice = int(input())

        if user_choice == 1:
            print("Please enter your password to encode: ")
            user_pwd = input()
            encoderValue = encoder(user_pwd)

            print("Your password has been encoded and stored!")
        elif user_choice == 2:
            decodedvalue = decoder(encoderValue)
            print(f"The encoded password is {encoderValue}, and the original password is {decodedvalue}.")

        elif user_choice == 3:
            break




        #print("The encoded password is", result,"and the original password is", user_pwd,".", end="")
        else:
            print("Please enter a valid input. ")
            pass

if __name__ == "__main__":
     menu()


