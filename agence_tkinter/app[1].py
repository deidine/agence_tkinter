#----------------------connection to database
import pymysql.cursors
# Connect to the database
def connects():
   return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='agencetk',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
#-----------------------------------------------------------------------


#-----------------------------client----------------------
#------------------------REgister
import customtkinter
from tkinter import scrolledtext as st
import tempfile,os
import os,sys
sys.path.append("..") #this is importent when you import some thing in other folder
from tkcalendar import DateEntry
from tkinter import CENTER, Label,Entry,Spinbox,Button,END,Frame,Tk
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox


class RegClient:
    """
    if you dont put self behind eny image will not import in others folder \n
    this class for enregister client into data base
    """
    def __init__(self, root ): # default constructor and root is a tkinter class object
        customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.root = root
        scr_width=self.root.winfo_screenwidth()/2+50
        scr_height=self.root.winfo_screenheight()/2+130
        self.root.geometry("%ix%i+200+100"% (scr_width,scr_height)) # Setting width
        self.root.title("Registration Window")
        self.root.config(bg="white")
        self.root.resizable(width=False, height=False)# self.root.resizable(width=False, height=False)
        #***********Bg Image***********
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg",master=self.root)
        # self.bg=ImageTk.PhotoImage(file="../images/b2.jpg",master=self.root)

        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #***********Register Frame***********
        frame1=Frame(self.root,bg="#08A3D2")
        frame1.place(x=10,y=10,width=700,height=500)
        frame2=Frame(self.root)
        frame2.place(x=800,y=10,width=700,height=500)

        
        title=customtkinter.CTkLabel(frame1,text="ENREGISTRER CLIENT ICI سجل معلومات المسافر هنا", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="green").place(x=50,y=30)
        #***********Row1***********
        noml=customtkinter.CTkLabel(frame1,text="NOM الإسم", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=100)
        nom=customtkinter.CTkEntry(frame1,placeholder_text="Nom ...",text_font=("times new roman",15),fg_color="white",text_color="black")
        nom.place(x=50,y=130,width=250)

        prenoml=customtkinter.CTkLabel(frame1,text="PRESNOM الإسم العائلي",text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=100)
        prenom=customtkinter.CTkEntry(frame1,placeholder_text="Prenom ...",text_font=("times new roman",15),fg_color="white",text_color="black")
        prenom.place(x=370,y=130,width=250)

        #***********Row2***********
        
        telel=customtkinter.CTkLabel(frame1,text="Numero Telephone الهاتف", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=170)
        tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightblue")
        tele.place(x=50,y=200,width=250)

        numL=customtkinter.CTkLabel(frame1,text="NUMERO chaise رقم المقعد", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=170)
        num=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightblue")
        num.place(x=370,y=200,width=250)
#reloadfunction
            
        def reload():
            self.root.destroy()
            os.system("py print.py")
        #***********Row3***********
        directioinl=customtkinter.CTkLabel(frame1,text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=240)
        cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        cmb_dir["values"]=("Selection"," أنواكشوط"," أطار"," أكجوجت","  أزويرت"," أنواذيبوا")
        cmb_dir.place(x=50,y=270,width=250)
        cmb_dir.current(0)

        datel=customtkinter.CTkLabel(frame1,text="Date now تاريخ اليوم", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=240)
        date=DateEntry(frame1,selectmode='day',font=("times new roman",15),fg="black",bg="white")
        date.place(x=370,y=270,width=250)

        #***********Row4***********

        prixl=customtkinter.CTkLabel(frame1,text="prix De Ticket", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=250,y=310)
        prix=customtkinter.CTkEntry(frame1,text_color="black", text_font=("times new roman",15),fg_color="white")
        prix.place(x=300,y=340,width=90)
        cmb_prix=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        cmb_prix["values"]=("✅","❌")
        cmb_prix.place(x=400,y=340,width=50)
        cmb_prix.current(0)
        prix.insert(END,"5000")
        tele.delete(0,END)
        num.delete(0,END)
        cmb_dir.current(0)

        text_ear=st.ScrolledText(frame2,width=40,height=20)
        text_ear.place(x=50,y=50)

        def retour():
            self.root.destroy()

        def write():
            
            text_ear.insert(END,f" Bouha El Moustapha VOYAGES\tسفريات بوه ولد مصطفى ")
            text_ear.insert(END,f"\n")
            text_ear.insert(END,f"Telephone:48775476")
            text_ear.insert(END,f"\n"+"_"*49+"\n")
            text_ear.insert(END,f"\nNOM:\t"+nom.get().upper()+"/"+prenom.get().upper()+"\t:إسم المسافر")
            text_ear.insert(END,f"\nTELEPHONE:\t"+tele.get()+"\t:الهاتف")
            text_ear.insert(END,f"\nNUMERO CHAISE:\t"+num.get()+"\t:رقم المقعد")
            text_ear.insert(END,f"\nDIRECTION:\t"+cmb_dir.get().upper()+"\t:الوجهة")
            text_ear.insert(END,f"\n\tPRIX:\t"+prix.get().upper()+"\tالسعر")
            text_ear.insert(END,f"\n"+"_"*49+"\n")
            text_ear.insert(END,f"\nDATE D'IMPRIMATION:\t"+str(date.get_date())+"\t:تاريخ الطباعة ")
            text_ear.insert(END,f"\nلا نتحمل المسؤلية بعد 15 يوم")
            text_ear.insert(END,f"\n")
            text_ear.insert(END,f"aucun responsabiliter apres 15 jours")
            text_ear.insert(END,f"\n"+"."*49+"\n")

        def print_text():
            a=text_ear.get('1.0',END)
            with open("enreg.txt","w",encoding='utf-8') as dd:
                dd.write(a)
                dd.close()
            os.startfile("enreg.txt","print")

        btn1=Button(frame2,text='print',command=lambda: print_text(text_ear.get('1.0',END)))
        btn1.place(x=400,y=300)
        btn1=Button(frame2,text='reload',command=reload)
        btn1.place(x=450,y=300)
        btn=Button(frame2,text='write',command=write)
        btn.place(x=200,y=300)
#==================================================================
        def clear():
            nom.delete(0,END)
            prenom.delete(0,END)
            tele.delete(0,END)
            num.delete(0,END)
            cmb_dir.current(0)
            cmb_prix.current(0)

        def register_data():
            """test if the user enter  only the number 
            in telephone and numero chaise"""
            numVal=num.get()
            teleVal=tele.get()
            if nom.get()=="" or numVal=="" or teleVal=="" or prenom.get()=="" or  cmb_dir.get()=="Selection"  or prix.get()=="" or num.get()=="":
                messagebox.showerror("Error", "tous les champs sont obligatoire", parent=root)
            else:
                try:
                        if numVal.isdigit() and teleVal.isdigit():
                            n=num.get()
                            with open("login.txt") as file:
                                f=file.read()
                            t=tele.get()
                            con=connects()
                            cur=con.cursor()
                        else: 
                            messagebox.showerror("Error", "numero du chaise ou numero de telephone doit etre des nombre", parent=self.root)
                        cur.execute("insert into client (nom,prenom,numero,telephone,direction,prix,date,payer,	emploiyer) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            nom.get(),
                            prenom.get(),
                            n,
                            t,
                            cmb_dir.get(),
                            prix.get(),
                            date.get_date(),
                            cmb_prix.get(),f
                        ))
                        con.commit()
                        con.close()
                        write()
                        op=messagebox.askyesno("Confirm", "tu veut imprimer le voyageur ?", parent=root)
                        if op==True:
                            print_text()
                            text_ear.delete('1.0',END)
                        else :
                            text_ear.delete('1.0',END)
                        clear()

                        

                except Exception as es:
                    messagebox.showerror("Error", f"Error due to: {str(es)}", parent=root)

        btn1=customtkinter.CTkButton(master=self.root,text="RETOUR",text_font=(15),    command=retour, width=50, height=40,text_color="white", compound="right",fg_color="green", hover_color="black")
        btn1.place(x=450,y=400)
        customtkinter.CTkButton(master=root,command=register_data,bg_color="systembuttonface",text="ENREGISTRER",text_font=15, width=90,text_color="white", height=40, compound="right",fg_color="green", hover_color="blue").place(x=300,y=400)


# root=customtkinter.CTk()
# obj=Register(root)
# root.mainloop()

#----------------------------show client
import os
import sys
import tempfile
from time import strftime
import tkinter
from tkinter import simpledialog
from tkcalendar import DateEntry
from tkinter import CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk,scrolledtext as st
from tkinter import messagebox
import customtkinter
from tabulate import tabulate
from tkinter.messagebox import showinfo
from turtle import width
sys.path.append('..')#this is importent when you import some thing in other folder
from PIL import Image, ImageTk # pip install pillow

import tkinter as tk



class ShowClient:
    """
    this class show information in treeview 
    you can update ,delete and search data 

    """
    def __init__(self,my_w) :
            customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
            customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
         
            my_conn = connects()
            cur=my_conn.cursor()
            # Creating tkinter my_w
            scr_width=my_w.winfo_screenwidth()
            scr_height=my_w.winfo_screenheight()
            my_w.geometry("%ix%i+0+0"% (scr_width,scr_height))
            my_w.title("l'inforamtion du client")  
            my_w.tk.call('encoding','system','utf-8')
            my_w.resizable(0,0)
            #style
            # Add Some Style
            style = ttk.Style()
            # Pick A Theme
            style.theme_use('default')
            # Configure the Treeview Colors
            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")
            
