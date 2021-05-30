# Problem 14 Longest Collatz sequence

def create_sequence_num(n):
    terms = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        terms += 1
    return terms


def Collatz_starting_num():
    temp = 0
    i = 1
    while i < 1000000:
        s = create_sequence_num(i)
        if s > temp:
            temp = s
            value = i
        i += 1

    return value

print(Collatz_starting_num())