def solution(D, A):
    # Construct the reverse graph.
    n = len(A)
    G = [[] for _ in range(n)]
    for i, a in enumerate(A):
        if a != -1:
            G[a].append(i)

    # Define globals.
    used, stack = set(), []
    answer = [-1 for _ in range(n)]

    def dfs(v):
        if len(stack) >= D:
            answer[v] = stack[-D]

        used.add(v)
        stack.append(v)

        for u in G[v]:
            if u not in used:
                dfs(u)

        stack.pop()

    # Traverse the graph starting from the root.
    dfs(0)

    return answer


def main():
    print(solution(2, [-1, 0, 1, 2, 3]))
    print(solution(3, [-1, 0, 4, 2, 1]))
    print(solution(1, [-1]))
    print(solution(10, [-1, 0, 1, 2, 3]))
    print(solution(1, [-1, 0, 1, 2, 3]))


if __name__ == '__main__':
    main()
