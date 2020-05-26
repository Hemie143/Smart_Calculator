from collections import deque

n_logs = int(input())
queue = deque()
for _ in range(n_logs):
    task = input()
    if task.startswith('ISSUE'):
        queue.append(task.split(' ')[1])
    elif task.startswith('SOLVED'):
        queue.popleft()
    else:
        print('ERROR')
while len(queue) > 0:
    print(queue.popleft())
