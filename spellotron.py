"""
author:  andrew lee
file: spellotron.py
"""

import sys
import string

class WordHolder:
    def __init__(self, indexOfCharInWord, indexOfCharInKeyboard, indexOfCharInChars, givenWord):
        self.indexOfWord = indexOfCharInWord
        self.indexOfKeyboard = indexOfCharInKeyboard
        self.indexOfChars = indexOfCharInChars
        self.word = givenWord
        self.wordFound = False
    
def readKeyboardLetters(txt_keyboard_letters):
    """
    reads the file inputted and stores them into a list
    :param txt_keyboard_letters: the keyboard text file
    :return: list with the keyboard keys
    """

    try:
        fpkeyboardletters = open(txt_keyboard_letters, 'r')
    except IOError:
        print("cannot find file " + txt_keyboard_letters)
        
    keyboard_letters = []
    for read_line in fpkeyboardletters:
        keyboard_letters.append(read_line.replace('\n','').split(' '))
    
    return keyboard_letters
    

def readAmericanEnglish(txt_american_english):
    """
    reads the american english text file and stores it into a list
    :param txt_american_english: the american english text file
    :return: a list with the words of the american english text file imported
    """
    try:
        fpamericanenglish = open(txt_american_english, 'r')
    except IOError:
        print("cannot find file " + txt_american_english) 

    american_english = []
    for read_line in fpamericanenglish:
        american_english.append(read_line.replace('\n',''))

    return american_english

