"""Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesnt matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.
"""
def readfile2dict(filename):
    d = dict()
    f = open(filename)
    for line in f:
        word = line.strip()
        d[word] = len(word)
    return d

di = readfile2dict('../words.txt')
print 'house' in di
print 'hik' in di

"""Exercise 11.2. Dictionaries have a method called get that takes a key and a default value. If the
key appears in the dictionary, get returns the corresponding value; otherwise it returns the default
value.
Use get to write histogram more concisely. You should be able to eliminate the if statement.
"""
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

print histogram('brontosaurus')


"""Exercise 11.3. Dictionaries have a method called keys that returns the keys of the dictionary, in
no particular order, as a list.
Modify print_hist to print the keys and their values in alphabetical order.
"""
def print_hist(h):
    letters = h.keys()
    letters.sort()
    for l in letters:
        print l


h = histogram('jeroen wagt')
print_hist(h)


"""Exercise 11.4. Modify reverse_lookup so that it builds and returns a list of all keys that map to
v, or an empty list if there are none.
"""
def reverse_lookup(d, v):
    l = []
    for k in d:
        if d[k] == v:
            l.append(k)
    return l


k = reverse_lookup(h, 2)
print k


"""Exercise 11.5. Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict.
"""
def invert_dict(d):
    inverse = dict()
    for key, val in d.iteritems():
        inverse.setdefault(val, []).append(key)
    return inverse

inverse = invert_dict(h)
print inverse


"""Exercise 11.6. Run this version of fibonacci and the original with a range of parameters and
compare their run times.
"""
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print fibonacci(60)