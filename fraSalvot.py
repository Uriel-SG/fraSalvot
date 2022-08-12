import json
import time
import subprocess

with open('freiSalvot.json', 'r') as openfile:
	vocabulary = json.load(openfile)

class color:
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'
   
time.sleep(0.5)

print(color.BLUE + color.BOLD + "\n########## BENVENUTO/A nella chat di FRA SALVOT! ##########" + color.END)
time.sleep(1.8)

while True:
	print(color.GREEN + '''
	Scegli una opzione:
		
		1- Parlami e insegnami ciò che ancora non so
		
		2- Esci
		
		''' + color.BLUE)
	
	scelta = input("--> " + color.GREEN)			
	if scelta == "1":	
		print(color.BLUE + "\n############################################################")
		time.sleep(1)
		print(color.RED + "Inizio chat")
		time.sleep(0.8)
		print("digita 'exit' per uscire dalla chat in qualsiasi momento\n")
		time.sleep(1.5)
		while True:
			io = input(color.END + color.BOLD + "\nTu: " + color.END)
			io = io.lower()
			if io == "exit":
				time.sleep(0.5)
				print(color.BLUE + color.BOLD + "\nfra Salvot:" + color.END + "Ciao! È stato un piacere, torna in qualsiasi momento...\n")
				time.sleep(2)
				print(color.BLUE + "\n############################################################" + color.END)
				break
				
			if io == "myip":
				time.sleep(0.5)
				subprocess.run(["curl", "ipinfo.io/ip"])
			if io == "uriel":
				subprocess.run(["termux-open", "https://uriel-code.web.app"])
			
			if io == "puoi fare una ricerca per me?" or io == "google":
				time.sleep(0.5)
				testo = "spero la ricerca sia stata fruttuosa! :-)"
				input(color.BLUE + "\nFra Salvot: " + color.END + "ti dò la possibilità di fare qualsiasi ricerca da qui... per uscire poi, basterà digitare 'q' e poi 'y' ok? andiamo!")
				vocabulary[io] = testo
				subprocess.run(["w3m", "www.google.com"])
			
			if io in vocabulary:
				time.sleep(1)
				print(color.BLUE + color.BOLD + "\nFra Salvot: " + color.END + vocabulary[io])
			else:
				time.sleep(0.5)
				learn = input(color.BLUE + "\nFra Salvot: " + color.END + "è la prima volta che sento questo, tu come risponderesti? Insegnami!\n Risposta: ")
				vocabulary[io] = learn
				continue
				
	elif scelta == "2":
				break
				
json_object = json.dumps(vocabulary, indent=4)

with open("freiSalvot.json", "w") as outfile:
	outfile.write(json_object)
	
print(color.BLUE + "\nfra Salvot: " + color.END + "Alla prossima!")



