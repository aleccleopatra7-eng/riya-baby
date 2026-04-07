import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Riya's Ultimate Creative Space", layout="wide")

# ---------------- FLOATING HEARTS + WELCOME ----------------
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
st.markdown("<h3 style='text-align:center; color:#ffffff;'>May our friendship last forever 💖</h3>", unsafe_allow_html=True)

# ---------------- SIDEBAR MENU ----------------
menu = st.sidebar.radio("✨ Explore", [
    "Home",
    "Music 🎵",
    "K-Drama 🎬",
    "BTS Updates 📰",
    "Message 💌"
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

    music_library = {
        "BTS": {
            "Dynamite": "https://www.youtube.com/watch?v=gdZLi9oWNZg",
            "Butter": "https://www.youtube.com/watch?v=WMweEpGlu_U",
            "Permission to Dance": "https://www.youtube.com/watch?v=CuklIb9d3fI"
        },
        "Blackpink": {
            "How You Like That": "https://www.youtube.com/watch?v=ioNng23DkIM",
            "Kill This Love": "https://www.youtube.com/watch?v=2S24-y0Ij3Y",
            "DDU-DU DDU-DU": "https://www.youtube.com/watch?v=IHNzOHi8sJs"
        },
        "Alan Walker": {
            "Faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
            "Alone": "https://www.youtube.com/watch?v=1-xGerv5FOk",
            "Spectre": "https://www.youtube.com/watch?v=AOeY-nDp7hI"
        }
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

    # Expanded drama/film library – 1 episode per drama
    dramas = {
        "Crash Landing on You": {"Episode 1": "https://www.youtube.com/watch?v=eXMjTXL2Vks"},
        "True Beauty": {"Episode 1": "https://www.youtube.com/watch?v=RHe2P8lG6bI"},
        "All of Us Are Dead": {"Episode 1": "https://www.youtube.com/watch?v=IN5TD4VRcSM"},
        "Itaewon Class": {"Episode 1": "https://www.youtube.com/watch?v=example1"},
        "Vincenzo": {"Episode 1": "https://www.youtube.com/watch?v=example1"},
        "Love Alarm": {"Episode 1": "https://www.youtube.com/watch?v=example1"},
        "Goblin": {"Episode 1": "https://www.youtube.com/watch?v=example1"},
        "My Love From the Star": {"Episode 1": "https://www.youtube.com/watch?v=example1"},
        "Extraordinary You": {"Episode 1": "https://www.youtube.com/watch?v=example1"},
        "Nevertheless": {"Episode 1": "https://www.youtube.com/watch?v=example1"}
    }

    drama_choice = st.selectbox("Pick a drama or film", list(dramas.keys()))
    if drama_choice:
        st.write(f"💜 Episode for {drama_choice}:")
        for ep_name, ep_link in dramas[drama_choice].items():
            st.markdown(f"[{ep_name}]({ep_link})")

# ---------------- BTS UPDATES ----------------
elif menu == "BTS Updates 📰":
    st.subheader("📰 Trending BTS Updates 💜")
    updates = [
        "BTS is trending worldwide with their latest single 'Yet to Come'!",
        "Upcoming BTS tour dates announced for Asia and Europe.",
        "BTS just hit 100M views on 'Butter' YouTube video!",
        "RM, Jin, Suga, J-Hope, Jimin, V, Jungkook continue making global headlines!"
    ]
    for update in updates:
        st.write(f"💜 {update}")

# ---------------- MESSAGE ----------------
elif menu == "Message 💌":
    st.subheader("💌 A Special Message For You 💌")
    messages = [
        "You make everything brighter 💜",
        "Keep smiling 😊",
        "This space is yours ✨",
        "You are special and appreciated 🖤",
        "May our friendship last forever 💖"
    ]
    st.write(random.choice(messages))

    if st.button("🎁 Reveal Surprise"):
        st.success("You matter a lot! 💜")
        st.balloons()
