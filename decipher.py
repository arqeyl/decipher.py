arrangement = 'Enter cipher arrangement: '
keyword = 'Enter cipher to decode: '
array_a = [] # arrangement
array_c = [] # keyword


def _enter_arrangement():
    x = input(arrangement)
    for i in x:
        array_a.append(i)
    _enter_keyword()


def _enter_keyword():
    y = input(keyword)
    for i in y:
        array_c.append(i)
    print('Cipher (to ABC) decoded; answer: ' + _decipher_keyword(array_c, array_a, _true_alphabetical_order()))
    print('Cipher (from ABC) decoded; answer: ' + _decipher_keyword(array_c, _true_alphabetical_order(), array_a))
    print('Cipher () decoded; answer: ' + _decipher_keyword_index_order())
    print('Cipher (ASCII) decoded; answer: ' + _decipher_keyword_to_ascii())
    print('Cipher (binary) decoded; answer: ' + _decipher_keyword_to_binary())


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
    for j in range(0,len(_key_ascii)):
        answer.append(array_a[_key_ascii[j]-66])
    return _deciphered_answer(answer)


def _decipher_keyword_to_ascii():
    x = []
    for i in range(0,len(array_c)):
        x.append(ord(array_c[i])) # ord() takes character in unicode and translate to integer; P = 80; Q = 81; etc.
    return _deciphered_answer(str(x))


def _decipher_keyword_to_binary():
    x = []
    for i in range(0,len(array_c)):
        x.append(bin(ord(array_c[i]))) # bin() change an int or a converted string to ord() to a binary code
    return _deciphered_answer(str(x))


def _true_alphabetical_order():
    a = []
    for i in range(0,26):
        a.append(chr(65+i)) # get from A to Z from ascii 
    return a


def _convert_keyword_to_ascii():
    x = []
    for i in range(0,len(array_c)):
        x.append(ord(array_c[i])) # ord() takes character in unicode and translate to integer; P = 80; Q = 81; etc.
    return x


def main():
    _enter_arrangement()
    

main()
