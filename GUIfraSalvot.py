import tkinter as tk
import json
import time

with open('test.json', 'r') as openfile:
	vocabulary = json.load(openfile)

window = tk.Tk()
window.configure(bg="black")
window.attributes("-fullscreen", True)

texttosend = ""

def teach():
	global texttosend
	string_to_teach = entrytext.get()
	vocabulary[texttosend] = string_to_teach
	entrytext.delete("0", tk.END)
	chattext["state"] = "normal"
	chattext.insert(tk.END, "fra Salvot: Grazie! Ora ho imparato... Possiamo continuare...\n\n")
	sendbutt["state"] = "normal"
	teachbutt["state"] = "disabled"

def sendtext():
	global texttosend
	texttosend = entrytext.get()
	chattext["state"] = "normal"
	chattext.insert(tk.END, "Tu: " + texttosend + "\n\n")
	entrytext.delete("0", tk.END)
	if texttosend in vocabulary:
		time.sleep(0.8)
		chattext.insert(tk.END, "fra Salvot: " + vocabulary[texttosend] + "\n\n")
		chattext["state"] = "disabled"
	else:
		chattext.insert(tk.END, "fra Salvot: ancora non conosco questa risposta. Tu cosa risponderesti? Insegnami!\n\n")
		chattext["state"] = "disabled"
		sendbutt["state"] = "disabled"
		teachbutt["state"] = "normal"


title = tk.Label(text="fra Salvot's Chat\n", font=("Times", 11, "bold"), bg="black", fg="green").pack()

chattext = tk.Text(padx=15, pady=15,font=("Times", 7), wrap="word", state="disabled")
chattext.pack()

entrytext = tk.Entry(font=("Times", 7), bd=4)
entrytext.pack(side="left")

teachbutt = tk.Button(text="Teach", font=("Times", 7), relief="raised", command=teach, state="disabled")
teachbutt.pack(side="right")

sendbutt = tk.Button(text=" Send ", font=("Times", 7), relief="raised", command=sendtext)
sendbutt.pack(side="right")



window.mainloop()