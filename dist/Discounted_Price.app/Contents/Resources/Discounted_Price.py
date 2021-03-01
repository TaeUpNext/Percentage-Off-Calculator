from tkinter import *

def discountedPrice():
    price=eval(priceEnt.get())
    discount=eval(percentEnt.get())
    percentOff=discount/100
    discountAmount=price*percentOff
    newPrice=(price-discountAmount)
    newPriceSum=(f'{newPrice:,.2f}')
    results.set(newPriceSum)




master=Tk()
master.title('Discounted Price')
master.config(bg='grey')

#creates a the price label and entry box 
priceLbl=Label(master,bg='grey',fg='white',text='Enter the price of the item: ',font=('Arial',14))
priceLbl.grid(row=0,column=0,padx=5,pady=15,sticky=E)
priceEnt=Entry(master)
priceEnt.grid(row=0,column=1,sticky=W,pady=15,padx=10)
priceSign=Label(master,text='$',bg='grey',fg='white')
priceSign.grid(row=0,column=1,sticky=W)
 

#creates the percent off label and entry box
percentLbl=Label(master,bg='grey',fg='white',text='Enter the price of the item: ',font=('Arial',14))
percentLbl.grid(row=1,column=0,padx=5,pady=15,sticky=E)
percentEnt=Entry(master)
percentEnt.grid(row=1,column=1,pady=15,padx=15)
percentSign=Label(master,text='%',bg='grey',fg='white')
percentSign.grid(row=1,column=1,sticky=W,)

#Creates the button to calculate
calcButton=Button(master,text='Calculate',font=('none',13),command=discountedPrice)
calcButton.grid(row=2,column=0,columnspan=2,sticky=S,pady=20)



#creates the percent off label and entry box
results=StringVar()
resultLbl=Label(master,bg='grey',fg='white',text='Discounted Price: ',font=('Arial',14))
resultLbl.grid(row=3,column=0,padx=5,pady=15,sticky=W)
resultEnt=Entry(master,state='readonly',text=results,fg='green')
resultEnt.grid(row=3,column=1,pady=15,padx=10,sticky=W)
resultSign=Label(master,text='$',bg='grey',fg='white')
resultSign.grid(row=3,column=1,sticky=W,)                
