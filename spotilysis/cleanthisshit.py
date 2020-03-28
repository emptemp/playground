
content = []
spotilysis = "spotilysis_#.txt"
for i in range(1,8):
	spotilysis.replace("#", str(i))
	with open('spotilysis_1.txt') as f:
		content.append(f.readlines())

cleanshit = open('cleanshit.txt', 'w') 

cleanshit.write("{};".format("artist_name"))
cleanshit.write("{};".format("album_name"))
cleanshit.write("{};".format("track_name"))
cleanshit.write("{};".format("energy"))
cleanshit.write("{};".format("liveness"))
cleanshit.write("{};".format("tempo"))
cleanshit.write("{};".format("speechiness"))
cleanshit.write("{};".format("acousticness"))
cleanshit.write("{};".format("instrumentalness"))
cleanshit.write("{};".format("time_signature"))
cleanshit.write("{};".format("danceability"))
cleanshit.write("{};".format("key"))
cleanshit.write("{};".format("duration_ms"))
cleanshit.write("{};".format("loudness"))
cleanshit.write("{}\n".format("valence"))

for list in content:
	for items in list:
		item = items.split('\t')
		cleanshit.write("{};".format(item[0]))
		cleanshit.write("{};".format(item[1]))
		cleanshit.write("{};".format(item[2]))
		cleanshit.write("{};".format(item[3].replace(".",",")))
		cleanshit.write("{};".format(item[4].replace(".",",")))
		cleanshit.write("{};".format(item[5].replace(".",",")))
		cleanshit.write("{};".format(item[6].replace(".",",")))
		cleanshit.write("{};".format(item[7].replace(".",",")))
		cleanshit.write("{};".format(item[8].replace(".",",")))
		cleanshit.write("{};".format(item[9].replace(".",",")))
		cleanshit.write("{};".format(item[10].replace(".",",")))
		cleanshit.write("{};".format(item[11].replace(".",",")))
		cleanshit.write("{};".format(item[12].replace(".",",")))
		cleanshit.write("{};".format(item[13].replace(".",",")))
		cleanshit.write("{}\n".format(item[14].replace(".",",")))
		#cleanshit.write("\n")
cleanshit.close()