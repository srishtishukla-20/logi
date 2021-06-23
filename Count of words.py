a="my name is  best srishti and my  best family is best"
List=a.split()  
user=input("enter your word") 
count=0
i=0
dict={}
while i<len(List):
    if List[i]==user:
        count+=1
        dict[count]=List[i]
    i+=1
print(dict)

                                                               