def collatz(x):
             steps = 0

             while x!=1:
                          print(x,end='')
                          print("\n")
                          if x%2 == 0:
                                       x = x/2
                          else:
                                       x = (3*x) +1

                          steps += 1

             print(1)
             return steps

n = int(input("enter the no"))
steps = collatz(n)
print("total no of stepos",steps)
