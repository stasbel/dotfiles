def find_number(arr, k):
    return 'YES' if k in arr else 'NO'


def odd_numbers(l, r):
    return [i for i in range(l, r + 1) if i % 2 == 1]


def main():
    # print(find_number([-1, 0, 1, 2, 3], 3))
    print(odd_numbers(3, 9))


if __name__ == '__main__':
    main()
