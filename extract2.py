import pandas as pd
import numpy as np
from tabulate import tabulate as tb

cantones={901:'GUAYAQUIL',902:'JUJAN',903:'BALAO',904:'BALZAR',905:'COLIMES',906:'DAULE',907:'DURAN',\
              908:'EL EMPALME',909:'EL TRIUNFO',910:'MILAGRO',911:'NARANJAL',912:'NARANJITO',\
              913:'PALESTINA',914:'PEDRO CARBO',916:'SAMBORONDON',918:'SANTA LUCIA',919:'URBINA JADO',\
              920:'YAGUACHI',921:'PLAYAS',922:'SIMON BOLIVAR',923:'MARCELINO MARIDUENA',\
              924:'LOMAS DE SARGENTILLO',925:'NOBOL',927:'ANTONIO ELIZALDE',928:'ISIDRO AYORA'}
meses={1:'ENERO',2:'FEBRERO',3:'MARZO',4:'ABRIL',5:'MAYO',6:'JUNIO',7:'JULIO',8:'AGOSTO',9:'SEPTIEMBRE',
       10:'OCTUBRE',11:'NOVIEMBRE',12:'DICIEMBRE'}
dias={1:'LUNES',2:'MARTES',3:'MIERCOLES',4:'JUEVES',5:'VIERNES',6:'SABADO',7:'DOMINGO'}
horas={0:'00:00 A 00:59',1:'01:00 A 01:59',2:'02:00 A 02:59',3:'03:00 A 03:59',4:'04:00 A 04:59',\
      5:'05:00 A 05:59',6:'06:00 A 06:59',7:'07:00 A 07:59',8:'08:00 A 08:59',9:'09:00 A 09:59',\
      10:'10:00 A 10:59',11:'11:00 A 11:59',12:'12:00 A 12:59',13:'13:00 A 13:59',14:'14:00 A 14:59',\
      15:'15:00 A 15:59',16:'16:00 A 16:59',17:'17:00 A 17:59',18:'18:00 A 18:59',19:'19:00 A 19:59',\
      20:'20:00 A 20:59',21:'21:00 A 21:59',22:'22:00 A 22:59',23:'23:00 A 23:59'}
clases={1:'ATROPELLOS',2:'CAÍDA PASAJEROS',3:'CHOQUES',4:'ESTRELLAMIENTOS',5:'ROZAMIENTOS',6:'VOLCAMIENTOS',\
       7:'PERDIDA DE PISTA',8:'OTROS'}
causas={1:'EMBRIAGUEZ O DROGA',2:'MAL REBASAMIENTO INVADIR CARRIL',3:'EXCESO VELOCIDAD',4:'IMPERICIA E IMPRUDENCIA DEL CONDUCTOR',\
       5:'IMPRUDENCIA  DEL PEATÓN',6:'DAÑOS MECÁNICOS',7:'NO RESPETA LAS SEÑALES DE TRÁNSITO',\
       8:'FACTORES CLIMÁTICOS',9:'MAL ESTADO DE LA VÍA',10:'OTRAS CAUSAS'}
zonas={2:'RURAL',1:'URBANA'}

data=[]
f=open('Datanew.csv','r')
for line in f:
    line=line.strip()
    provincia,canton,mes,dia,hora,clase,causa,zona,nh,nf,tv=line.split(',')
    l=[cantones[int(canton[1::])],zonas[int(zona)],clases[int(clase)],causas[int(causa)],meses[int(mes)],\
       dias[int(dia)],horas[int(hora)],nh,nf,tv]
    data.append(l)

columnas=['Canton','Zona','Clase','Causa','Mes','Dia','Hora','Heridos','Fallecidos','Total']

d1=pd.DataFrame(data,columns=columnas)
#print(tb(d1,tablefmt='grid',stralign='center',showindex=False,headers=columnas))
#d2=d1.groupby(['Clase'])
f2=open('Data.txt','w')
f2.write(tb(d1,tablefmt='grid',stralign='center',showindex=False,headers=columnas))
f2.close()