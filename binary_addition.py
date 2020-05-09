import binary_conversion
import gates

def binary_addition_func(a, b):
    print()
    print()
    a_bin = binary_conversion.dec_to_bin(a) #is a list for proper binary placement
    print()
    b_bin = binary_conversion.dec_to_bin(b) #is a list
    
    carry = []
    final_before_reverse = []
    final = []
    
    #For the half adder - let's take out the last digits from the lists a_bin and b_bin
    #XOR gate for the last digit
    # Sum = A XOR B , Co = A AND B
    
    sum_1 = gates.XOR(a_bin[-1], b_bin[-1])

    carry_1 = gates.AND(a_bin[-1], b_bin[-1])
    carry_in = carry_1
    final_before_reverse.append(sum_1)
    print()
    
    #For the full adder - remaining seven places has to be added with a carry over too
    # Sum = A XOR B XOR C
    # Co = Cin AND ( A XOR B) + A AND B
    Co = 0
    for i in range(-2, -9, -1):
        sum_all = gates.XOR(carry_in, gates.XOR(a_bin[i],b_bin[i]))
        final_before_reverse.append(sum_all)

        Co = gates.OR(gates.AND(a_bin[i], b_bin[i]), gates.AND(carry_in, gates.XOR(a_bin[i],b_bin[i])))
        
        carry_in = Co

    print("Result in Binary : ", end = " ")

    for numbers in final_before_reverse[::-1]: #slicing
        final.append(numbers)
        print((numbers), end = " ")
    binary_conversion.bin_to_dec(final)
    return(final)

    
        