# ------------------------------------frame 
            frame1=customtkinter.CTkFrame(my_w,bg_color="white")
            frame1.place(x=10,y=350,width=1400,height=500)
            frame2=Frame(my_w)
            frame2.place(x=800,y=1000,width=700,height=500)

            title=customtkinter.CTkLabel(frame1,text_color="white",text="MODIFFIER CLIENT ICI غير معلومات المسافر هنا", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="black").place(x=400,y=170)
            noml=customtkinter.CTkLabel(frame1,text="NOM الإسم",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=0,y=200)
            nom=customtkinter.CTkEntry(frame1,placeholder_text="NOM",text_font=("times new roman",15),bg_color="lightgray")
            nom.place(x=0,y=250,width=100)
            prenoml=customtkinter.CTkLabel(frame1,text_color="white",text="PRESNOM الإسم العائلي",text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=200,y=200)
            prenom=customtkinter.CTkEntry(frame1,placeholder_text="PRENOM",text_font=("times new roman",15),bg_color="lightgray")
            prenom.place(x=200,y=250,width=100)
            telel=customtkinter.CTkLabel(frame1,text_color="white",text="Telephone ", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=400,y=200)
            tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            tele.place(x=400,y=250,width=100)
            numL=customtkinter.CTkLabel(frame1,width=50,text_color="white",text="chaise ", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=600,y=200)
            num=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            num.place(x=600,y=250,width=90)
            directioinl=customtkinter.CTkLabel(frame1,text_color="white",text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=700,y=200)
            cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
            cmb_dir["values"]=("Selection"," أنواكشوط"," أطار"," أكجوجت","  أزويرت"," أنواذيبوا")
            cmb_dir.place(x=700,y=250,width=180)
            cmb_dir.current(0)
            datel=customtkinter.CTkLabel(frame1,text_color="white",text="Date now", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=900,y=250)
            date=DateEntry(frame1,selectmode='day',font=("times new roman",15),bg="lightgray")
            date.place(x=900,y=200,width=150)
            prixl=customtkinter.CTkLabel(frame1,width=50,text_color="white",text="payer دفع", text_font=("times new roman", 19, "bold"),bg_color="white",fg_color="gray").place(x=1100,y=200)
            prix=customtkinter.CTkEntry(frame1,text_font=("times new roman",1),bg_color="green")
            prix.place(x=1100,y=250,width=10)
            cmb_prix=ttk.Combobox(frame1,font=("times new roman",19), state="readonly", justify=CENTER)
            cmb_prix["values"]=("payer","✅","❌")
            cmb_prix.place(x=1100,y=250,width=80)
            cmb_prix.current(0)
            # prix.insert(END,'5000')#for inserting time at entry time 
            tele.delete(0,'end')
            num.delete(0,'end')
            # Change Selected Color
            style.map('Treeview',background=[('selected', "#347083")])           
            style.configure("Vertical.TScrollbar", background="green", bordercolor="red", arrowcolor="white")
        #serch-------------
            serchl=Label(my_w,text="serch",font=("times new roman", 15, "bold"),bg="white",fg="gray")
            serchl.place(x=1000,y=500)
            serchE=customtkinter.CTkEntry(my_w,placeholder_text="Rechercher phone ,nom...",text_font=("times new roman",15),bg_color="lightgray")
            serchE.place(x=1080,y=500,width=250)
            def serch():
                """
                 used for finding spesific data in treeview\n
                this serchE.get()+"%" because you can't write in sql code like % %s %
                """
                for item in trv.get_children():
                    trv.delete(item)    
                conn=connects()
                cur=conn.cursor()
                q="SELECT * from client where nom like %s or prenom like %s or telephone like %s order by (id) desc"
                cur.execute(q,(serchE.get()+"%",serchE.get()+"%",serchE.get()+"%"))
                res=cur.fetchall()
                # print(res)
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['nom'],dt['prenom'],dt['numero'],dt['telephone'],dt['direction'],dt['prix'],dt['date'],dt['payer'],dt['emploiyer']))
                    
            sr=customtkinter.CTkButton(master=my_w,text_color="white", text="search",command=serch, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
            sr.place(x=1000,y=500)
                
        
        
            # Using treeview widget 
            my_str = tk.StringVar()
            r_set=cur.execute("SELECT count(id) as no from client")
            data_row=cur.fetchall()
            no_rec=data_row[0]['no']# Total number of rows in tabl
            limit = 30;
            # serchE.grid(row=9,column=0)

            def display(offset):
                """ this function for display data by limit and next and previous method \n
                param offset for the numbre will show in data and shoul start by 0 and \n
                increment when click next or prev button

                """
                global trv
                trv = ttk.Treeview(my_w,height=18,selectmode ='browse',columns=("0","1", "2", "3","4","5","6","7","8","9"),show='headings')
                trv.grid(row=10, column=0, sticky='nsew')
                trv.bind("<ButtonRelease-1>",select)

                # width of columns and alignment 
                trv.column("0", width = 100, anchor ='c')
                trv.column("1", width = 100, anchor ='c')
                trv.column("2", width = 100, anchor ='c')
                trv.column("3", width = 100, anchor ='c')
                trv.column("4", width = 100, anchor ='c')
                trv.column("5", width = 180, anchor ='c')
                trv.column("6", width = 40, anchor ='c')
                trv.column("7", width = 180, anchor ='c')
                trv.column("8", width = 100, anchor ='c')
                trv.column("9", width = 100, anchor ='c')
                #nom,prenom,numero,telephone,direction,prix,date
                # Headings  
                # respective columns 
                trv.heading("0", text ="id")
                trv.heading("1", text ="nom")
                trv.heading("2", text ="prenom")
                trv.heading("3", text ="numero")
                trv.heading("4", text ="telephone")
                trv.heading("5", text ="direction")
                trv.heading("6", text ="prixs")
                trv.heading("7", text ="date")
                trv.heading("8", text ="payer")
                trv.heading("9", text ="emploiyer")
                
                # add a scrollbar
                scrollbar = ttk.Scrollbar(my_w, orient=tk.VERTICAL, command=trv.yview)
                trv.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=10, column=1, sticky='ns')
                # # getting data from MySQL student table 
                # r_set=cur.execute("SELECT * from client ")
                # res=cur.fetchall()
                q="SELECT * from client order by id desc LIMIT "+ str(offset) +","+str(limit)
                cur.execute(q)
                res=cur.fetchall()
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['nom'],dt['prenom'],dt['numero'],dt['telephone'],dt['direction'],dt['prix'],dt['date'],dt['payer'],dt['emploiyer']))
                            # Show buttons 
                back = offset - limit # This value is used by Previous button
                next = offset + limit # This value is used by Next button       
                


                if(no_rec <= next): 
                    b2=customtkinter.CTkButton(master=my_w,state=tkinter.DISABLED , text="suivant>>>",command=lambda: display(next), width=50, height=40, compound="right",fg_color="white", hover_color="#C77C78")

                else:
                    b2=customtkinter.CTkButton(master=my_w, text="suivant>>>",text_color="white",command=lambda: display(next), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")

                b2.place(x=200,y=500)
                    
                if(back >= 0):
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",text_color="white",command=lambda: display(back), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")
                else:
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",state=tkinter.DISABLED ,command=lambda: display(back), width=50, height=40, compound="right",fg_color="white", hover_color="yellow")
                b1.place(x=50,y=500)

#----------------------functions---------------
            def retour():
                my_w.destroy()
            def reload1():
                my_w.destroy()
                os.system("py showCL.py")
            def delete():
                #for delete a row in tree view
                op=messagebox.askyesno("Confirm", "tu veut vraimment suprimer ?", parent=my_w)
                if op==True:
                    selected_item = trv.selection()[0]#the frist column id
                    trv.delete(selected_item)
                    try:
                        cur.execute("delete from client where id=%s",(selected_item))
                        my_conn.commit()
                        messagebox.showinfo("Success", "le nom et suprimer", parent=my_w)
                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
            
            def select(ev):
                """
                this function used when you click the treeview and it will insert the data into input to be updated later\n
                param ev is very imported if you forget it the function trv.bind("<ButtonRelease-1>",select)\n
                will simply not work

                """
                clear()
                r=trv.focus()
                content=trv.item(r)
                row=content["values"]
                nom.insert(END,row[1])
                prenom.insert(END,row[2])
                num.insert(END,row[3])
                tele.insert(END,row[4])
                prix.insert(END,row[6])
            def table():
                conn=connects()
                cur=conn.cursor()
                op=simpledialog.askinteger("Input","أدخل عدد المسافرين للطباعة",parent=my_w)
                q="SELECT numero,CONCAT_WS(' oul ',nom,prenom) as nom,telephone,payer from client  order by (id) desc limit %s"
                cur.execute(q,op)
                res=cur.fetchall()
                txt=" Bouha El Moustapha VOYAGES\t\t\t\t\tسفريات بوه ولد مصطفى "
                txt+="\n"
                txt+="LISTES DES PASSAGERS"
                txt+="\t\t\tTelephone:48775476"
                txt+="\n"+"_"*80+"\n"
                a1="رقم المقعد"
                a2="إسم المسافر "
                a3="الهاتف"
                a4="دفع"
                txt+="\t\t"+a1+"\t\t"+a2+"\t\t"+a3+"\t\t"+a4+"\n"
                txt+="\n"+"_"*80+"\n"
                txt+=tabulate(res,headers='keys',tablefmt="rounded_grid")
                txt+="\n"
                time=strftime('%m-%d-%Y')
                txt+="DATE D'IMPRIMATION:\t"+str(time)+"\t:تاريخ الطباعة "
                with open("print.txt","w",encoding="utf-8") as log:
                    log.write(txt)
                    os.startfile("print.txt","print")
                    log.close()
                
            def imp():
                table()
                clear()
                
            def update_data():
                """
                this function is for updating data mysql \n
                it test two option if the user click direction or forget it and that will not evect the changing of information 
                """
                #for updating data at the tree view and in our data base
                op=messagebox.askyesno("Confirm", "tu veut vraimment editer ?", parent=my_w)
                if op==True:
                    numVal=num.get()
                    teleVal=tele.get()
                    if nom.get()=="" or numVal=="" or teleVal=="" or prenom.get()=="" or num.get()=="":
                        messagebox.showerror("Error", "tous les champs sont obligatoire", parent=my_w)
                    else:
                        try:
                            id=trv.selection()[0]
                            if numVal.isdigit() and teleVal.isdigit() and   cmb_prix.get()!="payer" and cmb_dir.get()!="Selection":
                                #cette if et pour le cas ou l'user nest pas entrer le direction dans update system
                                n=num.get()
                                t=tele.get()
                                con=connects()
                                cur=con.cursor()
                                sql="update client set nom=%s,prenom=%s,numero=%s,telephone=%s,direction=%s,payer=%s,date=%s where id=%s"
                                cur.execute(sql,(nom.get(),prenom.get(),n,t,cmb_dir.get(),cmb_prix.get(),date.get_date(),id))
                                selected = trv.focus()
                                 
                            elif numVal.isdigit() and teleVal.isdigit():
                                n=num.get()
                                t=tele.get() 
                                sql="update client set nom=%s,prenom=%s,numero=%s,telephone=%s,prix=%s,date=%s where id=%s"
                                con=connects()
                                cur=con.cursor()
                                cur.execute(sql,(nom.get(),prenom.get(),n,t,prix.get(),date.get_date(),id))
                                selected = trv.focus()
                            trv.item(selected, text="", values=(id,nom.get(), prenom.get(), n, t, cmb_dir.get(),prix.get(), date.get_date(),cmb_prix.get()))
                            selected = trv.focus()
                            con.commit()
                            clear()
                        except Exception as es:
                            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
                else :
                    clear()

            def clear():
                nom.delete(0,END)
                prenom.delete(0,END)
                tele.delete(0,END)
                prix.delete(0,END)
                num.delete(0,END)
                cmb_dir.current(0)
            btn=customtkinter.CTkButton(master=frame1,text_font=(20) ,text="suprimer حذف",command=delete, width=50, height=40, compound="right",fg_color="#D35B58", hover_color="#C77C78")
            btn.place(x=350,y=300)
            btn3=customtkinter.CTkButton(master=frame1,text_font=(20), text="editer تغير",command=update_data, width=50, height=40, compound="right",fg_color="yellow", hover_color="#C77C78")
            btn3.place(x=700,y=300)
            btn4=customtkinter.CTkButton(master=frame1,text_font=(20), text="Imprimer طباعة",command=imp, width=50, height=40, compound="right",fg_color="green", hover_color="#C77C78")
            btn4.place(x=550,y=300) 
            display(0)      
            

# my_w =customtkinter.CTk()
# my_w1=Show(my_w)
# my_w.mainloop()

#------------------------------------------------------------

#---------------------------------------reservation
#---------------------------show reservation
import os
import sys
import tempfile
import tkinter
from tkcalendar import DateEntry
from tkinter import CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk,scrolledtext as st
from tkinter import messagebox
import customtkinter
from tkinter.messagebox import showinfo
from turtle import width
sys.path.append('..')#this is importent when you import some thing in other folder
from PIL import Image, ImageTk # pip install pillow

import tkinter as tk



class ShowRes:
    """
    this class show information in treeview 
    you can update ,delete and search data 

    """
    def __init__(self,my_w) :
            customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
            customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
         
            my_conn = connects()
            cur=my_conn.cursor()
            # Creating tkinter my_w
            scr_width=my_w.winfo_screenwidth()
            scr_height=my_w.winfo_screenheight()
            my_w.geometry("%ix%i+0+0"% (scr_width,scr_height))
            my_w.title("l'inforamtion du client")  
            my_w.tk.call('encoding','system','utf-8')
            my_w.resizable(0,0)
            #style
            # Add Some Style
            style = ttk.Style()
            # Pick A Theme
            style.theme_use('default')
            # Configure the Treeview Colors
            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")
            
