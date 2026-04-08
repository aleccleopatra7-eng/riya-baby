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

    # Full 20-song library per artist
    music_library = {
        "BTS": {
            "Dynamite": "https://www.youtube.com/watch?v=gdZLi9oWNZg",
            "Butter": "https://www.youtube.com/watch?v=WMweEpGlu_U",
            "Permission to Dance": "https://www.youtube.com/watch?v=CuklIb9d3fI",
            "Life Goes On": "https://www.youtube.com/watch?v=FgfsP5d8xv0",
            "Boy With Luv": "https://www.youtube.com/watch?v=XsX3ATc3FbA",
            "ON": "https://www.youtube.com/watch?v=bpOSxM0rNPM",
            "Fake Love": "https://www.youtube.com/watch?v=7C2z4GqqS5E",
            "Idol": "https://www.youtube.com/watch?v=pBuZEGYXA6E",
            "Spring Day": "https://www.youtube.com/watch?v=xEeFrLSkMm8",
            "Black Swan": "https://www.youtube.com/watch?v=3tmd-ClpJxA",
            "Butterfly": "https://www.youtube.com/watch?v=km3gj9WxXos",
            "Save Me": "https://www.youtube.com/watch?v=7C2z4GqqS5E",
            "I Need U": "https://www.youtube.com/watch?v=6BzF-UVF6C0",
            "Run": "https://www.youtube.com/watch?v=7C2z4GqqS5E",
            "Not Today": "https://www.youtube.com/watch?v=9DwzBICPhdM",
            "Fire": "https://www.youtube.com/watch?v=ALj5MKjy2BU",
            "Dope": "https://www.youtube.com/watch?v=B5hVxkGG32s",
            "Mic Drop": "https://www.youtube.com/watch?v=kTlv5_Bs8aw",
            "DNA": "https://www.youtube.com/watch?v=MBdVXkSdhwU",
            "Anpanman": "https://www.youtube.com/watch?v=8SbUC-UaAxE"
        },
        "Blackpink": {
            "How You Like That": "https://www.youtube.com/watch?v=ioNng23DkIM",
            "Kill This Love": "https://www.youtube.com/watch?v=2S24-y0Ij3Y",
            "Ddu-Du Ddu-Du": "https://www.youtube.com/watch?v=IHNzOHi8sJs",
            "Boombayah": "https://www.youtube.com/watch?v=bwmSjveL3Lc",
            "Lovesick Girls": "https://www.youtube.com/watch?v=dyRsYk0LyA8",
            "Pretty Savage": "https://www.youtube.com/watch?v=9Jw9RrMZrj8",
            "Forever Young": "https://www.youtube.com/watch?v=LRlR1ggh0O4",
            "Whistle": "https://www.youtube.com/watch?v=dISNgvVpWlo",
            "Playing With Fire": "https://www.youtube.com/watch?v=Amq-qlqbjYA",
            "As If It's Your Last": "https://www.youtube.com/watch?v=Amq-qlqbjYA",
            "Stay": "https://www.youtube.com/watch?v=0KxEjkS8Ixg",
            "See U Later": "https://www.youtube.com/watch?v=xTlNMmZKwpA",
            "Ice Cream": "https://www.youtube.com/watch?v=vRXZj0DzXIA",
            "Bet You Wanna": "https://www.youtube.com/watch?v=uP7QX3NmW5k",
            "Don't Know What To Do": "https://www.youtube.com/watch?v=aROsFsj0-YM",
            "Love To Hate Me": "https://www.youtube.com/watch?v=dU7mt5-0sdg",
            "You Never Know": "https://www.youtube.com/watch?v=Xe-1vE-tfqU",
            "Hope Not": "https://www.youtube.com/watch?v=3f9J2-9nMfw",
            "Lovesick Girls (Alt)": "https://www.youtube.com/watch?v=dyRsYk0LyA8",
            "Pretty Savage (Alt)": "https://www.youtube.com/watch?v=LRlR1ggh0O4"
        },
        "Alan Walker": {
            "Faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
            "Alone": "https://www.youtube.com/watch?v=1-xGerv5FOk",
            "On My Way": "https://www.youtube.com/watch?v=x6tK2S3t3Kw",
            "Darkside": "https://www.youtube.com/watch?v=bpOSxM0rNPM",
            "Sing Me to Sleep": "https://www.youtube.com/watch?v=2i2khp_npdE",
            "Tired": "https://www.youtube.com/watch?v=gOsM-DYAEhY",
            "All Falls Down": "https://www.youtube.com/watch?v=2zNSgSzhBfM",
            "The Spectre": "https://www.youtube.com/watch?v=wFM4rU6j0tI",
            "Diamond Heart": "https://www.youtube.com/watch?v=5M5C3xKf96s",
            "On My Way (feat. Sabrina Carpenter & Farruko)": "https://www.youtube.com/watch?v=5M5C3xKf96s",
            "Different World": "https://www.youtube.com/watch?v=AoRrG8CJtHg",
            "Heading Home": "https://www.youtube.com/watch?v=6K5tDeYyJQs",
            "Lost Control": "https://www.youtube.com/watch?v=V2UuUjHBqLk",
            "Paradise": "https://www.youtube.com/watch?v=2vf0j2P4ohU",
            "Routine": "https://www.youtube.com/watch?v=zS9q5iFvhb0",
            "End of Time": "https://www.youtube.com/watch?v=xy1D0T7Z0Ak",
            "Faded (Restrung)": "https://www.youtube.com/watch?v=6UQa8g1h3KI",
            "Lost Control (feat. Sorana)": "https://www.youtube.com/watch?v=V2UuUjHBqLk",
            "Alone, Pt. II": "https://www.youtube.com/watch?v=HgzGwKwLmgM",
            "Darkside (feat. Au/Ra & Tomine Harket)": "https://www.youtube.com/watch?v=bpOSxM0rNPM"
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
        "Crash Landing on You": {f"Episode {i}": f"https://www.youtube.com/watch?v=example{i}" for i in range(1, 11)},
        "True Beauty": {f"Episode {i}": f"https://www.youtube.com/watch?v=example{i}" for i in range(1, 12)},
        "Vincenzo": {f"Episode {i}": f"https://www.youtube.com/watch?v=example{i}" for i in range(1, 10)}
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

# ---------------- STORY WORLD ----------------
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

    if st.button("💾 Save Story"):
        if story_title.strip() == "" or story_text.strip() == "":
            st.warning("Please enter both a title and story text!")
        else:
            base_path = os.path.join(story_folder, story_title)
            file_path = base_path + ".txt"
            counter = 1
            while os.path.exists(file_path):
                file_path = f"{base_path}_{counter}.txt"
                counter += 1
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(story_text)
            st.success(f"Story '{story_title}' saved successfully! 💜")

    words = len(story_text.split())
    st.write(f"📝 Words: {words} | Estimated reading time: {max(1, words//200)} min")

    if st.button("💡 Give me a story prompt"):
        prompts = [
            "Your character finds a magical object in the park…",
            "A secret letter changes everything for your character…",
            "Two best friends discover a hidden world…",
            "Your main character meets someone mysterious in a storm…",
            "A journey begins in an unexpected place…"
        ]
        st.info(random.choice(prompts))

    st.subheader("Read your saved stories:")
    stories = os.listdir(story_folder)
    if stories:
        story_choice = st.selectbox("Pick a story to read", stories)
        if story_choice:
            with open(os.path.join(story_folder, story_choice), "r", encoding="utf-8") as f:
                content = f.read()
            st.markdown(f"### {story_choice.replace('.txt','')}")
            st.write(content)
    else:
        st.info("No stories saved yet. Go write one! ✨")

    # ---------------- COMIC GENERATOR ----------------
    st.subheader("🎨 Turn Your Story Into a Comic")

    if story_text.strip() != "":
        def generate_comic(story):
            lines = story.split(".")
            panels = []
            for i, line in enumerate(lines):
                if line.strip():
                    # Add random emoji per panel for fun
                    panel_emoji = random.choice(["💜","✨","🖤","💖","🌸","🎉"])
                    panels.append(f"Panel {i+1}: {line.strip()} {panel_emoji}")
            return panels

        if st.button("✨ Generate Comic Panels"):
            comic_panels = generate_comic(story_text)
            st.markdown("### 🖼️ Your Comic Panels:")
            for panel in comic_panels:
                st.info(panel)
            st.balloons()

        st.markdown("### 🎭 Optional: Make visuals later if you want:")
        st.markdown("This is now fully free inside the app — no paid site needed!")
    else:
        st.info("Write a story first to turn it into a comic 💜")

st.markdown("</div>", unsafe_allow_html=True)
