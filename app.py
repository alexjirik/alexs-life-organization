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
        
        work_tasks = [task1, task2, task3]
        work_completed = sum(work_tasks)
        work_total = len(work_tasks)
        
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
    st.write("Write your lists below, and matching recipes will appear automatically.")
    
    # Bottom section split into store-specific lists
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Trader Joe's List")
        tj_list = st.text_area("Produce, frozen meals, snacks...", height=150, key="tj_list")
            
    with col2:
        st.subheader("Whole Foods List")
        wf_list = st.text_area("Fresh produce, bulk items...", height=150, key="wf_list")

    st.markdown("---")

    # --- DYNAMIC RECIPE LOGIC ---
    st.subheader("Dynamic Meal Inspiration")
    
    # Combine both lists and make them lowercase for easy keyword searching
    combined_cart = (tj_list + " " + wf_list).lower()
    
    # Our simple "database" of keywords and their corresponding recipes
    recipe_database = {
        "chicken": "- **Chicken Dish:** Mandarin Orange Chicken + Jasmine Rice + Broccoli\n- **Chicken Dish:** Lemon Herb Roasted Chicken",
        "gnocchi": "- **Pasta Night:** Cauliflower Gnocchi + Pesto + Chicken Sausage",
        "salmon": "- **Seafood:** Baked Miso Salmon with Asparagus\n- **Seafood:** Salmon Rice Bowl with Avocado",
        "lentils": "- **Quick Meal:** Steamed Lentils + Bruschetta Sauce + Feta (TJ's classic!)",
        "eggs": "- **Breakfast/Brunch:** Spinach and Feta Omelette\n- **Dinner:** Shakshuka with crusty bread",
        "pasta": "- **Italian:** Garlic Parmesan Pasta\n- **Italian:** Pasta Primavera with seasonal veggies",
        "tofu": "- **Plant-Based:** Crispy Tofu Stir-fry with soy sauce and ginger"
    }
    
    suggested_recipes = []
    
    # Scan the combined cart for keywords
    for ingredient, recipes in recipe_database.items():
        if ingredient in combined_cart:
            suggested_recipes.append(recipes)
            
    # Display the results
    if suggested_recipes:
        st.write("Based on your cart, you could make:")
        for recipe in suggested_recipes:
            st.markdown(recipe)
    else:
        st.info("Add items like 'chicken', 'salmon', 'gnocchi', 'pasta', or 'eggs' to your lists above to see recipe ideas!")
