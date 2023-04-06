def find_most_profitable_combination(combinations):
    max_profit = 0
    best_combination = []
    for combination in combinations:
        total_profit = get_profit(combination)
        if total_profit > max_profit:
            max_profit = total_profit
            best_combination = combination
    return best_combination, max_profit

def get_profit(combination):
    return sum([contract["price"] for contract in combination])

def overlaps(c1, c2):
    c1_end = c1["start"] + c1["duration"]
    c2_end = c2["start"] + c2["duration"]
    if c1["start"] <= c2["start"] < c1_end or c2["start"] <= c1["start"] < c2_end:
        return True
    else: 
        return False
    
def has_overlaps(contracts):
    for i in range(len(contracts)):
        for j in range(i+1, len(contracts)):
            if overlaps(contracts[i], contracts[j]):
                return True
    return False

def early_termination(func):
    def wrapper(contracts):
        if len(contracts)<=1: 
            return contracts, get_profit(contracts)
        return func(contracts)
    return wrapper