# ------------------------------------frame 
            frame1=customtkinter.CTkFrame(my_w,bg_color="white")
            frame1.place(x=10,y=350,width=1400,height=500)
            frame2=Frame(my_w)
            frame2.place(x=800,y=1000,width=700,height=500)

            title=customtkinter.CTkLabel(frame1,text_color="white",text="MODIFFIER CLIENT ICI غير معلومات المسافر هنا", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="black").place(x=400,y=170)
            noml=customtkinter.CTkLabel(frame1,text="NOM الإسم",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=0,y=200)
            nom=customtkinter.CTkEntry(frame1,placeholder_text="NOM",text_font=("times new roman",15),bg_color="lightgray")
            nom.place(x=0,y=250,width=100)
            prenoml=customtkinter.CTkLabel(frame1,text_color="white",text="PRESNOM الإسم العائلي",text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=200,y=200)
            prenom=customtkinter.CTkEntry(frame1,placeholder_text="PRENOM",text_font=("times new roman",15),bg_color="lightgray")
            prenom.place(x=200,y=250,width=100)
            telel=customtkinter.CTkLabel(frame1,text_color="white",text="Telephone ", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=400,y=200)
            tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            tele.place(x=400,y=250,width=100)
            numL=customtkinter.CTkLabel(frame1,width=50,text_color="white",text="chaise ", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=600,y=200)
            num=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            num.place(x=600,y=250,width=90)
            directioinl=customtkinter.CTkLabel(frame1,text_color="white",text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=700,y=200)
            # cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
            # cmb_dir["values"]=("Selection"," أنواكشوط"," أطار"," أكجوجت","  أزويرت"," أنواذيبوا")
            # cmb_dir.place(x=700,y=250,width=180)
            # cmb_dir.current(0)
            cmb_dir=customtkinter.CTkEntry(frame1,placeholder_text="PRENOM",text_font=("times new roman",15),bg_color="lightgray")
            cmb_dir.place(x=700,y=250,width=180)
            datel=customtkinter.CTkLabel(frame1,text_color="white",text="Date now", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=900,y=250)
            date=DateEntry(frame1,selectmode='day',font=("times new roman",15),bg="lightgray")
            date.place(x=900,y=200,width=150)
            prixl=customtkinter.CTkLabel(frame1,width=50,text_color="white",text="payer دفع", text_font=("times new roman", 19, "bold"),bg_color="white",fg_color="gray").place(x=1100,y=200)
            prix=customtkinter.CTkEntry(frame1,text_font=("times new roman",1),bg_color="green")
            prix.place(x=1100,y=250,width=10)
            cmb_prix=ttk.Combobox(frame1,font=("times new roman",19), state="readonly", justify=CENTER)
            cmb_prix["values"]=("✅","❌")
            cmb_prix.place(x=1100,y=250,width=80)
            cmb_prix.current(0)
            # prix.insert(END,'5000')#for inserting time at entry time 
            tele.delete(0,'end')
            num.delete(0,'end')
            # Change Selected Color
            style.map('Treeview',background=[('selected', "#347083")])           
            style.configure("Vertical.TScrollbar", background="green", bordercolor="red", arrowcolor="white")
        #serch-------------
            serchl=Label(my_w,text="serch",font=("times new roman", 15, "bold"),bg="white",fg="gray")
            serchl.place(x=1000,y=500)
            serchE=customtkinter.CTkEntry(my_w,placeholder_text="Rechercher phone ,nom...",text_font=("times new roman",15),bg_color="lightgray")
            serchE.place(x=1080,y=500,width=250)
            def serch():
                """
                 used for finding spesific data in treeview\n
                this serchE.get()+"%" because you can't write in sql code like % %s %
                """
                for item in trv.get_children():
                    trv.delete(item)    
                conn=connects()
                cur=conn.cursor()
                q="SELECT * from clienttarder where nom like %s or prenom like %s or telephone like %s order by (id) desc"
                cur.execute(q,(serchE.get()+"%",serchE.get()+"%",serchE.get()+"%"))
                res=cur.fetchall()
                # print(res)
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['nom'],dt['prenom'],dt['numero'],dt['telephone'],dt['direction'],dt['prix'],dt['date'],dt['payer'],dt['emploiyer']))
                    
            sr=customtkinter.CTkButton(master=my_w,text_color="white", text="search",command=serch, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
            sr.place(x=1000,y=500)
                
        
        
            # Using treeview widget 
            my_str = tk.StringVar()
            r_set=cur.execute("SELECT count(id) as no from clienttarder")
            data_row=cur.fetchall()
            no_rec=data_row[0]['no']# Total number of rows in tabl
            limit = 30;
            # serchE.grid(row=9,column=0)

            def display(offset):
                """ this function for display data by limit and next and previous method \n
                param offset for the numbre will show in data and shoul start by 0 and \n
                increment when click next or prev button

                """
                global trv
                trv = ttk.Treeview(my_w,height=18,selectmode ='browse',columns=("0","1", "2", "3","4","5","6","7","8","9"),show='headings')
                trv.grid(row=10, column=0, sticky='nsew')
                trv.bind("<ButtonRelease-1>",select)

                # width of columns and alignment 
                trv.column("0", width = 100, anchor ='c')
                trv.column("1", width = 100, anchor ='c')
                trv.column("2", width = 100, anchor ='c')
                trv.column("3", width = 100, anchor ='c')
                trv.column("4", width = 100, anchor ='c')
                trv.column("5", width = 180, anchor ='c')
                trv.column("6", width = 40, anchor ='c')
                trv.column("7", width = 180, anchor ='c')
                trv.column("8", width = 100, anchor ='c')
                trv.column("9", width = 100, anchor ='c')
                #nom,prenom,numero,telephone,direction,prix,date
                # Headings  
                # respective columns 
                trv.heading("0", text ="id")
                trv.heading("1", text ="nom")
                trv.heading("2", text ="prenom")
                trv.heading("3", text ="numero")
                trv.heading("4", text ="telephone")
                trv.heading("5", text ="direction")
                trv.heading("6", text ="prixs")
                trv.heading("7", text ="date")
                trv.heading("8", text ="payer")
                trv.heading("9", text ="emploiyer")
                
                # add a scrollbar
                scrollbar = ttk.Scrollbar(my_w, orient=tk.VERTICAL, command=trv.yview)
                trv.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=10, column=1, sticky='ns')
                # # getting data from MySQL student table 
                # r_set=cur.execute("SELECT * from client ")
                # res=cur.fetchall()
                q="SELECT * from clienttarder order by id desc LIMIT "+ str(offset) +","+str(limit)
                cur.execute(q)
                res=cur.fetchall()
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['nom'],dt['prenom'],dt['numero'],dt['telephone'],dt['direction'],dt['prix'],dt['date'],dt['payer'],dt['emploiyer']))
                            # Show buttons 
                back = offset - limit # This value is used by Previous button
                next = offset + limit # This value is used by Next button       
                


                if(no_rec <= next): 
                    b2=customtkinter.CTkButton(master=my_w,state=tkinter.DISABLED , text="suivant>>>",command=lambda: display(next), width=50, height=40, compound="right",fg_color="white", hover_color="#C77C78")

                else:
                    b2=customtkinter.CTkButton(master=my_w, text="suivant>>>",text_color="white",command=lambda: display(next), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")

                b2.place(x=200,y=500)
                    
                if(back >= 0):
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",text_color="white",command=lambda: display(back), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")
                else:
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",state=tkinter.DISABLED ,command=lambda: display(back), width=50, height=40, compound="right",fg_color="white", hover_color="yellow")
                b1.place(x=50,y=500)

#----------------------functions---------------
            def retour():
                my_w.destroy()
            def reload1():
                my_w.destroy()
                os.system("py showCL.py")
            def delete():
                #for delete a row in tree view
                op=messagebox.askyesno("Confirm", "tu veut vraimment suprimer ?", parent=my_w)
                if op==True:
                    selected_item = trv.selection()[0]#the frist column id
                    trv.delete(selected_item)
                    try:
                        cur.execute("delete from client where id=%s",(selected_item))
                        my_conn.commit()
                        messagebox.showinfo("Success", "le nom et suprimer", parent=my_w)
                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
            
            def select(ev):
                """
                this function used when you click the treeview and it will insert the data into input to be updated later\n
                param ev is very imported if you forget it the function trv.bind("<ButtonRelease-1>",select)\n
                will simply not work

                """
                clear()
                r=trv.focus()
                content=trv.item(r)
                row=content["values"]
                nom.insert(END,row[1])
                prenom.insert(END,row[2])
                num.insert(END,row[3])
                tele.insert(END,row[4])
                prix.insert(END,row[6])
                prix.insert(END,row[6])
                cmb_dir.insert(END,row[5])

            def envoiyer():
                numVal=num.get()
                teleVal=tele.get()
                if nom.get()=="" or numVal=="" or teleVal=="" or prenom.get()=="" or  cmb_dir.get()=="Selection"  or prix.get()=="" or num.get()=="":
                    messagebox.showerror("Error", "tous les champs sont obligatoire", parent=my_w)
                else:
                    try:
                            if numVal.isdigit() and teleVal.isdigit():
                                n=num.get()
                                # with open("../login.txt") as file:
                                with open("login.txt") as file:
                                    f=file.read()
                                t=tele.get()
                                con=connects()
                                cur=con.cursor()
                            else: 
                                messagebox.showerror("Error", "numero du chaise ou numero de telephone doit etre des nombre", parent=self.root)
                            cur.execute("insert into client (nom,prenom,numero,telephone,direction,prix,date,payer,	emploiyer) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (
                                nom.get(),
                                prenom.get(),
                                n,
                                t,
                                cmb_dir.get(),
                                prix.get(),
                                date.get_date(),
                                cmb_prix.get(),f
                            ))
                            con.commit()
                            con.close()
                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)

                clear()
                
            def update_data():
                """
                this function is for updating data mysql \n
                it test two option if the user click direction or forget it and that will not evect the changing of information 
                """
                #for updating data at the tree view and in our data base
                op=messagebox.askyesno("Confirm", "tu veut vraimment editer ?", parent=my_w)
                if op==True:
                    numVal=num.get()
                    teleVal=tele.get()
                    if nom.get()=="" or numVal=="" or teleVal=="" or prenom.get()=="" or num.get()=="":
                        messagebox.showerror("Error", "tous les champs sont obligatoire", parent=my_w)
                    else:
                        try:
                            id=trv.selection()[0]
                            if numVal.isdigit() and teleVal.isdigit() and   cmb_prix.get()!="payer" and cmb_dir.get()!="Selection":
                                #cette if et pour le cas ou l'user nest pas entrer le direction dans update system
                                n=num.get()
                                t=tele.get()
                                con=connects()
                                cur=con.cursor()
                                sql="update clienttarder set nom=%s,prenom=%s,numero=%s,telephone=%s,direction=%s,payer=%s,date=%s where id=%s"
                                cur.execute(sql,(nom.get(),prenom.get(),n,t,cmb_dir.get(),cmb_prix.get(),date.get_date(),id))
                                selected = trv.focus()
                                 
                            elif numVal.isdigit() and teleVal.isdigit():
                                n=num.get()
                                t=tele.get() 
                                sql="update clienttarder set nom=%s,prenom=%s,numero=%s,telephone=%s,prix=%s,date=%s where id=%s"
                                con=connects()
                                cur=con.cursor()
                                cur.execute(sql,(nom.get(),prenom.get(),n,t,prix.get(),date.get_date(),id))
                                selected = trv.focus()
                            trv.item(selected, text="", values=(id,nom.get(), prenom.get(), n, t, cmb_dir.get(),prix.get(), date.get_date(),cmb_prix.get()))
                            selected = trv.focus()
                            con.commit()
                            # messagebox.showinfo("Success", "l'update est terminer", parent=my_w)
                            clear()
                        except Exception as es:
                            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
                else :
                    clear()

            def clear():
                nom.delete(0,END)
                prenom.delete(0,END)
                tele.delete(0,END)
                prix.delete(0,END)
                num.delete(0,END)
                cmb_dir.delete(0,END)

            btn=customtkinter.CTkButton(master=frame1,text_font=(20) ,text="suprimer حذف",command=delete, width=50, height=40, compound="right",fg_color="#D35B58", hover_color="#C77C78")
            btn.place(x=350,y=300)
            btn3=customtkinter.CTkButton(master=frame1,text_font=(20), text="editer تغير",command=update_data, width=50, height=40, compound="right",fg_color="yellow", hover_color="#C77C78")
            btn3.place(x=700,y=300)
            btn4=customtkinter.CTkButton(master=frame1,text_font=(20), text="envoiyer ارسال ",command=envoiyer, width=50, height=40, compound="right",fg_color="green", hover_color="#C77C78")
            btn4.place(x=550,y=300) 
            display(0)
            
            




# my_w =customtkinter.CTk()
# my_w1=Show(my_w)
# my_w.mainloop()

#----------------------enregister 
import customtkinter
# from tkinter import scrolledtext as st
import tempfile,os
import os,sys
sys.path.append("..") #this is importent when you import some thing in other folder
from tkcalendar import DateEntry
from tkinter import CENTER, Label,Entry,Spinbox,Button,END,Frame,Tk
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox


class RegRes:
    """
    if you dont put self behind eny image will not import in others folder \n
    this class for enregister client into data base
    """
    def __init__(self, root ): # default constructor and root is a tkinter class object
        customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.root = root
        scr_width=self.root.winfo_screenwidth()/2+50
        scr_height=self.root.winfo_screenheight()/2+130
        self.root.geometry("%ix%i+200+100"% (scr_width,scr_height)) # Setting width
        self.root.title("Registration Window")
        self.root.config(bg="white")
        self.root.resizable(width=False, height=False)# self.root.resizable(width=False, height=False)
        #***********Bg Image***********
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg",master=self.root)
        # self.bg=ImageTk.PhotoImage(file="../images/b2.jpg",master=self.root)

        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #***********Register Frame***********
        frame1=Frame(self.root,bg="#08A3D2")
        frame1.place(x=10,y=10,width=700,height=500)
        frame2=Frame(self.root)
        frame2.place(x=800,y=10,width=700,height=500)

        
        title=customtkinter.CTkLabel(frame1,text="ENREGISTRER CLIENT ICI سجل معلومات المسافر هنا", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="green").place(x=50,y=30)
        #***********Row1***********
        noml=customtkinter.CTkLabel(frame1,text="NOM الإسم", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=100)
        nom=customtkinter.CTkEntry(frame1,placeholder_text="Nom ...",text_font=("times new roman",15),fg_color="white",text_color="black")
        nom.place(x=50,y=130,width=250)

        prenoml=customtkinter.CTkLabel(frame1,text="PRESNOM الإسم العائلي",text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=100)
        prenom=customtkinter.CTkEntry(frame1,placeholder_text="Prenom ...",text_font=("times new roman",15),fg_color="white",text_color="black")
        prenom.place(x=370,y=130,width=250)

        #***********Row2***********
        
        telel=customtkinter.CTkLabel(frame1,text="Numero Telephone الهاتف", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=170)
        tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightblue")
        tele.place(x=50,y=200,width=250)

        numL=customtkinter.CTkLabel(frame1,text="NUMERO chaise رقم المقعد", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=170)
        num=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightblue")
        num.place(x=370,y=200,width=250)
