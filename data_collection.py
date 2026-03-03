# complete_music_data_collection.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

if not client_id or not client_secret:
    raise ValueError(
        "Missing Spotify credentials. Set SPOTIPY_CLIENT_ID and "
        "SPOTIPY_CLIENT_SECRET in your .env file."
    )

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# # EXTENDED SONG LIST (80+ songs)
# extended_song_list = [
#     # 🎉 HAPPY/UPBEAT
#     {"name": "Happy", "artist": "Pharrell Williams"},
#     {"name": "Uptown Funk", "artist": "Mark Ronson ft Bruno Mars"},
#     {"name": "Can't Stop the Feeling", "artist": "Justin Timberlake"},
#     {"name": "Dance Monkey", "artist": "Tones and I"},
#     {"name": "Shut Up and Dance", "artist": "Walk The Moon"},
#     {"name": "I Gotta Feeling", "artist": "Black Eyed Peas"},
#     {"name": "Good Feeling", "artist": "Flo Rida"},
#     {"name": "Walking on Sunshine", "artist": "Katrina & The Waves"},
#     {"name": "Don't Stop Me Now", "artist": "Queen"},
#     {"name": "Dynamite", "artist": "BTS"},
#     {"name": "Levitating", "artist": "Dua Lipa"},
#     {"name": "24K Magic", "artist": "Bruno Mars"},
#     {"name": "Sorry", "artist": "Justin Bieber"},
#     {"name": "Shape of You", "artist": "Ed Sheeran"},
#     {"name": "Get Lucky", "artist": "Daft Punk"},
#     {"name": "Treasure", "artist": "Bruno Mars"},
#     {"name": "Sugar", "artist": "Maroon 5"},
#     {"name": "Party Rock Anthem", "artist": "LMFAO"},
#     {"name": "We Found Love", "artist": "Rihanna"},
#     {"name": "Call Me Maybe", "artist": "Carly Rae Jepsen"},
    
#     # ⚡ ENERGETIC/INTENSE
#     {"name": "Thunder", "artist": "Imagine Dragons"},
#     {"name": "Eye of the Tiger", "artist": "Survivor"},
#     {"name": "Lose Yourself", "artist": "Eminem"},
#     {"name": "Stronger", "artist": "Kanye West"},
#     {"name": "Till I Collapse", "artist": "Eminem"},
#     {"name": "Radioactive", "artist": "Imagine Dragons"},
#     {"name": "Believer", "artist": "Imagine Dragons"},
#     {"name": "Thunderstruck", "artist": "AC/DC"},
#     {"name": "Back In Black", "artist": "AC/DC"},
#     {"name": "Enter Sandman", "artist": "Metallica"},
#     {"name": "Killing In The Name", "artist": "Rage Against The Machine"},
#     {"name": "Basket Case", "artist": "Green Day"},
#     {"name": "Numb", "artist": "Linkin Park"},
#     {"name": "In The End", "artist": "Linkin Park"},
#     {"name": "Bring Me To Life", "artist": "Evanescence"},
#     {"name": "Seven Nation Army", "artist": "The White Stripes"},
#     {"name": "Sabotage", "artist": "Beastie Boys"},
#     {"name": "Bulls On Parade", "artist": "Rage Against The Machine"},
#     {"name": "Crazy Train", "artist": "Ozzy Osbourne"},
#     {"name": "Welcome to the Jungle", "artist": "Guns N' Roses"},
    
#     # 😴 CHILL/RELAXED
#     {"name": "Blinding Lights", "artist": "The Weeknd"},
#     {"name": "Circles", "artist": "Post Malone"},
#     {"name": "Sunflower", "artist": "Post Malone"},
#     {"name": "Watermelon Sugar", "artist": "Harry Styles"},
#     {"name": "Starboy", "artist": "The Weeknd"},
#     {"name": "Heat Waves", "artist": "Glass Animals"},
#     {"name": "The Less I Know The Better", "artist": "Tame Impala"},
#     {"name": "Electric Feel", "artist": "MGMT"},
#     {"name": "Time to Relax", "artist": "Offspring"},
#     {"name": "Island In The Sun", "artist": "Weezer"},
#     {"name": "Banana Pancakes", "artist": "Jack Johnson"},
#     {"name": "Breathe", "artist": "Telepopmusik"},
#     {"name": "No Diggity", "artist": "Blackstreet"},
#     {"name": "Smooth", "artist": "Santana"},
#     {"name": "Mirrors", "artist": "Justin Timberlake"},
#     {"name": "Thinking Out Loud", "artist": "Ed Sheeran"},
#     {"name": "All of Me", "artist": "John Legend"},
#     {"name": "Stay With Me", "artist": "Sam Smith"},
#     {"name": "Say You Won't Let Go", "artist": "James Arthur"},
#     {"name": "Perfect", "artist": "Ed Sheeran"},
    
