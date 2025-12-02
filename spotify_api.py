from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from urllib.parse import quote

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

""" Spotify API Authentication"""
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
        }
    data = {"grant_type": "client_credentials"}

    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

"""Search for album using album name and artist name"""
def search_for_album(token, album_name, artist_name = None):
    url = f'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)

    if artist_name:
        query = f'album:"{album_name}" artist:"{artist_name}"'
    else:
        query = f'album:"{album_name}"'

    # URL-encode the entire query
    encoded_query = quote(query)

    # Final search URL
    query_url = f"{url}?q={encoded_query}&type=album&limit=5"

    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["albums"]["items"]

    if len(json_result) == 0:
        print("No album found")
        return None
    return json_result[0]

'''Get tracks from album using album ID'''
def get_songs_by_album(token, album_id):
    url = f'https://api.spotify.com/v1/albums/{album_id}/tracks'
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["items"]
    return json_result

"""track info via Get Several Tracks"""
def get_track_info(token, track_ids):
    ids = ','.join(track_ids)
    url = f'https://api.spotify.com/v1/tracks'
    headers = get_auth_header(token)
    params = {"ids": ids}

    result = get(url, headers=headers, params=params)
    json_result = json.loads(result.content)["tracks"]
    return json_result

"""audio features via Get Track's Audio Features"""
def get_audio_features(token, track_ids):
    ids = ','.join(track_ids)
    url = f'https://api.spotify.com/v1/audio-features'
    headers = get_auth_header(token)
    params = {"ids": ids}
    
    result = get(url, headers=headers, params=params)
    data = json.loads(result.content)

    if "audio_features" not in data:
        print("Spotify API error:", data)
    return None
    #json_result = json.loads(result.content)["audio_features"]
    #return json_result

"""Create .csv for full album"""

"""

Abandoned b/c spotify depreciated gettting track's audio features, and audio analysis

"""

token = get_token()

# Search album
album = search_for_album(token, "Film Noir", "Faouzia")
album_id = album["id"]

# Get all tracks
songs = get_songs_by_album(token, album_id)
song_ids = [s["id"] for s in songs]

# Test each function
track_info = get_track_info(token, song_ids)
audio_features = get_audio_features(token, song_ids)

#print(track_info)
print(audio_features)