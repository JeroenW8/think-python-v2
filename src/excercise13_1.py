import string

def process_file(filename):
    """.."""
    hist = dict()
    fin = open(filename)
    for line in fin:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1

hist = process_file('../test.txt')

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

print 'Total number of words: ', total_words(hist)
print 'Number of different words: ', different_words(hist)

print hist