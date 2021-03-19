import random
mylist=[random.randint(1,5) for i in range(0,10) ]
print("Exercise 1: ",end="")
print(mylist)

#Converting lists within lists to single list
listoflists=[[1,2,3],[4,5,6],[7,8,9]]
results=[]
for sublist in listoflists:
    for inner_value in sublist:
        results.append(inner_value)
print("Exercise 2: ",end="")
print(results)

#Flattening using list comprehension
print("Exercise 2 method 2: ",end="")
results=[inner_value for sublist in listoflists for inner_value in sublist]
print(results)
