

import random
words=["jazz", "microwave", "rhythm", "submarine", "onyx"]
one_word=random.choice(words)
print(one_word)
total_g=[]
Length=len(one_word)
print(Length)

guess_c=["_"]*Length
while True:
    if "_" in guess_c:
        print(" ".join (guess_c))

        character=input("What letter do you want to choose?:")
        if character in total_g:
            print("You have already tryed this letter")
        else:
                if character in one_word:
                    for i in range(len(one_word)):
                        if character==one_word[i]:
                            guess_c[i]=character


                total_g.append(character)
    else:
        print("You have found the word!!")
        break