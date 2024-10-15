MOD = 987654321

def diamond_sum(N):
    if N == 1:
        return 1 % MOD
    
    mid = (N * N + 1) // 2
    step = (N - 1) // 2
    
    # Calculate diamond points around the center
    diamond_positions = [
        mid - step,
        mid + step,
        mid - step * N,
        mid + step * N,
        mid - step * (N + 1),
        mid + step * (N + 1),
        mid - step * (N - 1),
        mid + step * (N - 1)
    ]
    
    # Sum these positions and return result modulo MOD
    diamond_sum_value = sum(diamond_positions) % MOD
    return diamond_sum_value

# Input values from the file
input_values = [5, 1000, 1000000, 10000000000000]

# Output the diamond sum for each input
for N in input_values:
    print(diamond_sum(N))