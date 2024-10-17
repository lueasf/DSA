# Python file for the mugshot exercise
# Refer to the paper instructions for the semantics of the parameters and return type


def mugshot(mugsCapacity: list[int], target: int, filledMugIndex: int, maxExplorations: int) -> list[list[int]]:
    initial_state = [0] * len(mugsCapacity)
    initial_state[filledMugIndex] = mugsCapacity[filledMugIndex]
    already_seen: dict[tuple[int, ...], list[int]] = {}

    queue: list[tuple[list[int], int]] = [(initial_state, 0)]
    already_seen[(*initial_state, )] = []
    
    while queue != []:
        current_state, step = queue.pop(0)
        step = step + 1

        for src in range(len(mugsCapacity)):
            for dst in range(len(mugsCapacity) + 1):
                if src == dst:
                    continue

                new_state = current_state.copy()

                if dst == len(mugsCapacity):
                    new_state[src] = 0
                else:
                    new_state[dst] = min(mugsCapacity[dst], current_state[dst] + current_state[src])
                    new_state[src] = max(0, current_state[src] - (mugsCapacity[dst] - current_state[dst]))

                if tuple(new_state) in already_seen:
                    continue

                already_seen[tuple(new_state)] = current_state

                if target in new_state:
                    path = [new_state]
                    p = new_state
                    while p != initial_state:
                        p = already_seen[tuple(p)]
                        path.append(p)
                    path.reverse()
                    return path

                if step < maxExplorations:
                    queue.append((new_state, step))
    return []
            
if __name__ == "__main__":
    r = mugshot([10, 3, 7], 5, 0, 7)
    print(r)
    r = mugshot([10, 3, 7], 5, 0, 8)
    print(r)
