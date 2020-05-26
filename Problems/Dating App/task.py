def select_dates(potentional_dates):
    dates = [p['name'] for p in potentional_dates if p['age'] > 30 and p['city'] == 'Berlin' and 'art' in p['hobbies']]
    return ', '.join(dates)


