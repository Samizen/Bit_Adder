#Functions for 3 gates required

def AND(a, b):   
    if a == 1 and b == 1: 
        return 1
    else: 
        return 0

def OR(a, b): 
    if a == 1: 
        return 1
    elif b == 1: 
        return 1
    else: 
        return 0

def XOR(a, b): 
    if a != b: 
        return 1
    else: 
        return 0
