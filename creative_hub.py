import streamlit as st
import os
import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Riya's Ultimate Creative Hub", layout="wide")

# ---------------- FLOATING HEARTS ----------------
st.markdown("""
<style>
@keyframes float {
  0% { transform: translateY(0px); opacity: 1;}
  100% { transform: translateY(-200px); opacity: 0;}
}
.heart {
  position: fixed;
  font-size: 24px;
  animation: float 5s infinite;
}
</style>

<div class="heart" style="left:10%; animation-delay:0s;">💜</div>
<div class="heart" style="left:30%; animation-delay:1s;">💜</div>
<div class="heart" style="left:50%; animation-delay:2s;">💜</div>
<div class="heart" style="left:70%; animation-delay:3s;">💜</div>
<div class="heart" style="left:90%; animation-delay:4s;">💜</div>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center; color:#d8b4ff;'>Welcome, Riya Smiley! 💜</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#000000;'>May our friendship last forever 💖</h3>", unsafe_allow_html=True)

# ---------------- STORY FOLDER ----------------
story_folder = "riya_stories"
if not os.path.exists(story_folder):
    os.makedirs(story_folder)

# ---------------- SIDEBAR MENU ----------------
menu = st.sidebar.radio("✨ Explore", [
    "Home",
    "Music 🎵",
    "K-Drama 🎬",
    "BTS Updates 📰",
    "Message 💌",
    "Story World ✍️"
])

# ---------------- HOME ----------------
if menu == "Home":
    st.subheader("💫 Your Creative Space 💫")
    st.write("This space was made just for you, Riya 🖤💜")
    if st.button("💜 Secret 💜"):
        st.success("You found the secret! 🎉")
        st.balloons()

# ---------------- MUSIC ----------------
elif menu == "Music 🎵":
    st.subheader("🎧 Music Zone 💜")
    st.write("Select an artist and enjoy your favorite songs!")

    # 20 songs per artist
    music_library = {
        "BTS": {f"Song {i}": f"https://www.youtube.com/watch?v=example{i}" for i in range(1, 21)},
        "Blackpink": {f"Song {i}": f"https://www.youtube.com/watch?v=example{i+100}" for i in range(1, 21)},
        "Alan Walker": {f"Song {i}": f"https://www.youtube.com/watch?v=example{i+200}" for i in range(1, 21)}
    }

    artist = st.selectbox("Pick an artist", list(music_library.keys()))
    if artist:
        st.write(f"💜 Songs by {artist}:")
        for song, link in music_library[artist].items():
            st.markdown(f"[{song}]({link})")

# ---------------- K-DRAMA ----------------
elif menu == "K-Drama 🎬":
    st.subheader("🍿 K-Drama / Films 💜")
    st.write("Select a drama or film to watch episodes:")

    dramas = {
        "Crash Landing on You": {f"Episode {i}": f"https://www.youtube.com/watch?v=example{i}" for i in range(1, 11)},
        "True Beauty": {f"Episode {i}": f"https://www.youtube.com/watch?v=example{i+10}" for i in range(1, 12)},
        "Vincenzo": {f"Episode {i}": f"https://www.youtube.com/watch?v=example{i+22}" for i in range(1, 10)}
    }

    drama_choice = st.selectbox("Pick a drama or film", list(dramas.keys()))
    if drama_choice:
        st.write(f"💜 Episodes for {drama_choice}:")
        for ep_name, ep_link in dramas[drama_choice].items():
            st.markdown(f"[{ep_name}]({ep_link})")

# ---------------- BTS UPDATES ----------------
elif menu == "BTS Updates 📰":
    st.subheader("📰 Trending BTS Updates 💜")
    updates = [
        "BTS is trending worldwide with their latest single 'Yet to Come'!",
        "BTS announces new tour dates!",
        "BTS hits record views on Butter!",
        "RM, Jin, Suga, J‑Hope, Jimin, V, Jungkook trending worldwide!"
    ]
    for update in updates:
        st.write(f"💜 {update}")

# ---------------- MESSAGE ----------------
elif menu == "Message 💌":
    st.subheader("💌 A Special Message For You 💌")
    st.markdown("💖 You are amazing, Riya! May our friendship last forever 💖")

    messages = [
        "You make everything brighter 💜",
        "Keep smiling 😊",
        "This space is yours ✨",
        "You are special and appreciated 🖤",
        "May our friendship last forever 💖"
    ]
    if st.button("🎁 Reveal Another Surprise"):
        st.success(random.choice(messages))
        st.balloons()

# ---------------- STORY WORLD + COMIC ----------------
elif menu == "Story World ✍️":
    st.subheader("Write, play, and enjoy your stories!")

    mood = st.selectbox("Pick a Mood 🎨", ["Normal", "Magical", "Happy", "Sad"])
    mood_colors = {"Normal": "#ffffff", "Magical": "#f8f0ff", "Happy": "#fff0f8", "Sad": "#f0f0f8"}
    st.markdown(f"<div style='background-color:{mood_colors[mood]}; padding:10px;'>", unsafe_allow_html=True)

    emoji_list = ["💜", "✨", "🖤", "💖", "🌸", "🎉"]
    st.sidebar.write("Add Emojis:")
    for emoji in emoji_list:
        if st.sidebar.button(emoji):
            st.session_state.setdefault("story_text", "")
            st.session_state.story_text += emoji

    story_title = st.text_input("Story Title")
    story_text = st.text_area("Your story text", value=st.session_state.get("story_text", ""), key="story_text")

    if st.button("💾
