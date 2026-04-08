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

<div class="heart" style="left:10%;">💜</div>
<div class="heart" style="left:30%; animation-delay:1s;">💜</div>
<div class="heart" style="left:50%; animation-delay:2s;">💜</div>
<div class="heart" style="left:70%; animation-delay:3s;">💜</div>
<div class="heart" style="left:90%; animation-delay:4s;">💜</div>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center; color:#d8b4ff;'>Welcome, Riya Smiley! 💜</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>May our friendship last forever 💖</h3>", unsafe_allow_html=True)

# ---------------- STORY FOLDER ----------------
story_folder = "riya_stories"
if not os.path.exists(story_folder):
    os.makedirs(story_folder)

# ---------------- SIDEBAR ----------------
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

    music_library = {
        "BTS": {
            "Dynamite": "https://www.youtube.com/watch?v=gdZLi9oWNZg",
            "Butter": "https://www.youtube.com/watch?v=WMweEpGlu_U",
            "Permission to Dance": "https://www.youtube.com/watch?v=CuklIb9d3fI",
            "Boy With Luv": "https://www.youtube.com/watch?v=XsX3ATc3FbA",
            "Fake Love": "https://www.youtube.com/watch?v=7C2z4GqqS5E",
            "DNA": "https://www.youtube.com/watch?v=MBdVXkSdhwU",
            "Idol": "https://www.youtube.com/watch?v=pBuZEGYXA6E",
            "Fire": "https://www.youtube.com/watch?v=ALj5MKjy2BU",
            "Dope": "https://www.youtube.com/watch?v=B5hVxkGG32s",
            "Spring Day": "https://www.youtube.com/watch?v=xEeFrLSkMm8",
            "Black Swan": "https://www.youtube.com/watch?v=0lapF4DQPKQ",
            "Mic Drop": "https://www.youtube.com/watch?v=kTlv5_Bs8aw",
            "Save Me": "https://www.youtube.com/watch?v=GZjt_sA2eso",
            "Run": "https://www.youtube.com/watch?v=wKysONrSmew",
            "I Need U": "https://www.youtube.com/watch?v=nmjdaBaZe8Y",
            "Not Today": "https://www.youtube.com/watch?v=9DwzBICPhdM",
            "On": "https://www.youtube.com/watch?v=gwMa6gpoE9I",
            "Life Goes On": "https://www.youtube.com/watch?v=-5q5mZbe3V8",
            "Yet To Come": "https://www.youtube.com/watch?v=kXpOEzNZ8hQ",
            "Anpanman": "https://www.youtube.com/watch?v=8SbUC-UaAxE"
        },
        "Blackpink": {
            "How You Like That": "https://www.youtube.com/watch?v=ioNng23DkIM",
            "Kill This Love": "https://www.youtube.com/watch?v=2S24-y0Ij3Y",
            "Ddu-Du Ddu-Du": "https://www.youtube.com/watch?v=IHNzOHi8sJs",
            "Boombayah": "https://www.youtube.com/watch?v=bwmSjveL3Lc",
            "Lovesick Girls": "https://www.youtube.com/watch?v=dyRsYk0LyA8",
            "Pink Venom": "https://www.youtube.com/watch?v=gQlMMD8auMs",
            "Ice Cream": "https://www.youtube.com/watch?v=vRXZj0DzXIA",
            "Pretty Savage": "https://www.youtube.com/watch?v=9Jw9RrMZrj8",
            "Forever Young": "https://www.youtube.com/watch?v=7PrxONon7jg",
            "Whistle": "https://www.youtube.com/watch?v=dISNgvVpWlo",
            "Playing With Fire": "https://www.youtube.com/watch?v=Amq-qlqbjYA",
            "Stay": "https://www.youtube.com/watch?v=FzVR_fymZw4",
            "As If It's Your Last": "https://www.youtube.com/watch?v=Amq-qlqbjYA",
            "You Never Know": "https://www.youtube.com/watch?v=4Kk_iaaHd_Y",
            "Love To Hate Me": "https://www.youtube.com/watch?v=wlzGXcTzdzU",
            "Bet You Wanna": "https://www.youtube.com/watch?v=gXBdvSj9F2I",
            "See U Later": "https://www.youtube.com/watch?v=1o7h6qV-3XU",
            "Hope Not": "https://www.youtube.com/watch?v=l6zMnMMzsss",
            "Really": "https://www.youtube.com/watch?v=He322O1JWgU",
            "Kick It": "https://www.youtube.com/watch?v=sYUlykDe4as"
        },
        "Alan Walker": {
            "Faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
            "Alone": "https://www.youtube.com/watch?v=1-xGerv5FOk",
            "The Spectre": "https://www.youtube.com/watch?v=wJnBTPUQS5A",
            "On My Way": "https://www.youtube.com/watch?v=x6tK2S3t3Kw",
            "Darkside": "https://www.youtube.com/watch?v=bpOSxM0rNPM",
            "Sing Me To Sleep": "https://www.youtube.com/watch?v=2i2khp_npdE",
            "Tired": "https://www.youtube.com/watch?v=gOsM-DYAEhY",
            "All Falls Down": "https://www.youtube.com/watch?v=2zNSgSzhBfM",
            "Diamond Heart": "https://www.youtube.com/watch?v=5M5C3xKf96s",
            "Different World": "https://www.youtube.com/watch?v=AoRrG8CJtHg",
            "Heading Home": "https://www.youtube.com/watch?v=6K5tDeYyJQs",
            "Lost Control": "https://www.youtube.com/watch?v=V2UuUjHBqLk",
            "Paradise": "https://www.youtube.com/watch?v=2vf0j2P4ohU",
            "Routine": "https://www.youtube.com/watch?v=zS9q5iFvhb0",
            "End of Time": "https://www.youtube.com/watch?v=xy1D0T7Z0Ak",
            "Alone Pt II": "https://www.youtube.com/watch?v=HgzGwKwLmgM",
            "Force": "https://www.youtube.com/watch?v=NLZRYQMLDW4",
            "Sky": "https://www.youtube.com/watch?v=QpYk2Q9tR9M",
            "Unity": "https://www.youtube.com/watch?v=E3x_dLVTEuA"
        }
    }

    artist = st.selectbox("Pick an artist", list(music_library.keys()))
    for song, link in music_library[artist].items():
        st.markdown(f"[{song}]({link})")