#     # 💔 SAD/MELANCHOLIC
#     {"name": "Someone Like You", "artist": "Adele"},
#     {"name": "All I Want", "artist": "Kodaline"},
#     {"name": "Say Something", "artist": "A Great Big World"},
#     {"name": "When I Was Your Man", "artist": "Bruno Mars"},
#     {"name": "Stay", "artist": "Rihanna"},
#     {"name": "Skinny Love", "artist": "Bon Iver"},
#     {"name": "The Scientist", "artist": "Coldplay"},
#     {"name": "Fix You", "artist": "Coldplay"},
#     {"name": "Hurt", "artist": "Johnny Cash"},
#     {"name": "Mad World", "artist": "Gary Jules"},
#     {"name": "Nothing Compares 2 U", "artist": "Sinead O'Connor"},
#     {"name": "Everybody Hurts", "artist": "R.E.M."},
#     {"name": "Tears In Heaven", "artist": "Eric Clapton"},
#     {"name": "My Heart Will Go On", "artist": "Celine Dion"},
#     {"name": "Unbreak My Heart", "artist": "Toni Braxton"},
#     {"name": "I Will Always Love You", "artist": "Whitney Houston"},
#     {"name": "Nothing Else Matters", "artist": "Metallica"},
#     {"name": "Hallelujah", "artist": "Jeff Buckley"},
#     {"name": "Sound of Silence", "artist": "Simon & Garfunkel"},
#     {"name": "Yesterday", "artist": "The Beatles"}
# ]

# def auto_label_mood(features):
#     """
#     Enhanced rule-based mood classification
#     """
#     valence = features['valence']  # Musical positiveness (0=sad, 1=happy)
#     energy = features['energy']    # Intensity (0=calm, 1=intense)
#     danceability = features['danceability']
    
#     # Enhanced rules
#     if valence > 0.75 and energy > 0.7 and danceability > 0.6:
#         return "happy"
#     elif valence < 0.3 and energy < 0.4:
#         return "sad"
#     elif energy > 0.8 and valence > 0.5:
#         return "energetic"
#     elif energy > 0.8 and valence <= 0.5:
#         return "intense"
#     elif danceability > 0.6 and energy > 0.4 and energy < 0.7:
#         return "chill"
#     else:
#         return "neutral"

# def get_song_data(song_name, artist_name):
#     """Get audio features from Spotify API with error handling"""
#     try:
#         # Small delay to avoid rate limiting
#         time.sleep(0.1)
        
#         # Search for the song
#         query = f"track:{song_name} artist:{artist_name}"
#         results = sp.search(q=query, type='track', limit=1)
        
#         if not results['tracks']['items']:
#             # Try with just the song name
#             results = sp.search(q=f"track:{song_name}", type='track', limit=1)
#             if not results['tracks']['items']:
#                 return None
        
#         track = results['tracks']['items'][0]
#         song_id = track['id']
        
#         # Get audio features
#         audio_features = sp.audio_features(song_id)[0]
        
#         if not audio_features:
#             return None
            
#         # Auto-label the mood
#         mood_label = auto_label_mood(audio_features)
        
#         return {
#             'song_name': song_name,
#             'artist': artist_name,
#             'mood': mood_label,
#             'danceability': audio_features['danceability'],
#             'energy': audio_features['energy'],
#             'valence': audio_features['valence'],
#             'tempo': audio_features['tempo'],
#             'acousticness': audio_features['acousticness'],
#             'instrumentalness': audio_features['instrumentalness'],
#             'liveness': audio_features['liveness'],
#             'loudness': audio_features['loudness'],
#             'speechiness': audio_features['speechiness'],
#             'duration_ms': audio_features['duration_ms'],
#             'popularity': track['popularity']
#         }
        
#     except Exception as e:
#         print(f"❌ Error with {song_name}: {str(e)[:50]}...")
#         return None

# # Collect all song data
# print("🎵 Starting extended music data collection...")
# print(f"📀 Processing {len(extended_song_list)} songs...")
# dataset = []
# success_count = 0

# for i, song in enumerate(extended_song_list):
#     print(f"({i+1:2d}/{len(extended_song_list)}) Processing: {song['name'][:25]:25}...", end="")
    
#     song_data = get_song_data(song['name'], song['artist'])
#     if song_data:
#         dataset.append(song_data)
#         success_count += 1
#         print(f" ✅ ({song_data['mood']})")
#     else:
#         print(f" ❌ (Not found)")

# # Create DataFrame and save
# if dataset:
#     df = pd.DataFrame(dataset)
    
#     # Analysis
#     mood_counts = df['mood'].value_counts()
    
#     print(f"\n" + "="*50)
#     print("🎊 DATA COLLECTION COMPLETE!")
#     print("="*50)
#     print(f"✅ Successfully collected: {success_count}/{len(extended_song_list)} songs")
#     print(f"📊 Mood Distribution:")
#     for mood, count in mood_counts.items():
#         percentage = (count / len(df)) * 100
#         print(f"   {mood:10}: {count:2d} songs ({percentage:.1f}%)")
    
#     # Save to CSV
#     filename = f'music_mood_dataset_{len(df)}_songs.csv'
#     df.to_csv(filename, index=False)
#     print(f"💾 Saved to '{filename}'")
    
#     # Show sample
#     print(f"\n📋 Sample of your dataset:")
#     sample = df[['song_name', 'artist', 'mood', 'valence', 'energy']].head(8)
#     print(sample.to_string(index=False))
    
#     # Show some statistics
#     print(f"\n📈 Feature Statistics:")
#     print(f"   Average Valence: {df['valence'].mean():.3f}")
#     print(f"   Average Energy:  {df['energy'].mean():.3f}")
#     print(f"   Average Tempo:   {df['tempo'].mean():.1f} BPM")
    
# else:
#     print("❌ No data collected. Please check your Spotify API credentials.")

# print(f"\n✨ Your dataset is ready for machine learning!")
# print("   Next step: Use this CSV file to train your mood classification models.")

track_id = "6JV2JOEocMgcZxYSZelKcc"  # Happy - Pharrell Williams
features = sp.audio_features([track_id])  # wrap in a list

if features and features[0]:
    print("✅ Audio features:", features[0])
else:
    print("⚠️ No audio features found for this track.")
