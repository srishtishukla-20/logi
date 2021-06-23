lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
for num in range(lower,upper + 1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10  
if num == sum:
    print(num)

    # 2, 3, 4, 5, 6, 7, 8, 9
3	#153, 370, 371, 407