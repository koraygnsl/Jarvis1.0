import spotipy
import json
import webbrowser
from spotipy.oauth2 import SpotifyClientCredentials

username = 'spotify-name'
clientID = ''
clientSecret = ''
redirectURI = 'http://google.com/'

oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

print(json.dumps(user,sort_keys=True, indent=4))

def findTrack(trackname):
    searchQuery = trackname
    searchResults = spotifyObject.search(searchQuery, 1, 0, "track")
    tracks_dict = searchResults['tracks']
    tracks_items = tracks_dict['items']
    song = tracks_items[0]['external_urls']['spotify']
    webbrowser.open(song)
