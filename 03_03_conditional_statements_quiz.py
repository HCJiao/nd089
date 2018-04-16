points = 174

def which_prize_ternary(points):
    prize = (
        "wooden rabbit"   if points <=  50 else
        "no prize"        if points <= 150 else
        "wafer-thin mint" if points <= 180 else
        "penguin"
    )
    return (
        "Congratulations! You won a "+prize+"!" if prize != "no prize" else 
        "Oh dear, no prize this time."
    )
print(which_prize_ternary(points))


points = 174  # use this input when submitting your answer

def which_prize_if(points):
    if points > 50 and points <= 150:
        result = "Oh dear, no prize this time."
    else:
        if points <= 50:
            prize = "wooden rabbit"
        elif points <=180:
            prize = "wafer-thin mint"
        else:
            prize = "penguin"
        result = "Congratulations! You won a "+prize+"!"
    return result

print(which_prize_if(points))
