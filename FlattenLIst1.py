list1=[1,2,[3,4,5],6,7,[8,9,10],[-1,-2,-3]]
newlist=[]
l=[]
for i in list1:
    if type(i)==list:
        l.append(i)
        k=0
        l1=[]
        while k<len(l):
            j=0
            while j<len(l[k]):
                if l[k] not in l1:
                    l1.append(l[k][j])
                j+=1
            k+=1
    else:
        newlist.append(i)
list2=l1+newlist
list2.sort()
print(list2)

