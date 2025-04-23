All_chars = ''.join([chr(x) for x in range(97, 123)] +  
                    [chr(x) for x in range(65, 91)] +  
                    [chr(x) for x in range(48, 58)])

print(All_chars)

for char in All_chars:
    print(f"{char}: {ord(char)}")