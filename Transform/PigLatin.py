'''
Created on March 5, 2020

@author: Julia Rosner
'''

#finds the index of first vowel in a word
def findVowel(word):
    """
    Return True if ch is a vowel and False otherwise
    """
    vowels = "aeiouyAEIOUY"
    for i in range(len(word)):
        letter = word[i]
        if letter in vowels:
            return i
    return "no vowels"

#turns english word into piglatin
def encrypt(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "-way"
    if word[0:2] == "qu":
        #find the index of the first vowel, ignoring the qu at the front
        index = findVowel(word[2:])
        # print(index)
        index += 2
        return word[index:] + "-" + word[0:index] + "ay"
    else:
        index = findVowel(word)
        if index == "no vowels":
            return word + "-way"
        if index == 0: #starting with y
            index = findVowel(word[1:])
            index += 1
        return word[index:] + "-" + word[0:index] + "ay"


#turns piglatin word back into english
def decrypt(word):
    word = word.split("-")
    if word[1] == "way":
        return word[0]
    else:
        return word[1][0:-2] + word[0]


if __name__ == '__main__':
    print(encrypt("anchor"))
    print(decrypt(encrypt("anchor")))
    print(encrypt("quiz"))
    print(decrypt(encrypt("quiz")))
    print(encrypt("zzz"))
    print(decrypt(encrypt("zzz")))
    print(encrypt("yesterday"))
    print(decrypt(encrypt("yesterday")))
    print(encrypt("rhythm"))
    print(decrypt(encrypt("ryhthm")))
    print(encrypt("quran"))
    print(decrypt(encrypt("quran")))
    print(encrypt("with"))
    print(decrypt(encrypt("with")))
