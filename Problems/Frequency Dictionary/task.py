# put your python code here
entry = input().split()
entry = [e.lower() for e in entry]
data = {e: entry.count(e) for e in entry}
for k, v in data.items():
    print(f'{k} {v}')
