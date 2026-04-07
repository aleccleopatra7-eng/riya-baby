import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Riya's Creative Space", layout="wide")

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

# ---------------- SIDEBAR MENU ----------------
menu = st.sidebar.radio("✨ Explore", [
    "Home",
    "Music 🎵",
    "K-Drama 🎬",
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
    st.subheader("🎧 BTS Music Zone 💜")
    st.write("Enjoy some BTS music!")

    # Example: Dynamite YouTube embed
    st.video("https://www.youtube.com/watch?v=gdZLi9oWNZg")

    # Optional: let her add other songs
    song = st.text_input("Paste another YouTube song link if you want:")
    if song:
        st.video(song)

# ---------------- K-DRAMA ----------------
elif menu == "K-Drama 🎬":
    st.subheader("🍿 K-Drama Lounge 💜")
    st.write("Click a drama to watch its trailer or clip:")

    drama_choice = st.selectbox(
        "Select a drama",
        ["Crash Landing on You", "True Beauty", "All of Us Are Dead"]
    )

    if drama_choice == "Crash Landing on You":
        st.video("https://www.youtube.com/watch?v=eXMjTXL2Vks")  # Trailer
    elif drama_choice == "True Beauty":
        st.video("https://www.youtube.com/watch?v=RHe2P8lG6bI")  # Trailer
    elif drama_choice == "All of Us Are Dead":
        st.video("https://www.youtube.com/watch?v=IN5TD4VRcSM")  # Trailer

    st.write("💜 You can watch full episodes on Netflix or Viki!")

# ---------------- MESSAGE ----------------
elif menu == "Message 💌":
    st.subheader("💌 A Special Message For You 💌")
    messages = [
        "You make everything brighter 💜",
        "Keep smiling 😊",
        "This space is yours ✨",
        "You are special and appreciated 🖤"
    ]
    st.write(random.choice(messages))

    if st.button("🎁 Reveal Surprise"):
        st.success("You matter a lot! 💜")
        st.balloons()