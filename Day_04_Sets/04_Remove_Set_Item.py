set1 = {'apple', 'banana','rr', 'cherry', 'add'}

set1.remove('rr') # If the item to remove does not exist, remove() will raise an error.
set1.discard("pp") # If the item to remove does not exist, discard() will NOT raise an error.

x = set1.pop() # (debugging) to check which item is removed 

print(x) # remove first item adter assanding order

# set1.clear()  # clear() method empties the set
# del set1     # del keyword will delete the set completely
 
print(set1)