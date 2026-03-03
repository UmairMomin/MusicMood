# app.py
import streamlit as st
import joblib
import pandas as pd

# Load your trained model
model = joblib.load('best_mood_model.pkl')
st.title("🎵 Music Mood Predictor")
st.write("Adjust all audio features to predict the song's mood!")

st.markdown("---")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎭 Core Features")
    danceability = st.slider('Danceability', 0.0, 1.0, 0.5, 0.01,
                           help="How suitable for dancing (0=not danceable, 1=very danceable)")
    energy = st.slider('Energy', 0.0, 1.0, 0.5, 0.01,
                      help="Perceived intensity and activity (0=calm, 1=energetic)")
    valence = st.slider('Valence', 0.0, 1.0, 0.5, 0.01,
                       help="Musical positiveness (0=sad/depressing, 1=happy/euphoric)")
    tempo = st.slider('Tempo (BPM)', 60.0, 200.0, 120.0, 1.0,
                     help="Overall estimated tempo in beats per minute")
    acousticness = st.slider('Acousticness', 0.0, 1.0, 0.5, 0.01,
                           help="Confidence measure of whether the track is acoustic (1=high confidence)")

with col2:
    st.subheader("🎵 Advanced Features")
    instrumentalness = st.slider('Instrumentalness', 0.0, 1.0, 0.5, 0.01,
                               help="Predicts whether a track contains no vocals (1=no vocals)")
    liveness = st.slider('Liveness', 0.0, 1.0, 0.5, 0.01,
                        help="Detects presence of an audience in the recording (1=live)")
    loudness = st.slider('Loudness (dB)', -60.0, 0.0, -20.0, 1.0,
                        help="Overall loudness in decibels (typically -60 to 0 dB)")
    speechiness = st.slider('Speechiness', 0.0, 1.0, 0.5, 0.01,
                          help="Detects presence of spoken words (1=entirely speech)")
    duration_ms = st.slider('Duration (minutes)', 1.0, 10.0, 3.5, 0.1,
                          help="Duration of the song in minutes")

# Convert duration from minutes to milliseconds
duration_ms_value = duration_ms * 60000

st.markdown("---")

if st.button('🎯 Predict Mood', type='primary'):
    # Create feature array with ALL 10 features in the correct order
    features = [[
        danceability,      # 0
        energy,           # 1  
        valence,          # 2
        tempo,            # 3
        acousticness,     # 4
        instrumentalness, # 5
        liveness,         # 6
        loudness,         # 7
        speechiness,      # 8
        duration_ms_value # 9
    ]]
    
    try:
        prediction = model.predict(features)[0]
        
        # Add emojis based on mood
        mood_emojis = {
            'happy': '😊 🎉',
            'sad': '😢 🌧️', 
            'energetic': '⚡ 💥',
            'chill': '😌 🌴',
            'neutral': '😐 ⚖️'
        }
        
        emoji = mood_emojis.get(prediction, '🎵')
        
        st.success(f"{emoji} **Predicted Mood: {prediction.upper()}**")
        
        # Show feature summary
        st.info("""
        **📊 Feature Summary:**
        - **Danceability**: {:.2f} {}
        - **Energy**: {:.2f} {}
        - **Valence**: {:.2f} {}
        - **Tempo**: {:.0f} BPM
        - **Acousticness**: {:.2f}
        - **Duration**: {:.1f} minutes
        """.format(
            danceability, "💃" if danceability > 0.6 else "🚶",
            energy, "⚡" if energy > 0.7 else "🔋", 
            valence, "😊" if valence > 0.6 else "😢",
            tempo, acousticness, duration_ms
        ))
        
    except Exception as e:
        st.error(f"❌ Prediction failed: {str(e)}")
        st.info("💡 Make sure your model was trained with exactly these 10 features in this order.")

# Add some information about what each feature means
with st.expander("ℹ️ About Audio Features"):
    st.markdown("""
    **Audio Features Explained:**
    
    - **Danceability**: How suitable a track is for dancing based on tempo, rhythm stability, beat strength, and overall regularity
    - **Energy**: Represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy
    - **Valence**: Describes the musical positiveness. Tracks with high valence sound more positive (happy, cheerful, euphoric)
    - **Tempo**: The overall estimated tempo of a track in beats per minute (BPM)
    - **Acousticness**: A confidence measure of whether the track is acoustic
    - **Instrumentalness**: Predicts whether a track contains no vocals
    - **Liveness**: Detects the presence of an audience in the recording
    - **Loudness**: The overall loudness of a track in decibels (dB)
    - **Speechiness**: Detects the presence of spoken words in a track
    - **Duration**: The length of the track in milliseconds
    """)

# Add preset examples
st.markdown("---")
st.subheader("🎼 Quick Presets")

preset_col1, preset_col2, preset_col3, preset_col4 = st.columns(4)

with preset_col1:
    if st.button("😊 Happy Pop"):
        st.session_state.danceability = 0.8
        st.session_state.energy = 0.7
        st.session_state.valence = 0.9
        st.session_state.tempo = 120
        st.rerun()

with preset_col2:
    if st.button("😢 Sad Ballad"):
        st.session_state.danceability = 0.3
        st.session_state.energy = 0.2
        st.session_state.valence = 0.1
        st.session_state.tempo = 70
        st.rerun()

with preset_col3:
    if st.button("⚡ Energetic Rock"):
        st.session_state.danceability = 0.6
        st.session_state.energy = 0.9
        st.session_state.valence = 0.7
        st.session_state.tempo = 140
        st.rerun()

with preset_col4:
    if st.button("😌 Chill Lo-fi"):
        st.session_state.danceability = 0.7
        st.session_state.energy = 0.4
        st.session_state.valence = 0.5
        st.session_state.tempo = 85
        st.rerun()