import numpy
import pandas as pd
import sys
import hashlib

diceware = pd.read_csv("diceware.wordlist.txt")

dictionary = dict()
with open('diceware.wordlist.txt') as f:
    for line in f:
        (key, value) = line.split()
        dictionary[int(key)] = value

md5 = sys.argv[1]
prob1 = sys.argv[2]
prob2 = sys.argv[3]
prob3 = sys.argv[4]
prob4 = sys.argv[5]
prob5 = sys.argv[6]
prob6 = sys.argv[7]

found = False


previous_words = []


print "Procurando senha:  " + md5
while found != True:
    word_list = []
    for i in range(0, 6):
        dice_rolls = []
        for i in range(0, 5):
            chosen_dice = numpy.random.choice(numpy.arange(1,7), p=[prob1, prob2, prob3, prob4, prob5, prob6])
            dice_rolls.append(chosen_dice)
        key = int(''.join(map(str,dice_rolls)))
        word = dictionary[key]
        word_list.append(word)
    full_word = ''.join(word_list)
    if full_word not in previous_words:
        guess = hashlib.md5(full_word).hexdigest()
        previous_words.append(full_word)
        if guess == md5:
            found = True


print "A senha eh:  " + full_word
print "achou"
