from tkinter import *
from datetime import date, datetime 
from fpdf import FPDF

productNames = [""]*100000
productPrices = [0]*100000
noOfItems = 0

def addToCart():
    global noOfItems
    global productNames
    global productPrices
    
    noOfItems = noOfItems + 1
    productName = str(entryBox4.get())
    productPrice = int(entryBox5.get())
    productNames[noOfItems] = productName
    productPrices[noOfItems] = productPrice
    

def display():
    customerName = str(entryBox1.get())
    customerMobile = str(entryBox2.get())
    customerEmail = str(entryBox3.get())
    
    global productNames
    global productPrices
    global noOfItems

    j= 1
    total = 0
    while(j<=noOfItems):
        total = total + productPrices[j]
        j = j+1

    global discount
    if(total>1000 and total<2500): discount = 0.025 * total
    elif(total>2500 and total<5000): discount = 0.05 * total
    elif(total>5000 and total<7500): discount = 0.1 * total
    elif(total>7500 and total<10000): discount = 0.15 * total
    elif(total>10000): discount = 0.2 * total
   
    final_amt = total - discount

    txt1 = "Customer's Name : " + customerName
    txt2 = "Customer's Contact Number : " + customerMobile
    txt3 = "Customer's Email ID : " + customerEmail
    txt4 = "Gross Total : " + str(total)
    txt5 = "Discount : " + str(discount)
    txt6 = "Amount to be Paid : " + str(final_amt)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times",'BIU',size = 35)
    pdf.cell(200,20,txt="Big Bazaar Bill Receipt",ln=1,align="C")
    pdf.set_font("Times",'I',size = 15)
    pdf.cell(200,10,txt=txt1,ln=3,align="L")
    pdf.cell(200,10,txt=txt2,ln=4,align="L")
    pdf.cell(200,10,txt=txt3,ln=5,align="L")

    pdf.cell(200,10,txt=txt4,ln=7,align="L")
    pdf.cell(200,10,txt=txt5,ln=8,align="L")
    pdf.cell(200,10,txt=txt6,ln=9,align="L")


    pdf.set_font("Times",'BI',size = 22)
    pdf.cell(200,10,txt="Items :-",ln=15,align="L")
    pdf.set_font("Times",'I',size = 15)

    k=1
    while(k<=noOfItems):
        textPrint = productNames[k] + "  :  " + str(productPrices[k])
        pdf.cell(200,10,txt=textPrint,ln=18,align="L")
        k = k + 1

        
    pdf.output("Bill.pdf")
    

window = Tk()
window.geometry("500x390")
window.title("Bill Calculation Dashboard ")

bgImg = PhotoImage(file="bg.png")
bgLabel = Label(window,image=bgImg)
bgLabel.place(x=0)

heading = Label(window,text="Big Bazaar",font=("Cambria",30),bg="Black",fg ="Orange")
heading.place(x=150)

now = datetime.now()
data = now.strftime("%A , %d-%m-%Y %H:%M")

label1 = Label(window,text=data,font=("Times New Roman",15),bg="Black",fg="White")
label1.place(x=120,y=45)

label2 = Label(window,text="Customer's name : ",font=("Times New Roman",15),bg="Black",fg="Blue")
label2.place(y=100)

label3 = Label(window,text="Customer's Contact Number : ",font=("Times New Roman",15),bg="Black",fg="Blue")
label3.place(y=130)

label4 = Label(window,text="Customer's Email ID : ",font=("Times New Roman",15),bg="Black",fg="Blue")
label4.place(y=160)


entryBox1 = Entry(window,width=25,bg="Light Grey",font=("Times New Roman",13),fg="Black")
entryBox1.place(x=260,y=103)

entryBox2 = Entry(window,width=25,bg="Light Grey",font=("Times New Roman",13),fg="Black")
entryBox2.place(x=260,y=133)

entryBox3 = Entry(window,width=25,bg="Light Grey",font=("Times New Roman",13),fg="Black")
entryBox3.place(x=260,y=163)

label5 = Label(window,text="Product Name : ",font=("Times New Roman",13),bg="Black",fg="Blue")
label5.place(x=5,y=250)

label6 = Label(window,text="Product Price : ",font=("Times New Roman",13),bg="Black",fg="Blue")
label6.place(x=5,y=280)

entryBox4 = Entry(window,width=20,bg="Light Grey",font=("Times New Roman",13),fg ="Black")
entryBox4.place(x=140,y=253)

entryBox5 = Entry(window,width=20,bg="Light Grey",font=("Times New Roman",13),fg ="Black")
entryBox5.place(x=140,y=283)

addButton = Button(window,text="Add to Cart",font=("Times New Roman",13),fg ="White",bg="Red",command=addToCart)
addButton.place(x=350,y=260)

submitButton = Button(window,text="Submit",width="15",font=("Times New Roman",13),fg ="White",bg="Black",command=display)
submitButton.place(x=150,y=340)


window.mainloop()

