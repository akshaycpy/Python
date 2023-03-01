data={}
n=int(input("Enter the number of inputs:"))
for i in range(n):
    name=input("Enter the name:")
    did=int(input("Enter the id:"))
    data[did]=[name]
data1={}
m=int(input("Enter the number of inputs:"))
for i in range(m):
    name=input("Enter the name:")
    did=int(input("Enter the id:"))
    data1[did]=[name]
data.update(data1)
print(data)