# Convert the tuple into a list to be able to change it:

tuple1 = (1, 2, 3, 4, 5, 8, 0)
tuple2 = ('New Tuple Value',)

list1 = list(tuple1)  # Tuple to List Convirsion
list1[2] = 'UPdate'    # update 2nd index
list1.append('APPEND')
list1.remove(0) # remove 0

tuple1 = tuple(list1)  # list to Tuple Conversion 
tuple1 += tuple2 # Create a new tuple with the value "orange", and add that tuple:

# del tuple1 # print cauese (error) because tuple is del

print (tuple1)