import tkinter as tk 

root = tk.Tk()     

 # Tk() is a special meyhod called a contructor
 # A constructor is a special method onlt called once it is set up




lab = tk.Label(root, text = "Enter a number")
#To pack an element using the grid geometry manager, We use # <object>.grid(<parameters>)


lab.grid(root, row = 0, column = 0)


ent = tk.Entry(root)
ent.grid(row = 1, column = 0)

btn = tk.Button(root, text = "Press me dad")
btn.grid(row = 2, column = 0)

output = tk.Text(root)
output.configure(state = "disable")
output.grid(row = 0, column = 1, rowspan = 3)





root.mainloop()
