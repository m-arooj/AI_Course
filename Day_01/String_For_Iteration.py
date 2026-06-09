greet = 'HELLO'
i = 0

for letter in greet:   
    i += 1  # Iterating through greet string
    # print (letter + " " + i + "    Iteration") # Error
    print (f"{letter}  {i}    Iteration")