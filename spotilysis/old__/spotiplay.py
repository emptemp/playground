import sys
import string
import spotipy
import spotipy.util as util

username = "emptemp"
scope = 'playlist-modify-public'
#spotify = spotipy.Spotify()
token = util.prompt_for_user_token(username, scope, "4700275f9f084f0b98ad9f3530fe9a3d", "c76e2ba36d6b41f6b1b6dcf73ec63378", "http://stannio.li")

if token:
	sp = spotipy.Spotify(auth=token)

else:
	print "Can't get token for", username
	

def spotisearch(content):
	alb_ids = open('alb_ids.txt','w')
	for band in content:
		album1 = band.replace( "\t", " " )
		album = album1.replace("\n", "")
		results = sp.search(q='album:' + album, type='album')
		albums = results['albums']['items']
		if albums:
			#print " - " + albums[0]['name'].replace(u"\u2018", "'").replace(u"\u2019", "'"),
			album_name = albums[0]['name']
			#print " ",
			#print albums[0]['artists'][0]['name']
			artist_name = albums[0]['artists'][0]['name']
			album_id = albums[0]['uri'].replace("spotify:album:","")
			print album_id
			alb_ids.write("{}\t{}\t{}\t".format(artist_name, album_name, album_id))
			alb_ids.write("\n")		
	return album_ids


scope = 'user-library-read'

def get_details():
	spotilysis = open('spotilysis.txt','w')
	with open('alb_ids.txt') as al:
		lines = al.readlines()
		for albums in lines:
			album = albums.split("\t")
			#print album
			artist_name = album[0]
			album_name = album[1]
			album_id = album[2]
			tracks = sp.album_tracks(album[2], limit=50, offset=0)	
			for track in tracks['items']:
				track_name = track['name']
				track_id = track['uri'].replace("spotify:track:","")
				print track_name,
				print track_id
				energy = sp.audio_features(  str(track_id)  )[0]['energy']
				liveness = sp.audio_features(  str(track_id)  )[0]['liveness']
				tempo = sp.audio_features(  str(track_id)  )[0]['tempo']
				speechiness = sp.audio_features(  str(track_id)  )[0]['speechiness']
				acousticness = sp.audio_features(  str(track_id)  )[0]['acousticness']
				instrumentalness = sp.audio_features(  str(track_id)  )[0]['instrumentalness']
				time_signature = sp.audio_features(  str(track_id)  )[0]['time_signature']
				danceability = sp.audio_features(  str(track_id)  )[0]['danceability']
				key = sp.audio_features(  str(track_id)  )[0]['key']
				duration_ms = sp.audio_features(  str(track_id)  )[0]['duration_ms']
				loudness = sp.audio_features(  str(track_id)  )[0]['loudness']
				valence = sp.audio_features(  str(track_id)  )[0]['valence']

				spotilysis.write("{}\t".format(artist_name))
				spotilysis.write("{}\t".format(album_name))
				spotilysis.write("{}\t".format(track_name))
				spotilysis.write("{}\t".format(energy))
				spotilysis.write("{}\t".format(liveness))
				spotilysis.write("{}\t".format(tempo))
				spotilysis.write("{}\t".format(speechiness))
				spotilysis.write("{}\t".format(acousticness))
				spotilysis.write("{}\t".format(instrumentalness))
				spotilysis.write("{}\t".format(time_signature))
				spotilysis.write("{}\t".format(danceability))
				spotilysis.write("{}\t".format(key))
				spotilysis.write("{}\t".format(duration_ms))
				spotilysis.write("{}\t".format(loudness))
				spotilysis.write("{}\t".format(valence))
				spotilysis.write("\n")
				#track_item = tracks.get('items')
		
#############################################################################################


	#print(content)
	#spotify:track:6dRx7OUXfvosnXG3g9lWGi

print "1 fuer spotisearch, sonst get_details\n"
answer = raw_input()
if answer is "1":
	with open('cleanwanted.txt') as f:
		content = f.readlines()
	spotisearch(content)
	print "woot"
else:
	get_details()	


