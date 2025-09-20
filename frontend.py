from tkinter import *
from tkinter import messagebox
import time
import backend
#==props===============================================================================================================
mainwin = Tk()
mainwin.geometry('800x550+200+50')
mainwin.resizable(0,0)
mainwin.title('Library Management')
mainwin.config(bg= '#10153D')
#__DataBase____________________________________________________________________________________________________________
db =  backend.Database("Back_End.db")
#==functions===========================================================================================================
#__Insert______________________________________________________________________________________________________________
def insert_records():
    name = ent_name.get().strip().title()
    author  = ent_author.get().strip().title()
    date  = ent_date.get().strip()
    isbn = ent_isbn.get().strip()
    if name == '' or author == '' or  date == '' or isbn == '':
        messagebox.showerror('ERROR','Plese Fill the fields First')
        return
    db.insert(name,author,date,isbn)
    messagebox.showinfo('INFO','Information Recorded')
    ent_name.focus_set()
    clear()
#__Show_all____________________________________________________________________________________________________________
all_records = []

def showall():
    lstbox.delete(0,END)
    records = db.select()
    for recs in records:
        all_records.append(recs)
        disply_txt = ', '.join(str(item) for item in recs)
        lstbox.insert(END, disply_txt)
#__Delete______________________________________________________________________________________________________________
def delette():
    index = lstbox.curselection()
    if not index:
        messagebox.showerror('ERROR','Please select one first')
        return
    record = lstbox.get(index)
    dell = messagebox.askyesno('WARNING','Do you want to remove this option?')
    if dell:
        record = all_records[index[0]]
        db.delete(record[0])
        showall()
        clear()
#__Search______________________________________________________________________________________________________________
def search_records():
    name = ent_name.get().strip().title()
    author = ent_author.get().strip().title()
    date = ent_date.get().strip()
    isbn = ent_isbn.get().strip()

    lstbox.delete(0, END)
    all_records.clear()

    results = db.search(name, author, date, isbn)

    for rec in results:
        all_records.append(rec)
        disply_txt = ', '.join(str(item) for item in rec)
        lstbox.insert(END, disply_txt)
#____Select_items__________________________________________________________________________________________________
def select_items(event):
    clear()
    index = lstbox.curselection()
    if not index:
        return
    record = all_records[index[0]]
    ent_name.delete(0, END)
    ent_name.insert(0, record[1])
    ent_author.delete(0, END)
    ent_author.insert(0, record[2])
    ent_date.delete(0,END)
    ent_date.insert(0, record[3])
    ent_isbn.delete(0,END)
    ent_isbn.insert(0, record[4])
#__Exeption____________________________________________________________________________________________________________
def get_selected_row(event):
    global selected_id
    try:
        index = lstbox.curselection()[0]
        selected_tuple = lstbox.get(index)
        selected_id = selected_tuple[0]
        ent_name.delete(0, END)
        ent_name.insert(END, selected_tuple[1])
        ent_author.delete(0, END)
        ent_author.insert(END, selected_tuple[2])
        ent_date.delete(0, END)
        ent_date.insert(END, selected_tuple[3])
        ent_isbn.delete(0, END)
        ent_isbn.insert(END, selected_tuple[4])
    except IndexError:
        selected_id = None
#__Clear_______________________________________________________________________________________________________________
def clear():
    ent_name.delete(0,END)
    ent_author.delete(0,END)
    ent_date.delete(0,END)
    ent_isbn.delete(0,END)
    ent_name.focus()
#__Exit________________________________________________________________________________________________________________
def Exit():
    exitt = messagebox.askyesno('EXIT','Do you want exit?')
    if exitt:
        time.sleep(0.5)
        mainwin.destroy()
#==Widgets=============================================================================================================
#__Labels______________________________________________________________________________________________________________
lbl_name = Label(text= 'Title ',font= ('Book Antiqua', 16,'bold'),bg= '#10153D',fg= '#FFFFFF')
lbl_name.place(x= 45,y= 15)

lbl_author = Label(text= 'Author' ,font= ('Book Antiqua', 16,'bold'),bg= '#10153D',fg= '#FFFFFF')
lbl_author.place(x= 405,y= 15)

lbl_Date0 = Label(text= 'PY ',font= ('Book Antiqua', 16,'bold'),bg= '#10153D',fg= '#FFFFFF')
lbl_Date0.place(x= 55,y= 68)

