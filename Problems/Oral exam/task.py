from collections import deque

n_logs = int(input())
queue = deque()
for _ in range(n_logs):
    task = input()
    if task.startswith('READY'):
        queue.append(task.split(' ')[1])
    elif task.startswith('EXTRA'):
        queue.append(queue.popleft())
    elif task == 'PASSED':
        print(queue.popleft())
    else:
        print('ERROR')
