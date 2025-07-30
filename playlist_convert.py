import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from pprint import pprint
import os
from dotenv import load_dotenv, dotenv_values 
import json 
load_dotenv() 


def spotify():
	playlistDict = {
		
	}

	client_id = os.getenv('CLIENT_ID')
	client_secret = os.getenv('CLIENT_SECRET')


	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
	                                               client_secret,
	                                               redirect_uri="http://127.0.0.1",
	                                               scope="user-library-read playlist-modify-public"))

	# Get URI of my username
	user_id = sp.me()["id"]


	#print(user_id)

	playlist = sp.current_user_playlists(limit=50, offset=0)
	#print(json.dumps(playlist, indent=2))


	#print(json.dumps(playlist, indent=2))
	playlistNames = playlist["items"]
	#pprint(playlistNames)

	for playlist in playlistNames:
		playstid = playlist["id"]
		playlistName = playlist["name"]
		count = playlist["tracks"]['total']
		#print(count)
		playlistDict[playlistName] = [playstid, count]


	for name, songid in playlistDict.items():
		print(f"{name}: {songid}")

	# 'oh yah': '5cKRkbgXP1fHrajweNstp6'
	# songsList = sp.playlist_items('5cKRkbgXP1fHrajweNstp6', limit=2)
	# songs = songsList["items"]
	# pprint(songs)


	# for song in songs:
	# 	songName = song['track']['name']
	# 	songid = song['track']['id']
	# 	print(songName)


if __name__ == "__main__":
	spotify()