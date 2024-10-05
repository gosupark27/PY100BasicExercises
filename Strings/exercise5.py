# Write code that checks whether the string char_sequence contains the character x.
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

def contains_char(char_seq, char):
    return True if char_seq.find(char) != -1 else False

print(contains_char(char_sequence, 'x'))
print(contains_char(char_sequence, 't'))
print(contains_char(char_sequence, 'C'))
print(contains_char(char_sequence, '4'))

print('x' in char_sequence)