#reloadfunction
            
        def reload():
            self.root.destroy()
            os.system("py print.py")
        #***********Row3***********
        directioinl=customtkinter.CTkLabel(frame1,text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=240)
        cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        cmb_dir["values"]=("Selection"," أنواكشوط"," أطار"," أكجوجت","  أزويرت"," أنواذيبوا")
        cmb_dir.place(x=50,y=270,width=250)
        cmb_dir.current(0)

        datel=customtkinter.CTkLabel(frame1,text="Date now تاريخ اليوم", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=240)
        date=DateEntry(frame1,selectmode='day',font=("times new roman",15),fg="black",bg="white")
        date.place(x=370,y=270,width=250)

        #***********Row4***********

        prixl=customtkinter.CTkLabel(frame1,text="prix De Ticket", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=250,y=310)
        prix=customtkinter.CTkEntry(frame1,text_color="black", text_font=("times new roman",15),fg_color="white")
        prix.place(x=300,y=340,width=90)
        cmb_prix=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        cmb_prix["values"]=("✅","❌")
        cmb_prix.place(x=400,y=340,width=50)
        cmb_prix.current(0)
        prix.insert(END,"5000")
        tele.delete(0,END)
        num.delete(0,END)
        cmb_dir.current(0)

        def retour():
            self.root.destroy()
       
#==================================================================
        def clear():
            nom.delete(0,END)
            prenom.delete(0,END)
            tele.delete(0,END)
            num.delete(0,END)
            cmb_dir.current(0)
            cmb_prix.current(0)

        def register_data():
            """test if the user enter  only the number 
            in telephone and numero chaise"""
            numVal=num.get()
            teleVal=tele.get()
            if nom.get()=="" or numVal=="" or teleVal=="" or prenom.get()=="" or  cmb_dir.get()=="Selection"  or prix.get()=="" or num.get()=="":
                messagebox.showerror("Error", "tous les champs sont obligatoire", parent=root)
            else:
                try:
                        if numVal.isdigit() and teleVal.isdigit():
                            n=num.get()
                            # with open("../login.txt") as file:
                            with open("login.txt") as file:
                                f=file.read()
                            t=tele.get()
                            con=connects()
                            cur=con.cursor()
                        else: 
                            messagebox.showerror("Error", "numero du chaise ou numero de telephone doit etre des nombre", parent=self.root)
                        cur.execute("insert into clienttarder (nom,prenom,numero,telephone,direction,prix,date,payer,	emploiyer) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            nom.get(),
                            prenom.get(),
                            n,
                            t,
                            cmb_dir.get(),
                            prix.get(),
                            date.get_date(),
                            cmb_prix.get(),f
                        ))
                        con.commit()
                        con.close()
                        clear()

                        

                except Exception as es:
                    messagebox.showerror("Error", f"Error due to: {str(es)}", parent=root)

        btn1=customtkinter.CTkButton(master=self.root,text="RETOUR",text_font=(15),    command=retour, width=50, height=40,text_color="white", compound="right",fg_color="green", hover_color="black")
        btn1.place(x=450,y=400)
        customtkinter.CTkButton(master=root,command=register_data,bg_color="systembuttonface",text="ENREGISTRER",text_font=15, width=90,text_color="white", height=40, compound="right",fg_color="green", hover_color="blue").place(x=300,y=400)


# root=customtkinter.CTk()
# obj=Register(root)
# root.mainloop()
#------------------------------------------------------------
#--------------------------------message-----------------------------
#---------------------------Register message

from doctest import master
import tempfile
from tkinter.scrolledtext import ScrolledText
import customtkinter
import os,sys
sys.path.append("..")
from time import strftime
from tkcalendar import DateEntry
from tkinter import CENTER, Label,Entry,Spinbox,Button,END,Frame,Tk
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox


class RegMess:
    """
    if you dont put self behind eny image will not import in others folder \n
    this class for enregister client into data base
    """
    def __init__(self, root ): # default constructor and root is a tkinter class object
        customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.root = root
        scr_width=self.root.winfo_screenwidth()/2+50
        scr_height=self.root.winfo_screenheight()/2+130
        self.root.geometry("%ix%i+200+100"% (scr_width,scr_height))
        self.root.geometry("720x520+300+90") # Setting width
        self.root.config(bg="white")
        self.root.resizable(width=False, height=False)
        #***********Bg Image***********
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg",master=self.root)
        # self.bg=ImageTk.PhotoImage(file="../images/b2.jpg",master=self.root)


        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #***********Register Frame***********
        frame1=Frame(self.root,bg="#031F3C")
        frame1.place(x=10,y=10,width=700,height=500)
        frame2=Frame(self.root)
        frame2.place(x=800,y=10,width=700,height=500)

        title=customtkinter.CTkLabel(frame1,text_color="white",text="ENREGISTRER LES MESSAGES ICI سجل معلومات الرسالة هنا", text_font=("times new roman", 18, "bold"),bg_color="white",fg_color="green").place(x=50,y=30)

        #***********Row1***********

        # self.var_fname=StringVar()

        envl=customtkinter.CTkLabel(frame1,text="l'envoiyeur المرسل",text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=100)
        # self.prenomv=StringVar()
        env=customtkinter.CTkEntry(frame1,placeholder_text="nom et Prenom ...",text_font=("times new roman",15),fg_color="white",text_color="black")
        env.place(x=50,y=130,width=250)

        typel=customtkinter.CTkLabel(frame1,text="type message نوعية الرسالة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=100)
        # self.nomv=StringVar()
        type=customtkinter.CTkEntry(frame1,placeholder_text="type mess...",text_font=("times new roman",15),fg_color="white",text_color="black")
        type.place(x=370,y=130,width=250)

        #***********Row2***********
        
        telel=customtkinter.CTkLabel(frame1,text="Numero Telephone الهاتف", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=170)
        # self.telev=IntVar()
        # self.tele=Entry(frame1,textvariable=self.telev,font=("times new roman",15),bg="lightblue")
        tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightblue")
        tele.place(x=50,y=200,width=250)

        prixl=customtkinter.CTkLabel(frame1,text="السعر", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=170)
        prix=customtkinter.CTkEntry(frame1,text_color="black", text_font=("times new roman",15),fg_color="white")
        prix.place(x=370,y=200,width=70)
        prix.insert(END,"5000")
        nmbl=customtkinter.CTkLabel(frame1,text="العدد", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=500,y=170)
        nmb=customtkinter.CTkEntry(frame1,text_color="black", text_font=("times new roman",15),fg_color="white")
        nmb.place(x=500,y=200,width=70)

        
#reload------------------function
        # def validator(num):
        #     return num.isdigit() or num == ""
       

        text_ear=ScrolledText(frame2,width=40,height=20)
        text_ear.place(x=50,y=50)

            
        def reload():
            self.root.destroy()
            os.system("py enclient.py")
        # Button(self.root,text="reload",command=reload).place(x=660,y=5)
        #***********Row3***********

        directioinl=customtkinter.CTkLabel(frame1,text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=240)
        # dirv=StringVar()
        cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
        cmb_dir["values"]=("Selection"," أنواكشوط"," أطار"," أكجوجت","  أزويرت"," أنواذيبوا")
        cmb_dir.place(x=50,y=270,width=250)
        cmb_dir.current(0)

        datel=customtkinter.CTkLabel(frame1,text="Date now تاريخ اليوم", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=240)
        # datev=IntVar()
        #self.date=Calendar(self.root,selectmode='day',year=2020,month=5,day=22,width=50)
        date=DateEntry(frame1,selectmode='day',font=("times new roman",15),fg="black",bg="white")
        date.place(x=370,y=270,width=250)

        def retour():
            self.root.destroy()

        def print_text(txt):
            print_item=tempfile.mktemp('.txt')
            open(print_item,'w',encoding="utf-8").write(txt)
            os.startfile(print_item,"print")

        def write():
                        
            text_ear.insert(END,f" Bouha El Moustapha vOYAGES\tسفريات بوه ولد مصطفى ")
            text_ear.insert(END,f"\n")
            text_ear.insert(END,f"Telephone:48775476")
            text_ear.insert(END,f"\n"+"_"*49+"\n")
            text_ear.insert(END,f"\nNOM D'ENVOIYEUR : "+env.get()+"\t :إسم المرسل")
            text_ear.insert(END,f"\nNOM DE RESSEVOIR : "+type.get()+"\t :إسم المستلم")
            text_ear.insert(END,f"\nTELEPHONE:\t"+tele.get()+"\t:الهاتف")
            text_ear.insert(END,f"\nDIRECTION:\t"+cmb_dir.get().upper()+"\t:الوجهة")
            text_ear.insert(END,f"\n\tPRIX:\t"+prix.get().upper()+"\tالسعر")
            text_ear.insert(END,f"\n"+"_"*49+"\n")
            text_ear.insert(END,f"\nDATE D'IMPRIMATION:\t"+str(date.get_date())+"\t:تاريخ الطباعة ")
            text_ear.insert(END,f"\nلا نتحمل المسؤلية بعد 15 يوم")
            text_ear.insert(END,f"\n")
            text_ear.insert(END,f"aucun responsabiliter apres 15 jours")
            text_ear.insert(END,f"\n"+"."*49+"\n")

        btn1=Button(frame2,text='print',command=lambda: print_text(text_ear.get('1.0',END)))
        btn1.place(x=400,y=300)
        btn1=Button(frame2,text='reload',command=reload)
        btn1.place(x=450,y=300)
        btn=Button(frame2,text='write',command=write)
        btn.place(x=200,y=300)
        tele.delete(0,END)
        #self.temp.delete(0,END)
        # prix.delete(0,END)
        cmb_dir.current(0)

#===================================================================
    
        def clear():
            env.delete(0,END)
            type.delete(0,END)
            tele.delete(0,END)
            # self.temp.delete(0,END)
            prix.delete(0,END)
            cmb_dir.current(0)

        def register_data():
            """
                    test if the user enter  only the number 
                    in telephone and prix
            """
            # print(self.var_fname.get(), self.prenom.get())
            prixVal=prix.get()
            teleVal=tele.get()
            nmbval=nmb.get()

            if env.get()=="" or prixVal=="" or teleVal=="" or type.get()=="" or  cmb_dir.get()=="Selection"  or prix.get()=="":
                messagebox.showerror("Error", "tous les champs sont obligatoire", parent=root)
                # messagebox.showerror("Error", numVal, parent=self.root)
            else:
                try:
                    
                        if prixVal.isdigit() and teleVal.isdigit() and nmbval.isdigit():
                            n=prix.get()
                            m=nmb.get()
                            t=tele.get()
                            con=connects()
                            cur=con.cursor()
                        else: 
                            messagebox.showerror("Error", "numero du chaise ou numero de telephone doit etre des nombre", parent=self.root)
                        with open("../login.txt") as file:
                             f=file.read()
                        cur.execute("INSERT INTO message(nombre,typemessage,respteur,prix, telephone ,direction, date,emploiyer ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(
                            m,type.get(),
                            env.get(),
                            n,
                            t,
                            cmb_dir.get(),
                            date.get_date(),f
                        ))
                        con.commit()
                        con.close()
                        write()
                        op=messagebox.askyesno("Confirm", "tu veut imprimer le voyageur ?", parent=root)
                        if op==True:
                            print_text(text_ear.get('1.0',END))
                            text_ear.delete('1.0',END)
                        else :
                            text_ear.delete('1.0',END)
                        clear()
                        # self.login_window()
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to: {str(es)}", parent=root)

        btn1=customtkinter.CTkButton(master=self.root,text="RETOUR",text_font=(15),    command=retour, width=50, height=40,text_color="white", compound="right",fg_color="green", hover_color="black")
        btn1.place(x=450,y=400)
        customtkinter.CTkButton(master=root,command=register_data,bg_color="systembuttonface",text="ENREGISTRER",text_font=15, width=90,text_color="white", height=40, compound="right",fg_color="green", hover_color="blue").place(x=300,y=400)
