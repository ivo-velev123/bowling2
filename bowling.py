def calc_score(frames):
    total_score = 0
    frames = frames.replace(" ", "")
    #we iterate through the code to get the seperate values for each roll in a frame
    for index in range(0, len(frames)):
        #check if the roll is a strike
        if frames[index] == "X":
            #if the next roll is a strike consider it a double
            if index != (len(frames) - 1):
                if frames[index+1] == "X":
                    total_score += 20 + int(frames[index+2])
                #otherwise score the strike normally
                else:
                    if frames[index+2] == "/":
                        total_score += 20
                    else:
                        total_score += 10 + (int(frames[index+1]) + int(frames[index+2]))
            else:
                total_score += 10
        #check if the roll is a spare
        elif frames[index] == "/":
            if index != (len(frames) - 1):
                #if the roll is a spare calculate the value of the marking and add it to the total score.
                total_score += (10 - int(frames[index-1])) + int(frames[index+1])
            else:
                total_score += (10 - int(frames[index-1]))
        else:
            #else just add the number to the total
            total_score += int(frames[index])
    return total_score