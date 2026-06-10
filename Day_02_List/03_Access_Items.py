mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print ("First item", mylist[0]) #start from 0
print ("Last item", mylist[-1]) #start from -1
print (mylist[2:4]) # 4th index will not print
print (mylist[:5])  # auto start from 0 index
print (mylist[-3:]) # auto start from most last index

# Check if item Exists

if 'apple' in mylist:
    print ("Yes! 'apple' is in the list.")