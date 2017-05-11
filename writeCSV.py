import csv
from interface import prises2
with open('prises.csv', 'w') as csvfile:
	fieldnames = ['Prise_Id', 'type_prise','Surface','x','y', 'difficulte','apprehension','proximite','ordre','prise_Depart','prise_Fin']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for i in range(len(prises2)):
		writer.writerow({'Prise_Id': prises2[i].priseId, 'type_prise':prises2[i].type_prise, 'Surface': prises2[i].surface, 'x' : prises2[i].centre[0], 'y' : prises2[i].centre[1],'difficulte':prises2[i].difficulte,'apprehension':prises2[i].apprehension,'proximite':prises2[i].proximite,'ordre':prises2[i].ordre,'prise_Depart':prises2[i].prise_Depart,'prise_Fin':prises2[i].prise_Fin})
