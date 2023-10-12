#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    encrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in s:
        if char.isupper():
            encrypted += alphabet[
                (ord(char) - ord("A") + k) % len(alphabet)
            ].capitalize()
        elif char.islower():
            encrypted += alphabet[(ord(char) - ord("a") + k) % len(alphabet)]
        else:
            encrypted += char
    return encrypted
