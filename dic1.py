marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(len(marks))
list=[]
list1=[]
for i in marks.values():
    if i not in list:
        list.append(i)
for j in marks:
    if j not in list1:
        list1.append(j)
a=0
d={}
while a<len(list):
    a1=0
    while a1<len(list[j]):
        d={list1[j]:{list[j]}}
        print(d)
    a1+=1
a+=1










