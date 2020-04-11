menuList = []
priceList = []
def showBill():
    Shop = "Marwan"
    print(Shop.center(20, "-"))
    for i in range(len(menuList)):
        print(menuList[i].ljust(15),priceList[i])
    total = str(sum(priceList))
    print("ราคารวม",total.center(15))
    print("-".center(20, "-"))

while True :
    menuName = input("Please Enter Menu : ").capitalize()
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
