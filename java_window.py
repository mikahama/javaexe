#-*- coding: UTF-8 -*-
run = None
from main import *
#-*- coding: UTF-8 -*-


from ttk import *
from Tkinter import *
import tkFont

true = True
false = False
def noaction():
	pass
def component_state(comp_state):
	if comp_state:
		return NORMAL
	else:
		return DISABLED
class kWindowClass:
	kWindow = Tk()
	def __init__(self):
		kWindow = self.kWindow
		kWindow.geometry(("%dx%d")%(320,200))
		kWindow.title("JRE is missing")

		kLabel1 = Label(kWindow,name="kLabel1",text="Java is missing", font=tkFont.Font(family="Arial", size=30, weight="normal", slant="roman"), state=component_state(true) )
		kLabel1.place(x=10,y=10,width=249, height=30)


		kLabel2 = Label(kWindow,name="kLabel2",text="A Java virtual machine needs to be installed to run this program", font=tkFont.Font(family="Helvetica", size=8, weight="normal", slant="roman"), state=component_state(true) )
		kLabel2.place(x=0,y=49,width=315, height=51)


		kButton1 = Button(kWindow,name="kButton1", text="Download Java",font=tkFont.Font(family="Helvetica", size=8, weight="normal", slant="roman"), underline=-1, default=component_state(true) , command=lambda:download(self))
		kButton1.place(x=20,y=151,width=93, height=33)


		kButton2 = Button(kWindow,name="kButton2", text="Quit",font=tkFont.Font(family="Helvetica", size=8, weight="normal", slant="roman"), underline=-1, default=component_state(true) , command=lambda:quit(self))
		kButton2.place(x=216,y=151,width=64, height=32)


		kWindow.mainloop()
run = kWindowClass()
#The generated UI code ends
