def ceaser_shift(s,shift):
    shift=shift%26
    out=""
    for i in s:
        case=i.islower()
        if not i.isalpha():
            out+=i
            continue
        new=ord(i.lower())+shift
        if not chr(new).islower():
            new-=26
        if not case:
            out += chr(new).upper()
        else:
            out+=chr(new)
    return out

def vigenere(s,key):
    out=""
    for i in range(len(s)):
        if not (key[i%len(key)].isalpha() and s[i].isalpha()):
            out+=s[i]
            continue
        out+=ceaser_shift(s[i],(ord(key[i%len(key)].lower())-ord('a')))
    return out

def decode_vigenere(s,key):
    out=""
    for i in range(len(s)):
        if (key[i%len(key)].isalpha() and s[i].isalpha()):
            out+=s[i]
            continue
        out+=ceaser_shift(s[i],-(ord(key[i%len(key)].lower())-ord('a')))
    return out

def decode_autokey(s,key):
    out=""+key
    for i in range(len(s)):
        if not (key[i%len(key)].isalpha() and s[i].isalpha()):
            out+=s[i]
            continue
        out+=ceaser_shift(s[i],-(ord(out[i].lower())-ord('a')))
    return out[len(key):]

def autokey(s,key):
    nkey=key+s
    return vigenere(s,nkey)

while(1):
    print('''
    What do you want to perform?
    1     : Encrypt
    2     : Decrypt
    other : Exit
    ''')
    inp=input()
    if inp=='1':
        print('''
        Which Cipher to Encrypt
        1     : Vigenere
        2     : Autokey
        other : Exit
        ''')
        inp = input()
        if inp=='1':
            plaintext = input("Enter Plaintext:")
            key = input("Enter Key:")
            print(f"Encrypted Text is: {vigenere(plaintext, key)}")
        elif inp=='2':
            plaintext = input("Enter Plaintext:")
            key = input("Enter Key:")
            print(f"Encrypted Text is: {autokey(plaintext, key)}")
        else:
            continue
    elif inp=='2':
        print('''
                Which Cipher to Decrypt
                1     : Vigenere
                2     : Autokey
                other : Exit
                ''')
        inp = input()
        if inp == '1':
            plaintext = input("Enter Plaintext:")
            key = input("Enter Key:")
            print(f"Decrypted Text is: {decode_vigenere(plaintext, key)}")
        elif inp == '2':
            plaintext = input("Enter Plaintext:")
            key = input("Enter Key:")
            print(f"Decrypted Text is: {decode_autokey(plaintext, key)}")
        else:
            continue
    else:
        print("Exiting...")
        break
