usernameInput = input("Username : ")
paswordInput = input("Password : ")
if usernameInput == "admin" and paswordInput == "1234" :
    print("ไปรษณีย์ไทย สาขาหลักสี่")
    print("รายการสินค้ามีดังนี้")
    print("กล่อง ก ราคา 9 บาท")
    print("กล่อง ข ราคา 12 บาท")
    print("กล่อง ค ราคา 16 บาท")
    print("กล่อง ง ราคา 10 บาท")
    product = (input("กรุณาระบุชื่อสินค้า หรือ สแกนบาร์โค้ดสินค้า : "))
    quantity = int(input("จำนวน : "))
    if product == "1" or product == "กล่อง ก":
        print("กล่อง ก จำนวน",quantity,"เป็นเงิน : %0.2f" %(quantity*9),"บาท")
    elif product == "2" or product == "กล่อง ข":
        print("กล่อง ข จำนวน",quantity,"เป็นเงิน : %0.2f" %(quantity*12),"บาท")
    elif product == "3" or product == "กล่อง ค":
        print("กล่อง ค จำนวน",quantity,"เป็นเงิน : %0.2f" %(quantity*16),"บาท")
    elif product == "4" or product == "กล่อง ง":
        print("กล่อง ง จำนวน",quantity,"เป็นเงิน : %0.2f" %(quantity*20),"บาท")
else :
    print("เกิดข้อผิดพลาด โปรดตรวจสอบข้อมููล")