# root=customtkinter.CTk()
# obj=Register(root)
# root.mainloop()
#-----------------------show message
import os
import sys
from time import strftime
import tkinter
from tkinter import simpledialog
from tkcalendar import DateEntry
from tkinter import CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk
from tkinter import messagebox
import customtkinter
from tkinter.messagebox import showinfo
from tabulate import tabulate
from turtle import width
sys.path.append('..')
from PIL import Image, ImageTk # pip install pillow

import tkinter as tk



class ShowMess:
    """
    this class show information in treeview 
    you can update ,delete and search data 

    """
    def __init__(self,my_w) :
            customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
            customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
         
            my_conn = connects()
            cur=my_conn.cursor()
            # Creating tkinter my_w
            scr_width=my_w.winfo_screenwidth()
            scr_height=my_w.winfo_screenheight()
            my_w.geometry("%ix%i+0+0"% (scr_width,scr_height))
            my_w.title("l'inforamtion du message")  
            my_w.resizable(0,0)
            #style
            # Add Some Style
            style = ttk.Style()

            # Pick A Theme
            style.theme_use('default')

            # Configure the Treeview Colors
            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")
# ------------------------------------frame 
            frame1=customtkinter.CTkFrame(my_w,bg_color="white")
            frame1.place(x=10,y=350,width=1400,height=500)
            title=customtkinter.CTkLabel(frame1,text_color="white",text="MODIFFIER MESSAGE ICI غير معلومات الرسالة هنا", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="black").place(x=400,y=170)
            resvl=customtkinter.CTkLabel(frame1,text="le respteur المستلم",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=0,y=200)
            resv=customtkinter.CTkEntry(frame1,placeholder_text="...المستلم",text_font=("times new roman",15),bg_color="lightgray")
            resv.place(x=0,y=250,width=250)
            typel=customtkinter.CTkLabel(frame1,text="type message نوعية الرسالة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=370,y=200)
            # self.nomv=StringVar()
            type=customtkinter.CTkEntry(frame1,placeholder_text="type mess...",text_font=("times new roman",15),fg_color="white",text_color="black")
            type.place(x=300,y=250,width=250)

            telel=customtkinter.CTkLabel(frame1,text_color="white",text="Telephone ", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=600,y=200)
            tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            tele.place(x=600,y=250,width=150)
            prixl=customtkinter.CTkLabel(frame1,width=50,text_color="white",text="prix السعر", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=790,y=200)
            prix=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            prix.place(x=800,y=250,width=50)
   
            directioinl=customtkinter.CTkLabel(frame1,text_color="white",text="DIRECTION الوجهة", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=900,y=200)
            cmb_dir=ttk.Combobox(frame1,font=("times new roman",13), state="readonly", justify=CENTER)
            cmb_dir["values"]=("Selection"," أنواكشوط"," أطار"," أكجوجت","  أزويرت"," أنواذيبوا")
            cmb_dir.place(x=900,y=250,width=180)
            cmb_dir.current(0)
            datel=customtkinter.CTkLabel(frame1,text_color="white",text="Date now", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=1100,y=250)
            date=DateEntry(frame1,selectmode='day',font=("times new roman",15),bg="lightgray")
            date.place(x=1100,y=200,width=150)
            tele.delete(0,'end')
            prix.delete(0,'end')
        
        
            # Change Selected Color
            style.map('Treeview',background=[('selected', "#347083")])           
            style.configure("Vertical.TScrollbar", background="green", bordercolor="red", arrowcolor="white")

        
        #serch-------------
            serchl=Label(my_w,text="serch",font=("times new roman", 15, "bold"),bg="white",fg="gray")
            serchl.place(x=1000,y=500)
            serchE=customtkinter.CTkEntry(my_w,placeholder_text="Rechercher phone ,nom...",text_font=("times new roman",15),bg_color="lightgray")
            serchE.place(x=1080,y=500,width=250)
            def serch():
                """
                used for finding spesific data in treeview\n
                this serchE.get()+"%" because you can't write in sql code like % %s %

                """
                for item in trv.get_children():
                    trv.delete(item)    
                conn=connects()
                cur=conn.cursor()
                q="SELECT * from message where respteur like %s or envoiyeur like %s or telephone like %s order by (id) desc"
                cur.execute(q,(serchE.get()+"%",serchE.get()+"%",serchE.get()+"%"))
                res=cur.fetchall()
                # print(res)
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['respteur'],dt['envoiyeur'],dt['telephone'],dt['prix'],dt['direction'],dt['date'],dt['emploiyer']))
                    selected = trv.focus()
                    
            sr=customtkinter.CTkButton(master=my_w,text_color="white", text="search",command=serch, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
            sr.place(x=1000,y=500)
                
        
        
            # Using treeview widget 
            r_set=cur.execute("SELECT count(id) as no from message")
            data_row=cur.fetchall()
            no_rec=data_row[0]['no']# Total number of rows in tabl
            limit = 30;
            # serchE.grid(row=9,column=0)
            
            def display(offset):
                """
                this function for display data by limit and next and previous method \n
                param offset for the numbre will show in data and shoul start by 0 and \n
                increment when click next or prev button
and shoul trv variable be global to acced into it for the others funtion
the buttonn will not appere because of some connditionell 
                """
                global trv
                
                trv = ttk.Treeview(my_w,height=18,selectmode ='browse',columns=("0","1", "2", "3","4","5","6","7"),show='headings')
                trv.grid(row=10, column=0, sticky='nsew')
                # trv.place(x=50)
                trv.bind("<ButtonRelease-1>",select)

                    
                # width of columns and alignment 
                trv.column("0", width = 100, anchor ='c')
                trv.column("1", width = 100, anchor ='c')
                trv.column("2", width = 100, anchor ='c')
                trv.column("3", width = 100, anchor ='c')
                trv.column("4", width = 50, anchor ='c')
                trv.column("5", width = 280, anchor ='c')
                trv.column("6", width = 180, anchor ='c')
                trv.column("7", width = 180, anchor ='c')
                # Headings  
                # respective columns
                trv.heading("0", text ="id")
                trv.heading("1", text ="respteur")
                trv.heading("2", text ="typemessage")
                trv.heading("3", text ="telephone")
                trv.heading("4", text ="prix")
                trv.heading("5", text ="direction")
                trv.heading("6", text ="date")
                trv.heading("7", text ="emploiyer")

                # add a scrollbar
                scrollbar = ttk.Scrollbar(my_w, orient=tk.VERTICAL, command=trv.yview)
                trv.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=10, column=1, sticky='ns')
               
                # # getting data from MySQL student table 
                # r_set=cur.execute("SELECT * from message ")
                # res=cur.fetchall()
                q="SELECT * from message order by id desc LIMIT "+ str(offset) +","+str(limit)
                cur.execute(q)
                res=cur.fetchall()
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['respteur'],dt['typemessage'],dt['telephone'],dt['prix'],dt['direction'],dt['date'],dt['emploiyer']))
                    
                            # Show buttons 
                back = offset - limit # This value is used by Previous button
                next = offset + limit # This value is used by Next button       
                


                if(no_rec <= next): 
                    b2=customtkinter.CTkButton(master=my_w,state=tkinter.DISABLED , text="suivant>>>",command=lambda: display(next), width=50, height=40, compound="right",fg_color="white", hover_color="#C77C78")

                else:
                    b2=customtkinter.CTkButton(master=my_w, text="suivant>>>",text_color="white",command=lambda: display(next), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")

                b2.place(x=200,y=500)
                    
                if(back >= 0):
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",text_color="white",command=lambda: display(back), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")
                else:
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",state=tkinter.DISABLED ,command=lambda: display(back), width=50, height=40, compound="right",fg_color="white", hover_color="yellow")
                b1.place(x=50,y=500)
                
#----------------------functions---------------
            def retour():
                my_w.destroy()
            def reload1():
                my_w.destroy()
                os.system("py showMess.py")
            def delete():
                #for delete a row in tree view
                op=messagebox.askyesno("Confirm", "tu veut vraimment suprimer ?", parent=my_w)
                if op==True:
                    selected_item = trv.selection()[0]#the frist column id
                    trv.delete(selected_item)
                    try:
                        cur.execute("delete from message where id=%s",(selected_item))
                        my_conn.commit()
                        # messagebox.showinfo("Success", "le nom et suprimer", parent=my_w)
                        clear()

                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
            def table():
                    conn=connects()
                    cur=conn.cursor()
                    op=simpledialog.askinteger("Input","أدخل عدد الرسائل للطباعة",parent=my_w)
                    q="SELECT respteur ,telephone ,typemessage as type_message,nombre ,direction  from message  order by (id) desc limit %s"
                    # q="SELECT respteur ,telephone ,prix ,typemessage as type_message,nombre ,direction  from message  order by (id) desc limit %s"
                    cur.execute(q,op)
                    res=cur.fetchall()
                    txt=" Bouha El Moustapha VOYAGES\t\t\t\t\tسفريات بوه ولد مصطفى "
                    txt+="\n"
                    txt+="LISTES DES PASSAGERS"
                    txt+="\t\t\tTelephone:48775476"
                    txt+="\n"+"_"*80+"\n"
                    a1="المرسل_له"
                    a2="الهاتف"
                    a3="نوعية الرسالة"
                    # a4="المبلغ"
                    a5="العدد"
                    a6="الاتجاه"
                    txt+="\t"+a1+"\t"+a2+"\t"+a3+"\t"+a5+"\t"+a6+"\n"
                    # txt+="\t"+a1+"\t"+a2+"\t"+a3+"\t"+a4+"\t"+a5+"\t"+a6+"\n"
                    txt+="\n"+"_"*80+"\n"
                    txt+=tabulate(res,headers='keys',tablefmt="rounded_grid")
                    txt+="\n"
                    time=strftime('%m-%d-%Y')
                    txt+="DATE D'IMPRIMATION:\t"+str(time)+"\t:تاريخ الطباعة "
                    with open("print.txt","w",encoding="utf-8") as log:
                        log.write(txt)
                        os.startfile("print.txt","print")
                        log.close()
                    
            def imp():
                table()
                    
            def imp():
                table()
                
                
            
            def select(event):
                """
                 this function used when you click the treeview and it will insert the data into input to be updated later\n
                param event is very imported if you forget it the function trv.bind("<ButtonRelease-1>",select)\n
                will simply not work
                """
                clear()
                r=trv.focus()#the frist column id
                # r=trv.selection()[0]
                content=trv.item(r)
                row=content["values"]
                resv.insert(END,row[1])
                type.insert(END,row[2])
                tele.insert(END,row[3])
                prix.insert(END,row[4])
                
            def update_data():
                #for updating data at the tree view and in our data base
                op=messagebox.askyesno("Confirm", "tu veut vraimment editer ?", parent=my_w)
                if op==True:
                    prixVal=prix.get()
                    teleVal=tele.get()
                    if type.get()=="" or prixVal=="" or teleVal=="" or resv.get()=="" or prix.get()=="":
                        messagebox.showerror("Error", "tous les champs sont obligatoire", parent=my_w)
                    else:
                        try:
                            id=trv.selection()[0]
                            if prixVal.isdigit() and teleVal.isdigit() and cmb_dir.get()=="Selection":
                                #cette if et pour le cas ou l'user nest pas entrer le direction dans update system
                                p=prix.get()
                                t=tele.get()
                                con=connects()
                                cur=con.cursor()
                                sql="update message set  typemessage=%s,respteur=%s,prix=%s,telephone=%s,direction=%s,date=%s where id=%s"
                                cur.execute(sql,(type.get(),resv.get(),p,t,cmb_dir.get(),date.get_date(),id))
                                selected = trv.focus()
                                 
                            elif prixVal.isdigit() and teleVal.isdigit():
                                p=prix.get()
                                t=tele.get()
                                sql="update message set typemessage=%s,respteur=%s,prix=%s,telephone=%s,date=%s where id=%s"
                                con=connects()
                                cur=con.cursor()
                                cur.execute(sql,(type.get(),resv.get(),p,t,date.get_date(),id))
                                selected = trv.focus()
                            trv.item(selected, text="", values=(id,resv.get(), type.get(),t, p,  cmb_dir.get(), date.get_date()))
                            selected = trv.focus()
                            con.commit()
                            # messagebox.showinfo("Success", "l'update est terminer", parent=my_w)
                            clear()
                        except Exception as es:
                            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
                else :
                    clear()

            def clear():
                type.delete(0,END)
                resv.delete(0,END)
                tele.delete(0,END)
                # temp.delete(0,END)
                prix.delete(0,END)
                cmb_dir.current(0)
            btn=customtkinter.CTkButton(master=frame1, text="suprimer",command=delete, width=50, height=40, compound="right",fg_color="#D35B58", hover_color="#C77C78")
            btn.place(x=350,y=280)
            # btn1=customtkinter.CTkButton(master=frame1, text="retour",command=retour, width=50, height=40, compound="right",fg_color="pink", hover_color="#C77C78")
            # btn1.place(x=1000,y=280)
            # btn2=customtkinter.CTkButton(master=frame1, text="reload",command=reload1, width=50, height=40, compound="right",fg_color="#D35B58", hover_color="#C77C78")
            # btn2.place(x=1100,y=280)
            btn3=customtkinter.CTkButton(master=frame1, text="editer",command=update_data, width=50, height=40, compound="right",fg_color="yellow", hover_color="#C77C78")
            btn3.place(x=450,y=280)
            btn4=customtkinter.CTkButton(master=frame1,text_font=(20), text="Imprimer طباعة",command=imp, width=50, height=40, compound="right",fg_color="green", hover_color="#C77C78")
            btn4.place(x=550,y=300)
            
            display(0)
       




