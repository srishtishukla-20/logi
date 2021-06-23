a = ["a","b","c","d","e","f","g","h","i"]
#op:[[a,d,g][b,e,h][c,f,i][d,g][e,h][f,i][g][h][i]]
i=0
list=[]
while i<len(a):
    j=i
    list2=[]
    while j<len(a):
        list2.append(a[j])
        j+=3
    list.append(list2)
    i+=1
print(list)


