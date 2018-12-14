import tkinter as tk 

root = tk.Tk()


#############################################VARIABLES############################################


#Take your variables and put them in a list where you know the index 


var = ["",0,0,1,0]
text = "" #var[0]
length = 0 #var[1]
toxicity = 0 #var[2]
words = 1 #var[3]
swear = 0 #var[4]


#############################################FUNCTIONS############################################


def clicked():

	

	print("Button Clicked")

	var[0] = entry.get("1.0", tk.END) 
	var[0] = var[0].lower()
	length = len(var[0])

	print(var[0])
	for i in range (0, length, 1):
		if var[0][i] == " ":
			var[3] = var[3] +  1

	for i in range (0,length - 2,1):
		print("test")
		if var[0][i:i+3] == "bad":
			var[4] = var[4] + 1

	for i in range (0,length - 4,1):
		if var[0][i:i+5] == "badaa":
			var[4] = var[4] + 1

	for i in range (0,length - 3,1):
		if var[0][i:i+4] == "bads":
			var[4] = var[4] + 1

	for i in range (0,length - 3,1):
		if var[0][i:i+4] == "badc":
			var[4] = var[4] + 1

	for i in range (0,length - 2,1):
		if var[0][i:i+3] == "bak":
			var[4] = var[4] + 1

	for i in range (0,length - 2,1):
		print("TEST")
		if var[0][i:i+3] == "baf":
			var[4] = var[4] + 1

	for i in range (0,length - 8,1):
		if var[0][i:i+9] == "badb badm":
			var[4] = var[4] + 1

	for i in range (0,length - 5,1):
		if var[0][i:i+6] == "badtard":
			var[4] = var[4] + 1


	if var[3] > 0:
		print("IN")
		print(var[4]," : var4")
		print(var[3]," : var3")
		toxicity = var[4] / var[3] * 100
		print(toxicity)
	else:
		toxicity = 0

	toxicOutput.config(state= "normal")
	toxicOutput.insert(tk.INSERT, "You are "+str(toxicity)+"% toxic.\n")
	toxicOutput.config(state="disabled")

	
	toxicity = int(toxicity)
	xy = 20, 20, 180, 180
	canvas.create_arc(xy, start=0, extent=int((toxicity/100)*360), fill="#ff7070")
	canvas.create_arc(xy, start=int((toxicity/100)*360), extent=360 - ((toxicity/100)*360), fill="#a4ff70")


##############################################GUI###################################################

root.configure(background='white')

title1 = tk.Label(root, text = "ENTER TEXT")
title1.grid(row =0, column =0, columnspan = 3, sticky = "NSW")

entry = tk.Text(root, background = "white", height = 10, width = 100)
entry.grid(row =1, column =1, rowspan = 3, sticky = "NESW")

title1 = tk.Label(root, text = "RESULTS")
title1.grid(row =1, column =2, columnspan = 1, sticky = "NESW")

canvas = tk.Canvas(root, background = "black")
canvas.grid(row = 2, column = 2)

toxicOutput = tk.Text(root, background = "white", height = 2, width = 10)
toxicOutput.grid(row = 3, column = 2, sticky = "NESW")

computeBtn = tk.Button(root, text = "COMPUTE", command = clicked)
computeBtn.grid(row = 4, column = 0, columnspan = 2, sticky = "NESW")


root.mainloop()