list1=[1,[2,3],4,[5,6],7]
list2=[]
list3=[]
i=0
count=1
while i<len(list1):
    if i%2!=0:
        list2.append(list1[i])
        #print(list2)
    else:
        list3.append(list1[i])
        #print(list3)
    i+=1
k=0
l=[]
while k<len(list2):
    j=0
    while j<len(list2[k]):
        if list2[k] not in l:
            l.append(list2[k][j])
            print(l)
        j+=1
    k+=1
list=list3+l
list.sort()
print(list)



