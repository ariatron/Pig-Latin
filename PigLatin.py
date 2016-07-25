# Pig Latin Translator #

pyg = 'ay'

original = raw_input('Enter a word:')
# What do I put here #
word = original.lower()
first = word[0]
# Do you like piglatin? #
new_word = word[1:len(word)] + first + pyg
if len(original) > 0 and original.isalpha():
# Aliens made me do it #
    print new_word
else:
    print 'empty'