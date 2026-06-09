import streamlit as st
import random
import streamlit.components.v1 as components

# --- BEACH VIBES PAGE CONFIG ---
st.set_page_config(page_title="My Beach Organizer", page_icon="🌴", layout="wide")

# --- CUSTOM CSS FOR EXTRA SUNSHINE ---
# This adds a soft, sandy background tint to the sidebar
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #fcf4e3; 
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR COMPASS ---
st.sidebar.title("🧭 The Surf Report")
page = st.sidebar.radio("Where are we paddling out to?", ["💻 The Daily Grind", "🥥 Island Time"])

st.sidebar.markdown("---")

# --- THE BOOMBOX (SPOTIFY EMBED) ---
st.sidebar.subheader("🎧 Jack Johnson Radio")
# Swapped to Jack Johnson vibes!
spotify_url = "https://open.spotify.com/embed/playlist/37i9dQZF1DZ06evO146hI7?utm_source=generator&theme=0"
with st.sidebar:
    components.iframe(spotify_url, height=352)

# --- QUOTES OF THE DAY ---
# Here is our stash of good vibes!
quotes = [
    "“You can't stop the waves, but you can learn to surf.” – Jon Kabat-Zinn",
    "“The ocean stirs the heart, inspires the imagination and brings eternal joy to the soul.” – Wyland",
    "“Smell the sea and feel the sky. Let your soul and spirit fly.” – Van Morrison",
    "“To escape and sit quietly on the beach — that's my idea of paradise.” – Emilia Wickstead",
    "“Live in the sunshine, swim the sea, drink the wild air.” – Ralph Waldo Emerson"
]
# This picks a random quote from our stash every time the page loads
daily_quote = random.choice(quotes)

# --- MAIN HEADER ---
st.title("🌊 The Flow State Organizer")

# The Quote of the Day section! 
st.markdown(f"> **{daily_quote}** 🐚")

st.write("Catch the good vibes and stay on top of your wave.")

st.markdown("---")

# --- WORK PAGE ---
if page == "💻 The Daily Grind":
    st.header("Tackling the Big Kahunas 🏄‍♀️")
    st.write("Keep your balance. Let's crush these work tasks so you can log off and chill!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 The Lineup (To-Do)")
        st.checkbox("Send out morning emails")
        st.checkbox("Finish the weekly report")
        st.checkbox("Prep for the afternoon sync")
        
    with col2:
        st.subheader("🐚 Message in a Bottle (Notes)")
        st.text_area("Drop your brilliant ideas and meeting notes right here...", height=150)

# --- PERSONAL PAGE ---
elif page == "🥥 Island Time":
    st.header("High Tides & Good Vibes 🌺")
    st.write("Time to nurture your personal life and soak up the sun.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🛒 Shore Leave (Chores)")
        st.checkbox("Grab fresh fruit from the market")
        st.checkbox("Do the laundry")
        st.checkbox("Call the fam")
        
    with col2:
        st.subheader("☀️ Sunset Journal")
        st.text_area("What are you grateful for today?", height=150)
