def vatCalculate(Price) :
    result = Price + (Price*0.07)
    return float(result)
Price = float(input("ป้อนราคา : "))
print("ราคา = %.2f บาท" %Price,"\nราคารวม vat = %.2f" %vatCalculate(Price),"บาท")