def binarySearch(word, american_english):
    """
    performs a binary search to check which word to compare with the word inputted
    :param word: the word that needs to be fixed
    :param american_english: the american english list of words
    :return: True if the word is the same and False if the words are not the same
    """
    first = 0
    last = len(american_english)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if american_english[midpoint] == word:
            found = True
        else:
            if word < american_english[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
	
    return found


def getNextWord(currentWord, keyboard_letters_arr):
    """
    checks the word with the keyboard characters that are around each key
    :param currentWord: the word that needs to be checked
    :param keyboard_letters_arr: the keyboard list with the keys
    :return: a corrected word
    """
    localWord = WordHolder(currentWord.indexOfWord, currentWord.indexOfKeyboard, currentWord.indexOfChars, currentWord.word)
    newList = list(localWord.word)
    
    localWord.indexOfKeyboard += 1
    if localWord.indexOfKeyboard < len(keyboard_letters_arr[localWord.indexOfChars]):
        newList[localWord.indexOfWord] = keyboard_letters_arr[localWord.indexOfChars][localWord.indexOfKeyboard]
    
    localWord.word = "".join(newList)

    return localWord
    

def searchWord(givenWord):
    """
    checks the spelling of the word input into the function
    :param givenWord: the word that needs to be checked for spelling
    :return: the correct spelling of the word
    """

    indexOfChar = ord(givenWord[0].lower()) - ord('a')
    result = binarySearch(givenWord, globalAmericanEnglish)
    if result == True:
        currentWord = WordHolder(0, 0, indexOfChar, givenWord)
        currentWord.wordFound = True
        return currentWord

    for count in range(len(givenWord)):
        if givenWord[count].lower() <= 'z':
            indexOfChar = ord(givenWord[count].lower()) - ord('a')
        else:
            break
        indexOfWord = count
        indexOfKeyboard = 0
        currentWord = WordHolder(indexOfWord, indexOfKeyboard, indexOfChar, givenWord)

        nextWord = getNextWord(currentWord, globalKeyboardLetters)
        result = binarySearch(nextWord.word, globalAmericanEnglish)
        if result == False:

            while nextWord.word != currentWord.word:
                nextWord.word = givenWord
                currentWord = nextWord
                nextWord = getNextWord(currentWord, globalKeyboardLetters)
                result = binarySearch(nextWord.word, globalAmericanEnglish)
                if result == False:
                    if nextWord.word == currentWord.word:
                        break

                else:
                    currentWord.word = nextWord.word
                    currentWord.wordFound = True
                    return currentWord
        else:
            currentWord.word = nextWord.word
            currentWord.wordFound = True
            return currentWord

    currentWord.wordFound = False
    return currentWord
 
    
def deleteOneWord(word, count):
    """
    deletes a letter in the word to see if the word is in the american english list
    :param word: the word that needs to be checked
    :param count: the index of the word
    :return: the corrected word
    """

    chars = list(word)
    found = False
    while count < len(chars) and not found:
        chars[count] = ''
        newWord = "".join(chars)
        currentWord = searchWord(newWord)
        found = currentWord.wordFound
        if not found:
            count += 1
            chars = list(word)

    return currentWord


def addOneWord(word, count):
    """
    inserts a letter into each position and then compares the word to the americanenglish list
    :param word: the word being checked
    :param count: the index of the list
    :return: a corrected word
    """
    chars = list(word)
    found = False
    while count <= len(chars) and not found:
        for i in range(ord('a'), ord('z')+1):
            chars.insert(count, chr(i))
            newWord = "".join(chars)
            found = binarySearch(newWord, globalAmericanEnglish)
            if found:
                break
            else:
                chars = list(word)
            
        if not found:
            count += 1
            chars = list(word)
            
    currentWord = WordHolder(0, 0, 0, newWord)
    currentWord.wordFound = found
    return currentWord

def upcaseOneWord(word, count):
    """
    checks if the uppercase word is in the
    :param word: the word that is being checked
    :param count: the index of the list
    :return: a corrected word
    """
    chars = list(word)
    found = False
    while count < len(chars) and not found:
        chars[count] = chars[count].upper()
        newWord = "".join(chars)
        currentWord = searchWord(newWord)
        found = currentWord.wordFound
        if not found:
            count += 1
            chars = list(word)

    return currentWord


def main():
    """
    executes the function and checks if the words in the document are spelled correctly and prints out the amount of
    words in the file, the amount of words that were corrected, and the amount of words that are unknown
    """
    arguments = sys.argv[1:]
    count = len(arguments)
    CorrectWords = []
    IncorrectWords = []
    UnknownWords = []
    word_count = 0

    if count <= 0:
        text_source = sys.stdin
    else:
        text_source = open(arguments[0], mode='r')

    testWords = text_source.readlines()

    for testWord in testWords:
        word_count += len(testWords)
        inputTestWords = testWord.replace('\n', '')
        print(inputTestWords)

        if inputTestWords != "":

            Words = inputTestWords.split(' ')
            KeepWords = inputTestWords.split(' ')
            wordIndex = 0


            for word in Words:

                exclude = set(string.punctuation)
                word = ''.join(ch for ch in word if ch not in exclude).lower()

                newWord = searchWord(word)
                if not newWord.wordFound:
                    IncorrectWords.append(newWord.word)
                    newWord = addOneWord(word, count)

                    if not newWord.wordFound:
                        IncorrectWords.append(newWord.word)
                        newWord = deleteOneWord(word, 0)

                        if not newWord.wordFound:
                            newWord = upcaseOneWord(word, 0)
                            UnknownWords.append(word)

                        else:
                            if (word != newWord.word):
                                CorrectWords.append(newWord.word)
                                KeepWords[wordIndex] = newWord.word


                    else:
                        if (word != newWord.word):
                            CorrectWords.append(newWord.word)
                            KeepWords[wordIndex] = newWord.word

                else:
                    if (word != newWord.word):
                        CorrectWords.append(newWord.word)
                        KeepWords[wordIndex] = newWord.word

                wordIndex += 1
            if len(KeepWords) > 0:
                print(" ".join(KeepWords))
            print("\n")

    if word_count > 0:
        print(word_count, "words read from file")
        print("\n")
    if len(IncorrectWords) > 0:
        for word in IncorrectWords:
            if word in UnknownWords:
                IncorrectWords.remove(word)
        print(len(IncorrectWords), "Corrected Words")
        print(IncorrectWords)
        print("\n")
    if len(UnknownWords) > 0:
        print(len(UnknownWords), "Unknown Words")
        print(UnknownWords)


    if text_source != sys.stdin:
        text_source.close()
    
KEY_ADJACENCY_FILE = 'keyboard_letters.txt'
LEGAL_WORD_FILE = 'american_english.txt'

globalKeyboardLetters = readKeyboardLetters(KEY_ADJACENCY_FILE)
globalAmericanEnglish = readAmericanEnglish(LEGAL_WORD_FILE)

if __name__ == '__main__':
    main()
