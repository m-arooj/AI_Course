mylist1 = [1, 2, 3, 4, 5, 6]

mylist2 = ('EXTEND', 'EXTEND') # This is Tuple(imutable)
mylist1.append('APPEND') # add an item in the end
mylist1.insert(1, 'INSERT') # add an item in specified index
mylist1.extend(mylist2)


print ("Updated list:",mylist1)