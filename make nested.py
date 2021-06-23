a=[1,2,3,4,5]
i=0
list1=[]
list2=[]
list=[]
count=0
i=0
while i<len(a):
    if count<=2:
        list1.append(a[i])
    else:
        list2.append(a[i])
        
    i+=1
    count+=1
list.append(list1)
list.append(list2)
print(list)