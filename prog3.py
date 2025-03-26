def info():
    name = input("enter urname")
    email = input("enter email")
    address = input("enter address")
    phno = input("enter phone no")

    return name,email,address,phno


def print_info(name,email,address,phno):

    print("persnal details")
    print("name:",name)
    print("email:",email)
    print("address:",address)
    print("phone number:",phno)


name,address,email,phone = info()
print_info(name,email,address,phone)

    
                  
