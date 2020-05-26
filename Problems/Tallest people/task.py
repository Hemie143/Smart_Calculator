def tallest_people(**people):
    max_height = max(people.values())
    result = {k: v for k, v in people.items() if v == max_height}
    for k, v in sorted(result.items()):
        print(f'{k} : {v}')
