from lab_tools import *

def permutated_choices(key):
    pass

plaintext="This is a plaintext which will be converted into blocks of 64 bits"
plaintext_blocks=to_blocks(ascii_to_bin(plaintext),64)
print(plaintext_blocks)
