# # ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set4 = {5,6}

#   union()
set3 = set1.union(set2)
set4 = set3 | set4  # union 2 or more set
myset = set1.union(set2, set3, set4)

# # update() method inserts the items in set2 into set1:

# set1.update(set2)

# # intersection() method will return a new set, that only contains the items that are present in both sets.

# set3 = set1.intersection(set2)

# # & operator instead of the intersection() method, and you will get the same result

# set3 = set1 & set2

# # intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set

# set1.intersection_update(set2)

# # difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

# set3 = set1.difference(set2)

# # difference_update() method to keep only the items from the first set that are not present in the other set:

# set1.difference_update(set2)

# # symmetric_difference() method will keep only the elements that are NOT present in both sets

# set3 = set1.symmetric_difference(set2)

# # ^ operator instead of the symmetric_difference() method, and you will get the same result

# set3 = set1 ^ set2

# # symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

# set1.symmetric_difference_update(set2)


print(set4)
print (set1)
print (myset)