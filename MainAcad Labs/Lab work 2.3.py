alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'

alpnumb = alphabet.lower()+alphabet.upper()+numbers

print(alpnumb[0])
print(alpnumb[-1])
print(alpnumb[2:-2])

alpnumb = alpnumb[7:]
print(alpnumb[3::3])

lenalpnumb = len(alpnumb)
print(alpnumb[lenalpnumb//2])

alpnumb = alpnumb[::-1]
