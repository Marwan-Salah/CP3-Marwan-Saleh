def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        print("User or Password Incorrect")
        login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()
def menuSelect():
    userselected = int(input("please select 1 or 2 :"))
    if  userselected == 1 :
        return vatCalculate(float(input("Enter Price : ")))
    elif  userselected == 2 :
        return priceCalculate()
    else :
        showMenu()
def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*0.07)
    print("ราคารวม vat = %.2f" %result,"บาท")
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1+price2)

login()
