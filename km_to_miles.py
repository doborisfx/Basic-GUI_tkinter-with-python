#used for gui
'''
Basic primitive UI using tkinter
this program shows a window and helps
to convert Kilometers to miles.'''

from tkinter import *
window=Tk()
window.title("Convert to Kgs to grams/Pouns/Onces")
def km_to_miles():
    #print(e1_value.get())
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)
#here the windows widges....
b1=Button(window,text="Execute",command=km_to_miles)
#b1.pack()
b1.grid(row=3,column=1)  #,rowspan=2)
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)

e1.grid(row=2,column=1)
t1=Text(window,height=1,widt=20)
t1.grid(row=4,column=1)
window.mainloop()
