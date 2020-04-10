from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy
import spotipy.util as util
import pprint

track_id_list = []

def search_file():
  with open('grateful_dead_garcia_hunter.txt') as o:
    search_tracks = o.readlines()
    for search_track in search_tracks:
      find_track(sp, search_track.split('\n')[0] + " Grateful Dead")

def find_track(sp, search_str):
  print(search_str)
  result = sp.search(search_str)
  for track in result['tracks']['items']:
    if track['album']['artists'][0]['name'] == "Grateful Dead" \
    or track['album']['artists'][0]['name'] == "Jerry Garcia Band" \
    or track['album']['artists'][0]['name'] == "Jerry Garcia":
      track_id_list.append(track['id'])
      print(track['name'])
      print(track['album']['name'])
      print(track['album']['artists'][0]['name'])
      print(track['id'])
      print("=================================")

def add_to_playlist(sp):
  i = 0
  for i in range(0,len(track_id_list),100):
    sp.trace = False
    add_list = track_id_list[i:i+100]
    print(len(add_list))
    results = sp.user_playlist_add_tracks(username, paylist_id, add_list)
    print(results)
    i += 100

if __name__ == '__main__':
  if len(sys.argv) > 1:
    username = sys.argv[1]
    paylist_id = '2eMWesnRkI2mqBJkTw7Riv'
  else:
    print("Whoops, need your username!")
    print("usage: python user_playlists.py [username]")
    sys.exit()

  scope = 'playlist-modify-public'
  token = util.prompt_for_user_token(username, scope)

  if token:
    sp = spotipy.Spotify(auth=token)
    track_id_list = []
#    find_track(sp, 'Ship of Fools Grateful Dead')
    search_file()
    print(len(track_id_list))
    add_to_playlist(sp)
  else:
    print("Can't get token for", username)
