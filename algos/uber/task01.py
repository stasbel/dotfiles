from collections import UserList


class MinList(UserList):
    def append(self, item):
        if self.data:
            self.data.append((item, min(item, self.data[-1][1])))
        else:
            self.data.append((item, item))


class S2Queue:
    def __init__(self):
        self.s1 = MinList()
        self.s2 = MinList()

    def append(self, item):
        self.s1.append(item)

    def pop(self):
        if not self.s2:
            for e, _ in reversed(self.s1):
                self.s2.append(e)

            self.s1 = MinList()

        return self.s2.pop()[0]

    def min(self):
        ans = None

        # s1
        if self.s1:
            ans = self.s1[-1][1]

        # s2
        if self.s2 and ans is not None:
            ans = min(ans, self.s2[-1][1])
        elif ans is None:
            ans = self.s2[-1][1]

        return ans


def segment(x, arr):
    q = S2Queue()
    for i in range(x):
        q.append(arr[i])

    ans = q.min()
    for i in range(x, len(arr)):
        q.append(arr[i])
        q.pop()
        ans = max(ans, q.min())

    return ans


def main():
    print(segment(1, [1, 2, 3, 1, 2]))
    print(segment(2, [1, 1, 1]))
    print(segment(3, [2, 5, 4, 6, 8]))


if __name__ == '__main__':
    main()
