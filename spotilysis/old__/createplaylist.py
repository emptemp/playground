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
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	with open("track_id.txt") as f:
		for line in f:
			track_id = re.findall("track\/(.*)", line)
			results = sp.user_playlist_add_tracks(username, playlist_id, track_id)
			print results
else:
	print "Can't get token for", username