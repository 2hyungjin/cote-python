from collections import deque

if __name__ == '__main__':
    stack = []
    stack.append(1)
    stack.append(4)
    stack.append(6)
    stack.pop()
    print(''.join(str(stack)))

    queue = deque()
    queue.append(1)
    queue.append(4)
    queue.append(6)
    queue.popleft()
    print(list(queue))
