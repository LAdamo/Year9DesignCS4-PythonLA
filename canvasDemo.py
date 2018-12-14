import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root,width = 200, height = 200, background = "black")

toxicity = 86

xy = 20, 20, 180, 180
canvas.create_arc(xy, start=0, extent=int((toxicity/100)*360), fill="red")
canvas.create_arc(xy, start=int((toxicity/100)*360), extent=360 - ((toxicity/100)*360), fill="blue")

canvas.pack()

root.mainloop()
