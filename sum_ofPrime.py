 
Number = 1
sum=0

while(Number <= 400):
    count = 0
    i = 2
    
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        sum=sum+Number
    Number = Number  + 1
print(sum)
a=str(sum)
a.split
k=0
sum2=0
while k<len(a):
    sum2=int(a[k])+sum2
    k+=1
print(sum2)
