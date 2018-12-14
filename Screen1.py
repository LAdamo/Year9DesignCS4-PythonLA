import tkinter as tk 
#With the login page, all elements are vertically alligned, so pack is going to be used






root = tk.Tk()
#Creates the standard main window 
#Tk() is a special function called a CONSTRUCTOR
#If a function starts with a capital letter, it indicates that it is a CONSTRUCTOR


#***********WIDGET 1******************
#Three stages to building elements/objects
#1: CONTRUCT the object. We build and configure it
#2: Configure the object: We give it specific behaviors and settings (Optional)
#3: Pack the object: Put it in a window
labUN = tk.Label(root, text = "Username")
#ordered parameters: The order we send them matters. (COMMON)
#named parapeters: JavaScript and Python specific 
labUN.pack()

entUN = tk.Entry(root)
entUN.pack(ipadx=10)

labPassword = tk.Label(root, text = "Password")
labPassword.pack(ipadx=10)

entPassword = tk.Entry(root, show ="*")
entPassword.pack(ipadx=10)

btnSubmit = tk.Button(root, text = "Submit")
btnSubmit.pack(ipadx=10)


#We are writing an EVENT DRIVEN PROGRAM
#Build the GUI
#Start it running
root.mainloop()
#Runs the program 


