import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

def authenticate_spotify():
    credentials = SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID, 
        client_secret=SPOTIPY_CLIENT_ID
    )
    return spotipy.Spotify(client_credentials_manager=credentials)

def get_songs_by_mood(mood):
    sp = authenticate_spotify()
    
    # Search for tracks based on the mood
    mood_map = {
        'happy': 'Pop',
        'sad': 'Indie',
        'angry': 'Phonk',
        'surprise': 'Jazz',
        'fear': 'Dark Ambient',
        'disgust': 'Grindcore'
    }

    search_query = mood_map.get(mood, 'chill')
    
    results = sp.search(q=f'genre:"{search_query}"', type='track', limit=50)  # Increased limit for better filtering
    
    set_mood = mood or 'Neutral'
    
    songs = []
    added_artists = set()  # To keep track of unique artists
    
    for item in results['tracks']['items']:
        artist_names = ', '.join([artist['name'] for artist in item['artists']])
        # Adding song only if the artist is unique
        if artist_names not in added_artists:
            song = {
                'name': item['name'],
                'artist': artist_names,
                'url': item['external_urls']['spotify'],
                'image': item['album']['images'][0]['url'],
                'mood': set_mood,
                'genre': mood_map.get(mood, 'Chill')
            }
            songs.append(song)
            added_artists.add(artist_names)  # Mark the artist as added

        # Stop adding if we have 10 unique artists
        if len(songs) >= 12:
            break

    return songs

# Example usage:
mood = 'sad'  # Replace with the desired mood
songs = get_songs_by_mood(mood)
