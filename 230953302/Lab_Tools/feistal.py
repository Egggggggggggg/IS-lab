def feistel(block,keys,f=bitwise_XOR,rounds=-1,swap=False,debug=False):
    halflen=int(len(block)/2)
    l0=block[:halflen]
    r0=block[halflen:]
    if rounds==-1:
        rounds=len(keys)
    if len(keys)!=rounds:
        print("ERROR: Missing or Extra Keys")
        return block
    if not all([halflen==len(f(r0,i)) for i in keys]):
        print("ERROR: Mismatched Length")
        return block
    if debug:
        print(f"l0 is {l0}")
        print(f"r0 is {r0}")
        print(f"full block is {l0+r0}")
    n=1
    for k in keys:
        r1=bitwise_XOR(l0,f(r0,k))
        l1=r0
        r0=r1
        l0=l1
        if debug:
            print(f"interation {n}\n r1 is {r1}\n l1 is {l1}\n r0 is {r0}\n l0 is {l0}")
        n+=1
    if swap:
        return l0+r0
    return r0+l0

#test feistal
'''
block="TEST"
keys=["YE","AH","th","is","is","a ","te","st"]
keys=[ascii_to_bin(i) for i in keys]
enc=feistel(ascii_to_bin(block,debug=True),keys,debug=True)
print(enc)
print(bin_to_ascii(enc))
print(bin_to_ascii(feistel(enc,keys[::-1])))
'''

#test bin conv
'''
teststr="abcABC123@#$"
print(ascii_to_bin(teststr))
print(len(ascii_to_bin(teststr)))
print(bin_to_ascii(ascii_to_bin(teststr)))
'''
