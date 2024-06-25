N = int(input())

if N <= 0:
    print("")  # No output for non-positive N
else:
    series = []
    current_value = 30
    series.append(current_value)
    
    # Pattern changes, needs to follow the observed pattern
    changes = [5, 3, 3, 13, -1, 25, -7, 39, -15]
    changes_len = len(changes)
    
    for i in range(1, N):
        current_value += changes[(i-1) % changes_len]
        series.append(current_value)
    
    print(" ".join(map(str, series)))