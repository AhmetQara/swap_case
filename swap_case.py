def swap_case(s):
    
    my_word = ''

    # [char for char in word]

    for char in s:
        
        if char.islower():
        
            my_word += char.upper()

        elif char.isupper():
            
            my_word += char.lower()
        
        else:
            my_word += char

    return (''.join(my_word))

# short way
#    return s.swapcase()

if __name__ == '__main__':