# ---------------- STORY WORLD ----------------
elif menu == "Story World ✍️":
    st.subheader("Create your story 💜")

    story_title = st.text_input("Title")
    story_text = st.text_area("Write your story")

    if st.button("💾 Save"):
        with open(os.path.join(story_folder, story_title + ".txt"), "w", encoding="utf-8") as f:
            f.write(story_text)
        st.success("Saved 💜")

    def generate_comic(story):
        lines = [l.strip() for l in story.split(".") if l.strip()]
        imgs = []

        for i, line in enumerate(lines):
            img = Image.new("RGB", (600,400), color="#f8c8dc")
            draw = ImageDraw.Draw(img)

            try:
                font = ImageFont.truetype("arial.ttf", 24)
            except:
                font = ImageFont.load_default()

            # speech bubble
            draw.rectangle([50,80,550,250], fill="white", outline="black", width=3)

            # wrap text
            wrapped = "\n".join([line[i:i+30] for i in range(0,len(line),30)])

            draw.text((70,100), wrapped, fill="black", font=font)

            # panel title
            draw.text((20,20), f"Panel {i+1}", fill="black", font=font)

            imgs.append(img)

        return imgs

    if st.button("🎨 Generate Comic"):
        imgs = generate_comic(story_text)

        for i, img in enumerate(imgs):
            st.image(img, caption=f"Panel {i+1}")

        buf = BytesIO()
        imgs[0].save(buf, format="PDF", save_all=True, append_images=imgs[1:])
        st.download_button("📥 Download Comic", buf.getvalue(), file_name="comic.pdf")
