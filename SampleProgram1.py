
import tkinter as tkinter

class Display:

	def __init__(self):

		self.root = tk.Tk()

		self.root.title("GUI Button Class")

		self.btn1 = tk.Button(self.root, text="Button 1")
		self.btn2 = tk.Button(self.root, text="Button 2")

		self.btn1.pack()
		self.btn2.pack()

		self.root.mainloop()

import tkinter as tkinter

root = tk.Tk()
root.title("GUI TEXT")
text1 = tk.Text(root, height = 50, width=12.5)

text1.config(state="normal")
text1.insert(tk.INSERT."Toxicity Calculator\n")
text1.insert(tk.INSERT."Input your text below")
text1.config(state="disabled")

text1.pack()
root.mainloop()

import tkinter as tk
from tkiner import tkk

def clicked() :
	print("button clicked")

 def hitReturn() :
 	print("user pressed return")
rot = tk.Tk(event)
root.title("GUI Tabs")

tabControl = tkk.Notebook(root)

tab1 = tkk.Frame(tabControl)
tabControl.add(tab1, text ="Tab 1")
tabControl.pack(expand=1, fill="both")

tab1 = tkk.Frame(tabControl)
tabControl.add(tab2, text ="Tab 2")
tabControl.pack(expand=1, fill="both")

ent1t1 = tk.Entry(tab1)
ent1t1.pack()
ent1t1.bind("<Return>",hitReturn)
 
btn = tk.Button(tab2, text="Button 2", command=clicked)
btn1t2.pck()

root.mainloop


