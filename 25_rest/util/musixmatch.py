#Kaitlin Wan
#SoftDev1 pd 6
#K25: Getting More REST
#2018-11-15

import urllib
from urllib.parse import urlparse
import urllib.request
import json

apikey = '559e0ebc8923216e02ede6053c35a18f'
apiurl = 'http://api.musixmatch.com/ws/1.1/'

def find_id(search_term):
    querystring = apiurl + "track.search?q=" + urllib.parse.quote(search_term) + "&apikey=" + apikey
    request = urllib.request.Request(querystring)
    response = urllib.request.urlopen(request)
    raw = response.read()
    json_obj = json.loads(raw)
    body = json_obj["message"]["body"]["track_list"]
    num_hits = len(body)
    if num_hits==0:
        return(("No results for: " + search_term))
    for result in body:
        if result["track"]["has_lyrics"] == 1:
            return result["track"]["track_id"]


def song_lyric(song_name,artist_name):
            querystring = apiurl + "matcher.lyrics.get?q_track=" + urllib.parse.quote(song_name) + "&q_artist=" + urllib.parse.quote(artist_name) +"&apikey=" + apikey + "&format=json&f_has_lyrics=1"
            request = urllib.request.Request(querystring)
            response = urllib.request.urlopen(request)
            raw = response.read()
            json_obj = json.loads(raw)
            body = json_obj["message"]["body"]["lyrics"]["lyrics_body"]
            #print(tracking_url)
            return (body + "\n\n")

'''
name = input("What is the artist's name: ")
type(name)
artist = name
title = input("What is the song title: ")
type(title)
song = title
track_id = (find_id(song + " " + artist))
print (track_id)
print (song_lyric(song,artist))

'''
