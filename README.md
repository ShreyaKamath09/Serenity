
## Serenity  
Serenity is an emotion music recommender system that provides a unique and personalized music streaming experience. It utilizes **facial emotion detection** and a **quiz** to analyze the user's emotions and recommend songs that match their mood. The application supports streaming from popular platforms such as Spotify, SoundCloud, and YouTube.

## Features
- **Emotion-based Music Recommendation:** Serenity uses facial emotion detection to analyze the user's emotions and recommends songs that match their mood.
- **Streaming from Multiple Platforms:** Users can stream music from their favorite platforms including Spotify, SoundCloud, and YouTube.
- **Personalized Playlists:** The application creates personalized playlists based on the user's emotions and preferences.
- **User-Friendly Interface:** Serenity offers an intuitive and easy-to-use interface for a seamless music streaming experience.

## Models
- **Facial Emotion Detection:** Implemented using the **VGG19** deep learning model trained on the **FER2013 dataset** for recognizing emotions from facial expressions.  
- **Mental Health Quiz Prediction:** Uses an **XGBoost** model to analyze quiz responses and assess emotional well-being.  
- **Spotify Track Analysis:** Integrated with the **Spotipy API** to fetch track features (tempo, energy, valence, etc.) for mood-based recommendations.  

## Emotion Detection
Serenity uses facial emotion detection and a quiz to analyze the user's emotions. Make sure your device has a camera enabled to utilize this feature effectively.

## Supported Platforms
Serenity supports music streaming from the following platforms:
- Spotify
- SoundCloud
- YouTube
