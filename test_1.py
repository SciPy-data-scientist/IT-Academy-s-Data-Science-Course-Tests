test_list = [7, 5, 6, 3, 5, 3, 8, 2, 1]

def sorted_set(l: list):
    """Create a sorted list without duplicates"""
    
    return sorted(set(l)) # The result is a sorted list but if you want a sorted set use the following code: return set(l) 

print(f"Sorted list without duplicates: {sorted_set(test_list)}")