def welcome():
    print("******Welcome to Food Shop ******")
    print()


def info():
    global name
    name = input("Can I know your good name : ")

    print("Hey " + name + "! Good to see you here!!!")
    print("You are on right place ,I will help you to book your dish and drinks ")
    print()


def menu():
    print('''Here is your menu with their prices
1.Pizza RS.200
2.Mango Juice RS.70
3.Apple Juice RS.80''')


def order(price, product):
    print()
    print("Thank you for choosing " + product)
    print()

    print("Please give us some more information about you!!!!")

    mob = input("Enter your mobile number : ")
    add = input("Enter your address of delivery : ")

    print('''Choose payment of mode :
1.Online
2.Cash on delivery''')

    pay = input()

    paymode = ""

    if(pay == "2"):
        paymode = "Cash on delivery"
    else:
        paymode = "Online"

    print()

    print('''*******Here is detail of selected order******''')

    print()

    print("Customer Name : " + name)
    print("Product name: " + product)
    print("Price of product : " + str(price))
    print("Mode of payment : " + paymode)
    print("Delivery Address : " + add)

    print()

    b = input("Please confirm by pressing 1 else 0 to cancel ")

    print()

    if(b == "1"):
        print()
        print("*******Your order is booked successfully*******")

        print("Customer Name : " + name)
        print("Product name: " + product)
        print("Price of product : " + str(price))
        print("Mode of payment : " + paymode)
        print("Delivery Address : " + add)

        print()
        print("Thank you for your interest !!! Have a nice day !!!")

    else:
        print("*****Thank you for visit !!!! Have a nice day !!! *****")


def choice():
    print("Please select product which you wish : ")

    price = 0

    a = input()

    if(a.lower() == "pizza"):
        price = 200
        order(price, a)

    elif(a.lower() == "mango juice"):
        price = 70
        order(price, a)

    elif(a.lower() == "apple juice"):
        price = 80
        order(price, a)

    else:
        print("You have not selected any product....")
        print("Thank you for visit !!!! Have a nice day!!!!")


welcome()
info()
menu()
choice()