def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_perfect_numbers(limit):
    """Find perfect numbers up to the given limit."""
    perfect_numbers = []
    p = 2  # Start checking for primes from 2
    while True:
        if is_prime(p):
            mersenne_prime = (1 << p) - 1  # This is 2^p - 1
            if is_prime(mersenne_prime):
                perfect_number = (1 << (p - 1)) * mersenne_prime  # This is 2^(p-1) * (2^p - 1)
                if perfect_number > limit:
                    break
                perfect_numbers.append(perfect_number)
        p += 1

    return perfect_numbers

# Find perfect numbers up to 100,000,000
perfect_numbers = find_perfect_numbers(100000000)

# Output the perfect numbers
for number in perfect_numbers:
    print(number)

