import streamlit as st
import random
import streamlit.components.v1 as components

# --- CLEAN PAGE CONFIG ---
st.set_page_config(page_title="Flow State", page_icon="🌊", layout="wide")

# --- SUBTLE STYLING ---
# Keeps the soft, warm background tint for the sidebar
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #fcf4e3; 
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a view:", ["Work Focus", "Life Balance"])

st.sidebar.markdown("---")

# --- FOCUS MUSIC ---
st.sidebar.subheader("Acoustic Focus")
spotify_url = "https://open.spotify.com/embed/album/4vM1HNAHAnB1Hq0L98Fto3?utm_source=generator"
with st.sidebar:
    components.iframe(spotify_url, height=352)

# --- MINDFUL QUOTES ---
quotes = [
    "“Nature does not hurry, yet everything is accomplished.” – Lao Tzu",
    "“The mind is like water. When it's turbulent, it's difficult to see. When it's calm, everything becomes clear.” – Prasad Mahes",
    "“You can't stop the waves, but you can learn to surf.” – Jon Kabat-Zinn",
    "“Breath is the bridge which connects life to consciousness.” – Thich Nhat Hanh",
    "“Almost everything will work again if you unplug it for a few minutes, including you.” – Anne Lamott"
]
daily_quote = random.choice(quotes)

# --- MAIN HEADER ---
st.title("Flow State Organizer")
st.markdown(f"> *{daily_quote}*")
st.markdown("---")

# --- WORK PAGE ---
if page == "Work Focus":
    st.header("Work Focus")
    st.write("Clear your mind and tackle today's priorities.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Current Tasks")
        
        task1 = st.checkbox("Review morning emails")
        task2 = st.checkbox("Draft weekly report")
        task3 = st.checkbox("Prepare for afternoon sync")
        
        # Progress Bar Logic
        work_tasks = [task1, task2, task3]
        work_completed = sum(work_tasks)
        work_total = len(work_tasks)
        work_progress = int((work_completed / work_total) * 100)
        
        st.markdown(f"**Progress: {work_progress}%**")
        st.progress(work_progress)
        
    with col2:
        st.subheader("Brain Dump")
        st.text_area("Drop meeting notes and quick ideas here...", height=150)

# --- PERSONAL PAGE ---
elif page == "Life Balance":
    st.header("Life Balance")
    st.write("Take care of your space and your mind.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Life Admin")
        
        life_task1 = st.checkbox("Grocery run")
        life_task2 = st.checkbox("Laundry")
        life_task3 = st.checkbox("Call family")
        
        # Progress Bar Logic
        life_tasks = [life_task1, life_task2, life_task3]
        life_completed = sum(life_tasks)
        life_total = len(life_tasks)
        life_progress = int((life_completed / life_total) * 100)
        
        st.markdown(f"**Progress: {life_progress}%**")
        st.progress(life_progress)
        
    with col2:
        st.subheader("Journal")
        st.text_area("What's on your mind today?", height=150)
