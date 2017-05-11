# Copyright (c) 2016 Guillemette Massot <guillemette.massot@telecom-bretagne.eu>
#                    Elisa Blanchard <elisa.blanchard@telecom-bretagne.eu>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter
from tkinter.filedialog import *

from PIL.Image import *
import sys
from Prise import Prise 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage
import csv
from Reglages import *
#Initialisation des variables globales
x      = 0
y      = 0
rouge  = []
vert   = []
bleu   = []
index  = 0
arrayX = []
arrayY = []
couleurs = []
global prises
global prises2
prises = []
prises2 = []
count_clicks=0
flag = False
#Creation d'une fenetre 
fenetre =  Tk()
fenetre.title('Braille pour grimpeur')
v = IntVar()
v.set(1) 

#Ouverture de l'image
filepath                         =  askopenfilename(title = "Ouvrir une image",filetypes = [('png files','.png'),('all files','.*')])
photo                            =  PhotoImage(file = filepath)
canvas                           =  Canvas(fenetre, width = photo.width(), height = photo.height())
canvas.pack(anchor=W)
canvas.create_image(0, 0, anchor = NW, image = photo)
fenetre.geometry("500x300") 
"""
def CreationCSV(prises2):
	with open('prises.csv', 'w') as csvfile:
		fieldnames = ['Prise_id', 'Colour','Surface','x','y']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		#for i in prises2:
		writer.writerow({'Prise_id': '1', 'Colour': 'red', 'Surface': '1500', 'x': '80','y': '150'})
			#writer.writerow({'Prise_id': prises2[i].prise_Id, 'Colour': 'red', 'Surface': prises2[i].surface, 'x': prise2[i].centre[0],'y': prise2[i].centre[0]})
    
"""

def creationPrise(img):
   global prises
   global prises2
   im = open(filepath)
   byn = ndimage.gaussian_filter(img.convert("L"), 0.9) # image improvement filter
   byn2 = img.convert("L") # black and white image
   s = [[0, 1, 0], [1,1,1], [0,1,0]] # connectivity condition
   label_im, nb_labels = ndimage.label(byn,s) #introduction of the labels to the image's matrix
   lbl = ndimage.label(label_im)[0]
   centers=ndimage.measurements.center_of_mass(label_im, lbl,range(nb_labels + 1))
   windows=ndimage.find_objects(label_im) #making windows wherer there is a prise
   for i in range(nb_labels): 
   		counter=0
   		prises.append(Prise(i))
   		prises[i].centre=(centers[i+1][1],centers[i+1][0]) # centers had (y,x), so we put it inverted, center[0] doesn't exist
   		for k in range(windows[i][0].start,windows[i][0].stop):  # going throw the array using the slices of windows
   			for j in range(windows[i][1].start,windows[i][1].stop):
   				if label_im[k,j]==i+1:  #first slice is 0 but label 0 is background
   					counter+=1
   		prises[i].surface=counter
   		(red,green,blue)  =  im.getpixel((centers[i+1][1],centers[i+1][0]))
   		prises[i].couleur=[red,green,blue]


   j=0
   for i in range(len(prises)):
   		if prises[i].surface>400:
   			prises2.append(prises[i])
   			prises2[j].priseId=j
   			print (prises2[j].centre)
   			print (prises2[j].surface)
   			j+=1
   #plt.figure()
   #plt.imshow(label_im)
   #plt.show()
   #CreationCSV(prises2)
   """mean_vals = ndimage.sum(byn, label_im, range(1, nb_labels + 1)) # this part was another option instead of filter
   mask_size = sizes < 1000
   remove_pixel = mask_size[label_im]
   #remove_pixel.shape(256, 256)
   label_im[remove_pixel] = 0
   labels = np.unique(label_im)
   label_im = np.searchsorted(labels, label_im)
   #c=ndimage.measurements.center_of_mass(label_im,2)       
   #print(ndimage.measurements.center_of_mass(img2, label_im, [1,2]))
   plt.figure()
   plt.imshow(label_im)
   plt.show()"""


