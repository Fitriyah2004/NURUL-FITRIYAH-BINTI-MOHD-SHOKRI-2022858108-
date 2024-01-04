import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector

#Connect ke database
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="music_class_registration"
)
mycursor= mydb.cursor()

#Define for calculation ()
def collect_data():
    
    #Put the info in terminal
    student_full_name=student_full_name_entry.get()
    print("student full name:", student_full_name)

    student_year=student_year_spinbox.get()
    print("student year:", student_year)

    student_address=student_address_entry.get()
    print("student adress:", student_address)

    student_gender=student_gender_combobox.get()
    print("student gender:", student_gender)

    parent_full_name=parent_full_name_entry.get()
    print("parent full name:", parent_full_name)

    parent_email=parent_email_entry.get()
    print("parent email:", parent_email)

    student_set=student_set_combobox.get()
    print("student set:", student_set)

    student_pack_quantity=student_pack_quantity_entry.get()
    print("student pack quantity:", student_pack_quantity)



    set_type = student_set_combobox.get()
    quantity = int(student_pack_quantity_entry.get())

    #Price below is to defined the value from your selections
    prices = {"Package 1": 80, "Package 2": 150, "Package 3": 200}

     # Calculate the total price. This will be derived from your selection (Package, Pack).
    total_price = (prices[set_type] * quantity)

    #Untuk Print total harga
    #It will happen in the function collect_data().
    #The f before the string indicates an f-string in Python. 
    output_label.config(bg='#E9C3E1', fg="#4A1C40", width=100, font= ("Impact", 15), text=f"Set: {set_type}, Pax: {quantity}, Total Price: RM{total_price}\nTHANK YOU")
   
    #Insert data into a table
    sql = "INSERT INTO class (student_full_name, student_year, student_address, student_gender, parent_full_name, parent_email, student_set, student_pack_quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (student_full_name, student_year, student_address, student_gender, parent_full_name, parent_email, student_set, student_pack_quantity)
    mycursor.execute(sql,val)
    mydb.commit()


# Rest of your GUI code remains unchanged
root = tk.Tk()
root["bg"]="#E9C3E1"            
root.title("Music Class Registration")
root.geometry('1080x1080')

#Title in FORM
label = tkinter.Label(root, bg= "#BBA4F4", fg="#34403A", text="WELCOME TO FIT'S MUSIC", font=('Cooper Black',18))
label.pack(padx=20, pady=20)

#Saving user info
frame = tkinter.Frame(root)
frame.pack()

#Frame 1
student_info_frame =tkinter.LabelFrame(frame, bg= "#BBA4F4",text="Student Information")
student_info_frame.grid(row= 0, column=0, padx=20, pady=0)

#Student Full Name
student_full_name = tkinter.Label(student_info_frame, bg= "#E9C3E1", width=10, font= ("Times New Roman", 10), text="Full Name")
student_full_name.grid(row=0, column=0)
student_full_name_entry = tkinter.Entry(student_info_frame)
student_full_name_entry.grid(row=1, column=0)

#Student Year
student_year = tkinter.Label(student_info_frame, bg= "#E9C3E1", width=10, font= ("Times New Roman", 10), text="Year")
student_year.grid(row=0, column=1)
student_year_spinbox = tkinter.Spinbox(student_info_frame, from_=1, to=6)
student_year_spinbox.grid(row=1, column=1)

#Student Address
student_address = tkinter.Label(student_info_frame, bg= "#E9C3E1", width=15, font= ("Times New Roman", 10), text="Student Address")
student_address.grid(row=2, column=0)
student_address_entry =tkinter.Entry(student_info_frame)
student_address_entry.grid(row=3, column=0)

#Gender
student_gender = tkinter.Label (student_info_frame, bg= "#E9C3E1", width=10, font= ("Times New Roman", 10), text="Gender")
student_gender.grid(row=2, column=1)
student_gender_combobox= ttk.Combobox (student_info_frame, values=["Male", "Female"])
student_gender_combobox.grid(row=3, column=1)


for widget in student_info_frame.winfo_children():
    widget.grid_configure(padx=60, pady=5)

#-----------------------------------------------------------------------------------------------------------------------------------------

# Frame 2
parent_info_frame = tkinter.LabelFrame(frame, bg= "#BBA4F4", text="Father/ Mother/ Guardian Information")
parent_info_frame.grid(row=0, column=1, padx=20, pady=0)

#Parents Full Name
parent_full_name = tkinter.Label(parent_info_frame, bg= "#E9C3E1", width=10, font= ("Times New Roman", 10), text="Full Name")
parent_full_name.grid(row=0, column=0)
parent_full_name_entry = tkinter.Entry(parent_info_frame)
parent_full_name_entry.grid(row=1, column=0)

#Parent Email Info
parent_email = tkinter.Label(parent_info_frame, bg= "#E9C3E1", width=10, font= ("Times New Roman", 10), text="Email")
parent_email.grid(row=0, column=1)
parent_email_entry = tkinter.Entry(parent_info_frame)
parent_email_entry.grid(row=1, column=1)

for widget in parent_info_frame.winfo_children():
    widget.grid_configure(padx=60, pady=20)

#----------------------------------------------------------------------------------------

#Frame 3
stat_pack_frame =tkinter.LabelFrame(frame, bg= "#BBA4F4", text="Music Class Package")
stat_pack_frame.grid(row= 1, column=0, padx=20, pady=10)

#Prices list using textbox
prices_text = tkinter.Text(stat_pack_frame, bg="#E9C3E1", fg='#31572c', height=15, width=45, font= ("Cooper Black", 10))

#Define list by using pricebox
prices_text.insert(tkinter.END, "Package 1:\n Beginner Class,\nFree Food\nRM 80\n\n")
prices_text.insert(tkinter.END, "Package 2:\n Intermediate Class\nFree Food\nRM 150\n\n")
prices_text.insert(tkinter.END, "Package 3:\n Deluxe Class\nFree Food\nRM200\n\n")
prices_text.configure(state='disabled')
prices_text.grid(padx=70, pady=0)

#----------------------------------------------------------------------------------------------

#Frame 4
sp_info_frame = tkinter.LabelFrame(frame, bg= "#BBA4F4", text="Select & Pay")
sp_info_frame.grid(row= 1, column=1, padx=20, pady=0)

#Set
student_set = tkinter.Label (sp_info_frame, bg= "#E9C3E1", width=10, font= ("Times New Roman", 10), text="Package")
student_set.grid(row=0, column=0)
student_set_combobox= ttk.Combobox (sp_info_frame, values=["Package 1", "Package 2", "Package 3"])
student_set_combobox.grid(row=0, column=1)

#Quantity
student_pack_quantity = tkinter.Label(sp_info_frame, bg= "#E9C3E1", width=10, font= ("Times New Roman", 10), text="Quantity / Pax")
student_pack_quantity.grid(row=1, column=0)
student_pack_quantity_entry = tkinter.Entry(sp_info_frame)
student_pack_quantity_entry.grid(row=1, column=1)

for widget in sp_info_frame.winfo_children():
    widget.grid_configure(padx=70, pady=45)

#---------------------------------------------------------------------------------------------

# Button
save_button = tkinter.Button(root, bg= "#926EED", text="Submit Data", font= ("Times New Roman", 15), command=collect_data)
save_button.pack(pady=5)

# Print Output & result
label = tkinter.Label(root, bg= "#926EED", text='Payment Details:', font=("Times New Roman",15))
label.pack(ipadx=10, ipady=10)
output_label = tkinter.Label(root, text="")
output_label.pack()
 

root.mainloop()
