# OBSSpotifyAlbum
Display realtime album art on OBS using Spotify's API
Implemented using Spotipy python library.

## Requirements

To run this python script, Python3, Spotipy and a Spotify Account are required. 
To install the Spotipy library, run this command: 

`pip3 install git+https://github.com/plamere/spotipy.git --upgrade`


## Instructions

To use this python script you must first know your Spotify User ID. To find this ID, Open Spotify and visit your user page. Click on the settings dots and under share, Copy your Spotify URI. Keep just the identification number and keep reference to that value.

To run, first have Spotify playing. Once Spotify is running, run the script as follows:

`python3 spotifyAlbum.py <user ID>`
  
  Once it runs, an internet browser will prompt for your authorization of your user account. After accepting, copy the web address to the command line and press enter. The program will now begin running. Once this is authorized for the inital time, it should not require you to continuously authorize yourself.
 
  The program will store an album.png and a track.txt file in the repository.
To display these values in OBS, simply create a new image with a reference to the album.png file, as well as a new text module with reference to the track.txt file.
These files will automatically update with the song change, and will display on OBS.
