n=int(input("enter the number of tuples"))
m=[]
for i in range(n):
    x=int(input("enter any x : "))
    y=int(input("enter any y : "))
    m.append((x,y))
print("original list")
print(m)
for i in range(n):
    for j in range(i+1,n):
        if m[i][1]>m[j][1]:
            m[i],m[j]=m[j],m[i]
print("sorted list")
print(m)
    