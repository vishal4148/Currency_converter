#                             CURRENCY_CONVERTER


#*******************************import_libraries*******************************
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from forex_python.converter import CurrencyRates

#*******************************Creating GUI window*****************************
root = tk.Tk()

root.title("Currency converter")   

Top= Frame(root, bg='#e6e5e5', pady= 2 , width=1850, height=100, relief="ridge")
Top.grid(row=0, column=0)

head_label = tk.Label(Top,font=('lato black',19,'bold'),
	text='                             Currency converter              '              ,bg='#e6e5e5', fg='black')
head_label.grid(row=1,column = 0,sticky=W)

#********************************Currency class*********************************


variable_1 = tk.StringVar(root)
variable_2 = tk.StringVar(root)

variable_1.set('Currency')
variable_2.set('Currency')

def CurrencyConverter():
	from forex_python.converter import CurrencyRates
	c= CurrencyRates()

	from_currency = variable_1.get()
	to_currency = variable_2.get()

	if(Amount_1_field.get()== ""):
		tkinter.messagebox.showinfo("Error !!!","Sorry :( \n Please enter valid amount.\n Amount not entered!!")

	elif (from_currency == "currency" or to_currency == "currency"):
		tkinter.messagebox.showinfo("Error!!","You Currency Not Selected.\n Please select From Menu.")

	else:
		new_amount = c.convert(from_currency , to_currency, float(Amount_1_field.get()))
		new_new_amount = float("{:.4f}".format(new_amount))
		amount_2_field.insert(0,str(new_new_amount))



def clear_all():
	Amount_1_field.delete(0, tk.END)
	amount_2_field.delete(0,tk.END)

#*****************************************Currency converter UI************************************

Currency_code_list =["INR", "USD", "CAD", "CNY","DDK", "EUR","GBP","JPY","SGD","NZD"]

root.configure(background='#e6e5e5')
root.geometry("700x400")

Label_1 = Label(root, font=(' black', 14, 'bold'), text="                   welcome", padx=200,
 pady=15, bg="#e6e5e5", fg="red")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Enter Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t                 From  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t                     To  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)


#******************************Main Function*************************************

from_currency_option = tk.OptionMenu(root, variable_1,*Currency_code_list)
To_currency_option = tk.OptionMenu(root,variable_2,*Currency_code_list)

from_currency_option.grid(row=3,column=0,ipadx=45,sticky=E)
To_currency_option.grid(row=4,column=0,ipadx=45,sticky=E)

Amount_1_field=tk.Entry(root)
Amount_1_field.grid(row=2,column=0,ipadx=28,sticky=E)

amount_2_field=tk.Entry(root)
amount_2_field.grid(row=8,column=0,ipadx=31,sticky=E)

Label_3 = Button(root,font=('arial',15,'bold'),text="  Convert ",padx=2,pady=2,bg='lightblue',fg='white',
	command=CurrencyConverter)
Label_3.grid(row=6,column=0)

label_1 =Label(root,font=('lato black',7,'bold'),text="",padx=2,pady=2,bg='#e6e5e5',fg='black')
Label_1.grid(row=9,column=0,sticky=W)

Label_3=Button(root,font=('arial',15,'bold'),text="  Clear All  ",padx=2, pady=2, bg='lightblue',fg='white',
	command = clear_all)
Label_3.grid(row=10,column=0)

root.mainloop()  