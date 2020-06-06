from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Kamaml Classes App")
root.geometry("300x500+300+100")
lblname=Label(root,text="NAME",font=("arial",18,"bold"))
entname=Entry(root,bd=10,font=("arial",18,"bold"))

lblname.grid()
entname.grid()
lblfeedback=Label(root,text="Feedback",font=("arial",18,"bold"))
f=IntVar()
f.set(1)
rbf=Radiobutton(root,text="Fantastic",font=("arial",18,"bold"),variable=f,value=1)
rbs=Radiobutton(root,text="Superb",font=("arial",18,"bold"),variable=f,value=2)
rbe=Radiobutton(root,text="Excellent",font=("arial",18,"bold"),variable=f,value=3)

lblfeedback.grid()
rbf.grid(sticky="W")
rbs.grid(sticky="W")
rbe.grid(sticky="W")
lblmaterial=Label(root,text="Materials",font=("arial",18,"bold"))
s,n,c=IntVar(),IntVar(),IntVar()
cbsw=Checkbutton(root,text="Software",font=("arial",18,"bold"),variable=s)
cbnotes=Checkbutton(root,text="Notes",font=("arial",18,"bold"),variable=n)
cbcer=Checkbutton(root,text="Certificate",font=("arial",18,"bold"),variable=c)
lblmaterial.grid()
cbsw.grid(sticky="W")
cbnotes.grid(sticky="W")
cbcer.grid(sticky="W")

def f1():
	name=entname.get()
	if len(name)<2 or not name.isalpha():
		messagebox.showerror("Galat kar raha hai broo")
		entname.delete(0,END)
		entname.focus()
	fe=f.get()
	if fe==1:
		fb="Fantastic"
	elif fe==2:
		fb="Superb"
	else:
		fb="Excellent"
	material=""
	if s.get()==1:
		material=material+"Software"
	if n.get()==1:
		material=material+"Notes"
	if c.get()==1:
		material=material+"Certificate"
				
	msg="Name="+name+"\n Feedback="+fb+"\nMaterials="+material
	messagebox.showinfo("Msg",msg)

	to="kamalsir@ymail.com"
	subject="Feedback By"+name
	text=msg
	import smtplib
	sender='pradhan.prachi10@gmail.com'
	password='9870162027'
	message='Subject:{}\n\n'.format(subject,text)
	server=smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.ehlo()
	server.login(sender,password)
	print('logged in')
	try:
		server.sendmail(sender,to,message)
		print("email sent")
	except:
		print("Galti se mistake hua re baba")
	server.quit

btnSubmit=Button(root,text="Submit",font=("arial",18,"bold"),command=f1)
btnSubmit.grid()



root.mainloop()