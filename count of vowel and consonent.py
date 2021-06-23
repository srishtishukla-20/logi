vowel=("a","e","i","o","u")
count = 0
count1 = 0 
user= input("enter sentence")
i=0
while i<len(user):  
    if user[i] in vowel:  
        count = count + 1  
    elif (user[i] >= 'a' and user[i] <= 'z'):  
        count1 = count1 + 1
    i+=1  
print("vowel:",count) 
print("consonent:",count1) 
#number of vowel and consonents