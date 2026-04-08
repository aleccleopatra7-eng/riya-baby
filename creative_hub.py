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

    # --- COMIC GENERATOR ---
    st.subheader("🎨 Turn Your Story Into a Comic with Visuals")

    if story_text.strip() != "":
        def generate_comic_images(story):
            lines = [line.strip() for line in story.split(".") if line.strip()]
            images = []
            for i, line in enumerate(lines):
                img = Image.new('RGB', (600, 400), color=random.choice(["#f8f0ff", "#fff0f8", "#f0f0f8", "#ffffff"]))
                draw = ImageDraw.Draw(img)
                font = ImageFont.load_default()
                draw.text((10, 10), f"Panel {i+1}", fill="black", font=font)
                draw.text((10, 50), line, fill="black", font=font)
                draw.text((10, 300), random.choice(["💜","✨","🖤","💖","🌸","🎉"]), fill="purple", font=font)
                images.append(img)
            return images

        if st.button("✨ Generate Comic Images"):
            comic_images = generate_comic_images(story_text)
            st.markdown("### 🖼️ Your Comic Panels:")
            for idx, img in enumerate(comic_images):
                st.image(img, caption=f"Panel {idx+1}", use_column_width=True)

            pdf_bytes = BytesIO()
            comic_images[0].save(pdf_bytes, format="PDF", save_all=True, append_images=comic_images[1:])
            pdf_bytes.seek(0)
            st.download_button("📥 Download Comic as PDF", data=pdf_bytes, file_name=f"{story_title}.pdf", mime="application/pdf")
    else:
        st.info("Write a story first to turn it into a comic 💜")

st.markdown("</div>", unsafe_allow_html=True)
