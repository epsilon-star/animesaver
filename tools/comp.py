# Function
def comp(value,min,max):
    output = value
    if value > min and value < max: output = value
    elif value > max: output = max
    elif value < min: output = min
    return output