lbl_isbn0 = Label(text= 'ISBN ',font= ('Book Antiqua', 16,'bold'),bg= '#10153D',fg= '#FFFFFF')
lbl_isbn0.place(x= 415,y= 68)

lbl_date1 = Label(text= '1',font= ('Book Antiqua', 8,'bold'),bg= '#10153D',fg= '#FFFFFF')
lbl_date1.place(x= 86,y= 58)

lbl_isbn1 = Label(text= '2',font= ('Book Antiqua', 8,'bold'),bg= '#10153D',fg= '#FFFFFF')
lbl_isbn1.place(x= 473,y= 64)

lbl_line = Label(text= '_'*59,font= ('Book Antiqua', 16,'bold'),bg= '#10153D',fg= '#FFFFFF')
lbl_line.place(x= 0,y= 470)

lbl_Date2 = Label(text= 'PY = Poblishing Year ',font= ('Book Antiqua', 8,'bold'),bg= '#10153D',fg= '#FFFFFF')
lbl_Date2.place(x= 19,y= 501)

lbl_isbn2 = Label(text= 'ISBN = International Standard Book Number '
                  ,font= ('Book Antiqua', 8,'bold'),bg= '#10153D',fg= '#FFFFFF')
lbl_isbn2.place(x= 19,y= 523)

lbl_star1 = Label(text= '1.',font= ('Book Antiqua', 10,'bold'),bg= '#10153D',fg= '#FFFFFF')
lbl_star1.place(x= 4,y= 500)

lbl_star2 = Label(text= '2.',font= ('Book Antiqua', 10,'bold'),bg= '#10153D',fg= '#FFFFFF')
lbl_star2.place(x= 3,y= 522)
#__Entries_____________________________________________________________________________________________________________
ent_name = Entry(mainwin,font= ('Book Antiqua', 16,'bold'))
ent_name.place(x= 120,y= 18,width= 260)

ent_author = Entry(mainwin,font= ('Book Antiqua', 16,'bold'))
ent_author.place(x= 490,y= 18,width= 260)

ent_date = Entry(mainwin,font= ('Book Antiqua', 16,'bold'))
ent_date.place(x= 120,y= 70,width= 260)

ent_isbn = Entry(mainwin,font= ('Book Antiqua', 16,'bold'))
ent_isbn.place(x= 490,y= 70,width= 260)
#__Buttons_____________________________________________________________________________________________________________
btn_show = Button(text= 'Show all',font= ('Book Antiqua', 14,'bold'),bg= '#10153D',fg= '#FFFFFF',command= showall)
btn_show.place(x= 650 ,y= 200,width= 140) 

btn_insert = Button(text= 'Insert',font= ('Book Antiqua', 14,'bold'),bg= '#10153D',fg= '#FFFFFF'
                    ,command= insert_records) 
btn_insert.place(x= 650,y= 250,width= 140) 

btn_search = Button(text= 'Search',font= ('Book Antiqua', 14,'bold'),bg= '#10153D',fg= '#FFFFFF'
                    ,command= search_records)
btn_search.place(x= 650,y= 300,width= 140) 

btn_delete = Button(text= 'Delete',font= ('Book Antiqua', 14,'bold'),bg= '#10153D',fg= '#FFFFFF',command= delette)
btn_delete.place(x= 650,y= 350,width= 140) 

btn_exit = Button(text= 'Exit',font= ('Book Antiqua', 14,'bold'),bg= '#10153D',fg= '#FFFFFF',command= Exit)
btn_exit.place(x= 650,y= 400,width= 140) 
#__Scrollbar___________________________________________________________________________________________________________
scrllbar_y = Scrollbar(mainwin,orient= VERTICAL,bg= '#10153D')
scrllbar_y.place(x= 610,y=200,height= 244)

scrllbar_x = Scrollbar(mainwin,orient= HORIZONTAL,bg= '#10153D')
scrllbar_x.place(x= 10,y=444,width= 600)

#__Listbox_____________________________________________________________________________________________________________
lstbox = Listbox(mainwin,font= ('Book Antiqua', 14,'bold')
                 , yscrollcommand= scrllbar_y.set
                 , xscrollcommand= scrllbar_x.set)
lstbox.place(x= 10,y= 200,width= 600)
#______________________________________________________________________________________________________________________
lstbox.bind('<<ListboxSelect>>',select_items)
#______________________________________________________________________________________________________________________
scrllbar_y.config(command=lstbox.yview)
scrllbar_x.config(command=lstbox.xview)
#==TheEnd==============================================================================================================
mainwin.mainloop()