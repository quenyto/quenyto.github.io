def letter_to_number(s):
  x = 0
  for i in range(len(s)):
    x *= 10
    x += (ord(s[i]) - ord('a') + 1) % 10
  return x

def strfy(n):
  return str(n).zfill(4)[0:4]

A = input("Last 4 digits of Vista phone number: ")
B = input("Last 4 digits of serial number of 3/23/18 purchase in checking account: ")
C = input("Last 4 digits of serial number of 7/05/18 purchase in checking account: ")
D = input("Last 4 digits of Stanford Student ID: ")
E = letter_to_number(raw_input("First letters of Stanford dorms for all four years (lowercase): "))
key = raw_input("Insert key: ")
K = [(pow(592589L, letter_to_number(key)*i, 730999993L)/10) % 10000 \
    for i in range(5)]
L = input("Password length: ")


A_UPPERCASE = ord('A')
ALPHABET_SIZE = 26


def _decompose(number):
    """Generate digits from `number` in base alphabet, least significants
    bits first.

    Since A is 1 rather than 0 in base alphabet, we are dealing with
    `number - 1` at each iteration to be able to extract the proper digits.
    """

    while number:
        number, remainder = divmod(number - 1, ALPHABET_SIZE)
        yield remainder


def base_10_to_alphabet(number):
    """Convert a decimal number to its base alphabet representation"""

    return ''.join( \
            chr(A_UPPERCASE + part) \
            for part in _decompose(number) \
    )[::-1]

c = (letter_to_number(key) / 99) % 5

Y = [strfy((A + K[(0 + c) % 5]) % 10000),\
     strfy((B + K[(1 + c) % 5]) % 10000), \
     strfy((C + K[(2 + c) % 5]) % 10000), \
     strfy((D + K[(3 + c) % 5]) % 10000), \
     strfy((E + K[(4 + c) % 5]) % 10000)]

numstr = ""
for i in range(4):
  for j in range(5):
    numstr += Y[j][i]

encoded = pow(814267044343L, long(numstr), 95428942451557009L)
pwd = base_10_to_alphabet(encoded).lower().rjust(12, 'z')

pl = L
if L < 7:
  pl = 7
if L > 14:
  pl = 14

pwd = pwd[:(pl - 3)] + str(len(key) % 10) + "@" + pwd[pl-3].upper()
 
print("Password is: " + pwd[:L])

raw_input()