# my_w =customtkinter.CTk()
# my_w1=Show(my_w)
# my_w.mainloop()

#---------------------------------------
#-----------------------------register chauffeur


import customtkinter
import os,sys
sys.path.append("..") #this is importent when you import some thing in other folder
from tkcalendar import DateEntry
from tkinter import CENTER, Label,Entry,Spinbox,Button,END,Frame,Tk
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox


class RegChauf:
    """
    if you dont put self behind eny image will not import in others folder \n
    this class for enregister client into data base
    """
    def __init__(self, root ): # default constructor and root is a tkinter class object
        customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.root = root
        scr_width=self.root.winfo_screenwidth()/2+50
        scr_height=self.root.winfo_screenheight()/2+130
        self.root.geometry("%ix%i+200+100"% (scr_width,scr_height)) # Setting width
        self.root.title("Registration Window")
        self.root.config(bg="white")
        self.root.resizable(width=False, height=False)
        
        #***********Bg Image***********
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg",master=self.root)
        # self.bg=ImageTk.PhotoImage(file="../images/b2.jpg",master=self.root)

        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #***********Register Frame***********
        frame1=Frame(self.root,bg="green")
        frame1.place(x=10,y=10,width=700,height=500)

        title=customtkinter.CTkLabel(frame1,text="ENREGISTRER chauffeur ICI سجل معلومات السائق هنا", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="green").place(x=50,y=30)

        #***********Row1***********
        noml=customtkinter.CTkLabel(frame1,text="NOM الإسم", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=100)
        nom=customtkinter.CTkEntry(frame1,placeholder_text="Nom ...",text_font=("times new roman",15),fg_color="white",text_color="black")
        nom.place(x=50,y=130,width=250)

        prenoml=customtkinter.CTkLabel(frame1,text="PRESNOM الإسم العائلي",text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=100)
        prenom=customtkinter.CTkEntry(frame1,placeholder_text="Prenom ...",text_font=("times new roman",15),fg_color="white",text_color="black")
        prenom.place(x=370,y=130,width=250)

        #***********Row2***********
        
        telel=customtkinter.CTkLabel(frame1,text="Numero Telephone الهاتف", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=50,y=170)
        tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightblue")
        tele.place(x=50,y=200,width=250)

        salL=customtkinter.CTkLabel(frame1,text="salaire الراتب", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="white").place(x=370,y=170)
        sal=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightblue")
        sal.place(x=370,y=200,width=250)
#reload------------------function
            
        def reload():
            self.root.destroy()
            os.system("py enchauf.py")
        def retour():
            self.root.destroy()

        tele.delete(0,END)
        sal.delete(0,END)

#===================================================================
    
        def clear():
            nom.delete(0,END)
            prenom.delete(0,END)
            tele.delete(0,END)
            sal.delete(0,END)
           

        def register_data():
            """test if the user enter  only the number 
            in telephone and numero chaise"""
            salVal=sal.get()
            teleVal=tele.get()
            if nom.get()=="" or salVal=="" or teleVal=="" or prenom.get()=="" :
                messagebox.showerror("Error", "tous les champs sont obligatoire", parent=root)
            else:
                try:
                        if salVal.isdigit() and teleVal.isdigit():
                            t=tele.get()
                            s=sal.get()

                            con=connects()
                            cur=con.cursor()
                        else: 
                            messagebox.showerror("Error", "numero du chaise ou numero de telephone doit etre des nombre", parent=self.root)
                        cur.execute("insert into chauffeur (nom,prenom,telephone,salaire) values(%s,%s,%s,%s)",
                        (
                            nom.get(),
                            prenom.get(),
                           s,
                            t,
                        ))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success", "Register Successful", parent=root)
                        clear()
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to: {str(es)}", parent=root)

        btn1=customtkinter.CTkButton(master=self.root,command=retour, text="RETOUR",text_font=(15),    width=50, height=40,text_color="white", compound="right",fg_color="blue", hover_color="black")
        btn1.place(x=400,y=300)
        customtkinter.CTkButton(master=root,command=register_data,bg_color="systembuttonface",text="ENREGISTRER",text_font=15, width=90,text_color="white", height=40, compound="right",fg_color="blue", hover_color="blue").place(x=200,y=300)
# root=customtkinter.CTk()
# obj=Register(root)
# root.mainloop()

#-------------------------show chauffeur
import os
import sys
import tkinter
from tkcalendar import DateEntry
from tkinter import CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk
from tkinter import messagebox
import customtkinter
from tkinter.messagebox import showinfo
from turtle import width
sys.path.append('..')#this is importent when you import some thing in other folder
from PIL import Image, ImageTk # pip install pillow

import tkinter as tk



class ShowChauf:
    """
    this class show information in treeview 
    you can update ,delete and search data 

    """
    def __init__(self,my_w) :
            customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
            customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
         
            my_conn = connects()
            cur=my_conn.cursor()
            # Creating tkinter my_w
            scr_width=my_w.winfo_screenwidth()
            scr_height=my_w.winfo_screenheight()
            my_w.geometry("%ix%i+0+0"% (scr_width,scr_height))
            my_w.title("l'inforamtion du client")  
            my_w.tk.call('encoding','system','utf-8')
            my_w.resizable(0,0)
            #style
            # Add Some Style
            style = ttk.Style()
            # Pick A Theme
            style.theme_use('default')
            # Configure the Treeview Colors
            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")
            
# ------------------------------------frame 
            frame1=customtkinter.CTkFrame(my_w,bg_color="white")
            frame1.place(x=10,y=350,width=1400,height=500)
            title=customtkinter.CTkLabel(frame1,text_color="white",text="MODIFFIER CHAUFFEUR ICI غير معلومات السائق هنا", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="black").place(x=400,y=170)
            noml=customtkinter.CTkLabel(frame1,text="NOM الإسم",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=0,y=200)
            nom=customtkinter.CTkEntry(frame1,placeholder_text="NOM",text_font=("times new roman",15),bg_color="lightgray")
            nom.place(x=0,y=250,width=250)
            prenoml=customtkinter.CTkLabel(frame1,text_color="white",text="PRESNOM الإسم العائلي",text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=300,y=200)
            prenom=customtkinter.CTkEntry(frame1,placeholder_text="PRENOM",text_font=("times new roman",15),bg_color="lightgray")
            prenom.place(x=300,y=250,width=250)
            telel=customtkinter.CTkLabel(frame1,text_color="white",text="Telephone ", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=600,y=200)
            tele=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            tele.place(x=600,y=250,width=150)
            salL=customtkinter.CTkLabel(frame1,width=50,text_color="white",text="salaire ", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="gray").place(x=790,y=200)
            sal=Spinbox(frame1,from_=0,to=50000000000000,font=("times new roman",15),bg="lightgray")
            sal.place(x=800,y=250,width=90)
            tele.delete(0,'end')
            sal.delete(0,'end')
            # Change Selected Color
            style.map('Treeview',background=[('selected', "#347083")])           
            style.configure("Vertical.TScrollbar", background="green", bordercolor="red", arrowcolor="white")
        #serch-------------
            serchl=Label(my_w,text="serch",font=("times new roman", 15, "bold"),bg="white",fg="gray")
            serchl.place(x=1000,y=500)
            serchE=customtkinter.CTkEntry(my_w,placeholder_text="Rechercher...",text_font=("times new roman",15),bg_color="lightgray")
            serchE.place(x=1080,y=500,width=250)
            def serch():
                """
                 used for finding spesific data in treeview\n
                this serchE.get()+"%" because you can't write in sql code like % %s %
                """
                for item in trv.get_children():
                    trv.delete(item)    
                conn=connects()
                cur=conn.cursor()
                q="SELECT * from chauffeur where nom like %s or prenom like %s or telephone like %s"
                cur.execute(q,(serchE.get()+"%",serchE.get()+"%",serchE.get()+"%"))
                res=cur.fetchall()
                # print(res)
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['nom'],dt['prenom'],dt['salaire'],dt['telephone']))
                    
            sr=customtkinter.CTkButton(master=my_w,text_color="white", text="search",command=serch, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
            sr.place(x=1000,y=500)
                
        
        
            # Using treeview widget 
            my_str = tk.StringVar()
            r_set=cur.execute("SELECT count(id) as no from chauffeur")
            data_row=cur.fetchall()
            no_rec=data_row[0]['no']# Total number of rows in tabl
            limit = 30;
            # serchE.grid(row=9,column=0)

            def display(offset):
                """ this function for display data by limit and next and previous method \n
                param offset for the numbre will show in data and shoul start by 0 and \n
                increment when click next or prev button

                """
                global trv
                trv = ttk.Treeview(my_w,height=18,selectmode ='browse',columns=("0","1", "2", "3","4"),show='headings')
                trv.grid(row=10, column=0, sticky='nsew')
                trv.bind("<ButtonRelease-1>",select)

                # width of columns and alignment 
                trv.column("0", width = 300, anchor ='c')
                trv.column("1", width = 300, anchor ='c')
                trv.column("2", width = 300, anchor ='c')
                trv.column("3", width = 200, anchor ='c')
                trv.column("4", width = 200, anchor ='c')
               
                #nom,prenom,numero,telephone,direction,prix,date
                # Headings  
                # respective columns
                trv.heading("0", text ="id")
                trv.heading("1", text ="nom")
                trv.heading("2", text ="prenom")
                trv.heading("3", text ="salaire")
                trv.heading("4", text ="telephone")
                
                # add a scrollbar
                scrollbar = ttk.Scrollbar(my_w, orient=tk.VERTICAL, command=trv.yview)
                trv.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=10, column=1, sticky='ns')
                # # getting data from MySQL student table 
                # r_set=cur.execute("SELECT * from client ")
                # res=cur.fetchall()
                q="SELECT * from chauffeur order by id desc LIMIT "+ str(offset) +","+str(limit)
                cur.execute(q)
                res=cur.fetchall()
                for dt in res:
                    trv.insert("", 'end',iid=dt['id'], text=dt['id'],
                    values =(dt['id'],dt['nom'],dt['prenom'],dt['salaire'],dt['telephone']))
                            # Show buttons 
                back = offset - limit # This value is used by Previous button
                next = offset + limit # This value is used by Next button       
                


                if(no_rec <= next): 
                    b2=customtkinter.CTkButton(master=my_w,state=tkinter.DISABLED , text="suivant>>>",command=lambda: display(next), width=50, height=40, compound="right",fg_color="white", hover_color="#C77C78")

                else:
                    b2=customtkinter.CTkButton(master=my_w, text="suivant>>>",text_color="white",command=lambda: display(next), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")

                b2.place(x=200,y=500)
                    
                if(back >= 0):
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",text_color="white",command=lambda: display(back), width=50, height=40, compound="right",fg_color="purple", hover_color="olive")
                else:
                    b1=customtkinter.CTkButton(master=my_w, text="<<<precedent",state=tkinter.DISABLED ,command=lambda: display(back), width=50, height=40, compound="right",fg_color="white", hover_color="yellow")
                b1.place(x=50,y=500)
                # for your understanding of how the offset value changes
                # query is displayed here, it is not part of the script 
                # my_str.set(q + '\n' + "next: " + str(next) + "\n back:"+str(back))
                # l1 = tk.Label(my_w, textvariable=my_str)
                # l1.grid(row=16,column=0,columnspan=3)
#----------------------functions---------------
            def retour():
                my_w.destroy()
            def reload1():
                my_w.destroy()
                os.system("py showCh.py")
            def delete():
                #for delete a row in tree view
                op=messagebox.askyesno("Confirm", "tu veut vraimment suprimer ?", parent=my_w)
                if op==True:
                    selected_item = trv.selection()[0]#the frist column id
                    trv.delete(selected_item)
                    try:
                        cur.execute("delete from chauffeur where id=%s",(selected_item))
                        my_conn.commit()
                        messagebox.showinfo("Success", "le nom et suprimer", parent=my_w)
                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
            
            def select(ev):
                """
                this function used when you click the treeview and it will insert the data into input to be updated later\n
                param ev is very imported if you forget it the function trv.bind("<ButtonRelease-1>",select)\n
                will simply not work

                """
                clear()
                r=trv.focus()
                content=trv.item(r)
                row=content["values"]
                nom.insert(END,row[1])
                prenom.insert(END,row[2])
                sal.insert(END,row[3])
                tele.insert(END,row[4])
                
                
            def update_data():
                """
                this function is for updating data mysql \n
                it test two option if the user click direction or forget it and that will not evect the changing of information 
                """
                #for updating data at the tree view and in our data base
                op=messagebox.askyesno("Confirm", "tu veut vraimment editer ?", parent=my_w)
                if op==True:
                    salVal=sal.get()
                    teleVal=tele.get()
                    if nom.get()=="" or salVal=="" or teleVal=="" or prenom.get()=="" :
                        messagebox.showerror("Error", "tous les champs sont obligatoire", parent=my_w)
                    else:
                        try:
                            id=trv.selection()[0]
                            if salVal.isdigit() and teleVal.isdigit() :
                                #cette if et pour le cas ou l'user nest pas entrer le direction dans update system
                                s=sal.get()
                                t=tele.get()
                                con=connects()
                                cur=con.cursor()
                                sql="update chauffeur set nom=%s,prenom=%s,salaire=%s,telephone=%s where id=%s"
                                cur.execute(sql,(nom.get(),prenom.get(),s,t,id))
                                selected = trv.focus()
                                 
                            trv.item(selected, text="", values=(id,nom.get(), prenom.get(), s, t))
                            selected = trv.focus()
                            con.commit()
                            # messagebox.showinfo("Success", "l'update est terminer", parent=my_w)
                            clear()
                        except Exception as es:
                            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=my_w)
                else :
                    clear()

            def clear():
                nom.delete(0,END)
                prenom.delete(0,END)
                tele.delete(0,END)
                sal.delete(0,END)
                
            btn=customtkinter.CTkButton(master=frame1, text="suprimer",command=delete, width=50, height=40, compound="right",fg_color="#D35B58", hover_color="#C77C78")
            btn.place(x=350,y=280)
            # btn1=customtkinter.CTkButton(master=frame1, text="retour",command=retour, width=50, height=40, compound="right",fg_color="pink", hover_color="#C77C78")
            # btn1.place(x=1000,y=280)
            # btn2=customtkinter.CTkButton(master=frame1, text="reload",command=reload1, width=50, height=40, compound="right",fg_color="#D35B58", hover_color="#C77C78")
            # btn2.place(x=1100,y=280)
            btn3=customtkinter.CTkButton(master=frame1, text="editer",command=update_data, width=50, height=40, compound="right",fg_color="yellow", hover_color="#C77C78")
            btn3.place(x=450,y=280)
            display(0)
            # serch()


