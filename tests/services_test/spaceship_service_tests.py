from app.services.spaceship_service import *

test_case = [
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
    {"name": "Contract4", "start": 5, "duration": 9, "price": 7}
]

expected_outcome_123 = ([{'name': 'Contract1', 'start': 0, 'duration': 5, 'price': 10}, {'name': 'Contract3', 'start': 5, 'duration': 9, 'price': 8}], 18)
expected_outcome_4 = ([{"name": "Contract2", "start": 3, "duration": 7, "price": 14}], 14)

def optimize_test():
    assert(optimize(test_case) == expected_outcome_123)

def brute_force_test():
    assert(brute_force(test_case) == expected_outcome_123)
    
def fcfs_test():
    assert(fcfs(test_case) == expected_outcome_123)
    
def greedy_selection_test():
    assert(greedy_selection(test_case) == expected_outcome_4)
    
if __name__ == "__main__":
    optimize_test()
    brute_force_test()
    fcfs_test()
    greedy_selection_test()
