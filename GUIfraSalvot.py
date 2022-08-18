import tkinter as tk
from tkinter.scrolledtext import *
import json
import time

#Open the responses database
with open('freiSalvot.json', 'r') as openfile:
	vocabulary = json.load(openfile)

#Window construction
window = tk.Tk()
window.configure(bg="black")
window.attributes("-fullscreen", True)

#Exit function
def exit_chat():
	global vocabulary
	json_object = json.dumps(vocabulary, indent=4)
	with open("freiSalvot.json", "w") as outfile:
		outfile.write(json_object)
	window.destroy()

#Menubar
menubar = tk.Menu(window)
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label='Exit', command=exit_chat)
window.config(menu=menubar)

#Code
texttosend = ""
	
def teach():
	global texttosend
	global vocabulary
	string_to_teach = entrytext.get()
	vocabulary[texttosend] = string_to_teach
	entrytext.delete("0", tk.END)
	chattext["state"] = "normal"
	chattext.insert(tk.END, "fra Salvot: Grazie! Ora ho imparato... Possiamo continuare...\n\n")
	chattext.yview(tk.END)
	sendbutt["state"] = "normal"
	teachbutt["state"] = "disabled"

def sendtext():
	global texttosend
	global vocabulary
	texttosend = entrytext.get()
	chattext["state"] = "normal"
	chattext.insert(tk.END, "\nTu: " + texttosend + "\n\n")
	entrytext.delete("0", tk.END)
	if texttosend in vocabulary:
		if texttosend.lower() == "exit":
			exit_chat()
		else:
			chattext.insert(tk.END, "fra Salvot: " + vocabulary[texttosend] + "\n\n")
			chattext.yview(tk.END)
			chattext["state"] = "disabled"
	else:
		chattext.insert(tk.END, "fra Salvot: ancora non conosco questa risposta. Tu cosa risponderesti? Insegnami!\n\n")
		chattext.yview(tk.END)
		chattext["state"] = "disabled"
		sendbutt["state"] = "disabled"
		teachbutt["state"] = "normal"

#Widgets
title = tk.Label(text="fra Salvot's Chat\n", font=("Times", 11, "bold"), bg="black", fg="green").pack()

chattext = ScrolledText(padx=15, pady=15,font=("Times", 7), wrap="word", state="disabled")
chattext.pack()

entrytext = tk.Entry(font=("Times", 7), bd=4)
entrytext.pack(side="left")

teachbutt = tk.Button(text="Teach", font=("Times", 7), relief="raised", command=teach, state="disabled")
teachbutt.pack(side="right")

sendbutt = tk.Button(text=" Send ", font=("Times", 7), relief="raised", command=sendtext)
sendbutt.pack(side="right")

#Image
fraSalvot = tk.PhotoImage(file = "image.gif")
chattext.image_create(tk.END, image= fraSalvot)
chattext["state"] = "normal"
chattext.insert(tk.END, "\n                           Benvenuto!\n")

#Database update
json_object = json.dumps(vocabulary, indent=4)
with open("freiSalvot.json", "w") as outfile:
	outfile.write(json_object)

window.mainloop()