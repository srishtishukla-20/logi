a="hello"
b=a.split()
j=""
i=0
while i<len(a):
    if a[i] not in j:
        j+=a[i]
    i+=1
print(j)
#remove duplicates
d="mamatha"
b=""
i=0
while i<len(d):
    if i==0:
        b+=d[i]
    if i==1:
        b+=d[i]
        b+=d[-i-1]
        b+=d[-i]
    i+=1
print(b)
#gives 1st 2 and last 2 output