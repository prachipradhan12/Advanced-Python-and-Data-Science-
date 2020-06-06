from tkinter import *
root=Tk()
def f1():
	root.configure(background="red")
	#btnRed.configure(background="red")
def f2():
	root.configure(background="green")

def f3():
	root.configure(background="blue")



root.title("Color me")
root.geometry("400x400+300+200")
btnRed=Button(root,text="Red",width=10,font=("arial",20,'bold'),command=f1)
btnGreen=Button(root,text="Green",width=10,font=("arial",20,'bold'),command=f2)
btnBlue=Button(root,text="Blue",width=10,font=("arial",20,'bold'),command=f3)
btnRed.pack(pady=20)
btnGreen.pack(pady=20)
btnBlue.pack(pady=20)

root.mainloop()