import pprint
import sys
import re
import spotipy
import spotipy.util as util

username = "emptemp"
playlist_id = "3O9lPskC6wGjUm5ut8YD8O"

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, "4700275f9f084f0b98ad9f3530fe9a3d", "c76e2ba36d6b41f6b1b6dcf73ec63378", "http://stannio.li")

if token:
	spotiness = open("spotiness.txt","w")
	spotiness.write("1\t2\t")
	spotiness.write("liveness"+"\t")
	spotiness.write("tempo"+"\t")
	spotiness.write("spechiness"+"\t")
	spotiness.write("acousticness"+"\t")
	spotiness.write("3\t")
	spotiness.write("instrumentalness"+"\t")
	spotiness.write("time_signature"+"\t")
	spotiness.write("danceability"+"\t")
	spotiness.write("key"+"\t")
	spotiness.write("time_signature"+"\t")
	spotiness.write("durcation_ms"+"\t")
	spotiness.write("loudness"+"\t")
	spotiness.write("valence"+"\t")
	spotiness.write("\n")
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	with open("track_id.txt") as f:
		for line in f:
			track_id = re.findall("track\/(.*)", line)
			results = sp.audio_features(track_id)
			for stuff in results:
				print track_id,
				for k in stuff.keys():
					write = str(stuff[k]) + "\t"
					spotiness.write(write)
					#spotiness.write("\n")
				print "\n"
				spotiness.write("\n")
else:
	print "Can't get token for", username
	
	
				#str_energy = str(stuff['energy'])
				#str_liveness = str(stuff['liveness'])
				#str_tempo = str(stuff['tempo'])
				#str_spechiness = str(stuff['spechiness'])
				#str_acousticness = str(stuff['acousticness'])
				#str_instrumentalness = str(stuff['instrumentalness'])
				#str_time_signature = str(stuff['time_signature'])
				#str_danceability = str(stuff['danceability'])
				#str_key =str(stuff['key'])
				#str_durcation_ms = str(stuff['durcation_ms'])
				#str_loudness = str(stuff['loudness'])
				#str_valence = str(stuff['valence'])
				