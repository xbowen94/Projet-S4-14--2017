from tkinter import *
from tkinter import font
from Prise import *
#from interface import *

global priseUpdated
priseUpdated=Prise(0)
def Reglages(fenetre,index,prise):
	#global prises2
	print('indice prise: ',index)
	priseUpdated=Prise(0)
	root =Toplevel(fenetre)
	root.geometry("800x500")
	root.resizable(width=TRUE, height=TRUE)
	#root.iconify()
	v1 = IntVar()
	v2 = IntVar()
	v3 = IntVar()
	v4 = IntVar()
	v5 = IntVar()
	v6 = IntVar()
	v7 = IntVar()

	# initializing the choice, i.e. Python
	v1.set(0)  
	v2.set(0)
	v3.set(0)
	v4.set(0)
	v5.set(0)
	v6.set(0)
	v7.set(0)

	type_Prise = [("Aucun information",0),
	    ("Prise main gauche",1),
	    ("Prise main droite",2),
	    ("Prise pied gauche",3),
	    ("Prise pied droit",4),
	    ]

	difficulte = [("Aucun information",0),
	    ("Abominable",1),
	    ("Dur",2),
	    ("Facile",3),
	    ("Très facile",4),
	    ]

	apprehension= [("Aucun information",0),
	    ("Arquée",1),
	    ("Pince",2),
	    ("Plat",3),
	    ("Bacs",4),
	    ]

	proximite = [("Aucun information",0),
	    ("Très loin",1),
	    ("Loin",2),
	    ("Proche",3),
	    ("Très proche",4),
	    ]

	def getValueofSpin(s):
		v7.set(Spinbox.get(s))
		

	def SaveChoice():

		root.withdraw()
	  
	  	#Set type de prise
		print('Type de Prise elegida: ',v1.get())
		prise.set_TypePrise(v1.get())
		#print('Type de Prise guardada: ',prise.type_prise)
		#print(priseUpdated.type_prise)

		#Set difficulté de prise
		prise.set_Difficulte(v2.get())

		#Set apprehension de la prise
		prise.set_Apprehension(v3.get())

		#Set proximité de la prise
		prise.set_Proximite(v4.get())

		#Indiquer prise départ
		prise.isPriseDepart(v5.get())

		#Indiquer prise fin
		prise.isPriseFin(v6.get())

		#Set ordre prise
		prise.set_Ordre(v7.get())

		priseUpdated=prise
		return priseUpdated

	#def SupprimerPrise():



	Helvfont = font.Font(family="Helvetica", size=10, weight="bold")
	title=Label(root, 
	      text="""CARACTERISATION DE LA PRISE""",
	      justify = LEFT,
	      font=Helvfont,
	      padx = 20)
	title.grid(row=1,column=1)

	l=Label(root, 
	      text="""Type de prise:""",
	      justify = LEFT)
	l.place(x = 20, y = 30)
	i=0
	for txt, val in type_Prise:
		r=Radiobutton(root, 
			        text=txt,
			        indicatoron=0,
			        width = 20,
			        padx = 20, 
			        variable=v1, 
			        #command=SaveChoice,
			        #fg='White' if brightness < 120 else 'Black', 
			        #bg=bg_colour,
			        value=val)
		r.place(x = 20, y =80 + i*30, width=120, height=25)
		i+=1

	l=Label(root, 
	  text="""Difficulté:""",
	  justify = LEFT)
	l.place(x = 220, y = 30)
	i=0
	for txt, val in difficulte:
		r=Radiobutton(root, 
			        text=txt,
			        indicatoron=0,
			        width = 20,
			        padx = 20, 
			        variable=v2, 
			        #command=SaveChoice,
			        #fg='White' if brightness < 120 else 'Black', 
			        #bg=bg_colour,
			        value=val)
		r.place(x = 220, y =80 + i*30, width=120, height=25)
		i+=1


	l=Label(root, 
	  text="""Apprehension:""",
	  justify = LEFT)
	l.place(x = 420, y = 30)
	i=0
	for txt, val in apprehension:
		r=Radiobutton(root, 
			        text=txt,
			        indicatoron=0,
			        width = 20,
			        padx = 20, 
			        variable=v3, 
			        #command=SaveChoice,
			        #fg='White' if brightness < 120 else 'Black', 
			        #bg=bg_colour,
			        value=val)
		r.place(x = 420, y =80 + i*30, width=120, height=25)
		i+=1

	l=Label(root, 
	  text="""Proximité:""",
	  justify = LEFT)
	l.place(x = 620, y = 30)
	i=0
	for txt, val in proximite:
		r=Radiobutton(root, 
			        text=txt,
			        indicatoron=0,
			        width = 20,
			        padx = 20, 
			        variable=v4, 
			        #command=SaveChoice,
			        #fg='White' if brightness < 120 else 'Black', 
			        #bg=bg_colour,
			        value=val)
		r.place(x = 620, y =80 + i*30, width=120, height=25)
		i+=1


	l=Label(root, 
	  text="""Prise de départ?""",
	  justify = LEFT)
	l.place(x = 20, y = 230)

	r=Radiobutton(root, 
		text='Oui',
		indicatoron=0,
		width = 20,
		padx = 20, 
		variable=v5, 
		#command=SaveChoice,
		#fg='White' if brightness < 120 else 'Black', 
		#bg=bg_colour,
		value=1)
	r.place(x = 20, y =280, width=120, height=25)

	r=Radiobutton(root, 
		text='Non',
		indicatoron=0,
		width = 20,
		padx = 20, 
		variable=v5, 
		#command=SaveChoice,
		#fg='White' if brightness < 120 else 'Black', 
		#bg=bg_colour,
		value=2)
	r.place(x = 20, y =310, width=120, height=25)

	l=Label(root, 
	  text="""Prise de fin?""",
	  justify = LEFT)
	l.place(x = 220, y = 230)

	r=Radiobutton(root, 
		text='Oui',
		indicatoron=0,
		width = 20,
		padx = 20, 
		variable=v6, 
		#command=SaveChoice,
		#fg='White' if brightness < 120 else 'Black', 
		#bg=bg_colour,
		value=1)
	r.place(x = 220, y =280, width=120, height=25)

	r=Radiobutton(root, 
		text='Non',
		indicatoron=0,
		width = 20,
		padx = 20, 
		variable=v6, 
		#command=SaveChoice,
		#fg='White' if brightness < 120 else 'Black', 
		#bg=bg_colour,
		value=2)
	r.place(x = 220, y =310, width=120, height=25)


	l=Label(root, 
	  text="""Numero de prise?""",
	  justify = LEFT)
	l.place(x = 420, y = 230)
	s = Spinbox(root, from_=0, to=10, command= lambda : getValueofSpin(s))
	s.place(x = 420, y = 280)
	#print(Spinbox.get(s))


	#bSup=Button(root, text  = 'Supprimer Prise', command  =  lambda : SupprimerPrise())
	#bSup.place(x=20,y=380)
	

	b=Button(root, text  = 'Ok', command  =  lambda : SaveChoice())
	b.place(x=20,y=420)
	
	# Label(root, 
	#   text="""Il s'agit d'une prise de départ?""",
	#   justify = RIGHT,
	#   padx = 20,
	#   anchor=N).grid(row=9,column=1)

	# Radiobutton(root,
	#         text='Oui',
	#         anchor=N,
	#         variable=v5,
	#         command=SaveChoice,
	#         value=1).grid(row=10,column=1)

	# Radiobutton(root,
	#         text='Non',
	#         anchor=N,
	#         variable=v5,
	#         command=SaveChoice,
	#         value=2).grid(row=11,column=1)

	# Label(root, 
	#   text="""Il s'agit d'une prise de fin?""",
	#   justify = RIGHT,
	#   padx = 20,
	#   anchor=N).grid(row=9,column=2)

	# Radiobutton(root,
	#         text='Oui',
	#         anchor=N,
	#         variable=v6,
	#         command=SaveChoice,
	#         value=1).grid(row=10,column=2)

	# Radiobutton(root,
	#         text='Non',
	#         anchor=N,
	#         variable=v6,
	#         command=SaveChoice,
	#         value=2).grid(row=11,column=2)

	# B_ok= Button(root, text  = 'Ok', command  =  lambda : SaveChoice())
	# B_ok.grid(row=14,column=5)


