#for sentence with numbers
name=input("enter any word which contain , . !=")
user=name.split(" ")
i=0
e=[]
s=[]
while i<len(user):
    j=0
    sum=0
    while j <len(user[i]):
        if user[i]>="a" and user[i]<="z":
            sum+=ord(user[i][j])-96
        else:
            sum+=ord(user[i][j])-64
        j+=1
    e.append(sum)
    s.append(user[i])
    k=0
    while k<len(e):
        if e[i]<e[k]:
            tem=e[i]
            e[i]=e[k]
            e[k]=tem
            s[i],s[k]=s[k],s[i]
        k=k+1
    i+=1
print(s)
print(e)