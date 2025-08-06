l1=[]
l2=[]
a=int(input("Enter the range of the list: "))
for i in range(a):
    x=int(input("Enter the element: "))
    l1.append(x)
print("the given list is \n",l1)
for i in l1:
    if i not in l2:
        l2.append(i)
print("the new list is \n",l2)           