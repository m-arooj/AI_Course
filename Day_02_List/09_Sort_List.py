list1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list1.sort()

print(list1) # ascending

list1.sort(reverse = True) # descending
print(list1)

def myfunc(n):
  return abs(n - 50)

list2 = [100, 50, 40 , 60, 65, 82, 23] #Sort the list based on how close the number is to 50:

list2.sort(key = myfunc)  #keyword argument key = function.

print(list2)

## (Error) sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# list4 = ["banana", "Orange", "Kiwi", "cherry"]
# list4.sort()
# print(list4)

list3 = ["banana", "Orange", "Kiwi", "cherry"] 
list3.sort(key = str.lower)  # case-insensitive sort use str.lower as a key function
print(list3)

list3.reverse()     #Reverse list item 
print (list3)