


cantones={901:'GUAYAQUIL',902:'JUJAN',903:'BALAO',904:'BALZAR',905:'COLIMES',906:'DAULE',907:'DURAN',\
              908:'EL EMPALME',909:'EL TRIUNFO',910:'MILAGRO',911:'NARANJAL',912:'NARANJITO',\
              913:'PALESTINA',914:'PEDRO CARBO',916:'SAMBORONDON',918:'SANTA LUCIA',919:'URBINA JADO',\
              920:'YAGUACHI',921:'PLAYAS',922:'SIMON BOLIVAR',923:'MARCELINO MARIDUENA',\
              924:'LOMAS DE SARGENTILLO',925:'NOBOL',927:'ANTONIO ELIZALDE',928:'ISIDRO AYORA'}

nombres_ciudades = cantones.values()
codigos = cantones.keys()

file1 = open('coordenadas_ecuador1.csv', 'r')
file2 = open('mapped_guayasCities.csv', 'w')
file2.write('codigo,ciudad,latitud,longitud\n')

ciudadesEscritas = set()

file1.readline()
for line in file1:
	line = line.strip()
	line = line.replace('\"', '')
	line = line.upper()
	print line
	campos = line.split(',')
	if campos[1] == 'GUAYAS':
		ciudad = campos[0]
		if ciudad in nombres_ciudades and ciudad not in ciudadesEscritas:
			pos = nombres_ciudades.index(ciudad)
			codigo = codigos[pos]
			lat = campos[2]
			lon = campos[3]
			file2.write(str(codigo) + ',' + ciudad + ',' + lat + ',' + lon + '\n')
			ciudadesEscritas.add(ciudad)

file2.write('927,ANTONIO ELIZALDE,-2.2,-79.17\n')
file2.write('923,MARCELINO MARIDUENA,-2.2,-79.42\n')
file2.write('908,EL EMPALME,-1.046111,-79.633611\n')
file2.write('902,JUJAN,-1.916667,-79.516667\n')
file2.write('902,URBINA JADO,-1.829444,\n')

ciudadesEscritas.add('ANTONIO ELIZALDE')
ciudadesEscritas.add('MARCELINO MARIDUENA')
ciudadesEscritas.add('EL EMPALME')
ciudadesEscritas.add('JUJAN')
ciudadesEscritas.add('URBINA JADO')


print set(nombres_ciudades) - ciudadesEscritas

file1.close()
file2.close()