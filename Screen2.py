import tkinter as tk

root = tk.Tk()



title1 = tk.Label(root, text = "Enter toxicity here")
title1.grid(row =0, column =0, columnspan = 3, sticky = "NESW")
output = tk.Text(root, background = "white", height = 10, width = 50)
#output.config(state = "disabled")
output.grid(row =1, column =1, columnspan = 2)

btnSubmit = tk.Button(root, text = "Submit", height = 2, width = 40)
btnSubmit.grid(row = 2, column = 2, columnspan = 1)










root.mainloop()