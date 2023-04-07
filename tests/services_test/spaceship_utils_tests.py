from app.services.spaceship_utils import *

test_case_1 = []
test_case_2 = [{"name": "Contract1", "start": 0, "duration": 5, "price": 10}]
test_case_3 = [
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
    {"name": "Contract4", "start": 5, "duration": 9, "price": 7}
]
test_case_overlap = [
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14}
]
test_case_no_overlap = [
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8}
]


def find_most_profitable_combination_test():
    assert(find_most_profitable_combination([test_case_1, test_case_2, test_case_3]) == (test_case_3, 39))

    
def get_profit_test():
    assert(get_profit(test_case_1) == 0)
    assert(get_profit(test_case_2) == 10)
    assert(get_profit(test_case_3) == 39)

def overlaps_test():
    assert(overlaps(*test_case_overlap) == True)
    assert(overlaps(*test_case_no_overlap) == False)

def has_overlaps_test():
    assert(has_overlaps(test_case_1) == False)
    assert(has_overlaps(test_case_2) == False)
    assert(has_overlaps(test_case_3) == True)
    
if __name__ == "__main__":
    find_most_profitable_combination_test()
    get_profit_test()
    overlaps_test()
    has_overlaps_test()