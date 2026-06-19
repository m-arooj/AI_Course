tuple_1 = (1, "banana", 5 , 8)

for x in tuple_1:
  print(x)
  
# Use the range() and len() functions to create a suitable iterable
for i in range(len(tuple_1)):
  print(tuple_1[i])

# Print all items, using a while loop to go through all the index numbers
i = 0
while i < len(tuple_1):
  print(tuple_1[i])
  i = i + 1