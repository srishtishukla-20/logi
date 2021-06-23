# user=int(input("enter value"))
# i=1

# while i<user:
#     Even=user-i
#     if Even%2==0:
#         count=3
#         if count<=user:
#             print(Even)
#         count+=1
#     i+=1

user=int(input("enter value"))
i=1
count=1
while i<user:
    if user%(2)==0:
        if count<=3:
            print(user)
        count+=1
j=1
count1=1
while j<user:
    if user%2!=0:
        if count1<=3:
            print(user)
        count1+=1
    user+=j
    user-=i
        