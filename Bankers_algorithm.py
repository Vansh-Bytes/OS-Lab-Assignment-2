# Banker's Algorithm Implementation

def calculate_need(max_matrix, allocation, n, m):
    need = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max_matrix[i][j] - allocation[i][j]
    return need


def is_safe(n, m, allocation, max_matrix, available):
    need = calculate_need(max_matrix, allocation, n, m)

    print("\nNeed Matrix:")
    for row in need:
        print(row)

    work = available[:]
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    
                    # Add allocated resources back
                    for j in range(m):
                        work[j] += allocation[i][j]

                    safe_sequence.append(i)
                    finish[i] = True
                    found = True

        if not found:
            return False, []

    return True, safe_sequence


# ----------- MAIN PROGRAM -------------

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    allocation.append(list(map(int, input().split())))

print("\nEnter Maximum Matrix:")
max_matrix = []
for i in range(n):
    max_matrix.append(list(map(int, input().split())))

print("\nEnter Available Resources:")
available = list(map(int, input().split()))

# Safety Check
safe, sequence = is_safe(n, m, allocation, max_matrix, available)

if safe:
    print("\nSystem is in SAFE state.")
    print("Safe Sequence:", " -> ".join(f"P{i}" for i in sequence))
else:
    print("\nSystem is in UNSAFE state (Deadlock possible).")
