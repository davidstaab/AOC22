from collections import deque


def slice_deque(d: deque, start: int, stop: int) -> list:
    if stop < start:
        raise ValueError("Play nice. Don't make stop < start.")

    d.rotate(-start + 1)
    ret = [d.popleft() for _ in range(stop - start)]
    d.extend(ret)
    d.rotate(stop - 1)
    return ret


def update_deque(d: deque, i: int, new):
    d.rotate(-i)
    d.popleft()
    d.appendleft(new)
    d.rotate(i)


if __name__ == '__main__':
    test = deque()
    test.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f'Test deque: {test}')
    print(f'Slicing [5:8]... {slice_deque(test, 5, 8)}')
    print(f'Deque after slice: {test}')
    update_deque(test, 3, 44)
    print(f'Updating at 3 with "44"... {test}')
