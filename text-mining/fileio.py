def read_file(path):
	file = open(path, "r")
	content=""
	while True:
		line = file.readline()
		if(not line):
			break

		content+=line

	file.close()
	return content

def write_dict_file(path, dict):
	file = open(path,"w")
	for k, v in dict.items():
		text = str(k)+ " : "+str(v)+'\n'
		file.write(text)
	file.close()

def write_list_file(path, listdata):
	file = open(path,"w")
	
	for listitem in listdata:
		for k, v in listitem.items():
			text = str(k)+ "("+str(v)+")\n"
			file.write(text)
		file.write("==============")
	file.close()


