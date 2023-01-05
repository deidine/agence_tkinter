import os
import tempfile
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from barcode import EAN13
from barcode.writer import ImageWriter
root=Tk()
root.geometry("700x600")
root.title('barcode')
number = Entry(root)
number.place(x=80,y=20)
def bar():
    my_code = EAN13(number.get(), writer=ImageWriter())
    my_code.save("deidine1")     
    
btn=Button(root,text="barcde",command=bar)
btn.place(x=80,y=50)

text_ear=ScrolledText(root,width=40,height=20)
text_ear.place(x=50,y=150)


def print_text(txt):
    print_item=tempfile.mktemp('.txt')
    open(print_item,'w',encoding="utf-8").write(txt)
    os.startfile(print_item,"print")
def print_code():
    print_item="deidine.png"
    os.startfile(print_item,"explore")

def write():
    text_ear.insert('1.0',"rrr")

btn1=Button(root,text='print',command=print_code)
btn1.place(x=100,y=100)
# btn1=Button(root,text='print',command=lambda: print_text(text_ear.get('1.0',END)))
# btn1.place(x=100,y=100)
# btn1=Button(root,text='reload',command=reload)
# btn1.place(x=450,y=300)
btn=Button(root,text='write',command=write)
btn.place(x=20,y=150)
root.mainloop()