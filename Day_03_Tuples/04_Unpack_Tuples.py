fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits # allowed to extract the values back into variables

print(green) # print apple 
print(yellow) # print banana
print(red)  # Due to *red all remaining values store in it (when num of value less the variable then use *)


(green, *tropic, red) = fruits

print(green) # assign Fist index 
print(tropic) # all remaining index
print(red)  # assign last index 