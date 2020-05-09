def dec_to_bin(dec_no):
    binary_reverse = []
    binary = []   
    
    # to display number as a byte ie 8 digits
    for i in range(8):
        rem = dec_no % 2
        binary_reverse.append(rem) #named binary_reverse because final result is the reverse of this
        dec_no = int(dec_no / 2)
    print("Binary Equivalent :", end = " ")
    for numbers in binary_reverse[::-1]: #slicing for reverse
        binary.append(numbers) 
        print((numbers), end = " ") #end = " " is placed because we need to display the result in same line
        
    return(binary)
    print()
    
def bin_to_dec(binary):
    num = 0
    ini = 0
    sum1 = 0
    print()
    for i in binary[::-1]:        
        num = 2**(ini) * i
        sum1 = sum1 + num
        ini = ini + 1
    print("Result in integer: ", sum1)
    return sum1
        
