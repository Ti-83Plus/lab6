#Name: Josh Gallardo
#lab6.py

"""
The password encoder should take in an 8-digit password in string format containing only integers. 
After passing the password into the encoder, the encoder stores the encoded password to a new 
variable, with each digit being shifted up by 3 numbers.
"""

def encoder(user_pwd):
    integer_list.append(int(user_pwd))
    for i in range():
        integer_list[i] += 3
    print(integer_list)




if __name__ == "__main__":

    
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
            user_pwd = int(input())
            encoder(user_pwd)
            print("Your password has been encoded and stored!")
        elif user_choice == 2:
            pass

        elif user_choice == 3:
            break
        else:
            print("Please enter a valid input. ")
            pass

    