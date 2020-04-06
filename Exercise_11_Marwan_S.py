x = int(input("จำนวนแถวของความสูงพีระมิดที่ต้องการ : "))
sum = 1
i = 0
for i in range(x):
    space = " "*(x-i)
    print(space,"*" *(sum))
    sum += 2
    i+=1
