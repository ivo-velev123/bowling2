def calc_score(rounds):
    total_score = 0
    rounds = rounds.replace(" ", "")
    for i in range(0, len(rounds)):
        if rounds[i] == "X":
            total_score += 10
        elif rounds[i] == "/":
            total_score += (10 - int(rounds[i-1]))
        else:
            total_score += int(rounds[i])
    return total_score