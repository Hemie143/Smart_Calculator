def final_deposit_amount(*interests, amount=1000):
    for i in interests:
        amount *= 1 + i / 100
    return round(amount, 2)
