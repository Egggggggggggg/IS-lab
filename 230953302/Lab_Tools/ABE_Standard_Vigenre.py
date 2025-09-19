import AliceBob as ab
import ParadigmStrings as ps
import string

plaintext=ps.setString("Eve you wont crack this one")
key="no"


def VigenreEncrypt(pt, key):
    pt = str(pt)
    key = key.lower()
    alphabet = string.ascii_lowercase
    encrypted = []

    for i, char in enumerate(pt):
        if char.lower() in alphabet:
            shift = alphabet.index(key[i % len(key)])
            base = 'A' if char.isupper() else 'a'
            enc_char = chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            encrypted.append(enc_char)
        else:
            encrypted.append(char)

    return ps.setString("".join(encrypted))

def VigenreDecrypt(ct, key):
    ct = str(ct)
    key = key.lower()
    alphabet = string.ascii_lowercase
    decrypted = []

    for i, char in enumerate(ct):
        if char.lower() in alphabet:
            shift = alphabet.index(key[i % len(key)])
            base = 'A' if char.isupper() else 'a'
            dec_char = chr((ord(char) - ord(base) - shift) % 26 + ord(base))
            decrypted.append(dec_char)
        else:
            decrypted.append(char)

    return ps.setString("".join(decrypted))

def BruteForceVigenre(ct, key):
    ct = str(ct)
    alphabet = string.ascii_lowercase
    all_decs = set()

    for length in range(1, 4):
        if length == 1:
            for a in alphabet:
                key = a
                decrypted = VigenreDecrypt(ct, key)
                all_decs.add(str(decrypted))
        elif length == 2:
            for a in alphabet:
                for b in alphabet:
                    key = a + b
                    decrypted = VigenreDecrypt(ct, key)
                    all_decs.add(str(decrypted))
        else:
            for a in alphabet:
                for b in alphabet:
                    for c in alphabet:
                        key = a + b + c
                        decrypted = VigenreDecrypt(ct, key)
                        all_decs.add(str(decrypted))

    return all_decs

Alice=ab.Agent("Alice")
Bob=ab.Agent("Bob")
Eve=ab.Agent("Eve")

InsecureChannel=ab.Channel()

ABE_Standard=ab.Model()

ABE_Standard.AddAgent(Alice)
ABE_Standard.AddAgent(Bob)
ABE_Standard.AddAgent(Eve)

ABE_Standard.AddChannel(InsecureChannel)

Alice.PlainText=plaintext
Alice.PrivateKey=key
Alice.PublicKey=key
Alice.encryption=VigenreEncrypt
Alice.decryption=VigenreDecrypt
Bob.PrivateKey=key
Bob.PublicKey=key
Bob.encryption=VigenreEncrypt
Bob.decryption=VigenreDecrypt

Eve.decryption=BruteForceVigenre

ABE_Standard.GenerateCompleteAccessList()
ABE_Standard.test()
