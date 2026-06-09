import streamlit as st
import random
import streamlit.components.v1 as components

# --- BEACH VIBES PAGE CONFIG ---
st.set_page_config(page_title="My Beach Organizer", page_icon="🌴", layout="wide")

# --- CUSTOM CSS FOR EXTRA SUNSHINE ---
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
st.sidebar.subheader("🎧 Jack Johnson Vibes")
spotify_url = "https://open.spotify.com/embed/album/4vM1HNAHAnB1Hq0L98Fto3?utm_source=generator"
with st.sidebar:
    components.iframe(spotify_url, height=352)

# --- QUOTES OF THE DAY ---
quotes = [
    "“You can't stop the waves, but you can learn to surf.” – Jon Kabat-Zinn",
    "“The ocean stirs the heart, inspires the imagination and brings eternal joy to the soul.” – Wyland",
    "“Smell the sea and feel the sky. Let your soul and spirit fly.” – Van Morrison",
    "“To escape and sit quietly on the beach — that's my idea of paradise.” – Emilia Wickstead",
    "“Live in the sunshine, swim the sea, drink the wild air.” – Ralph Waldo Emerson"
]
daily_quote = random.choice(quotes)

# --- MAIN HEADER ---
st.title("🌊 The Flow State Organizer")
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
        
        # We assign checkboxes to variables so Python can track them
        task1 = st.checkbox("Send out morning emails")
        task2 = st.checkbox("Finish the weekly report")
        task3 = st.checkbox("Prep for the afternoon sync")
        
        # --- WAVE PROGRESS BAR LOGIC ---
        work_tasks = [task1, task2, task3]
        work_completed = sum(work_tasks) # Counts how many are True (checked)
        work_total = len(work_tasks)
        work_progress = int((work_completed / work_total) * 100) # Calculates the percentage
        
        st.markdown(f"**Swell Size: {work_progress}%** 🌊")
        st.progress(work_progress)
        
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
        
        life_task1 = st.checkbox("Grab fresh fruit from the market")
        life_task2 = st.checkbox("Do the laundry")
        life_task3 = st.checkbox("Call the fam")
        
        # --- WAVE PROGRESS BAR LOGIC ---
        life_tasks = [life_task1, life_task2, life_task3]
        life_completed = sum(life_tasks)
        life_total = len(life_tasks)
        life_progress = int((life_completed / life_total) * 100)
        
        st.markdown(f"**Island Chill Level: {life_progress}%** 🌴")
        st.progress(life_progress)
        
    with col2:
        st.subheader("☀️ Sunset Journal")
        st.text_area("What are you grateful for today?", height=150)
