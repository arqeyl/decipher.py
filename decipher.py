from os import system, name

array_a = [] # arrangement
array_c = [] # keyword

roman_to_int = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
        }

#       result = 0
#       prev = 0
#       for c in s:
#           current = roman_to_int[c]
#           result += current
#           if current > prev:
#               result -= 2 * prev
#           prev = current
#       
#       return result
#


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def query(qu):
    while True:
        cli_input = input(qu)
        Fl = cli_input[0].lower()
        if cli_input == '' or not Fl in ['y','n']:
            print('Please respond with [Y]yes or [n]no!')
        else:
            return Fl
            break


def query_alphabet(qu):
    while True:
        Fl = ""
        cli_input = input(qu)
        for char in cli_input:
            Fl += char.upper()
        if cli_input == '' or not Fl.isalpha():
            print('Please respond without numbers nor symbol! Only alphabetic letters!')
        else:
            return Fl
            break

def query_morsecode(qu): 
    while True:
        cli_input = input(qu)
        if cli_input == '' or not cli_input == ['.', '_']: # this may convey an error, make the program look back to the morse code dictionary to verify correctness
            print('Please respond without numbers nor symbol! Only alphabetic letters!')
        else:
            return cli_input
            break


def _request_arrangement():
    clear()
    qinput = "\n> Do you need to decipher with arrangement? [Y/n] "
    reply = query(qinput)
    if reply == "y":
        _enter_arrangement()
    elif reply =="n":
        _request_alternative()


def _request_alternative():
    clear()
    while True:
        cli_input = input("\n"
            "Decipher [Plain Text]         type [0]\n"
            "Decipher [Binary]             type [1]\n"
            "Decipher [Morse Code]         type [2]\n"
            "Decipher [Integer to Roman]   type [3]\n"
            "Decipher [Roman to Integer]   type [4]\n\n"
            "> Select choices to decipher or convert to 'ciphertext': "
        )
        if cli_input == '' or int(cli_input) not in range(0,5): 
            print("Please respond correctly!")
        else:
            break
    
    if int(cli_input) == 0:
        _alternative_plain_text()
    if int(cli_input) == 1:
        _alternative_binary()
    if int(cli_input) == 2:
        _alternative_morse_code()
    if int(cli_input) == 3:
        _alternative_roman_to_int()
    if int(cli_input) == 4:
        _alternative_int_to_roman()


def _alternative_plain_text():
    clear()
    _enter_keyword()
    print(
    '\nCipher (ASCII) decoded;              answer: ' + _deciphered_answer(str(_convert_keyword_to_ascii())) +
    '\nCipher (binary) decoded;             answer: ' + _convert_keyword_to_binary() +
    '\nCipher (morse code) decoded;         answer: ' + _convert_keyword_to_morse_code()
    )


def _alternative_binary():
    clear()
    _enter_keyword()
    print("binary")


def _alternative_morse_code():
    clear()
    _convert_morse_code_to_plaintext()


def _alternative_roman_to_int():
    clear()
    print("romantoint")


def _alternative_int_to_roman():
    clear()
    print("inttoroman")


   
def _enter_arrangement():
    clear()
    arrangement = '\n> Enter cipher arrangement: '
    qinput = query_alphabet(arrangement)
    for char in qinput:
        array_a.append(char)
    _enter_keyword()
    print(
    '\nCipher (to ABC) decoded;             answer: ' + _decipher_keyword(array_c, array_a, _true_alphabetical_order()) +
    '\nCipher (from ABC) decoded;           answer: ' + _decipher_keyword(array_c, _true_alphabetical_order(), array_a) +
    '\nCipher (from arrangement) decoded;   answer: ' + _decipher_keyword_index_order() +
    '\nCipher (ASCII) decoded;              answer: ' + _deciphered_answer(str(_convert_keyword_to_ascii())) +
    '\nCipher (binary) decoded;             answer: ' + _convert_keyword_to_binary() +
    '\nCipher (morse code) decoded;         answer: ' + _convert_keyword_to_morse_code()
    )


def _enter_keyword():
    keyword = '\n> Enter cipher to decode: '
    qinput = query_alphabet(keyword)
    for char in qinput:
        array_c.append(char)


def _deciphered_answer(answer):
    out = ''
    for m in answer:
        out+=m
    return out


def _decipher_keyword(arrange1, arrange2, arrange3):
    ans = []
    answer = []
    for i in range(0,len(arrange1)):
        for j in range(0,len(arrange2)):
            if arrange1[i] == arrange2[j]:
                ans.append(j)
    for k in range(0,len(ans)):
        answer.append(arrange3[ans[k]])
    return _deciphered_answer(answer)


def _decipher_keyword_index_order():
    _key_ascii = _convert_keyword_to_ascii()
    answer = []
    for i in range(0,len(_key_ascii)):
        answer.append(array_a[_key_ascii[i]-66])
    return _deciphered_answer(answer)


def _true_alphabetical_order():
    a = []
    for char in range(0,26):
        a.append(chr(65+char))  
    return a


def _convert_keyword_to_ascii():
    x = []
    for char in range(0,len(array_c)):
        x.append(ord(array_c[char])) # ord() takes character in unicode and translate to integer; P = 80; Q = 81; etc.
    return x


def _convert_keyword_to_binary():
    x = []
    y = ''
    for char in range(0,len(array_c)):
        binary = bin(ord(array_c[char]))[2:]
        x.append(binary) 
    for char in x:
        y += char+" "
    return _deciphered_answer(y.strip())


def _convert_keyword_to_morse_code():
    string = ""
    x = ""
    for char in array_c:
        string += char.upper()
    for char in string:
        if char in morse_code:
            x += morse_code[char]+" "
    return x.strip()


def _convert_morse_code_to_plaintext():
    rev_mc = {v:k for k,v in morse_code.items()} # reverse morse code dict, char to morse
    
    morse_list = morse_str.split()

    text_list = [rev_mc.get(morse, morse) for morse in morse_list]

    text_str = ''.join(text_list)

    return text_str



def main():
    _request_arrangement()
    

main()
