a=int(input("Enter the limit:"))
d=[]
for i in range(a):
    i=int(input("Enter the number:"))
    if(i<=100):
        d.append(i)
    else:
        d.append('over')
print(d)