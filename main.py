import time,random
words = open('words.txt','r')    # so we first open the file words.txt in which words are presents and stored them
content = words.read()                                     # in a variable named words
content=content.split()
word = random.choice(content)             # we used random library for choosing the word randomly
uni_letter=[]
total_words = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'        #  total word are initialize
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
spe_char = '!@#$%^&*()_-+={}[]"":??/><; '
num = '0 1 2 3 4 5 6 7 8 9'                     # special characters and number are stored in their specific variables
total_wordsli = total_words.split(' ')        # we just convert the total words str to a list named total_wordsli
# print('Welcome to the hangman game')
# time.sleep(1)                                            # we use time library for some cool animation flow like sleep
# name = input('Enter your name to enter the game:')     # here user will enter his/her name
turns = 6
warning = 3                               # turns are basicially guesses which were given to user
em = ''
used_li = []                      # used_li initialize to used letters in a list
vovels = 'aeiou'                  # all vovels are specified in a particular string
print("x=x=x=x=x=x=x=x=x=x=x Welcome To The Hangman Game! x=x=x=x=x==x=x=x=x==x=x ")
# FROM HERE WE ARE GOING TO START ADMIN INTERFACE AND DISPLAY FOR PLAY
adminorgame = input("Press [A] To Open Administration Panel\nPress [H] To Play the Game ").upper()
if adminorgame == "A":
    print("--------------------ADMINISTRATION-----------------")
    print("Press [1] To Exit menu")
    while True:

        password = input("Enter password: ")

        if password == "admin":

            print()
            print("You want to enter a new word or reset high score".upper())
            print()
            print("Press [1] To Exit menu")
            print()

            while True:

                print("Press [N] For Entering New Words")
                print("Press [H] For Resetting High Score")
                print()
                choice = input("Enter Your Option").upper()

                if choice == "N":
                    print("TO exit this menu press any int".upper())
                    while True:
                        f = open('words.txt', 'a+')

                        x = input(f'Enter a new word : ')
                        f.write(f' {x}')
                        time.sleep(0.5)
                        if "0" <= x < "9":
                            break
                    print("words entered successfully")
                elif choice == "H":
                    z = open("highscore.txt", "w")
                    z.write("0")
                    time.sleep(0.5)
                    print("High score reseted successfully")
                elif choice == "1":
                    break


        elif password == "1":
            break
        elif password != "admin":
            print("Incorrect Password!")
            print("Try again")



elif adminorgame == "H":
    print('Looading list from file...')
    time.sleep(2)
    print(len(content),'words loaded')
    print('Welcome to the hangman game')
    time.sleep(1)  # we use time library for some cool animation flow like sleep
    name = input('Type your name to enter the game:')  # here user will enter his/her name
    print(f'Hello {name}\nYou have {turns} guesses and {warning} warnings')
    print(f'You\'ve to guess a word of {len(word)} letters')
    print(f'Total word : {total_words}')  # print particular command like name guesses and warnings
    guesses = ''  # here the interface will be seen by a user on a screen it will

    # as we dont know the duration of the game and when it will end
    # for this we simply use while loop in it

    while turns > 0:
        over = 0  # for loop is used for hidden word interface _
        for char in word:
            if char in guesses:
                print(char, end='')
                # print('Congrats! Your guess is right.')
                # print(f'you have {turns} guesses left and {warning} warnings left')

            else:  # over var is initialze to 0 and it will increment in loop if it is equal to zero
                print('_', end='')  # means all words are revealed then user will simply win the game
                over += 1
        if over == 0:
            count = 0
            for i in word:
                if word.count(i) > 1:
                    pass
                else:
                    count += 1

            scoree = (count * turns)
            print(f' Correct! the word is {word}')
            print(f'Congratulations {name} you have won the game')
            print(f'{name} your Score is {scoree}')
            break
            # guess is the var where user will input his no of guess
        guess = input(' Type your letter:').lower()
        # if len of guess not equal to 1 it simply show 'type your letter'
        if len(guess) == 1:
            guesses += guess
            used_li += guess
            if guess in total_wordsli:
                total_wordsli.remove(guess)  # In this module we are converting a used letter list in a str for the
                rem_letter = em.join(total_wordsli)  # Interface rem_letter is the remaining letters string
                # for x in total_wordsli:
                #     em+=x
            if guess in vovels and guess not in word:
                if used_li.count(guess) == 1:
                    turns -= 2
                    print(f'Remaining Letters are: {rem_letter}')
                    print('you type wrong vovel')
                    if turns > 0:
                        print(f'you have {turns} guesses left and {warning} warnings left')
            if guess in spe_char or guess in num:
                if used_li.count(guess) == 1:
                    if warning > 0:
                        warning -= 1
                        print('please type valid character')
                        print('Guess from this list of letters')
                        print(f'you have {turns} guesses left and {warning} warnings left')
                    elif warning == 0:
                        turns -= 1
                        print('Alert! your warnings are out of limits.')
                        print(f'Now you have {turns} guesses left')
            if guess in used_li:
                if used_li.count(guess) > 1:
                    if warning > 0:
                        #  print(c)
                        warning -= 1
                        print(f'sorry {name} you have already guess that letter!')
                        print(f'you have {turns} guesses left')
                        if warning > 0:
                            print(f'you have {warning} warnings left')
                        else:
                            print(f'you have 0 warnings')
                    elif warning <= 0:
                        # print(c)
                        turns -= 1
                        print(f'sorry {name} you have already guess that letter!')
                        print(f'you have {turns} guesses left')
                elif guess in consonant and guess not in word:
                    print(f'Remaining letters are: {rem_letter}')
                    turns -= 1
                    print('sorry wrong guess :(')
                    print(f'you have {turns} guesses left and {warning} warnings left')
                elif warning < 0:
                    if guess not in word:
                        turns -= 1
                        print('Alert! your warnings are out of limits.')
                        print(f'Now you have {turns} guesses left')

            if turns <= 0:
                print(f'Game over {name} you lost the game!')
                print('The given word was', word)
                print(f'{name} your score is 0')
                scoree=0
                break
            for u in word:
                if word.count(u) > 1:
                    uni_letter.append(u)

        else:
            print('please type only one letter at a time')
            guess

    # Highcore logic
    def score_write():
        f = open('highscore.txt', 'a')
        f.write(f'{name} {scoree}\n')


    score_write()


    def highscore():
        f = open('highscore.txt', 'r+')
        content = f.read()
        lines = content.split('\n')
        lines.pop(len(lines) - 1)
        high_score = 0
        high_score_name = ''
        # f.write(f'{name} {scoree}\n')
        for line in lines:
            data = line.split(' ')
            namee = data[0]
            score = data[1]
            # namee, score = line.split()
            score = int(score)
            if score > high_score:
                high_score = score
                high_score_name = namee
        print("The high score is", high_score, "and it was achieved by", high_score_name)


    highscore()

else:
    print("Invalid choice")
