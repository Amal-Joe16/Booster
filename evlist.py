a=int(input("Enter no. of numbers in list"))
c=[]
ev=[]
for i in range(a):
    b=int(input("Enter the number:"))
    c.append(b)
    if b%2==0:
        ev.append(b)
print("OG list: ",c)        
print("even list: ",ev)        



