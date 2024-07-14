def rotate(txt, key):
    def cipher(i, key):
        if i in range(32, 127):  # Considering all printable ASCII characters
            i = (i + key)
            if i > 127:
                return 'invalid'
        return chr(i)
    
    result = ''.join([cipher(ord(s), key) for s in txt])
    
    if 'invalid' in result:
        print('invalid')
    else:
        print(result)

txt = input()
key = int(input())
rotate(txt, key)