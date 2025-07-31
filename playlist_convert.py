import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from pprint import pprint
import os
from dotenv import load_dotenv, dotenv_values 
import json 
load_dotenv() 


class SpotifyClient:

	def __init__(self):
		client_id = os.getenv('CLIENT_ID')
		client_secret = os.getenv('CLIENT_SECRET')
		self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
	                                               client_secret,
	                                               redirect_uri="http://127.0.0.1",
	                                               scope="user-library-read playlist-modify-public"))

	# playlistDict = {
	# 	"oh yah": ['5cKRkbgXP1fHrajweNstp6', 10],
	# 	"sunshine biking" : ['3YaWFXSb1oV2IxGsm0nvl4', 18],
	# 	"family party": ['13dDta58USmjcLfZ0jVmOc', 106],
	# 	"Canciones": ['6qpCoWWbGQyGgOntQy9l3p', 15],
		
	# }




	# Get URI of my username
	#user_id = sp.me()["id"]


	#print(user_id)

	#playlist = sp.current_user_playlists(limit=50, offset=0)
	#print(json.dumps(playlist, indent=2))


	#print(json.dumps(playlist, indent=2))
	#playlistNames = playlist["items"]
	#pprint(playlistNames)

	# for playlist in playlistNames:
	# 	playstid = playlist["id"]
	# 	playlistName = playlist["name"]
	# 	count = playlist["tracks"]['total']
	# 	#print(count)
	# 	playlistDict[playlistName] = [playstid, count]

	def playlist_retriever(self):
		self.playlistDict = {}
		playlist = self.sp.current_user_playlists(limit=50, offset=0)
		playlistNames = playlist["items"]
		#print(playlistNames)
		for playlist in playlistNames:
			playstid = playlist["id"]
			playlistName = playlist["name"]
			count = playlist["tracks"]['total']
			#print(count)
			self.playlistDict[playlistName] = [playstid, count]
			#print(self.playlistDict)

			#print(f"playstid {playstid}, playlistName {playlistName}, count: {count}")

			
		#print(self.playlistDict)

	def gets_songs_from_playlist(self):

		print("from get songs")
		#print(self.playlistDict)

		# playlistDict = {
		# 	"oh yah": ['5cKRkbgXP1fHrajweNstp6', 10],
		# 	"sunshine biking" : ['3YaWFXSb1oV2IxGsm0nvl4', 18],
		# 	"family party": ['13dDta58USmjcLfZ0jVmOc', 106],
		# 	"Canciones": ['6qpCoWWbGQyGgOntQy9l3p', 15]}


		for name, songid in self.playlistDict.items():
			
			playlistID = songid[0]
			songCount = songid[1]
			#print(f"PlayList Name: {name}, playlistID: {playlistID}, Song Count: {songCount}")

			if songCount <= 100:
				#print(f"PlayList Name: {name}, playlistID: {playlistID}, Song Count: {songCount}")
				tracks = self.sp.playlist_items('5cKRkbgXP1fHrajweNstp6', limit = 100)
				songs = tracks["items"]
				#songs = tracks["items"]
				for song in songs:
					songID = song['track']['id']
					songName = song['track']['name']
					print(songName, songid)
				#songID = songs["track"]["id"]
				#print(f"Song: {songName} | ID: {songID}")
				#pprint(songs)

			else:
				print(f"Playist {name} is too long to check")


	# 'oh yah': '5cKRkbgXP1fHrajweNstp6'
	# songsList = sp.playlist_items('5cKRkbgXP1fHrajweNstp6', limit=2)
	# songs = songsList["items"]
	# pprint(songs)


	# for song in songs:
	# 	songName = song['track']['name']
	# 	songid = song['track']['id']
	# 	print(songName)


if __name__ == "__main__":
	client = SpotifyClient()
	client.playlist_retriever()
	client.gets_songs_from_playlist()