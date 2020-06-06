from tkinter import *
root=Tk()
def f(num):
	if(num==1):
		root.configure(background="red")
	elif(num==2):
		root.configure(background="green")
	else:
		root.configure(background="blue")



root.title("Color me 2.0")
root.geometry("400x400+300+200")
btnRed=Button(root,text="Red",width=10,font=("arial",20,'bold'),command=lambda:f(1))
btnGreen=Button(root,text="Green",width=10,font=("arial",20,'bold'),command=lambda:f(2))
btnBlue=Button(root,text="Blue",width=10,font=("arial",20,'bold'),command=lambda:f(3))
btnRed.place(x=10,y=120)
btnGreen.place(x=100,y=50)
btnBlue.place(x=200,y=200)

root.mainloop()