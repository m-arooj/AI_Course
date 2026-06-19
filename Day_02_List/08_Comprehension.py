fruits = ["apple", "banana", "cherry", "kiwi", 'app', "mango"]
newlist = []

for x in fruits:       # run loop till num of items
    if "app" in x:     # compair app in x 
       newlist.append(x)   # add x at end of new list
print(newlist)

# With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"] 

#newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if "a" in x] # return value is a new list, leaving the old list unchanged.
# newlist = [x for x in fruits if x != "apple"] #Only accept items that are not "apple":
# newlist = [x for x in fruits]    # With no if statement:
# newlist = [x for x in range(10)] # You can use the range() function to create an iterable:
# newlist = [x for x in range(10) if x < 5] #Accept only numbers lower than 5:
# newlist = [x.upper() for x in fruits]      # Set the values in the new list to upper case:
# newlist = ['hello' for x in fruits] # Set all values in the new list to 'hello':
# newlist = [x if x != "banana" else "orange" for x in fruits] # Return "orange" instead of "banana":

print(newlist)