from collections import deque


n, a = None, None


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        a = [int(i) for i in f.readline().strip().split()]

    a.sort()
    a = deque(a)
    result = 0
    while len(a) > 2:
        # x = a[0], y = a[n - 1], z = a[n - 2]
        x = a.popleft()
        y = a.pop()
        z = a.pop()
        result += x + z
        if x + z > y:
            a.append(y)
            a.append(x + z)
        else:
            a.append(x + z)
            a.append(y)

    result = str(sum(a) + result)
    with open('output.txt', 'w') as f:
        f.write(result)
        f.write('\n')
