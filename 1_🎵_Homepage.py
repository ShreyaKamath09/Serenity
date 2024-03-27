from pathlib import Path
#Imports for streamlit
import streamlit as st
import av
import cv2
from streamlit_webrtc import (
    RTCConfiguration,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo

#Imports for ml model
import numpy as np
import mediapipe as mp
from keras.models import load_model


st.set_page_config(
    page_title="Serenity",
    page_icon="🎵",
)

page_bg_img = """
<style>



[data-testid="stSelectbox"] .stSelectbox-placeholder {
    border-radius: 400px; /* Adjust the border-radius to change the shape */
    border: 2px solid #7B41F0; /* Border color */
    padding: 10px; /* Padding */
    font-size: 16px; /* Font size */
    background-color: #ffffff; /* Background color */
    color: #000000; /* Text color */
}

[data-testid="stSelectbox"] .stSelectbox-options {
    border-radius: 15px; /* Adjust the border-radius to match the placeholder */
    border: 2px solid #7B41F0; /* Border color */
    font-size: 16px; /* Font size */
    background-color: #ffffff; /* Background color */
    color: #000000; /* Text color */
    margin-top: 5px; /* Adjust the margin */
}

div.stButton > button:first-child {
    all: unset;
    width: 120px;
    height: 40px;
    font-size: 32px;
    background: transparent;
    border: none;
    position: relative;
    color: #f0f0f0;
    cursor: pointer;
    z-index: 1;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;

}
div.stButton > button:before, div.stButton > button:after {
    content: '';
    position: absolute;
    bottom: 0;
    right: 0;
    z-index: -99999;
    transition: all .4s;
}

div.stButton > button:before {
    transform: translate(0%, 0%);
    width: 100%;
    height: 100%;
    background: #0f001a;
    border-radius: 10px;
}
div.stButton > button:after {
  transform: translate(10px, 10px);
  width: 35px;
  height: 35px;
  background: #ffffff15;
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  border-radius: 50px;
}

div.stButton > button:hover::before {
    transform: translate(5%, 20%);
    width: 110%;
    height: 110%;
}


div.stButton > button:hover::after {
    border-radius: 10px;
    transform: translate(0, 0);
    width: 100%;
    height: 100%;
}

div.stButton > button:active::after {
    transition: 0s;
    transform: translate(0, 5%);
}



[data-testid="stAppViewContainer"] {
# background-image: url("https://images.unsplash.com/photo-1613327986042-63d4425a1a5d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
 background-color: #9771EB;
color: #ffffff; 
}

[data-testid="stSidebar"] > div:first-child {
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
background : black;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stHeader"] h1 {
    font-family: 'Indie Flower', cursive;
}

</style>
"""
add_logo("logo1.png")
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("SERENITY ")
# st.sidebar.success("Select a page below.")
# st.sidebar.text("Developed by Shambhavi")

st.markdown("**Welcome to Serenity!** We're here to make your music experience truly personal. Our clever AI analyzes your emotions through your webcam and crafts playlists that match your mood perfectly.")
st.markdown("**It's like having a musical companion who always knows how you feel. So, let's dive in together!** ")


RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{
        "urls": ["stun:stun.l.google.com:19302"]
    }]})

# CWD path
HERE = Path(__file__).parent

model = load_model("model.h5")
label = np.load("label.npy")

holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

if "run" not in st.session_state:
    st.session_state["run"] = ""

run = np.load("emotion.npy")[0]

try:
    emotion = np.load("emotion.npy")[0]
except:
    emotion = ""

    
class EmotionProcessor(VideoProcessorBase):
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        frm = frame.to_ndarray(format="bgr24")
        frm = cv2.flip(frm, 1)  
        res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
        
        lst = []
        if res.face_landmarks:
            for i in res.face_landmarks.landmark:
                lst.append(i.x - res.face_landmarks.landmark[1].x)
                lst.append(i.y - res.face_landmarks.landmark[1].y)
        
            if res.left_hand_landmarks:
                for i in res.left_hand_landmarks.landmark:
                    lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
            else:
                for i in range(42):
                    lst.append(0.0)
        
            if res.right_hand_landmarks:
                for i in res.right_hand_landmarks.landmark:
                    lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
            else:
                for i in range(42):
                    lst.append(0.0)
        
            lst = np.array(lst).reshape(1, -1)
        
            pred = label[np.argmax(model.predict(lst))]
            print(pred)
            cv2.putText(frm, pred, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            
            np.save("emotion.npy",np.array([pred]))
            
            emotion = pred
       
        drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_CONTOURS)
        drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS) 
        drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)
    
        return av.VideoFrame.from_ndarray(frm, format="bgr24")
    


webrtc_streamer(key="key", desired_playing_state=st.session_state.get("run", "") == "true" ,mode=WebRtcMode.SENDRECV,  rtc_configuration=RTC_CONFIGURATION, video_processor_factory=EmotionProcessor, media_stream_constraints={
        "video": True,
        "audio": False
    },
    async_processing=True)


col1, col2, col6 = st.columns([1, 1, 1])

with col1:
    start_btn = st.button("Start")
with col6:
    stop_btn = st.button("Stop")

if start_btn:
    st.session_state["run"] = "true"
    st.experimental_rerun()

if stop_btn:
    st.session_state["run"] = "false"
    st.experimental_rerun()
else:
    if not emotion:
        pass
    else:
        np.save("emotion.npy", np.array([""]))
        st.session_state["emotion"] = run
        st.success("Your current emotion is: " + emotion)
        st.subheader("Choose your streaming service")

col3, col4, col5 = st.columns(3)

with col4:
    btn = st.button("Spotify")
    if btn:
        switch_page("Spotify")

with col5:
    btn2 = st.button("Youtube")
    if btn2:
        switch_page("Youtube")

with col3:
    btn3 = st.button("Soundcloud")
    if btn3:
        switch_page("Soundcloud")