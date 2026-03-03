# app_recommendations.py
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load your trained model and recommendation database
try:
    model = joblib.load('best_mood_model.pkl')
    recommendation_db = pd.read_csv('music_recommendation_database.csv')
    st.success("✅ Models loaded successfully!")
except:
    st.error("❌ Could not load model files. Please make sure they are in the same directory.")
    recommendation_db = pd.DataFrame()

st.title("🎵 Music Mood & Recommendation System")
st.write("Predict song moods OR get song recommendations based on mood!")

# Create tabs for different functionalities
tab1, tab2 = st.tabs(["🎯 Mood Prediction", "🎵 Song Recommendations"])

with tab1:
    st.header("Predict Song Mood from Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        danceability = st.slider('Danceability', 0.0, 1.0, 0.5, 0.01)
        energy = st.slider('Energy', 0.0, 1.0, 0.5, 0.01)
        valence = st.slider('Valence', 0.0, 1.0, 0.5, 0.01)
        tempo = st.slider('Tempo (BPM)', 60.0, 200.0, 120.0, 1.0)
        acousticness = st.slider('Acousticness', 0.0, 1.0, 0.5, 0.01)
    
    with col2:
        instrumentalness = st.slider('Instrumentalness', 0.0, 1.0, 0.5, 0.01)
        liveness = st.slider('Liveness', 0.0, 1.0, 0.5, 0.01)
        loudness = st.slider('Loudness (dB)', -60.0, 0.0, -20.0, 1.0)
        speechiness = st.slider('Speechiness', 0.0, 1.0, 0.5, 0.01)
        duration_ms = st.slider('Duration (minutes)', 1.0, 10.0, 3.5, 0.1)
    
    duration_ms_value = duration_ms * 60000
    
    if st.button('🎯 Predict Mood', key='predict'):
        features = [[danceability, energy, valence, tempo, acousticness, 
                    instrumentalness, liveness, loudness, speechiness, duration_ms_value]]
        
        try:
            prediction = model.predict(features)[0]
            mood_emojis = {'happy': '😊', 'sad': '😢', 'energetic': '⚡', 'chill': '😌', 'neutral': '😐'}
            emoji = mood_emojis.get(prediction, '🎵')
            
            st.success(f"{emoji} **Predicted Mood: {prediction.upper()}**")
            
            # Show what this mood typically sounds like
            st.info(f"""
            **Songs with {prediction} mood typically have:**
            - **Valence**: {'High (positive)' if prediction == 'happy' else 'Low (negative)' if prediction == 'sad' else 'Medium'}
            - **Energy**: {'High' if prediction in ['happy', 'energetic'] else 'Low' if prediction == 'sad' else 'Medium'}
            - **Best for**: {'Parties, workouts' if prediction == 'energetic' else 'Relaxing, studying' if prediction == 'chill' else 'Emotional moments' if prediction == 'sad' else 'General listening'}
            """)
            
        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")

with tab2:
    st.header("Get Song Recommendations by Mood")
    
    # Mood selection
    selected_mood = st.selectbox(
        "Choose a mood:",
        ["happy", "sad", "energetic", "chill", "neutral"],
        format_func=lambda x: f"{x.title()} {'😊' if x=='happy' else '😢' if x=='sad' else '⚡' if x=='energetic' else '😌' if x=='chill' else '😐'}"
    )
    
    num_recommendations = st.slider("Number of recommendations:", 5, 20, 10)
    
    if st.button('🎵 Get Recommendations', key='recommend'):
        if recommendation_db.empty:
            st.error("Recommendation database not loaded!")
        else:
            # Filter songs by selected mood
            mood_songs = recommendation_db[recommendation_db['mood'] == selected_mood]
            
            if len(mood_songs) == 0:
                st.warning(f"No songs found with mood: {selected_mood}")
            else:
                # Get random sample for recommendations
                recommendations = mood_songs.sample(n=min(num_recommendations, len(mood_songs)))
                
                st.success(f"🎉 Here are {len(recommendations)} {selected_mood} songs for you!")
                
                # Display recommendations in a nice format
                for idx, song in recommendations.iterrows():
                    with st.container():
                        col1, col2 = st.columns([3, 1])
                        
                        with col1:
                            st.write(f"**{song['name']}**")
                            st.write(f"*by {song['artists']}*")
                            
                            # Show key features
                            feature_text = f"Danceability: {song['danceability']:.2f} | "
                            feature_text += f"Energy: {song['energy']:.2f} | "
                            feature_text += f"Valence: {song['valence']:.2f}"
                            st.caption(feature_text)
                        
                        with col2:
                            # Mood indicator
                            mood_colors = {
                                'happy': '🟡',
                                'sad': '🔵', 
                                'energetic': '🔴',
                                'chill': '🟢',
                                'neutral': '⚪'
                            }
                            st.write(mood_colors.get(selected_mood, '⚪'))
                        
                        st.divider()

# Add some statistics
st.sidebar.header("📊 System Statistics")
if not recommendation_db.empty:
    st.sidebar.write(f"**Total Songs:** {len(recommendation_db):,}")
    mood_counts = recommendation_db['mood'].value_counts()
    for mood, count in mood_counts.items():
        st.sidebar.write(f"**{mood.title()}:** {count} songs")

st.markdown("---")
st.caption("🎵 Music Mood Classification System | Built with Machine Learning")