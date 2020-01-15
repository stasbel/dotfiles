def solution(S: str, K: int):
    # Remove all dashes.
    S = ''.join(c for c in S if c != '-')

    groups = []

    # Add prefix.
    prefix_len = len(S) % K
    if prefix_len != 0:
        groups.append(S[:prefix_len])
        S = S[prefix_len:]

    # Add groups.
    groups.extend((S[i: i + K] for i in range(0, len(S), K)))

    # Return result in uppercase.
    return '-'.join(g.upper() for g in groups)


def main():
    print(solution('2-4A0r7-4k', 4))
    print(solution('2-4A0r7-4k', 3))
    print(solution('r', 1))
    print(solution('000', 1))
    print(solution('aaabbb', 1))


if __name__ == '__main__':
    main()
