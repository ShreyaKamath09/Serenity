import streamlit as st
import webbrowser
from streamlit_extras.app_logo import add_logo
import streamlit.components.v1 as components

page_bg_img = """
<style>
div.stButton > button:first-child {
    all: unset;
    width: 300px;
    height: 60px;
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
    background: #001a00;
    border-radius: 10px;
}
div.stButton > button:after {
  transform: translate(10px, 10px);
  width: 35px;
  height: 35px;
  background: #ffffff15;
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
background: linear-gradient(120deg, #1db954, #191414);
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
</style>
"""
add_logo("logo1.png")
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Serenity: Spotify")

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(''':white[**Note : It is recommended that you scan your face , for Serenity to groove with you!**]''')
# st.sidebar.success("Spotify has been selected as your music player.")


if "run" not in st.session_state:
    st.write("**Looks like you have skipped the face scan on the homepage and came here, just for music, just choose your vibe manually for Serenity to groove with you!**")
    option = st.selectbox(
    'What''s your vibe today?',
    ('Happy', 'Sad', 'Angry','Fear','Surprise','Neutral'))
    if option == "Happy":
        st.session_state["emotion"] = "Happy"
    elif option == "Sad":
        st.session_state["emotion"] = "Sad"
    elif option == "Angry":
        st.session_state["emotion"] = "Angry"
    elif option == "Fear":
        st.session_state["emotion"] = "Fear"
    elif option == "Surprise":
        st.session_state["emotion"] = "Surprise"
    else:
        st.session_state["emotion"] = "Neutral"
else:
    st.write("You current emotion is: " , st.session_state["emotion"])

col1, col2 = st.columns(2)

with col1:
    hindi = st.button("Hindi")
    if hindi:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWTwbZHrJRIgD?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWTwbZHrJRIgD?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/2r9tRVoHG3AMBTvKJ8abOl?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/08laqH1TPcPP4f0pkbJSa2?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>" 
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7vatYrf39uVaZ8G2cVtEik?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX0XUfTFmNBRM?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1E4mS880sTV9QE?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
            
    bengali = st.button("Bengali")
    if bengali:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/6xW5Vg6ItVIcGzpWpLxrkE?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/6xW5Vg6ItVIcGzpWpLxrkE?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXcjgclFIY2pu?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/1Gt1bGUTHneUptZtc9Msoi?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/0m1idUXUOeJ29oaufW0mLQ?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3RiXySA2fqrWlnAU9n3Lv2?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/7cOYpcvIHxyNdu1DhXkCpu?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
            
    marathi = st.button("Marathi")
    if marathi:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/4VyXj7QL7tcyJFM4h1wYe7?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/4VyXj7QL7tcyJFM4h1wYe7?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/5dKWOIUR0lmN5URKUVpV6a?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/0vccDJJVPeQc2F6hwy4Y4v?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX8BKauvV4z7b?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX84EApEEEkUc?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3sKYXN4FEWLpg4FiJlxSrN?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
   
with col2:
   english = st.button("English")
   if english:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1EIgNZCaOGb0Mi?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/4rIoHGE82kPRFP78nJ4HNG?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1EIfIhwClkyzKs?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZEVXbMDoHDwVN2tF?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/60eEo5VdhekyGJKTjK2xSV?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
            
   punjabi = st.button("Punjabi")
   if punjabi:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX7QeQjujWh9l?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX7QeQjujWh9l?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/5ecJF7ZFkufISEw6SZdKrB?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/45Mzf4oLd6vksC1cnKdZEM?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWZY9CnWbvq8Q?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DWXVJK4aT7pmk?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3sKYXN4FEWLpg4FiJlxSrN?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
            
   telugu = st.button("Telugu")
   if telugu:
        if st.session_state["emotion"] == "Happy":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX2UT3NuRgcHd?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Sad":
           components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX2UT3NuRgcHd?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Angry":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX4H5837Y8I1n?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Fear":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/1abCG2GayESKg6BjKLj93w?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Surprise":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DXcuAVsi45c0d?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        elif st.session_state["emotion"] == "Neutral":
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/37i9dQZF1DX6XE7HRLM75P?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write;  fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
        else:
            components.html(
            """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/2uTxm6no7uMOHOSYENE7My?utm_source=generator&theme=0" width="100%" height="600" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; fullscreen; picture-in-picture" loading="lazy"></iframe>
            """,height=600)
           