from tkinter import *
from tkinter import messagebox

win=Tk()
win.title("")
sel = IntVar()
sel.set(1)
rdJob=Radiobutton(win,text="Job",font=("courier",20,'bold italic'),variable=sel,value=1)
rdMS=Radiobutton(win,text="MS",font=("courier",20,'bold italic'),variable=sel,value=2)
rdMBA=Radiobutton(win,text="M B A",font=("courier",20,'bold italic'),variable=sel,value=3)
rdMtech=Radiobutton(win,text="MTech",font=("courier",20,'bold italic'),variable=sel,value=4)

rdJob.grid(sticky="W")
rdMS.grid(sticky="W")
rdMBA.grid(sticky="W")
rdMtech.grid(sticky="W")

def f1():
	res=sel.get()
	if res==1:
		msg="Job"
	elif res==2:
		msg="MS"
	elif res==3:
		msg="MBA"
	else:
		msg="MTech"

	messagebox.showinfo("Selection",msg)

btnsub=Button(win,text="Submit",width=10,font=("arial",20,'bold'),command=f1)
btnsub.grid()
win.mainloop()







