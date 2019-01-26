import sys
import spotipy
import spotipy.util as util
import urllib
import time

USERNAME = '1229546819?si=MER8uTCxSGueQIYzAewbbA' #your spotify username
CLIENT_ID = 'd392a6588f7349ccba315cf0b665f228'#set at your developer account
CLIENT_SECRET = '23c5b29752524b53bd62781a15e002e9' #set at your developer account
REDIRECT_URI = 'http://localhost/' #set at your developer account, usually "http://localhost:8000"
SCOPE = 'user-read-currently-playing' # or else
# User Id: 1229546819?si=MER8uTCxSGueQIYzAewbbA

def updateInfoDumb(albumArt, songName): 
    # recursively call update info when time of song runs out... this is cool but not proper since if the user changes a song
    # it will not account for that.. i could simply call for a check on the song every X seconds... just would prefer less API calls.
    current_track = sp.current_user_playing_track()
    albumArt = current_track['item']['album']['images'][0]['url']
    songName = current_track['item']['name']
    artist = current_track['item']['artists'][0]['name'] # only grab first artist for this project ..
    
    secondName = songName
    while secondName is songName:
        time.sleep(5)
        second_track = sp.current_user_playing_track()
        secondName = second_track['item']['name']
        albumArt = second_track['item']['album']['images'][0]['url']
        artist = second_track['item']['artists'][0]['name']
    
    urllib.urlretrieve(albumArt, "album.jpg")

    print str(secondName) + ' by ' + str(artist)
    updateInfoDumb(albumArt, secondName)

def updateInfo(current_track): 
    # recursively call update info when time of song runs out... this is cool but not proper since if the user changes a song
    # it will not account for that.. i could simply call for a check on the song every X seconds... just would prefer less API calls.

    progress = current_track['progress_ms']
    duration = duration = current_track['item']['duration_ms']
    albumArt = current_track['item']['album']['images'][0]['url']
    songName = current_track['item']['name']
    artist = current_track['item']['artists'][0]['name'] # only grab first artist for this project ..
    urllib.urlretrieve(albumArt, "album.jpg")

    print str(songName) + ' by ' + str(artist)
    time.sleep((duration - progress) / 1000.0)
    updateInfo(sp.current_user_playing_track())

token = util.prompt_for_user_token(USERNAME,SCOPE,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)
    current_track = sp.current_user_playing_track()
    albumArt = ''
    songName = ''
    if current_track is not None:
        if current_track['is_playing'] is not None:
            albumArt = current_track['item']['album']['images'][0]['url']
            songName = current_track['item']['name']
            artist = current_track['item']['artists'][0]['name'] # only grab first artist for this project ..

            duration = current_track['item']['duration_ms']
            progress = current_track['progress_ms']
            timestamp = current_track['timestamp']

            print str(songName) + ' by ' + str(artist)

            urllib.urlretrieve(albumArt, "album.jpg")

        else:
            print 'No song is playing.'
    else:
        print 'Spotify is not running.'

    #updateInfo(current_track)
    updateInfoDumb(albumArt, songName)
else:
    print("Can't get token for", USERNAME)


