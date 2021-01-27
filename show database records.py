import sqlite3
from tkinter import *
nitish_root= Tk()

l=[]

def Table(root,lst,total_rows,total_columns): 
     
    for i in range(total_rows): 
        for j in range(total_columns): 
            if(i==0):
                if(j==3):
                    e = Label(root,width=40,bg='grey',fg='white', font=('Arial',16,'bold'),text=lst[i][j],bd=1,relief = "solid",pady=10)
                    l.append(e)
                else:
                    e = Label(root,width=15,bg='grey',fg='white', font=('Arial',16,'bold'),text=lst[i][j],bd=1,relief = "solid",pady=10)
                    l.append(e)
            else:
                if(j==3):
                    e = Label(root,width=40,bg='white',fg='red', font=('Arial',16,'bold'),text=lst[i][j],bd=1,relief = "solid",pady=10)
                    l.append(e)
                else:
                    e = Label(root,width=15,bg='white',fg='red', font=('Arial',16,'bold'),text=lst[i][j],bd=1,relief = "solid",pady=10) 
                    l.append(e)
                  
            e.grid(row=i, column=j) 
            
            
    #Adding No. of columns and rows in Table
    countr="Rows = "+ str(total_rows-1)
    countc="Columns = "+ str(total_columns)
    
    count_r= Label(root,text=countc,width=16,bg='yellow',font=('Arial',16,'italic'))
    count_r.grid(row=total_rows,column=1)
    l.append(count_r)
    
    count_c= Label(root,text=countr,width=16,bg='yellow',font=('Arial',16,'italic'))
    count_c.grid(row=total_rows,column=0)
    l.append(count_c)

    def close_window():
        nitish_root.destroy()
    def hide_window():
        for x in l:
                x.destroy()
        print(len(l))
        l.clear()
        print(len(l))
        
    #Buttons of Hiding table and closing window
    b2 =Button(nitish_root, text='Close Window', width=14,bg='red',fg='white',activebackground='red',font=('Arial',17),command=close_window)
    l.append(b2)
    b2.grid(row=trows+3,column=0)
    b3 =Button(nitish_root, text='Hide Table', width=14,bg='green',fg='white',activebackground='yellow',font=('Arial',17),command=hide_window)
    l.append(b3)
    b3.grid(row=trows+2,column=0)


 
#opening Database
conn = sqlite3.connect('nitish_project1.db')
print("Opened database successfully");

#Getting schema and column names
h=conn.execute("PRAGMA table_info(students)")
h=list(h)
col_name=[]
for i in range(len(h)):
    col_name.append(h[i][1])
t=tuple(col_name)
col_name=[]
col_name.append(t) # getting a list as list of tuples
#print(col_name)
   
#getting data of table
data=conn.execute("SELECT * FROM students");
conn.commit()

#converting data into list
lst =list(data)
#print(lst)

#combining data of table with column names
for i in lst:
    col_name.append(i)
#print(col_name)
lst=col_name
print(lst)

   
# find total number of rows and 
# columns in list 
trows = len(lst)  
tcols = len(lst[0])

#Displaying number of rows and 
# columns in table 
print("No.of Rows = ",trows-1)
print("No.of Columns = ",tcols)

def show_table():
    t = Table(nitish_root,lst,trows,tcols)
 
#creating button 
b1 =Button(nitish_root, text='Show Table', width=25,bg='Yellow',activebackground='#FFFACD', command=show_table)
b1.grid(row=0,column=0)
nitish_root.geometry("1350x500")
nitish_root.title("UE188123 Nitish Gupta Project 1")

conn.close()
nitish_root.mainloop()
