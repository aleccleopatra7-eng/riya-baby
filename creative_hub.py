import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Riya's Ultimate Creative Space", layout="wide")

# ---------------- BACKGROUND IMAGE ----------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.imgur.com/OjQxgD8.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
            "Permission to Dance": "https://www.youtube.com/watch?v=CuklIb9d3fI",
            "Boy With Luv": "https://www.youtube.com/watch?v=XsX3ATc3FbA",
            "Fake Love": "https://www.youtube.com/watch?v=7C2z4GqqS5E",
            "Spring Day": "https://www.youtube.com/watch?v=xEeFrLSkMm8",
            "Idol": "https://www.youtube.com/watch?v=pBuZEGYXA6E",
            "ON": "https://www.youtube.com/watch?v=K3qNtM5MyvM",
            "Blood Sweat & Tears": "https://www.youtube.com/watch?v=hmE9f-TEutc",
            "MIC Drop": "https://www.youtube.com/watch?v=kTlv5_Bs8aw",
            "Black Swan": "https://www.youtube.com/watch?v=gmwea9gXdx8",
            "Life Goes On": "https://www.youtube.com/watch?v=Fg7tT1k2F9Q",
            "Not Today": "https://www.youtube.com/watch?v=9DwzBICPhdM",
            "Butterfly": "https://www.youtube.com/watch?v=co6WMzDOh1o",
            "Film Out": "https://www.youtube.com/watch?v=WjAf0IVGHtA",
            "Go Go": "https://www.youtube.com/watch?v=fsX4c-CMBmg",
            "Run BTS": "https://www.youtube.com/watch?v=2VZrkfkgN4o",
            "Stay Gold": "https://www.youtube.com/watch?v=5kENt_J8Jkg",
            "Permission to Dance (Dance Ver.)": "https://www.youtube.com/watch?v=R9tZp6hYIuo",
            "Dynamite (Dance Ver.)": "https://www.youtube.com/watch?v=9R8aWl_kG1o"
        },
        "Blackpink": {
            "How You Like That": "https://www.youtube.com/watch?v=ioNng23DkIM",
            "Kill This Love": "https://www.youtube.com/watch?v=2S24-y0Ij3Y",
            "DDU-DU DDU-DU": "https://www.youtube.com/watch?v=IHNzOHi8sJs",
            "BOOMBAYAH": "https://www.youtube.com/watch?v=ygJ_9y4x5kQ",
            "Pretty Savage": "https://www.youtube.com/watch?v=3P2v4xQ1q8o",
            "Lovesick Girls": "https://www.youtube.com/watch?v=dyRsYk0LyA8",
            "Whistle": "https://www.youtube.com/watch?v=dISNgvVpWlo",
            "Playing With Fire": "https://www.youtube.com/watch?v=9pdj4iJD08s",
            "As If It's Your Last": "https://www.youtube.com/watch?v=Amq-qlqbjYA",
            "Ice Cream": "https://www.youtube.com/watch?v=vRXZj0DzXIA",
            "Pink Venom": "https://www.youtube.com/watch?v=Q0CbN8sfihY",
            "Shut Down": "https://www.youtube.com/watch?v=w2hH9YZJljU",
            "Bet You Wanna": "https://www.youtube.com/watch?v=K4QVIx2sPog",
            "Gone": "https://www.youtube.com/watch?v=c4YtvmD0sUU",
            "The Girls": "https://www.youtube.com/watch?v=uGzFZr5y0XE",
            "Typa Girl": "https://www.youtube.com/watch?v=6xopuvcY2GQ",
            "Lalisa": "https://www.youtube.com/watch?v=awkkyBH2zEo",
            "Ready For Love": "https://www.youtube.com/watch?v=qltR2imF2IY",
            "Forever Young": "https://www.youtube.com/watch?v=9E8h5HLF3wY",
            "Love To Hate Me": "https://www.youtube.com/watch?v=Jx3d0lZ7L0o"
        },
        "Alan Walker": {
            "Faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
            "Alone": "https://www.youtube.com/watch?v=1-xGerv5FOk",
            "Spectre": "https://www.youtube.com/watch?v=AOeY-nDp7hI",
            "Darkside": "https://www.youtube.com/watch?v=zXhDqz5l32g",
            "On My Way": "https://www.youtube.com/watch?v=6K7EmsXzqF0",
            "Sing Me to Sleep": "https://www.youtube.com/watch?v=2i2khp_npdE",
            "All Falls Down": "https://www.youtube.com/watch?v=0dxOVlgxE5Q",
            "Tired": "https://www.youtube.com/watch?v=Hz8uF5nJ2ZA",
            "Different World": "https://www.youtube.com/watch?v=ltrMfT4Qz5k",
            "Ignite": "https://www.youtube.com/watch?v=7y_9F_3En7g",
            "Heading Home": "https://www.youtube.com/watch?v=dvI8C7f_Zrg",
            "Lost Control": "https://www.youtube.com/watch?v=PO3S9DhGbYg",
            "Dreamer": "https://www.youtube.com/watch?v=RJK7M6IdOqc",
            "Unity": "https://www.youtube.com/watch?v=3lgM8u0qQ2M",
            "Paradise": "https://www.youtube.com/watch?v=5VX3lAk3l4k",
            "Routine": "https://www.youtube.com/watch?v=0Fbd2Xn4qxM",
            "End of Time": "https://www.youtube.com/watch?v=U0uR8oFQt3U",
            "Lost Control (feat. Sorana)": "https://www.youtube.com/watch?v=_2gn4Hl62d4",
            "Different World (Feat. K-391)": "https://www.youtube.com/watch?v=example1"
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

    dramas = {
        "Crash Landing on You": {
            "Episode 1": "https://www.youtube.com/watch?v=eXMjTXL2Vks",
            "Episode 2": "https://www.youtube.com/watch?v=example2",
            "Episode 3": "https://www.youtube.com/watch?v=example3",
            "Episode 4": "https://www.youtube.com/watch?v=example4"
        },
        "True Beauty": {
            "Episode 1": "https://www.youtube.com/watch?v=RHe2P8lG6bI",
            "Episode 2": "https://www.youtube.com/watch?v=example2",
            "Episode 3": "https://www.youtube.com/watch?v=example3",
            "Episode 4": "https://www.youtube.com/watch?v=example4"
        },
        "Vincenzo": {
            "Episode 1": "https://www.youtube.com/watch?v=example1",
            "Episode 2": "https://www.youtube.com/watch?v=example2",
            "Episode 3": "https://www.youtube.com/watch?v=example3",
            "Episode 4": "https://www.youtube.com/watch?v=example4"
        }
        # add more dramas/films as desired
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
        {
            "text": "BTS is trending worldwide with their latest single 'Yet to Come'!",
            "image": "https://upload.wikimedia.org/wikipedia/en/4/4c/BTS_-_Yet_to_Come.png"
        },
        {
            "text": "BTS announces new tour dates!",
            "image": "https://upload.wikimedia.org/wikipedia/commons/6/65/BTS_concert.jpg"
        },
        {
            "text": "BTS hits record views on Butter!",
            "image": "https://upload.wikimedia.org/wikipedia/en/b/b3/BTS_-_Butter.png"
        },
        {
            "text": "RM, Jin, Suga, J‑Hope, Jimin, V, Jungkook trending worldwide!",
            "image": "https://upload.wikimedia.org/wikipedia/commons/8/81/BTS_2021.png"
        }
    ]

    for update in updates:
        st.write(f"💜 {update['text']}")
        st.image(update["image"], width=300)

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
