import random
 
def replace(guess_word):
    c = []
    for i in guess_word:
        i = "-"
        c += i
    print(*c)
    return c
 
 
def guess(guess_word, c):
    k = 8
    input_letter = input("Input a letter: ")
    typed = set()
    while k != 0:
        if input_letter in guess_word:
            typed.add(input_letter)
            print([i if i in typed else '_' for i in guess_word])
            print(c)
        else:
            print("No such letter in the word")
            k -= 1
        input_letter = input("Input a letter: ")
 
print("H A N G M A N")
c = []
word_list = ['python', 'java', 'kotlin', 'javascript']
guess_word = random.choice(word_list)
print(guess_word)
replace(guess_word)
guess(guess_word, c)
