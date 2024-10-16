def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    configurations = []
    i = 0
    while i < len(lines):
        m = int(lines[i].strip())
        initial = list(map(int, lines[i + 1].strip().split()))
        target = list(map(int, lines[i + 2].strip().split()))
        configurations.append((m, initial, target))
        i += 3
    
    return configurations

def calculate_rotations(m, initial, target):
    n = len(initial)
    rotations = [0] * n
    
    for i in range(n):
        diff = (target[i] - initial[i]) % m
        if diff > m // 2:
            diff -= m
        rotations[i] = diff
    
    return rotations

def process_pyramids(filename):
    configurations = read_input(filename)
    results = []
    
    for m, initial, target in configurations:
        result = calculate_rotations(m, initial, target)
        results.append(result)
    
    for result in results:
        print(result)

process_pyramids('3_Task_Input_File.txt')