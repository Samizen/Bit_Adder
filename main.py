import binary_conversion
import binary_addition
import validity

repeat = True
valid_input_a = False
valid_input_b = False

#Whole program repeats until repeat is True
while (repeat == True):
    while(valid_input_a == False):
        try:
            a = int(input("Enter first number: "))
            validity.number_validation(a)
            binary_conversion.dec_to_bin(a) #is a list for proper binary placement in 8
            valid_input_a = True
        except:
            print("Invalid Input. Please enter an integer between 0 to 255")
        
    print()

    while(valid_input_b == False):
        try:
            b = int(input("Enter second number: "))
            validity.number_validation(b)
            binary_conversion.dec_to_bin(b) #is a list
            valid_input_b = True
        except:
            print("Invalid Input. Please enter an integer")
            

    binary_addition.binary_addition_func(a, b)

    print()
    print()

    # validity of input is reset if the user wants to try again
    valid_input_a = False
    valid_input_b = False
    user_reply = input("Do you wish to continue? Press Y for Yes and any other keys for No: ")
    if(user_reply == "Y" or user_reply == "y"):
        repeat = True
    else:
        repeat = False
        break
