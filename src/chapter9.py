# exercise 9.1
def longwords(f, n):
    fin = open(f)
    for line in fin:
        word = line.strip()
        if len(word) > n:
            print word


longwords('..\words.txt', 19)

# exercise 9.2
def has_no_e(word):
    i = 0
    while i < len(word):
        if word[i] == 'e':
            return False
        i = i + 1
    return True

print has_no_e('hallo')

# exercise 9.3
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

# exercise 9.4
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

# exercise 9.5
def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

# exercise 9.6
def is_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i + 1
    return True

# exercise 9.7
def tcd(f):
    """Give me a word with three consecutive double letters in file f"""
    fin = open(f)
    for line in fin:
        word = line.strip()
        i = 0
        counter = 0
        while i < len(word)-1:
            if word[i] == word[i+1]:
                counter = counter + 1
            i = i + 1
        if counter > 2:
            print word

tcd('..\words.txt')

