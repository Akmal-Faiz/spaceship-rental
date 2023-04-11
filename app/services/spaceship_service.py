import itertools
from app.services.spaceship_utils import *
from app.utils.custom_exception import NoValidResultException
import random

@early_termination
def optimize(contracts):
    # Sort the contracts by their start times in ascending order
    contracts = sorted(contracts, key=lambda x: x["start"])

    # Compute the maximum end time of all the contracts
    max_end_time = max(c["start"] + c["duration"] for c in contracts)

    # Initialize the n by m array of profits
    # where n is the number of contracts
    # and m is the maximum end time of all contracts
    # each entry in this array represents the maximum amount of 
    # profit that can be earned after considering the current and all previous completed contracts, at the current hour
    profits = [[0] * (max_end_time + 1) for _ in range(len(contracts))]
    
    # Also, initialize a 2-d array to keep track of which contracts areresponse
    selected_contracts = [[[] for c in range(max_end_time+1)] for r in range(len(contracts))]
    
    # Loop through the contracts and end times
    for i, contract in enumerate(contracts):
        for j in range(max_end_time + 1):
            # If past end of contract, take max of previous and above cells
            if j >contract["start"] + contract["duration"]:
                if profits[i][j-1] > profits[i-1][j]:
                    profits[i][j] = profits[i][j-1]
                    selected_contracts[i][j] = selected_contracts[i][j-1]
                else:
                    profits[i][j] = profits[i-1][j]
                    selected_contracts[i][j] = selected_contracts[i-1][j]
                continue
                
            # Compute the profit obtained by not selecting the contract
            no_profit = profits[i-1][j] if i > 0 else 0

            # Compute the profit obtained by selecting the contract
            if j == contract["start"] + contract["duration"]:
                yes_profit = contract["price"] + profits[i-1][contract["start"]]              
            else:
                yes_profit = 0

            # Select the maximum profit
            if no_profit >= yes_profit:
                profits[i][j] = no_profit
                if i > 0: 
                    selected_contracts[i][j] = selected_contracts[i-1][j]
                
            else:
                profits[i][j] = yes_profit
                if j >= contract["start"] + contract["duration"]:
                    selected_contracts[i][j] = selected_contracts[i-1][contract["start"]].copy() + [contract]
    for i in profits:
        print(i)
    import pdb; pdb.set_trace()                 
   

    # Return the selected contracts and the maximum profit
    return selected_contracts[-1][-1], profits[-1][-1]

@early_termination
def brute_force(contracts):
    # Get all combinations
    all_combinations = []
    for i in range(len(contracts)+1):
        for subset in itertools.combinations(contracts, i):
            all_combinations.append(list(subset))
    
    no_overlap = []
    # Remove combinations with overlaps
    for combination in all_combinations:
        if not has_overlaps(combination):
            no_overlap.append(combination)
    
    # Return combination with maximum profit
    return find_most_profitable_combination(no_overlap)

@early_termination
def fcfs(contracts):
    res = []
    contracts = sorted(contracts, key=lambda x: x["start"])
    end = 0
    for i, contract in enumerate(contracts):
        # accept contract if previous contract has completed
        if contract["start"] >= end:
            res.append(contract)
            end = contract["start"] + contract["duration"]
    return res, get_profit(res)        

@early_termination
def greedy_selection(contracts):
    contracts = sorted(contracts, key=lambda x: x["price"], reverse=True)
    start, end = 0, 0
    res = []
    for i, contract in enumerate(contracts):
        if i == 0:
            res.append(contract)
            start = contract["start"]
            end = contract["start"] + contract["duration"]
            continue
        if (contract["start"]+contract["duration"]) <= start:
            res.append(contract)
            start = contract["start"]
            continue
        if contract["start"] >= end:
            res.append(contract)
            end = contract["start"] + contract["duration"]
    
    return res, get_profit(res)

@early_termination
def random_selection(contracts):
    res = random.sample(contracts, k=random.randint(1,len(contracts)))
    if has_overlaps(res):
        raise NoValidResultException( "No valid result found via random selection. Please try again or select a different algorithm.")
    return res, get_profit(res)