import streamlit as st
import random

# --- CLEAN PAGE CONFIG ---
st.set_page_config(page_title="Flow State", page_icon="🌊", layout="wide")

# --- SUBTLE STYLING ---
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #fcf4e3; 
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a view:", ["Work Focus", "Life Balance", "Groceries & Recipes"])

st.sidebar.markdown("---")

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
        
        # Avoid division by zero if list is empty
        if work_total > 0:
            work_progress = int((work_completed / work_total) * 100)
        else:
            work_progress = 0
            
        st.markdown(f"**Progress: {work_progress}%**")
        st.progress(work_progress)
        
    with col2:
        st.subheader("Brain Dump")
        st.text_area("Drop meeting notes and quick ideas here...", height=150, key="work_notes")

# --- PERSONAL PAGE ---
elif page == "Life Balance":
    st.header("Life Balance")
    st.write("Take care of your space and your mind.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Life Admin")
        
        life_task1 = st.checkbox("Pay utility bills")
        life_task2 = st.checkbox("Laundry")
        life_task3 = st.checkbox("Call family")
        
        # Progress Bar Logic
        life_tasks = [life_task1, life_task2, life_task3]
        life_completed = sum(life_tasks)
        life_total = len(life_tasks)
        
        if life_total > 0:
            life_progress = int((life_completed / life_total) * 100)
        else:
            life_progress = 0
            
        st.markdown(f"**Progress: {life_progress}%**")
        st.progress(life_progress)
        
    with col2:
        st.subheader("Journal")
        st.text_area("What's on your mind today?", height=150, key="life_journal")

# --- GROCERIES & RECIPES PAGE ---
elif page == "Groceries & Recipes":
    st.header("Groceries & Recipes")
    st.write("Plan your meals and organize your store runs.")
    
    # Top section for meal planning
    st.subheader("Weekly Meal Plan & Recipe Ideas")
    st.text_area("Write down your recipe ideas for the week here...", height=100, key="meal_plan")
    
    st.markdown("---")
    
    # Bottom section split into store-specific lists
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Trader Joe's List")
        st.text_area("Produce, frozen meals, snacks...", height=200, key="tj_list")
        
        # A helpful expander with ideas
        with st.expander("TJ's Quick Meal Inspo"):
            st.markdown("- Cauliflower Gnocchi + Pesto + Chicken Sausage")
            st.markdown("- Mandarin Orange Chicken + Jasmine Rice + Broccoli")
            st.markdown("- Steamed Lentils + Bruschetta Sauce + Feta")
            
    with col2:
        st.subheader("Whole Foods List")
        st.text_area("Fresh produce, bulk items, specialty ingredients...", height=200, key="wf_list")
        
        # A helpful expander with ideas
        with st.expander("Whole Foods Inspo"):
            st.markdown("- Hot bar items for a quick lunch")
            st.markdown("- 365 brand organic pantry staples")
            st.markdown("- Fresh salmon or meat from the counter")
