def sequence_max():
    n = int(input())
    if n == 0:
        return 0
    rest = sequence_max()
    if n > rest:
        return n
    return rest


print(sequence_max())
