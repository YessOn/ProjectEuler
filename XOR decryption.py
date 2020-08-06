from __future__ import print_function
from itertools import product
with open("p059_cipher.txt") as encrypt_file:
    cipher_list  = [int(i) for i in encrypt_file.read(-1).strip().split(',')]
for key in product(range(97, 123), repeat=3):
    temp = cipher_list[:]
    for i in range(0, len(temp), 3):
        size = 3 if (i+3) <= len(temp) else len(temp)-i
        temp[i:i+size] = [temp[i+j]^key[j] for j in range(size)]
    temp_str = ''.join(chr(j) for j in temp)
    if all([31<k<123 for k in temp]) and "the" in temp_str: print(sum(temp))

# The answer: 129448
