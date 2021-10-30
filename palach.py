score = 5
word = 'orange'
guess = str(input('Enter your guess: '))

while (score > 0) or (guess in ('o', 'r', 'a', 'n', 'g', 'e', 'orange')):
    if guess in ('o', 'r', 'a', 'n', 'g', 'e', 'orange'):
        print('CORRECT')
        break
    else:
        score -= 1
        print('WRONG')
        print('Your score is ' + str(score))
        guess = str(input('Enter your guess: '))