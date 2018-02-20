import math

# Exercise 6.1
def compare(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    else:
        return -1


# Exercise 6.2
def hypotenuse(a, b):
    """hypotenuse returns the length of the hypotenuse of a right triangle
    given the lengths of the two legs as arguments"""
    c = a**2 + b**2
    return math.sqrt(c)


# Exercise 6.3
def is_between(x, y, z):
    if x <= y:
        if y <= z:
            return True
    return False


def factorial(n):
    space = ' ' * (4 * n)
    print space, 'factorial', n
    if n == 0:
        print space, 'returning 1'
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print space, 'returning', result
        return result


def is_power(a, b):
    """A number a, is a power of b if it is divisible by b and a/b is a power of b
    8 is a power of 2 if 8 is divisible by 2 and 8/2 is a power of 2"""
    print 'is power ' + str(a)
    if a == b:
        return True
    if a % b != 0:
        return False
    else:
        return is_power(a/b, b)

print is_power(8, 2)
print is_power(9, 2)
print is_power(64, 4)