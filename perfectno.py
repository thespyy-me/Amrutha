n = int(input("enter the no"))
s = 0

for i in range(1,n):
             if n % i == 0:
                          s+=i


if s == n:
             print("the no is perfect no")
else :
             print("the no is not perfect")
