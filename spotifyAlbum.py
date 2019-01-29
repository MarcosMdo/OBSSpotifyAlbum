import sys
import os
import spotipy
import spotipy.util as util
import urllib.request
import time

CLIENT_ID = 'd392a6588f7349ccba315cf0b665f228'
CLIENT_SECRET = '23c5b29752524b53bd62781a15e002e9' 
REDIRECT_URI = 'http://localhost/' # set in dev acc.
SCOPE = 'user-read-currently-playing' 

def updateInfoSleepy(albumArt, songName, sp): 
    # Recursively call update info when difference found between current user track
    # Noted as "Sleepy" due to sleeping before making calls
    # Inefficient and calls API too often. Set to 10 second sleep times.

    current_track = sp.current_user_playing_track()
    if current_track is not None:
        albumArt = current_track['item']['album']['images'][0]['url']
        songName = current_track['item']['name']
        artist = current_track['item']['artists'][0]['name'] # only grab first artist for this project ..
        secondName = songName

        while secondName is songName:
            time.sleep(20)
            second_track = sp.current_user_playing_track()
            secondName = second_track['item']['name']

            if second_track is not None:
                albumArt = second_track['item']['album']['images'][0]['url']
                artist = second_track['item']['artists'][0]['name']
                songName = second_track['item']['name']
                
                print(str(songName) + ' by ' + str(artist))

                urllib.request.urlretrieve(albumArt, "album.jpg")
                track = open("track.txt", "w+")
                track.write(str(songName) + ' - ' + str(artist))
                track.close()
            else:
                break

        updateInfoSleepy(albumArt, secondName, sp)

def updateInfo(current_track): 
    # Recursively call update info when time of song runs out... this is cool but not proper since if the user changes a song
    # It will not account for that

    progress = current_track['progress_ms']
    duration = duration = current_track['item']['duration_ms']
    albumArt = current_track['item']['album']['images'][0]['url']
    songName = current_track['item']['name']
    artist = current_track['item']['artists'][0]['name'] # only grab first artist for this project ..
    #urllib.urlretrieve(albumArt, "album.jpg")

    print(str(songName) + ' by ' + str(artist))
    time.sleep((duration - progress) / 1000.0)
    updateInfo(sp.current_user_playing_track())

def main():
    username = sys.argv[1] # Username currently passed in as command line arg.. will have to come up with better way of retrieving
    token = util.prompt_for_user_token(username,SCOPE,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)

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

                print(str(songName) + ' by ' + str(artist))

                urllib.request.urlretrieve(albumArt, "album.jpg")

                track = open("track.txt", "w+")
                track.write(str(songName) + ' - ' + str(artist))
                track.close()

            else:
                print('No song is playing.')
        else:
            print('Spotify is not running.')

        # updateInfo(current_track)
        updateInfoSleepy(albumArt, songName, sp) # Recursive function call starts here..
    else:
        print("Can't get token for", username)


if __name__== "__main__":
  main()