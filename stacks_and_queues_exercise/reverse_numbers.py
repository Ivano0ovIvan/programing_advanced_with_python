from _collections import deque

some_string = deque(input().split())
some_string.reverse()

print(' '.join(some_string))