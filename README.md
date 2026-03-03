# MusicMood

MusicMood is a Python project for:
- Predicting a song's mood from Spotify-style audio features
- Recommending songs by mood from a prepared recommendation database

It includes a trained model (`best_mood_model.pkl`) and Streamlit apps for interactive use.
CSV datasets are intentionally not committed to Git.

## Features

- Mood prediction using 10 audio features
- Mood-based song recommendations
- Streamlit UI with sliders, tabs, and summary stats
- Spotify API utility scripts for collecting/checking audio features

## Project Structure

- `music_mood_classifier_real_data.py`: Main Streamlit app (mood prediction + recommendations)
- `test2.py`: Alternate Streamlit mood predictor UI
- `data_collection.py`: Spotify API collection/testing script
- `test.py`: Spotify authentication/API test script
- `best_mood_model.pkl`: Trained mood classification model
- `music_recommendation_database.csv`: Song recommendation database with mood labels (download separately)
- `spotify_songs.csv`: Large raw song dataset (download separately)

## Requirements

- Python 3.9+
- pip

Python packages used in the project:
- `streamlit`
- `pandas`
- `numpy`
- `joblib`
- `spotipy`
- `python-dotenv`
- `scikit-learn`

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install streamlit pandas numpy joblib spotipy python-dotenv scikit-learn
```

3. Create your `.env` file:

```env
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
```

## Dataset Links

- `spotify_songs.csv`: [Kaggle - 30000 Spotify Songs](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs)
- `music_recommendation_database.csv`: It is a generated dataset. Use a dataset you like from the web!

## Run the App

Main app (prediction + recommendations):

```bash
streamlit run music_mood_classifier_real_data.py
```

Alternate predictor app:

```bash
streamlit run test2.py
```

## Model Input Features

The model expects these features in this order:

1. `danceability`
2. `energy`
3. `valence`
4. `tempo`
5. `acousticness`
6. `instrumentalness`
7. `liveness`
8. `loudness`
9. `speechiness`
10. `duration_ms`

## Mood Labels

The app uses these mood categories:
- `happy`
- `sad`
- `energetic`
- `chill`
- `neutral`

## Spotify Scripts

- `data_collection.py` and `test.py` use Spotify API credentials.
- Credentials are loaded from `.env` (`SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, `SPOTIPY_REDIRECT_URI`).

## Troubleshooting

- If model load fails, ensure `best_mood_model.pkl` is present in the project root.
- If recommendations fail, ensure `music_recommendation_database.csv` is present and readable.
- If Spotify scripts fail, verify your Spotify credentials and app settings.

## Notes

- CSV files are excluded from Git via `.gitignore` (`*.csv`).
- Keep model and CSV files in the same directory as the Streamlit scripts unless you update file paths in code.