def pointeur(event):
   global x
   global y
   global index
   global arrayX
   global arrayY
   global count_clicks
   global flag
   #chaine.configure(text = "Clic detecte en X  =  "+str(event.x)+", Y  =  "+str(event.y))
   count_clicks+=1
   if flag==False: #        check if it is entering here to add prises or to recognise colours
   	chaine.configure(text = "couleurs sélectionnées  =  "+str(count_clicks))
   arrayX.append(event.x)
   arrayY.append(event.y)
   index+= 1	
   
def appuie(X,Y,filepath):
   " sauvegarde l'image traitee une fois que le bouton 'Fin' est appuye"
   global rouge
   global vert
   global bleu
   global flag
   im = open(filepath)
   for i in range (0, len(X)):
		  
	   (red,green,blue)  =  im.getpixel((X[i],Y[i]))
	   rouge.append(red)
	   vert.append(green)
	   bleu.append(blue)
	   
	#Donne les couleurs correspondants au pixel de coordonnees (x,y) (coordonnees selectionnees par l'utilisateur)
   img_matrice = selectionCouleurs(rouge,vert,bleu,40,filepath)
   instructions.delete(	1.0,END)
   instructions.insert(END,"-Pousser reglages pour voir tous les prises detectes")
   p  =  fromarray(img_matrice) #Cree une image de la matrice retournee par la fonction 'selectionCouleurs'
   p.save('image_traitee.png')
   creationPrise(p)
   chaine.destroy()
   flag=True # put in true so recognition phase is over
 
def selectionCouleurs(R,V,B,intervalle,filepath):
	im = open(filepath)
	img = np.array(im)       #Matrice de l'image selectionnee
	s1,s2  =  img.shape[:2]  #Dimensions de la matrice de l'image  
	

	#Definition des intervalles de couleur du pixel selectionne 
	
	pixelInRange=False
	
	for i in range(0,s1): #Parcourt les lignes de la matrice
		for j in range(0,s2): #Parcourt les colonnes de la matrice
			pixelInRange=False
			for k in range(0, len(R)):
				seuilR1 = R[k]-intervalle
				seuilR2 = R[k]+intervalle
				seuilV1 = V[k]-intervalle
				seuilV2 = V[k]+intervalle
				seuilB1 = B[k]-intervalle
				seuilB2 = B[k]+intervalle

				if img[i,j][0] in range(seuilR1,seuilR2) and img[i,j][1] in range(seuilV1,seuilV2) and img[i,j][2] in range(seuilB1,seuilB2):
							pixelInRange=True
							img[i,j][0] = R[k]
							img[i,j][1] = V[k]
							img[i,j][2] = B[k]
							break  #On garde la couleur des pixels
											
			if pixelInRange==False:
				img[i,j][0] = 0
				img[i,j][1] = 0
				img[i,j][2] = 0
		   

		# for i in range(0,3):
		# 	for j in range(0,s2):
		# 		img[i,j][0] = R
		# 		img[i,j][1] = V
		# 		img[i,j][2] = B
	

	#new2Window = tkinter.Toplevel(fenetre)
	#tkinter.Label(new2Window, 
    #  text="""Selectionnez le couleur de la voie:""",padx = 20).pack()
	#fenetre.iconify()

	#B_fin= tkinter.Button(new2Window, text  = 'ok', command = plt.imshow(label_im))
	#B_fin.pack()
	return img

def selectionVoie():
	global couleurs
	global rouge
	global bleu
	global vert

	newWindow = tkinter.Toplevel(fenetre)
	tkinter.Label(newWindow, 
      text="""Selectionnez le couleur de la voie:""",padx = 20).pack()
	fenetre.iconify()
	for i in range (0,len(rouge)):

		Rh=str(hex(rouge[i]))
		Gh=str(hex(vert[i]))
		Bh=str(hex(bleu[i]))
		chaine='#'+Rh[2:len(Rh)]+Gh[2:len(Gh)]+Bh[2:len(Bh)]
	   
		couleurs.append((chaine,i))




	for txt, val in couleurs:
	    Radiobutton(newWindow, 
	                text=' ',
	                padx = 20, 
	                variable=v, 
	                bg=txt,
	                value=val).pack(anchor=W)  

	B_fin= tkinter.Button(newWindow, text  = 'ok', command  =  lambda : ShowChoice())
	B_fin.pack()
 
	

