def shuffle(any_word):
    "takes any word, shuffles it and returns the jumbled word"

    import re
    import random
    length = len(any_word)
    word = any_word
    jumbled_word= ""

    for i in range(length):   

        x = random.randint(0, length-1)
        jumbled_word = jumbled_word + word[x]
        word = word.replace(word[x], " ", 1) 
        word = re.sub(r'\s', "", word)
        length = len(word)
    if jumbled_word == any_word:
        shuffle(any_word) 
    return jumbled_word
