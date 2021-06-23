user = input("enter your sentence")
list = []
a=""
i=0
while i<len(user):
    if user[i] ==" ":
        list.append(a)
        a =" "
    else:
        a=a+user[i]
    i+=1
if a:
    list.append(a)
print(list)
#without split