# my_w =customtkinter.CTk()
# my_w1=Show(my_w)
# my_w.mainloop()
#-----------------------------------------------------

#-----------------------------emploiyer---------------
import os
import sys
import tkinter
from tkcalendar import DateEntry
from tkinter import BOTTOM, CENTER, END, Button, Entry, Frame, Label, Spinbox, ttk
from tkinter import messagebox
import customtkinter
from tkinter.messagebox import showinfo
from turtle import width
sys.path.append('..')#this is importent when you import some thing in other folder
from PIL import Image, ImageTk # pip install pillow

import tkinter as tk



class Emp:
    """
    this class show information in treeview 
    you can update ,delete and search data 

    """
    def __init__(self,my_w) :
            customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
            customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
         
            my_conn = connects()
            cur=my_conn.cursor()
            # Creating tkinter my_w
            scr_width=my_w.winfo_screenwidth()
            scr_height=my_w.winfo_screenheight()
            my_w.geometry("%ix%i+0+0"% (scr_width/2,scr_height/2))
            my_w.title("l'inforamtion du client")  
            my_w.tk.call('encoding','system','utf-8')
            my_w.resizable(0,0)
            #style
            # Add Some Style
            style = ttk.Style()
            # Pick A Theme
            style.theme_use('default')
            # Configure the Treeview Colors
            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")
            with open("login.txt") as file:
                fl=file.read()
            
