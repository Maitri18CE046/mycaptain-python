n = int(input("How many terms you want:"))

n1 = 0
n2 = 1
temp = 0

if n<=0:
    print("Enter vaild integer number")
elif n==1:
    print(n1)
else:
    while temp<n:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        temp = temp + 1
    
