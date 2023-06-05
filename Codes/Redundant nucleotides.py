
terms=['N', 'R', 'Y', 'K', 'M', 'S', 'W', 'B', 'D', 'H', 'V']
with open("Datasets/Virus.txt") as file:
   
    line_count = 0
    i = 0

    # Loop over each line in the file
    for line in file:
        i =i+1
      
        if any(term in line for term in terms):
            # If it does, increment the line count
            line_count += 1

print("Redundant sequences: ", line_count)
print("Percentage of redundant sequences:", line_count/i*100
