points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
prize = (
    "wooden rabbit" if points <=50 else
    "wafer-thin mint" if points > 150 and points <= 180 else
    "penguin"
)

# use the truth value of prize to assign result to the correct message
if prize != None:
    result = "Congratulations! You won a "+prize+"!"
else:
    result = "Oh dear, no prize this time."

print(result)