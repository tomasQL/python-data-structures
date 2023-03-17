from stack import Stack

def convert_int_to_bin(dec_num):
    
    if dec_num == 0:
        return 0
    
    s = Stack()
    while dec_num > 0:
        resto = dec_num % 2
        s.push(resto)
        #   division entera 
        dec_num = dec_num // 2
    
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
    
    return bin_num

print("El equivalente binario para " + str(233)+" es "+ convert_int_to_bin(4))
print(str(233%2))