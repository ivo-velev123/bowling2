def calc_score(frames):
    total_score = 0
    frames = frames.replace(" ", "")
    #we iterate through the code to get the seperate values for each roll in a frame
    for i in range(0, len(frames)):
        #check if the roll is a strike
        
        if frames[i] == "X":
            #if the next roll is a strike consider it a double
            if frames[i+1] == "X":
                total_score += 20 + (int(frames[i+2]) + int(frames[i+3]))
            #otherwise score the strike normally
            else:
                total_score += 10 + (int(frames[i+1]) + int(frames[i+2]))
        #check if the roll is a spare
        elif frames[i] == "/":
            #if the roll is a spare calculate the value of the marking and add it to the total score.
            total_score += (10 - int(frames[i-1])) + int(frames[i+1])
        else:
            #else just add the number to the total
            total_score += int(frames[i])
    return total_score