def ShowChoice():
	global rouge
	global vert
	global bleu
	print (v.get())
	couleurChoisi=[rouge[v.get()],vert[v.get()],bleu[v.get()]]
	print(couleurChoisi)

	#creationPrise(QUE IMAGEN PASARLE?)


canvas.focus_set()
canvas.bind("<Button-1>", pointeur) #ecrit les coordonnees x et y lorsqu'on clique sur l'image
canvas.pack()
chaine = Label(fenetre)

def boutonCentres():
	B_ajouterPrise=Button(fenetre, text  = 'Ajouter prise', command  =  lambda : ajouterPrise())
	B_ajouterPrise.pack(side = LEFT, padx = 5, pady = 5)
	for i in range(len(prises2)):
		centrex=prises2[i].centre[0]
		centrey=prises2[i].centre[1]
		bouton=Button(fenetre,  command  =  lambda f=fenetre, ii=i, p=prises2[i]: Reglages(f,ii,p))
		bouton.pack(padx = 1, pady = 1)
		bouton.place(x=centrex,y=centrey, width=10, height=10)
		instructions.delete(1.0,END)
		instructions.insert(END,"-Pousser le bouton sur chaque prise pour le categoriser ou le supprimer\n-Faire click sur le prise qui n'a pas ete detectete\n-Pousser ajouter")

def imprime():	
	for i in range(len(prises2)):
		print(prises2[i].ordre)
		#print(priseUpdated.type_prise)


def ajouterPrise():
	global arrayX
	global arrayY
	#Création de la nouvelle prise
	nouvellePrise=Prise(len(prises2))
	#On considere comme centre de de la prise les coordonées x,y du clic
	centrex=arrayX[len(arrayX)-1]
	centrey=arrayY[len(arrayY)-1]
	nouvellePrise.centre=(centrex,centrey)
	#Récuperation du couleur de la prise
	im = open(filepath)
	(red,green,blue)  =  im.getpixel((arrayX[len(arrayX)-1],arrayY[len(arrayY)-1]))
	nouvellePrise.couleur=[red,green,blue] 
	prises2.append(nouvellePrise)  
	i=len(prises2)-1
	bouton=Button(fenetre,  command  =  lambda f=fenetre, ii=i, p=prises2[i]: Reglages(f,ii,p))
	bouton.pack(padx = 1, pady = 1)
	bouton.place(x=centrex,y=centrey, width=10, height=10)

#Affichage du bouton

B_OK= Button(fenetre, text  = 'OK', command  =  lambda : appuie(arrayX,arrayY,filepath))
B_OK.pack(side = LEFT, padx = 5, pady = 5)
B_SelectionVoie=Button(fenetre, text  = 'Selection de la voie', command  =  lambda : selectionVoie())
B_SelectionVoie.pack(side = LEFT, padx = 5, pady = 5)
B_reglages= Button(fenetre, text= 'Réglages',  command  =  lambda : boutonCentres())
B_reglages.pack(side = LEFT, padx = 5, pady = 5)
B_show= Button(fenetre, text= 'Impresion',  command  =  lambda : imprime())
B_show.pack(side = LEFT, padx = 5, pady = 5)
instructions=Text(fenetre,height=10,width=30,wrap=WORD)
instructions.insert(END,"-Faire un click sur une prise de chaque coulour\n-Pousser le bouton OK\n-Attendre")
instructions.place(x=photo.width()+5,rely=0)
#Execution de la fenetre generale
chaine.pack(side=LEFT)

fenetre.mainloop()

