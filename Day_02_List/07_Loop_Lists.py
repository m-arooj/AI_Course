mylist = [0.0, 1, 2, 3.0, 4.0, 5.0]

for x in mylist:
    print (x)   # print through items type(x)

[print(x) for x in mylist] # Print through items in 1 line

for x in range(len(mylist)):
  print("index ", x , "   Value", mylist[x])   # Print through item's index

i = 0
while i < len(mylist):    # list with While loop
    print (mylist[i])
    i += 1



# for index, value in enumerate(mylist):        
#     print("Index:", index, "Value:", value)