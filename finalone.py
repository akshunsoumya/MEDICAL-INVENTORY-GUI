from tkinter import *
import csv
import sys
from tempfile import NamedTemporaryFile
import shutil #The shutil module helps you automate copying files and directories.
import datetime as d #The datetime module is used to modify date and time objects in various ways.
#defination of subbuttons(def of MEDICINE BLOCK)
def add_medicine():
	with open('medicine.csv','a+') as csvfile:
		columns = ['medi_name','med_id','sale','unit','quantity','min_quantity', 'comp_name', 'sup_id','to_pur']
		writer = csv.DictWriter(csvfile,fieldnames = columns)

		medi_name = input("Enter medicine name : ")
		with open('medicine.csv','r+') as csfile:
			reader=csv.DictReader(csfile)


		med_id = input("Enter ID : ")
		sale = float(input("Enter sale price : "))
		unit = float(input("Enter cost price : "))
		quantity = int(input("Enter quantity : "))
		min_quantity = int(input("Enter min quantity to maintain : "))
		comp_name = input("Enter company name : ")
		sup_id = input("Enter supplier ID : ")
		cost = unit * quantity
		to_pur = min_quantity - quantity
		if quantity >min_quantity:
			to_pur = 0
		writer.writerow({'medi_name':medi_name,'med_id':med_id,'sale':sale,'unit':unit,'quantity':quantity,\
		'min_quantity':min_quantity,'comp_name':comp_name,'sup_id':sup_id,'to_pur':to_pur})


		with open('purchase.csv','a+') as csvfile:
			pur_date= d.strftime("%d")
			pur_month= d.strftime("%m")
			pur_year = d.strftime("%Y")
			columns = ['medi_name','med_id','unit','quantity','pur_date', 'pur_month','pur_year','sup_id','cost']
			writer = csv.DictWriter(csvfile,fieldnames = columns)

			writer.writerow({'medi_name':medi_name,'med_id':med_id,'unit':unit,'quantity':quantity,'pur_date':pur_date,'pur_month':pur_month,'pur_year':pur_year,'sup_id':sup_id,'cost':cost})
#defination of subbbuton under the medicine block(i.e= SEARCH MEDICINE)
def search_medicine():
    with open('medicine.csv','r') as csvfile:
        name=input('Enter the medicine to search : ')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['medi_name'] == name:
                print(' Name :', row['medi_name'],'\n','Quantity : ',row['quantity'],'\n','Price : ',row['sale'])
#defination of subbuton under the Medicine block (UPDATE MEDICINE)
def update_medicine():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    columns = ['medi_name','med_id','sale','unit','quantity','min_quantity','comp_name', 'sup_id','to_pur']
    with open('medicine.csv', 'r+') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=columns)
        writer.writeheader()
        med_name =input('Enter the name of the medicine you want to modify : ')
        for row in reader:
            if row['medi_name'] == med_name:
            	print('---------------------------------------------')
            	print('|1.To update Name                           |')
            	print('---------------------------------------------')
            	print('|2.To update Cost price                     |')
            	print('---------------------------------------------')
            	print('|3.To update Sale price                     |')
            	print('---------------------------------------------')
            	print('|4.To update supplier ID                    |')
            	print('---------------------------------------------')
            	choice=int(input())
            	if(choice==1):
            		row['medi_name']=input("Enter the new name : ")

            	elif(choice==2):
            		row['cost']=input("Enter the new cost price : ")

            	elif(choice==3):
            		row['sale']=input("Enter the new sale price : ")

            	elif(choice==4):
            		row['sup_id']=input("Enter the new supplier ID : ")
            row = {'medi_name':row['medi_name'],'med_id':row['med_id'],'sale':row['sale'],'unit':row['unit'],'quantity':row['quantity'],\
		    'min_quantity':row['min_quantity'],'comp_name':row['comp_name'],'sup_id':row['sup_id'],'to_pur':row['to_pur']}
            writer.writerow(row)
    shutil.move(tempfile.name, 'medicine.csv')



#Defination of the sub button under the Medicine Block(MEDICINE TO BE PURCHASED)
def medicine_to_be_purchased():

	with open('medicine.csv','r') as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
				print(' Name : ', row['medi_name'],'\n','Quantity : ',row['quantity'],'\n','Minimum Quantity : ',row['min_quantity']\
				,'\n','To be purchased : ',row['to_pur'],'\n','Supplier ID : ',row['sup_id'])

 #defination of B1(MEDICINE) main
