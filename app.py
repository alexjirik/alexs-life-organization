import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="My Magical Organizer", page_icon="✨", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🔮 Navigation")
page = st.sidebar.radio("Choose your realm:", ["💼 Work Quests", "🏡 Personal Life"])

# --- MAIN PAGE CONTENT ---
st.title("✨ My Magical Organizer")
st.write("Welcome to your personal command center!")

# --- WORK PAGE ---
if page == "💼 Work Quests":
    st.header("Your Professional Spells")
    st.write("Stay focused and conquer your work tasks.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("To-Do List")
        st.checkbox("Reply to the Archmage (Manager)")
        st.checkbox("Complete project proposal")
        st.checkbox("Update the guild board (Jira/Trello)")
        
    with col2:
        st.subheader("Quick Notes")
        st.text_area("Jot down meeting notes here...", height=150)

# --- PERSONAL PAGE ---
elif page == "🏡 Personal Life":
    st.header("Your Daily Grimoire")
    st.write("Balance your magic outside of work.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Daily Chores")
        st.checkbox("Buy potion ingredients (Groceries)")
        st.checkbox("Water the magical herbs (Houseplants)")
        st.checkbox("Feed the dragon (Pet)")
        
    with col2:
        st.subheader("Journal")
        st.text_area("How are you feeling today?", height=150)
