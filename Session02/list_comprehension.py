names=['MUMBAI','PUNE','AHMEDABAD']
lower_names=[i.lower() for i in names]
print(lower_names)
nos=[1,2,3,4]
double_nos=[i*i for i in nos]
print(double_nos)

mylist=[1,2,3,4]
new_list=[i for i in mylist if(i>2)]
print(new_list)
new_list=[i if(i>2) else(0) for i in mylist]
print(new_list)
