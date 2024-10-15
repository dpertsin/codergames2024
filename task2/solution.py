MOD = 987654321

# Function to compute the diamond sum for a given odd N
def diamond_sum(N):
    if N == 1:
        return 1
    half = N // 2
    diamond_indices = [
        N * half + 1,           # Middle of the top side
        N * (half + 1),         # Middle of the bottom side
        N * half - 1,           # Left side of the top
        N * half + N - 2        # Right side
    ]
    return sum(diamond_indices) % MOD

# Test with the provided inputs
test_cases = [1000, 1000000, 10000000000000]

# Compute results for each test case
results = [diamond_sum(N) for N in test_cases]
print(results)
