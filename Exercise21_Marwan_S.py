from tkinter import *
from tkinter import ttk
import math

def LeftClickButton(event):
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    #print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    textResult.configure(text= "%0.2f" %result)
    if result >= 30 :
        textSize.configure(text="อ้วนมาก",foreground='red' , font= ("Kanit Medium",16))
        textSize.grid(row=4,columnspan=2)
    elif result >= 25 and result <= 29.9 :
        textSize.configure(text="อ้วน", foreground = 'orange', font= ("Kanit Medium",16))
        textSize.grid(row=4, columnspan=2)
    elif result >=23 and result <= 24.9 :
        textSize.configure(text="น้ำหนักเกิน", foreground = 'yellow', font= ("Kanit Medium",16))
        textSize.grid(row=4, columnspan=2)
    elif result >= 18.6 and result <= 22.9:
        textSize.configure(text="ปกติ เหมาะสม", foreground='green', font= ("Kanit Medium",16))
        textSize.grid(row=4, columnspan=2)
    elif result <= 18.5 :
        textSize.configure(text="ผอมเกินไป", foreground = 'pink', font= ("Kanit Medium",16))
        textSize.grid(row=4, columnspan=2)
    else:
        pass

mainwindow = Tk()
mainwindow.title("โปรแกรมคำนวณ BMI")
labelTitle = ttk.Label(mainwindow,text="คำนวณ BMI", font= ("Kanit Medium",18),foreground='red')
labelTitle.grid(row=0,columnspan=2,padx=50,pady=10)
labelHeight = ttk.Label(mainwindow,text="ส่วนสูง (cm.)")
labelHeight.grid(row=1,column=0)
textBoxHeight = ttk.Entry(mainwindow,width=15)
textBoxHeight.grid(row=1,column=1)
labelWeight = ttk.Label(mainwindow,text="น้ำหนัก (kg.)")
labelWeight.grid(row=2,column=0,padx=10,pady=10)
textBoxWeight = ttk.Entry(mainwindow,width=15)
textBoxWeight.grid(row=2,column=1)
labelResult = ttk.Label(mainwindow,text="ผลลัพธ์ : ")
labelResult.grid(row=3,column=0,padx=10,pady=10)
textResult = ttk.Label(mainwindow)
textResult.grid(row=3,column=1)
textSize = ttk.Label(mainwindow)
textSize.grid(row=4,column=1)
CalculateButton = ttk.Button(mainwindow,text="คำนวณ")
CalculateButton.bind('<Button-1>' , LeftClickButton)
CalculateButton.grid(row=5,columnspan=2,padx=10,pady=10)
mainwindow.mainloop()
