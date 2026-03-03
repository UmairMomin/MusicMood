from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI", "http://127.0.0.1:8888/callback")

if not client_id or not client_secret:
    raise ValueError(
        "Missing Spotify credentials. Set SPOTIPY_CLIENT_ID and "
        "SPOTIPY_CLIENT_SECRET in your .env file."
    )


# # Step 1: Get token
auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)
token = auth_manager.get_access_token(as_dict=False)

print("Access Token:", token)  # just to verify it's being generated

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="user-library-read"  # any user scope is enough
))

results = sp.current_user_saved_tracks()
print(results)

# track_ids = ["3n3Ppam7vgaVa1iaRUc9Lp", "7ouMYWpwJ422jRcDASZB7P"]
# features = sp.audio_features("11dFghVXANMlKmJXsNCbNl")
# print(features)
