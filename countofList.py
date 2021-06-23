a=[["Bengali"],["Tamil"],["Tamil"],["Tamil"],["Hindi"],["Bengali"],["Telugu"],["Malayalam"],["Malayalam"],["Marathi"]]
flat_list = []
for element in a:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
print(flat_list)
i=0
dic={}
while i<len(flat_list):
    j=0
    count=0
    while j<len(flat_list):
        if flat_list[i]==flat_list[j]:
            count+=1
            dic[flat_list[i]]=count
        j+=1
    i+=1
print(dic)
#count_occurences

