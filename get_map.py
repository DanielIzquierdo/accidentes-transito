

def getFrecuencies(filename, data):
	f = open(filename, 'r')
	f.readline()
	for line in f:
		fields = line.strip().split(',')
		codigo = fields[1]
		if str(int(codigo)) in data:
			dicData = data[str(int(codigo))]		
			if 'frequency' in dicData:
				dicData['frequency'] += 1
			else:
				dicData['frequency'] = 1
	f.close()

#def getHourFrecuencies(filename, data):
#	d = {}
#	f = open(filename, 'r')
#	f.readline()
#	for line in f:
#		fields = line.strip().split(',')
#		codigo = fields[1]
#		hour = int(fields[4])
#		lat = data[codigo]
#	f.close()

#def writeFrecuencies(filename, data):
#	f = open(filename, 'w')
#	f.write('frequency,lat,lon\n')	
#	for codigo in data:
#		dicData = data[codigo]
#		lat = dicData['lat']
#		lon = dicData['lon']
#		if 'frequency' in dicData:
#			frequency = dicData['frequency']
#			f.write(str(frequency) + ',' + lat + ',' + lon + '\n')
#	f.close()

def writeHourFrecuencies(read_filename, write_filename, data):
	c = 0
	f1 = open(read_filename, 'r')
	f2 = open(write_filename, 'w')
	f2.write('hour,lat,lon\n')
	for line in f1:
		fields = line.strip().split(',')
		codigo = int(fields[1])
		hour = int(fields[4])
		if codigo in data:
			c+=1
			lat = data[codigo]['lat']
			lon = data[codigo]['lon']
			f2.write(str(hour) + ',' + lat + ',' + lon + '\n')
	f1.close()
	f2.close()
	print c

data = {}
f1 = open('mapped_guayasCities.csv', 'r')
f1.readline()
for line in f1:
	fields = line.strip().split(',')
	codigo = int(fields[0])
	lat = fields[2]
	lon = fields[3]
	data[codigo] = {'lat' : lat, 'lon' : lon}
f1.close()

#getFrecuencies('accidentes_guayas.csv', data)
#getHourFrecuencies('accidentes_guayas.csv', data)

print data
#writeFrecuencies('guayas_frequencyMap.csv', data)
writeHourFrecuencies('accidentes_guayas.csv', 'guayas_HourFrequency_Map.csv', data)


