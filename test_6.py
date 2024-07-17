#Case with different errors
def get_average(values):
    sum = 0
    for val in values:
        sum += val
    average = suma / len(values)
    return average

data = [1, "2", 3, 4, "5"]

average = get_averge(data)
print("Average is: " + average)
#AI understands the context
#But if the program has SyntaxError, no "explain with AI"
#But when copypaste the error with hands, AI doesn't understand the context