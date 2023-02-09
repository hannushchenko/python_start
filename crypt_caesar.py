inputword = input("write word to crypt:").upper()

hard = int(input("write hard 1-25: "))

result =''

for n in inputword:
    if n in (' ', '.', ','):
        result += n
    else:
        numb = ord(n)
        numb = numb + hard
        if 90 < numb:
            numb = numb + 6
        result += chr(numb)


print(result.lower())

# /91-96