def pal(str):
             if str == str[::-1]:
                          return "is palindrome"
             else:
                          return "nooooo"


str = input("enter string")

print(pal(str))
