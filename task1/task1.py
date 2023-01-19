import sys


def task1(n, m):
    arr = list(range(1, n + 1))
    i = 0
    j = 0
    result = ''

    while j != arr[0]:
        result += str(arr[i])
        i += m - 1
        while i >= n:
            i -= n
        j = arr[i]
    return result


argN = int(sys.argv[1])
argM = int(sys.argv[2])
print(task1(argN, argM))