# medicine Menu

def B1fun(top):
    medicine_menu_window = Tk()
    medicine_menu_window.geometry('400x400')
    medicine_menu_window.title("Pharmacy Management Software")
    medicine_menu_window.config(bg="#232528")

    lbl = Label(medicine_menu_window, text="Medicine Menu!",font=("consolas bold",15),height=1,width=35,bg="#232528",fg="white",bd=0)
    lbl.place(x=20,y=5)
    lbl2 = Label(medicine_menu_window, text="What would you like to do!",font=("consolas bold",15),height=1,width=35,bg="#232528",fg="white",bd=0)
    lbl2.place(x=20,y=45)
    btn1 = Button(medicine_menu_window, text="Add New Medicine",width=44,pady=10,fg="black",activebackground="grey",bg="#00ffff",command=add_medicine)
    btn1.place(x=40,y=90)
    btn2 = Button(medicine_menu_window, text="Search Medicine",width=44,pady=10,fg="black",activebackground="grey",bg="#00ffff",command=search_medicine )
    btn2.place(x=40,y=135)
    btn3 = Button(medicine_menu_window, text="Update Medicine",width=44,pady=10,fg="black",activebackground="grey",bg="#00ffff",command=update_medicine)
    btn3.place(x=40,y=180)
    btn4 = Button(medicine_menu_window, text="Medicines to be purchased",width=44,pady=10,fg="black",activebackground="grey",bg="#00ffff",command=medicine_to_be_purchased)
    btn4.place(x=40,y=225)
    top.withdraw()
    def back():
            top.deiconify()
            medicine_menu_window.destroy()

    btn5 = Button(medicine_menu_window, text="Return to main menu",width=44,pady=10,fg="black",activebackground="grey",bg="#00ffff",command=back)
    btn5.place(x=40,y=270)
    b6 = Button(medicine_menu_window,text="EXIT",width=20,pady=10,bg="#E9AD80",fg="black",command=quit)
    b6.place(x=250,y=355)
    medicine_menu_window.resizable(False,False)
    medicine_menu_window.mainloop()
#################################################################################################################################
#defination from the B2 button and(NEW CUSTOMER)# FOR TE NEW CUSTOMER

def new_customer():
    with open('customer.csv','a+') as csvfile:
        columns = ['customer_name','customer_id']
        writer = csv.DictWriter(csvfile,fieldnames = columns)

        customer_name = input("Enter customer name : ")
        with open('customer.csv','r+') as csfile:
            reader=csv.DictReader(csfile)


        customer_id = input("Enter ID : ")

        writer.writerow({'customer_name':customer_name,'customer_id':customer_id})




#defination for subbuton of the customer menu (UPDATE CUSTOMER)
def update_customer():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    columns = ['customer_name','customer_id',]
    with open('customer.csv', 'r+') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=columns)
        writer.writeheader()
        customer_name =input('Enter the name of the medicine you want to modify : ')
        for row in reader:
            if row['customer_name'] == customer_name:
                print('---------------------------------------------')
                print('|1.To update Name                           |')
                print('|2.To update supplier ID                    |')
                print('---------------------------------------------')
                choice=int(input())
                if(choice==1):
                    row['customer_name']=input("Enter the new name : ")

# defination of B2(CUSTOMER PORTAL) main
# Customer Menu
def B2fun(top):
    c_menu_window = Tk()
    c_menu_window.geometry('400x400')
    c_menu_window.title("Pharmacy Management Software")
    c_menu_window.config(bg="#232528")


    lbl = Label(c_menu_window, text="Customer Menu!",font=("consolas bold",15),height=1,width=35,bg="#232528",fg="white",bd=0)
    lbl.place(x=20,y=5)
    lbl2 = Label(c_menu_window, text="What would you like to do!",font=("consolas bold",15),height=1,width=35,bg="#232528",fg="white",bd=0)
    lbl2.place(x=20,y=45)
    btn1 = Button(c_menu_window, text="Search Customer",width=44,pady=10,fg="black",activebackground="grey",bg="#00ffff")
    btn1.place(x=40,y=210)
    btn2 = Button(c_menu_window, text="New Customer",width=44,pady=10,fg="black",activebackground="grey",bg="#00ffff",command=new_customer)
    btn2.place(x=40,y=120)
    btn3 = Button(c_menu_window, text="Update Customer Info", width=44,pady=10,fg="black",activebackground="grey",bg="#00ffff",command=update_customer)
    btn3.place(x=40,y=165)

    top.withdraw()
    def back():
            top.deiconify()
            c_menu_window.destroy()

    btn5 = Button(c_menu_window, text="Return to main menu",width=44,pady=10,fg="black",activebackground="grey",bg="#00ffff",command=back)
    btn5.place(x=40,y=255)
    b6 = Button(c_menu_window,text="EXIT",width=20,pady=10,bg="#E9AD80",fg="black",command=quit)
    b6.place(x=250,y=355)
    c_menu_window.resizable(FALSE,FALSE)
    c_menu_window.mainloop()
