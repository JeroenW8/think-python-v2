#exercise 10.1
def nested_sum(list):
    total = 0
    for t in list:
        total += sum(t)
    return  total

print nested_sum([[1, 2, 3], [4, 5, 6]])
