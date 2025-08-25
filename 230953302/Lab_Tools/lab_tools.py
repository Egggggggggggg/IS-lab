def bin_pad(b,l=8,p="0",debug=False):
    if l<len(b):
        if debug:
            print(f"binary {b} of length {len(b)} is bigger than desired size {l}")
        return b
    if debug:
        print(f"Padded {l-len(b)} {p} bits to {len(b)} bits")
    b=p*(l-len(b))+b
    return b

def ascii_to_bin(a,debug=False):
    out=""
    for i in a:
        binchr=str(bin(ord(i)))[2:]
        out+=bin_pad(binchr)
    if debug:
        print(out)
    return out

def to_blocks(s,size):
    bin_pad(s)
    return [s[i:i+size] for i in range(0,len(s),size)]

def bin_to_ascii(b,debug=False):
    blocks=to_blocks(b,8)
    if debug:
        print(blocks)
    out=""
    for i in blocks:
        out+=chr(int(i,2))
    return out

def bitwise_XOR(b1,b2):
    b1=bin_pad(b1,l=len(b2))
    b2=bin_pad(b2,l=len(b1))
    out=""
    for i in range(len(b1)):
        out+=str(int(b1[i])^int(b2[i]))
    return out

def bitwise_AND(b1,b2):
    b1=bin_pad(b1,l=len(b2))
    b2=bin_pad(b2,l=len(b1))
    out=""
    for i in range(len(b1)):
        out+=str(int(b1[i]) and int(b2[i]))
    return out

def bitwise_OR(b1,b2):
    b1=bin_pad(b1,l=len(b2))
    b2=bin_pad(b2,l=len(b1))
    out=""
    for i in range(len(b1)):
        out+=str(int(b1[i]) or int(b2[i]))
    return out

def circular_shift(b,shift=1):
    out=""
    for i in range(len(b)):
        out+=b[((i-shift)%len(b))]
    return out