# ------------------------------------frame 
            frame1=customtkinter.CTkFrame(my_w,bg_color="white")
            frame1.place(x=0,y=0,width=1400,height=500)
            title=customtkinter.CTkLabel(frame1,text_color="white",text="L'information du traveileur au system معلومات العمال المستعملين لتطبيق ", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="black").place(x=0,y=0)
            
            def rel():
                my_w.destroy()
                os.system("py emp.py")
            
            # sr=customtkinter.CTkButton(master=my_w,text_color="white", text="relod",command=rel, width=50, height=40, compound="right",fg_color="purple", hover_color="brown")
            # sr.place(x=0,y=50)
                          
            # def info():
            q="SELECT *,count(emploiyer) as total from client where emploiyer =%s "
            cur.execute(q,fl)
            res=cur.fetchall()
            for dt in res:
                a=dt['total']
                title=Label(my_w,text="Clock",font=("\nBook Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
                title.place(x=0,y=80)
                title.config(text=f"l'emploiyer {str(fl)} a registrer\n{str(a)} clients")
            q1="SELECT *,count(emploiyer) as total from message where emploiyer =%s "
            cur.execute(q1,fl)
            res1=cur.fetchall()
            for dt in res:
                a=dt['total']
                title1=Label(my_w,text="Clock",font=("\nBook Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
                title1.place(x=0,y=150)
                title1.config(text=f"l'emploiyer {str(fl)} a registrer\n{str(a)} messages")
            
# my_w =customtkinter.CTk()
# my_w1=Emp(my_w)
# my_w.mainloop()

#----------------------------------register login
from tkinter import*
from PIL import Image, ImageTk, ImageDraw # pip install pillow

from tkinter import messagebox, ttk
import customtkinter as cus
class Reg_Login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Fenetre d'EnRegistrement")
        self.root.geometry("600x555+300+70")
        self.root.config(bg="#021e2f")
        self.root.resizable(width=False, height=False)

        #***********Background***********
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=300)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        #***********Frames***********
        login_frame=cus.CTkFrame(self.root,bg_color="white")
        login_frame.place(x=100,y=30,width=370,height=500)

        
        #***********Title***********
        title=cus.CTkLabel(login_frame,text="D'ENREGISTRER NOUVELLE COMPT", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green",text_color="white").place(x=5,y=50)

        username=cus.CTkLabel(login_frame,text="Entrer nom utilisateur",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green").place(x=50,y=150)
        self.txt_username=cus.CTkEntry(master=login_frame,placeholder_text="nom d'utilisateur",text_font=("times new roman",15),bg_color="lightgray")
        self.txt_username.place(x=50,y=180,width=250)

        cus.CTkLabel(login_frame,text="Entrer password",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green").place(x=50,y=230)
        self.txt_password=cus.CTkEntry(master=login_frame,placeholder_text="mot de pass",text_font=("times new roman",15),bg_color="lightgray")
        self.txt_password.place(x=50,y=260,width=250)
        btn_login=cus.CTkButton(login_frame,text="EnRegistrer",text_color="white", text_font=("times new roman",18,"bold"),fg_color="purple",bg_color="white", cursor="hand2",command=self.login).place(x=100,y=350,width=150)
       
        
#===================functions===========================================================

    def register_window(self):
        self.root.destroy()
        #import register

    def login(self):
        if self.txt_username.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error", "tous les champs sont obligatoire",parent=self.root)
        else:
            try:
                con=connects()
                cur=con.cursor()
                cur.execute("select * from login where username=%s and password=%s",(self.txt_username.get(),self.txt_password.get(),))
                row=cur.fetchone()
                # print(row)
                if row == None:
                    cur.execute("insert into login (username,password) values(%s,%s) ",(self.txt_username.get(),self.txt_password.get(),))
                    con.commit()
                    messagebox.showinfo('succss',"l'inregistrement du nouveau compte et terminer")
                    self.txt_password.delete(0,END)
                    self.txt_username.delete(0,END)
                    self.root.destroy()
                else:
                    messagebox.showerror("error", "error le mod de pass et degas exist", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}",parent=self.root)

# root=cus.CTk()
# obj=Reg_Login_window(root)
# root.mainloop()


#--------------------------------home page----------------------------
import sys,os,customtkinter
from time import gmtime, strftime
import customtkinter as cus
from tkinter import*
from PIL import Image, ImageTk, ImageDraw # pip install pillow
from tkinter import messagebox
from datetime import *
from math import *

sys.path.append("..")

class Home:
    def __init__(self, root ): # default constructor and root is a tkinter class object
        con=connects()
        cur=con.cursor()
        self.root = root
        scr_width=self.root.winfo_screenwidth()
        scr_height=self.root.winfo_screenheight()
        self.root.title("System de voyage et transport")
        self.root.geometry("%ix%i+0+0"% (scr_width,scr_height)) # Setting width
        self.root.config(bg="white")
        self.root.resizable(0, 0)
        def Exit():
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=self.root)
            if sure == True:
                self.root.destroy()               
        self.root.protocol("WM_DELETE_WINDOW", Exit)
        #***********icons***********
        self.logo_dash = ImageTk.PhotoImage(file="images/n.jpg")
        #***********title***********
        title = Label(self.root, text="System de voyage et transport", padx=20, compound=LEFT, image=self.logo_dash, font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=100)
        def reload():
            self.root.withdraw()
            os.system("py main.py")
        #***********Creating Menu***********
        M_Frame=LabelFrame(self.root, text = "cliquer l'un des ses bouttons pou naviger vers d'autre fenetres  أضغط على زر من الأزرار لدخول الى نوافذ أخرى", font=("times new roman", 20), bg = "white")
        M_Frame.place(x=10, y=100, width = 1260, height = 100)
        btn_mes=customtkinter.CTkButton(M_Frame,text_color="white",text="الرسائل", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=message)
        btn_mes.place(x=10, y=5, width=150, height=40)       
        
        btn_cln=customtkinter.CTkButton(M_Frame,text_color="white",text="الزبناء", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=client)
        btn_cln.place(x=200, y=5, width=150, height=40)

        btn_chf=customtkinter.CTkButton(M_Frame,text_color="white",text="السائقين", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=chauffeur)
        btn_chf.place(x=400, y=5, width=150, height=40)

        btn_reg=customtkinter.CTkButton(M_Frame,text_color="white",text="اضافة مستخدم", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=verf_window)
        btn_reg.place(x=600, y=5, width=200, height=40)
        btn_reg=customtkinter.CTkButton(M_Frame,text_color="white",text="حجز زبون", text_font=("times new roman",15),bg_color="white",fg_color="green",cursor="hand2", command=Reservation)
        btn_reg.place(x=850, y=5, width=200, height=40)
        btn_exit=Button(self.root, text="خروج", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.exit_)
        btn_exit.place(x=430, y=5, width=100, height=40)

        btn_exit=Button(M_Frame, text="العامل", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.Emp_Inf)
        btn_exit.place(x=1100, y=5, width=100, height=40)
        
        #***********Content Window***********
        self.bg_img=Image.open("images/bus2.gif")
        self.bg_img=self.bg_img.resize((920, 350), Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=330, y=200, width=920, height=350)
        #***********Update Details***********
        self.lbl_message=Label(self.root, text="Total message\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_message.place(x=330, y=530, width=300, height=90)

        self.lbl_clt=Label(self.root, text="Total client\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_clt.place(x=640, y=530, width=300, height=90)
        
        self.lbl_chauf=Label(self.root, text="Total chauffeur\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_chauf.place(x=950, y=530, width=300, height=90)

        #***********clock***********
        self.lbl=Label(self.root,text="Clock",font=("\nBook Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10,y=200,height=450,width=310)
        time="\n"+strftime('%m-%d-%Y')+"\n"
        # time+=strftime('%H:%M')
        self.lbl.config(text=f"{str(time)}")
        self.working()

        #***********footer***********
        cur.execute("select * from message")
        cra=cur.fetchall()
        a=len(cra)
        cur.execute("select * from chauffeur")
        crb=cur.fetchall()
        b=len(crb)
        cur.execute("select * from client")
        crc=cur.fetchall()
        c=len(crc)
        footer = Label(self.root,width=150,height=5, text="System de voyage et transport devolloper par deidine 49619609", font=("goudy old style", 12), bg="#262626", fg="white")
        footer.place(x=0, y=650)
        self.lbl_message.config(text=f"Total message\n[{str(a)}]")
        self.lbl_chauf.config(text=f"Total chauffeur\n[{str(b)}]")
        self.lbl_clt.config(text=f"Total client\n[{str(c)}]")
        
#=============================================================================
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)

        #***********For clock Image***********
        bg=Image.open("images/c.png")
        bg=bg.resize((300,300),Image.Resampling.LANCZOS)
        clock.paste(bg,(50,50))

        #***********Hour Line Image***********
        origin = 200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #***********Min Line Image***********
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        #***********Sec Line Image***********
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("images/clock_new.png")       
    def logout(self):
        op=messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op==True:
            self.root.destroy()
            # root=Tk()
            # obj=Login_window(root)
            # root.mainloop()
    def exit_(self):
        op=messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op==True:
            self.root.destroy()
    def Emp_Inf(self):  
        # from home.emp import Emp
        my_w =customtkinter.CTk()
        my_w1=Emp(my_w)
        my_w.mainloop()

# verification  toplevl ------------------------------------------
def Reservation():
    topcl=Toplevel()
    topcl.geometry("300x300+500+70")
    topcl.resizable(0, 0)

    #***********Background***********
    lbl=Label(topcl,bg="#031F3C",bd=0)
    lbl.place(x=0,y=0,relheight=1,width=300)
    #***********Title***********
    title=cus.CTkLabel(lbl,text="bie venu dans \n la fenetre du reservation client\n مرحبا بكم في الجانب \nالمخصص لحجز زبون", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="#031F3C",text_color="white").place(x=7,y=0)
    def enclient():
        topcl.withdraw() 
        root=customtkinter.CTk()
        obj=RegRes(root)
        root.mainloop()
    def showcl():
        topcl.withdraw() 
        my_w =customtkinter.CTk()
        my_w1=ShowRes(my_w)
        my_w.mainloop()
    btn1=cus.CTkButton(lbl,command=showcl,text="afficher les\nclients",text_color="white", text_font=("times new roman",15,"bold"),fg_color="purple",bg_color="white", cursor="hand2")
    btn1.place(x=20,y=150,width=120)
    btn2=cus.CTkButton(lbl,text="register\n client",command=enclient,text_color="white", text_font=("times new roman",15,"bold"),fg_color="purple",bg_color="white", cursor="hand2")
    btn2.place(x=150,y=150,width=100)
def verf_window():            
            top=Toplevel()
            top.geometry("300x300+500+70")
            top.resizable(0, 0)

            login_frame=cus.CTkFrame(top,bg_color="white")
            login_frame.place(x=10,y=10,width=255,height=285)
            #***********Title***********
            title=cus.CTkLabel(login_frame,text="verification LOGIN ", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="red",text_color="white").place(x=7,y=0)

            username=cus.CTkLabel(login_frame,text="Entrer nom utilisateur",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green").place(x=5,y=70)
            txt_username=cus.CTkEntry(master=login_frame,placeholder_text="nom d'utilisateur",text_font=("times new roman",15),bg_color="lightgray")
            txt_username.place(x=0,y=100,width=250)

            cus.CTkLabel(login_frame,text="Entrer password",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green").place(x=5,y=170)
            txt_password=cus.CTkEntry(master=login_frame,placeholder_text="mot de pass",show="*",text_font=("times new roman",15),bg_color="lightgray")
            txt_password.place(x=0,y=200,width=250)
            def reset():
                txt_password.delete(0,END)
                txt_username.delete(0,END)
                    
            def login():
                if txt_username.get()=="" or txt_password.get()=="":
                    messagebox.showerror("Error", "All Fields Are Required",parent=top)
                else:
                    try:
                        con=connects()
                        cur=con.cursor()
                        cur.execute("select * from login where username=%s and password=%s",(txt_username.get(),txt_password.get(),))
                        row=cur.fetchone()
                        # print(row)
                        if row == None:
                            messagebox.showerror("Error", " nom  & mot de pass sont Invalid", parent=top) 
                            reset()
                        else:
                            # messagebox.showinfo("Success", f"ok : {txt_username.get()}", parent=top)
                            top.destroy()
                            root2=Tk()
                            obj=Reg_Login_window(root2)
                            root2.mainloop()
                        con.close()
                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to {str(es)}",parent=top)
            btn_login=cus.CTkButton(login_frame,text="Entrer",text_color="white", text_font=("times new roman",18,"bold"),fg_color="purple",bg_color="white", cursor="hand2",command=login).place(x=20,y=250,width=100)
#toplevel clien----------------------------
def client():
    topcl=Toplevel()
    topcl.geometry("300x300+500+70")
    topcl.resizable(0, 0)

    #***********Background***********
    lbl=Label(topcl,bg="#031F3C",bd=0)
    lbl.place(x=0,y=0,relheight=1,width=300)
    #***********Title***********
    title=cus.CTkLabel(lbl,text="bie venu dans \n la fenetre du client\n مرحبا بكم في الجانب \nالمخصص للزبون", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="#031F3C",text_color="white").place(x=7,y=0)
    def enclient():
        topcl.withdraw() 
        root=customtkinter.CTk()
        obj=RegClient(root)
        root.mainloop()
    def showcl():
        topcl.withdraw() 
        my_w =customtkinter.CTk()
        my_w1=ShowClient(my_w)
        my_w.mainloop()
    btn1=cus.CTkButton(lbl,command=showcl,text="afficher les\nclients",text_color="white", text_font=("times new roman",15,"bold"),fg_color="purple",bg_color="white", cursor="hand2")
    btn1.place(x=20,y=150,width=120)
    btn2=cus.CTkButton(lbl,text="register\n client",command=enclient,text_color="white", text_font=("times new roman",15,"bold"),fg_color="purple",bg_color="white", cursor="hand2")
    btn2.place(x=150,y=150,width=100)

#toplevel message-----------------------
def message():
   
    topmess=Toplevel()
    topmess.geometry("300x300+500+70")
    topmess.resizable(0, 0)

    #***********Background***********
    lbl=Label(topmess,bg="#031F3C",bd=0)
    lbl.place(x=0,y=0,relheight=1,width=300)
    #***********Title***********
    title=cus.CTkLabel(lbl,text="bie venu dans \n la fenetre du message\n مرحبا بكم في الجانب \nالمخصص  للرسائل  ", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="#031F3C",text_color="white").place(x=7,y=0)
    def enMessage():
        topmess.withdraw() 
        root=customtkinter.CTk()
        obj=RegMess(root)
        root.mainloop()
    def showMs():
        topmess.withdraw() 
        my_w =customtkinter.CTk()
        my_w1=ShowMess(my_w)
        my_w.mainloop()
    btn1=cus.CTkButton(lbl,command=showMs,text="afficher les\n messages",text_color="white", text_font=("times new roman",15,"bold"),fg_color="purple",bg_color="white", cursor="hand2")
    btn1.place(x=20,y=150,width=120)
    btn2=cus.CTkButton(lbl,text="register\nmessage",command=enMessage,text_color="white", text_font=("times new roman",15,"bold"),fg_color="purple",bg_color="white", cursor="hand2")
    btn2.place(x=150,y=150,width=100)
#chauffeur ------------------------

def chauffeur():
    topmess=Toplevel()
    topmess.geometry("300x300+500+70")
    topmess.resizable(0, 0)       
    #***********Background***********
    lbl=Label(topmess,bg="#031F3C",bd=0)
    lbl.place(x=0,y=0,relheight=1,width=300)
    #***********Title***********
    title=cus.CTkLabel(lbl,text="bie venu dans \n la fenetre du chauffeur\n مرحبا بكم في الجانب \nالمخصص للسائق  ", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="#031F3C",text_color="white").place(x=7,y=0)
    def enchauffeur():
        topmess.withdraw() 
        root=customtkinter.CTk()
        obj=RegChauf(root)
        root.mainloop()
    def showCh():
        topmess.withdraw() 
        my_w =customtkinter.CTk()
        my_w1=ShowChauf(my_w)
        my_w.mainloop()
    lblB=cus.CTkLabel(lbl,text=" عرض السائقين", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="#031F3C",text_color="white").place(x=0,y=100)
    btn1=cus.CTkButton(lbl,command=showCh,text="afficher les\nchauffeur",text_color="white", text_font=("times new roman",15,"bold"),fg_color="purple",bg_color="white", cursor="hand2")
    btn1.place(x=0,y=150,width=120)

    btn2=cus.CTkButton(lbl,text="register\nchauffeur",command=enchauffeur,text_color="white", text_font=("times new roman",15,"bold"),fg_color="purple",bg_color="white", cursor="hand2")
    btn2.place(x=150,y=150,width=100)
    



# if __name__=="__main__":
# root=Tk()
# obj=index(root)
# root.mainloop()

#-----------------------------------------login.py-------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------

# from home import index 
from tkinter import*
from PIL import Image, ImageTk, ImageDraw # pip install pillow
from datetime import*
import time
from math import*

from tkinter import messagebox, ttk
import os
import customtkinter as cus


class Login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Window")#)#هذا للموضوع الشاشة
        self.root.geometry("600x555+300+70")#)هذا لحجم الشاشة 
        self.root.config(bg="#021e2f")
        self.root.resizable(width=False, height=False)#)هذا لان تكون الشاشة غير قابلة التغير

        #***********Background***********
        left_lbl=cus.CTkLabel(self.root,bg_color="#08A3D2")
        left_lbl.place(x=0,y=0,relheight=1,width=300)

        right_lbl=cus.CTkLabel(self.root,bg_color="#031F3C")
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        #***********Frames***********
        login_frame=cus.CTkFrame(self.root,bg_color="white")
        login_frame.place(x=100,y=30,width=370,height=500)

        #***********Title***********
        title=cus.CTkLabel(login_frame,text="LOGIN ICI", text_font=("times new roman", 20, "bold"),bg_color="white",fg_color="green",text_color="white").place(x=100,y=50)
        username=cus.CTkLabel(login_frame,text="Entrer nom utilisateur",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green").place(x=50,y=150)
        self.txt_username=cus.CTkEntry(master=login_frame,placeholder_text="nom d'utilisateur",text_font=("times new roman",15),bg_color="lightgray")
        self.txt_username.place(x=50,y=180,width=250)

        cus.CTkLabel(login_frame,text="Entrer password",text_color="white", text_font=("times new roman", 15, "bold"),bg_color="white",fg_color="green").place(x=50,y=230)
        self.txt_password=cus.CTkEntry(master=login_frame,placeholder_text="mot de pass",show="*",text_font=("times new roman",15),bg_color="lightgray")
        self.txt_password.place(x=50,y=260,width=250)
        
        
        btn_login=cus.CTkButton(login_frame,text="Entrer",text_color="white", text_font=("times new roman",18,"bold"),fg_color="purple",bg_color="white", cursor="hand2",command=self.login).place(x=100,y=350,width=100)
       
        def reload():
            self.root.destroy()
            os.system("py login.py")
        # Button(login_frame,text="reload",command=reload).place(x=250,y=400)


#====================functions==========================================================
    def reset(self):
        self.txt_password.delete(0,END)#هذا يكون لحذف مكان الادخال
        self.txt_username.delete(0,END)
        
    def login(self):
        if self.txt_username.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error", "tous les champs sont obligatoire",parent=self.root)
        else:
            try:
                con=connects()
                cur=con.cursor()
                cur.execute("select * from login where username=%s and password=%s",(self.txt_username.get(),self.txt_password.get(),))
                row=cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error", "Invalid Username & Password", parent=self.root) 
                else:
                    # messagebox.showinfo("Success", f"Welcome: {self.txt_username.get()}", parent=self.root)
                    self.root.destroy()
                    # os.system("python index.py")
                    root2=Tk()
                    obj=Home(root2)
                    root2.mainloop()
                con.close()    
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}",parent=self.root)

     
root=Tk()
obj=Login_window(root)
root.mainloop()