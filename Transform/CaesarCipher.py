'''
Created on March 5, 2020

@author: Julia Rosner
'''

shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3]
shifted_upper = upper_alph[3:] + upper_alph[:3]

#shifts each letter in message over n alphabet shifts
def encrypt(message):
    result = ""
    for char in message:
        if char in lower_alph:
            index = lower_alph.index(char)
            result += shifted_lower[index]
        if char in upper_alph:
            index = upper_alph.index(char)
            result += shifted_upper[index]
        if char not in (lower_alph + upper_alph):
            result += char
    return result

#changes the shift to a new number
def setShift(n):
    global shift, shifted_lower, shifted_upper
    shift = n
    shifted_lower = lower_alph[shift:] + lower_alph[:shift]
    shifted_upper = upper_alph[shift:] + upper_alph[:shift]

#finds the original shift based on going through all shifts and returning the one with the most real words
def findShift(encrypted):
    import os.path
    file = os.path.join("data", "lowerwords.txt")
    f = open(file)
    wordsClean = [w.strip() for w in f.read().split()]
    max_shift = 0
    max_value = 0
    for sh in range(26):
        setShift(sh)
        n = 0
        for word in encrypt(encrypted).split():
            if word in wordsClean:
                n += 1
        if n > max_value:
            max_value = n
            max_shift = sh
    return (26-max_shift)



if __name__ == '__main__':
    print(encrypt("my name is"))
    setShift(1)
    print(encrypt("my name is"))
    findShift("nz obnf jt")
    setShift(26-findShift("nz obnf jt"))
    print(encrypt("nz obnf jt"))
