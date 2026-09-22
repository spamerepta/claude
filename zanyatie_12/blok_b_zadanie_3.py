def print_odd_positions():
    n = int(input())
    if n == 0:
        return
    print(n)
    n = int(input())
    if n == 0:
        return
    print_odd_positions()


print_odd_positions()
