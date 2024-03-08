MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Function to encrypt the regular string
def encrypt(message):
    result = ''
    
    for letter in message:
        if letter != ' ':
            result += MORSE_CODE_DICT[letter] + ' '
        else:
            result += ' '

    return result

#Function to decrypt the morse string
def decrypt(message):
    result = ''
    morse_letter = ''
    for letter in message:
        if letter != ' ':
            morse_letter += letter
        else:
            if morse_letter:
                morse_keys = list(MORSE_CODE_DICT.keys())
                morse_values = list(MORSE_CODE_DICT.values())
                result += morse_keys[morse_values.index(morse_letter)]
                morse_letter = ''
            else:
                result += ' '

    return result


if __name__ == '__main__':
    print(encrypt('help me please'.upper()))

    print(decrypt('.... . .-.. .--.  -- .  .--. .-.. . .- ... . '))