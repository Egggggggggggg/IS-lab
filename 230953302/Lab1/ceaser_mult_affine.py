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

def multiplicative(s,mult):
    out=""
    for i in s:
        case=i.islower()
        if not i.isalpha():
            out+=i
            continue
        shift=((ord(i.lower())-ord('a'))*mult)%26
        new = ord('a') + shift
        if not case:
            out += chr(new).upper()
        else:
            out += chr(new)
    return out

def affine(s,a,b):
    return multiplicative(ceaser_shift(s,b),a)

def modInverse(A, M):
    for i in range(M):
        if (((A % M) * (i % M)) % M == 1):
            return i
    return 0

print(-1%26)
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
        1     : Ceaser
        2     : Multiplicative
        3     : Affine
        other : Exit
        ''')
        inp = input()
        if inp=='1':
            plaintext = input("Enter Plaintext:")
            key = int(input("Enter Key:"))
            print(f"Encrypted Text is: {ceaser_shift(plaintext, key)}")
        elif inp=='2':
            plaintext = input("Enter Plaintext:")
            key = int(input("Enter Key:"))
            print(f"Encrypted Text is: {multiplicative(plaintext, key)}")
        elif inp=='3':
            plaintext = input("Enter Plaintext:")
            key1 = int(input("Enter Key 1:"))
            key2 = int(input("Enter Key 2:"))
            print(f"Encrypted Text is: {affine(plaintext, key1,key2)}")
        else:
            continue

    elif inp=='2':
        print('''
        Which Cipher to Decrypt
        1     : Ceaser
        2     : Multiplicative
        3     : Affine
        other : Exit
        ''')
        inp = input()
        if inp=='1':
            plaintext = input("Enter Ciphertext:")
            key = int(input("Enter Key:"))
            print(f"Decrypted Text is: {ceaser_shift(plaintext, -key)}")
        elif inp=='2':
            plaintext = input("Enter Ciphertext:")
            key = int(input("Enter Key:"))
            print(f"Decrypted Text is: {multiplicative(plaintext,modInverse(key,26))}")
        elif inp=='3':
            plaintext = input("Enter Ciphertext:")
            key1 = int(input("Enter Key 1:"))
            key2 = int(input("Enter Key 2:"))
            print(f"Decrypted Text is: {affine(plaintext,modInverse(key1,26),-key2)}")
        else:
            continue
    else:
        print("Exiting...")
        break
