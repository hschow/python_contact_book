def show():	
	global people
	cont=open("contacts.txt", "r")
	people=cont.read()
	print(people)
	cont.close()

def action():
	x=input("What would you like to do, add a new contact (0), display adddress book (1), search for a contact (2), modify a contact (3), delete a contact(4), or exit(5)?: ")
	global t
	t=0
	while t<1:
		if x=="add new contact" or x=="0":
			add()
			action()
		elif x=="display address book" or x=="1":
			display()
			action()
		elif x=="search for contact" or x=="2":
			search()
			action()
		elif x=="modify a contact" or x=="3":
			mod()
			action()
		elif x=="delete a contact" or x=="4":
			dele()
			action()
		elif x=="exit" or x=="5":
			exit()
		else:
			x=input("That is not an option, try again. What would you like to do with your contacts, add a new contact(0), display adddress book (1), search for a contact (2), modify a contact (3), delete a contact(4), or exit(5)?: ")


def display():
	show()

def add():
	global people	
	cont=open("contacts.txt","a")
	x=input("First put in the name: ")
	cont.write("\n")
	cont.write(x)
	cont.write("\n")
	y=input("Next add the address: ")
	cont.write(y)
	cont.write("\n")
	z=input("Now add the phone number of this contact: ")
	cont.write(z)
	cont.write("\n")
	j=input("Lastly add the email address:")
	cont.write(j)
	cont.write("\n")
	cont.write("\n")
	people=cont
	cont.close()

def search():
	lead=input("Who are you searching for: ")
	t=0
	v=0
	lead=lead+"\n"
	cont=open("contacts.txt","r")
	psb=cont.readlines()
	for x in psb[::]:
		t=t+1
		if lead==x:
			nm=psb[t-1]
			print(nm)
			adrs=psb[t]
			print(adrs)
			pnn=psb[t+1]
			print(pnn)
			eml=psb[t+2]
			print(eml)
			v=3
	if v==0:
		print("There is no contact with that name in your address book")
	cont.close()

def mod():
	lead=input("which contact do you wish to modify: ")
	t=0
	v=0
	lead=lead+"\n"
	cont=open("contacts.txt","r")
	psb=cont.readlines()
	for x in psb[::]:
		t=t+1
		if lead==x:
			nm=psb[t-1]
			print(nm)
			adrs=psb[t]
			print(adrs)
			pnn=psb[t+1]
			print(pnn)
			eml=psb[t+2]
			print(eml)
			v=3
			break
	if v==0:
		print("There is no contact with that name in your address book")
	cont.close()
	chnge=input("What part of the contact do you wish to modify: name(1), address(2), phone(3), email(4): ")
	j=0
	cont=open("contacts.txt","w")
	while j<1:
		if chnge=="name" or chnge=="1":
			new=input("What are you modifying the contact to say: ")
			for item in psb[:t-1:]:
				cont.write(item)
			cont.write(new)
			cont.write("\n")
			for item in psb[t::]:
				cont.write(item)
			j=3
		elif chnge=="address" or chnge=="2":
			new=input("What are you modifying the contact to say: ")
			for item in psb[:t:]:
				cont.write(item)
			cont.write(new)
			cont.write("\n")
			for item in psb[t+1::]:
				cont.write(item)
			j=3
		elif chnge=="phone" or chnge=="3":
			new=input("What are you modifying the contact to say: ")
			for item in psb[:t+1:]:
				cont.write(item)
			cont.write(new)
			cont.write("\n")
			for item in psb[t+2::]:
				cont.write(item)
			j=3
		elif chnge=="email" or chnge=="4":
			new=input("What are you modifying the contact to say: ")
			for item in psb[:t+2:]:
				cont.write(item)
			cont.write(new)
			cont.write("\n")
			for item in psb[t+3::]:
				cont.write(item)
			j=3
		else:
			chnge=input('That was not a valid answer, so what part of the contact do you wish to modify: name(1), address(2), phone(3), email(4): ')


def dele():
	lead=input("Which contact do you wish to delete: ")
	v=0
	lead=lead+"\n"
	cont=open("contacts.txt","r")
	psb=cont.readlines()
	t=0
	for x in psb[::]:
		t=t+1
		if lead==x:
			cont.close()
			cont=open("contacts.txt","w")
			for item in psb[:t-1:]:
				cont.write(item)
			cont.write("")
			for item in psb[t+5::]:
				cont.write(item)
			v=3
	if v==0:
		print("There is no contact with that name in your address book")
	cont.close()

def exit():
	global t
	t=4

def main():
	show()
	action()
main()