import sqlite3
conn = sqlite3.connect('nitish_project1.db')

from tkinter import *
nitish_root=Tk()
nitish_root.title('Nitish QUES 2')
nitish_root.geometry("300x250")

#Labeling
head1=Label(nitish_root, text="Enter Name of student", fg='red',bg='thistle2',width=20)
head2=Label(nitish_root, text="whose Record to Fetch", fg='red',bg='thistle2',width=20)
head1.place(x=80, y=20)
head2.place(x=80, y=40)

#Input field
input_fld=Entry(nitish_root, text="This is Entry Widget", bd=5)
input_fld.place(x=85, y=68)

def prints():
    x=conn.execute("select * from students where NAME='%s';"%(input_fld.get()));
    lst=list(x)
    m=lst[0]
    
    #Labeling
    q=Label(nitish_root, text="Name", fg='black',bg='yellow',width=10)
    w=Label(nitish_root, text="Roll No.", fg='black',bg='yellow',width=10)
    e=Label(nitish_root, text="Branch", fg='black',bg='yellow',width=10)
    q.place(x=80, y=160)
    w.place(x=80, y=184)
    e.place(x=80, y=210)
    margin=10;
    
    for d in m:
        y=Label(nitish_root, text=d, fg='Blue',bg='yellow',width=10)
        y.place(x=160, y=150+margin)
        margin=margin+24
        
btn=Button(nitish_root, text="Enter here", fg='white',bg='red',command=prints)
btn.place(x=120, y=100)
nitish_root.mainloop()

conn.commit()
conn.close()
