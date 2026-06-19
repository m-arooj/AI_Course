list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3] # round-brackets
list3 = [True, False, False]
multype = ["abc", 35, True, 6.7, 'm@le']

# List Items data types

print (f"String List: {list1} \nInt List: {list2} \nMul Datatype List:", multype) #Print List
print (type(list1))   #<class 'list'>

# check type of each element(index) inside the list

for item in multype:
    print (item, "Type", type(item))
    
print (type(list1[2])) #Type of selected index
print (type(list2[3]).__name__) #Print only DataType