def findShift(encrypted):
    import os.path
    file = os.path.join("data", "lowerwords.txt")
    f = open(file)
    wordsClean = [w.strip() for w in f.read().split()]
    max_shift = 0
    max_value = 0
    for sh in range(26):
        setShift(sh)
        print(sh, encrypt(encrypted))
        n = 0
        for word in encrypt(encrypted).split():
            if word in wordsClean:
                n += 1
        if n > max_value:
            max_value = n
            max_shift = sh
    decryption = setShift(max_shift)
    return decryption


Chat Conversation End
Type a message...

