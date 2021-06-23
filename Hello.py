a="hello"
a.split()
l=["a","e","i","o","u"]
i=0
c=0
while i<len(a):
    if a[i] in l:
        c=i*100
        Number = 1
        sum=0
        while(Number <=c):
            count1 = 0
            j = 2
            while(j <= Number//2):
                if(Number % j == 0):
                    count1 = count1 + 1
                    break
                j+= 1
            if (count1 == 0 and Number != 1):
                sum=sum+Number
            Number = Number  + 1
        b=str(sum)
        b.split()
        k=0
        sum2=0
        list=[]
        while k<len(b):
            sum2=int(b[k])+sum2
            k+=1
        u=str(sum2)
        f=int(u)
        list=[]
        list1=[]
        if f=="7":
            list.append(f)
        else:
            list.append(f)
        print(list)
        list1.append(list)
        print(list1)

        
    i+=1
