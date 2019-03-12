def solution(stores, houses):
    # Generating events.
    m, n = len(stores), len(houses)
    events = []

    for i, store in enumerate(stores):
        events.append((store, 0, i))

    for i, house in enumerate(houses):
        events.append((house, 1, i))

    # O((n + m) log (n + m))
    events.sort()

    # Define globals (store index for now).
    answer = [None for _ in range(n)]

    def traverse_events(ordered_events):
        last_store_index = None
        for _, event_id, event_index in ordered_events:
            if event_id == 0:  # Store
                last_store_index = event_index
            else:  # House
                if last_store_index is None:
                    continue

                if answer[event_index] is None:
                    answer[event_index] = last_store_index

                # Compare with previous store.
                prev_store = stores[answer[event_index]]
                new_store = stores[last_store_index]
                prev_abs = abs(prev_store - houses[event_index])
                new_abs = abs(new_store - houses[event_index])

                if prev_abs > new_abs:
                    answer[event_index] = last_store_index

    # Find leftmost and right most store and update closest stores array.
    traverse_events(events)
    traverse_events(reversed(events))

    return [stores[a] for a in answer]


def main():
    print(solution([1, 5, 20, 11, 16], [5, 10, 17]))
    print(solution([2, 4], [2, 3, 4, 5, 6]))
    print(solution([1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(solution([1000000], [100]))
    print(solution([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10], [9, 12]))


if __name__ == '__main__':
    main()