################################################################################################################################
#defnination of B4(INSTRUCTIONS/SUGGESTIONS)
def B5fun(top):
    ins= Tk()
    ins.geometry('400x530')
    ins.title("Pharmacy Management Software")
    ins.config(bg="#232528")
    b=Label(ins,text="Help",font=("consolas bold",16),height=1,width=23,bg="#232528",fg="white",bd=0,padx=5,pady=5).place(x=60,y=0)

    txt1 = Text(ins,font=("consolas",12),bg="#232528",fg="white",height=25,width=40)

    txt1.insert(END,"In Our Software  following can be done:\n\nIn the Medicine button :\nWE CAN ADD NEW MEDICINE(ADD DATABASE OF MEDICINES)\nWE CAN SEARCH A PARTICUAR MEDICINE\nWE CAN UPDATE A PARTICULAR MEDICINE\nCAN WATCH WHAT MEDICINE TO BE PURCHASED\n\nIn the customer portal button:\nWE CAN ADD NEW CUSTOMER\nWE CAN SEARCH A CUSTOMER\n\nIn the Supplier Menu:\nWE CAN ADD NEW SUPLIER\nWE CAN SEARCH  SUPPLIER\n\nIn the PATEINT MENU:\nWE CAN ADDD NEW DATABASE OF ANY PATEINT\nWE CAN UPDATE DISCHARGED PATIENT DATABASE\nWE CAN NO. OF AVAILABLE BEDS IN THE HOSPITAL\nWE CAN SEE TOTA AMMOUNT TO BE PAID")
    txt1.place(x=20,y=40)
    txt1.configure(state=DISABLED)


    top.resizable(False,False)
    top.withdraw()
    def back():
            top.deiconify()
            ins.destroy()
    back=Button(ins,text="<<",width=5,pady=5,bg="#232528",fg="white",command=back)
    back.place(x=0,y=0)
    ins.resizable(False,False)


    ins.mainloop()

#################################################################################################################################
# Main menu
def main_menu():

    top = Tk()
    top.geometry("400x400")
    top.title("_____MEDICAL DISPENSORY MANAGMENT_____")
    top.config(bg="#232528")
    L = Label(text="Following paths to visit:",font=("consolas bold",15),height=1,width=35,bg="#232528",fg="white",bd=0)
    L.place(x=20,y=5)
    B1 = Button(top,text="MEDICINE",width=44,pady=10,fg="black",activebackground="grey",bg="#00ffff",command=lambda : B1fun(top))
    B1.place(x=50,y=90)
    B2 = Button(text="CUSTOMER PORTAL",width=44,pady=10,fg="black", activebackground="grey", bg="#00ffff", activeforeground="black", command=lambda : B2fun(top))
    B2.place(x=50,y=135)
    B3 = Button(text="SUPPLIER MENU",width=44,pady=10,fg="black", activebackground="grey", bg="#00ffff", activeforeground="black")
    B3.place(x=50,y=180)
    B4 = Button(text="PATIENT DATABASE",width=44,pady=10,fg="black", activebackground="grey", bg="#00ffff", activeforeground="black")
    B4.place(x=50,y=225)
    B5 = Button(text="Help",width=44,pady=10,fg="black", activebackground="grey", bg="#00ffff", activeforeground="black",command=lambda : B5fun(top))
    B5.place(x=50,y=270)
    b6 = Button(top,text="EXIT",width=20,pady=10,bg="#E9AD80",fg="black",command=quit)
    b6.place(x=250,y=355)
    top.resizable(False,False)
    top.mainloop()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
main_menu()
