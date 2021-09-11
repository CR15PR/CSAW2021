
solve = "1010000011111000101010101000001010100100110110001111111010001000100000101000111011000100101111011001100011011000101011001100100010011001110110001001000010001100101111001110010011001100"

flag = "AAAABBBBCCCCDDDDEEEEFFF"
print("len ", len(flag))

def up(x):
    print("x is ", x) # still same as input
    x = [f"{ord(x[i]) << 1:08b}" for i in range(len(x))]     # bit shift right 1
    return ''.join(x) #return as a string

def down(x):
    #print(x)
    x = ''.join(['1' if x[i] == '0' else '0' for i in range(len(x))])
    #print(x)
    return x

def right(x,d):
    # d = 24, x = our binary string after bitshift
    x = x[d:] + x[0:d]
    return x

def left(x,d):
    print(len(x)) #184
    x = right(x,len(x)-d) # another swap, but instead of on d it's on length-d
    print(x)
    print(x[::-1])
    return x[::-1] # puts it backwaards

def encode(plain):
    d = 24
    #print(plain) # flag len should be 23
    x = up(plain) #converts to binary and shifts left one bit
    x = right(x,d) #takes a slice from 24: and swaps it
    x = down(x) #flip all the bits 0 to 1 or 1 to 0
    x = left(x,d) #swaps on position 160 and then returns string backwards
    return x


encoded = encode(flag)
print("What does this mean?")

print(encoded)
print("solve string")
print(solve)
