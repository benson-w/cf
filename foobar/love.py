def answer(s):
    a = ""
    for i in range(0, len(s)):
        place = ord(s[i])
        if (place >= 97 and place <= 122):
            place_ =  place - 97
            a = a + chr(122 - place_)
        else:
            a = a + s[i]
    print(a)
answer("abcdxyzAASDF")
