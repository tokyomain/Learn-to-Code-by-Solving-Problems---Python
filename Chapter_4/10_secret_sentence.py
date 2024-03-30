# COCI '08 Contest 3 #2 Kemija / Secret Sentence
# https://dmoj.ca/problem/coci08c3p2

# input : One line of text, encoded sentence. lowercase letters 
# and spaces.
# Output : Original/decoded sentence.

vowels = "aeiou"
encoded = str(input())
decoded = ""

i = 0

while i < len(encoded):
    decoded += encoded[i]
    if encoded[i] in vowels:
        i += 3
    else:
        i += 1

print(decoded)

