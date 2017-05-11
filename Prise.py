class Prise:

	priseId=0
	couleur=[]
	surface=0
	centre=(0,0)
	type_prise=0
	difficulte=0
	apprehension=0
	proximite=0
	ordre=0
	prise_Depart=False
	prise_Fin=False
	profondeur=[]


	def __init__(self, tag):
		self.priseId=tag

	def set_TypePrise(self,option):
	 	self.type_prise=option		

	def set_Difficulte(self,option):
		self.difficulte=option
	
	def set_Apprehension(self,option):
	 	self.apprehension=option

	def set_Proximite(self,option):
	 	self.proximite=option

	def set_Ordre(self,option):
		 	self.ordre=option

	def isPriseDepart(self,option):
	 	self.prise_Depart=option

	def isPriseFin(self,option):
	 	self.prise_Fin=option

	def createBowensFile(self):
 		print("Una vez que se completan los campos crea un archivo pa la app tablette")

# priseprueba=Prise(0)
# priseprueba.set_TypePrise(4)
# print(priseprueba.type_prise)