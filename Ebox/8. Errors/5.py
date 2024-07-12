def average(avg):
    average_score = sum(total_score) / x
    print(f"Batting average:{average_score:.2f}")

try:
    x = int(input("Enter the number of matches\n"))

    total_score = []
    print(f"Enter the scores")
    try:    
        for i in range(x):
            score = input()
            total_score.append(int(score))
        average(total_score)
    except ValueError:
        print("Type Error Exception")
except TypeError:
    print("Type Error Exception")   

    