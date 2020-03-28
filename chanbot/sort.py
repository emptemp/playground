import string

save = raw_input ("save= ")
this = raw_input ("enter? ")

nfile = open(save+this+"-links.html","w")


with open("links.txt") as file:
	for line in file:
		if this in line:
			line = string.replace(line,"//m","/m")
			nfile.write("<a href=\""+line+"\">"+line+"</a><br>")
			print line
nfile.close()

