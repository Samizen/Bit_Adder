import binary_conversion

def number_validation(a):
    valid = False
    while valid != True:
        if a < 0 or a > 255:
            clear(a)
            a = int(input("Enter the number between 0 and 255 again: "))            
        else:
            valid = True
