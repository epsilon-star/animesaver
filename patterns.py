import itertools

# Define the grid and the relationships where a pattern must pass through an intermediate dot
skip = {
    (1, 3): 2, (1, 7): 4, (1, 9): 5, (2, 8): 5, (3, 7): 5, (3, 9): 6,
    (4, 6): 5, (7, 9): 8, (1, 2): None, (2, 3): None, (4, 5): None, 
    # ... Add all valid skip relationships here
}

# Check if the pattern is valid
def is_valid_pattern(pattern):
    visited = set()
    for i in range(len(pattern) - 1):
        start, end = pattern[i], pattern[i+1]
        mid = skip.get((min(start, end), max(start, end)))
        if mid and mid not in visited:
            return False
        visited.add(start)
    return True

# Generate all possible permutations of the 9 dots
all_patterns = list(itertools.permutations(range(1, 10)))
valid_patterns = [pattern for pattern in all_patterns if is_valid_pattern(pattern)]

# Output the total number of valid patterns
print(f"Total Valid Patterns: {len(valid_patterns)}")