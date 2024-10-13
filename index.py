import base64
import streamlit as st
from task_manager_game import Game  # Import your Game class
from calendar_comp import show_calendar
from player_status import Player

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

player_id = "player123"
player = Player(player_id)


@st.cache_data(ttl=3600)  # Cache for 1 hour (3600 seconds)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file1,png_file2):
    bin_str1 = get_base64_of_bin_file(png_file1)
    bin_str2 = get_base64_of_bin_file(png_file2)
    page_bg_img = '''
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: 
            url("data:image/png;base64,%s"),
            url("data:image/png;base64,%s");
        background-repeat: repeat, no-repeat; 
        background-size: 200px, cover; 
        background-position: left, center;
        animation: scrollDiagonalRows 10s linear infinite;
        }
    
    @keyframes scrollDiagonalRows {
      0%% { background-position: 0 0, center; }
      25%% { background-position: 50px 50px, center; }
      50%% { background-position: 100px 100px, center; }
      75%% { background-position: 50px 150px, center; }
      100%% { background-position: 0 200px, center; } 
    }

    @font-face {
        font-family: 'Orbitron-Black';
        src: url('fonts/Orbitron-Black.ttf') format('truetype'); 
    }

    @font-face {
        font-family: 'Cageroll-Cage';  /* Add a font-family name */
        src: url('fonts/Cageroll-Cage.otf') format('opentype');
    }

    h1 {{
        font-family: 'Protomo';
        text-align: center;
        color: white; 
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }}
    h2 {{
        font-family: 'KILBY', sans-serif;
        color: white; 
        text-align: center;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    }}
    
    </style>
    ''' % (bin_str1, bin_str2)  # Pass both base64 strings
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

# Call the function with both image paths
set_png_as_page_bg("IMG/Life_Quest.png", "IMG/Indieground_Holographic_Textures_01.jpg")


st.title("GAME OF LIFE")

st.markdown("<div id='home' style></div>", unsafe_allow_html=True)  # Anchor for "Home" link
# Create three columns

st.markdown('<div class="main-content">', unsafe_allow_html=True)
left_column, middle_column, right_column = st.columns(3)

# --- Left Column: Calendar/Cyborg ---
with left_column:
    st.header("Calendar")
    # Placeholder for the calendar or cyborg animation
    show_calendar()

# --- Middle Column: Tasks ---
with middle_column:
    # Create an instance of your Game class
    game = Game()

# --- Right Column: Player Status ---
with right_column:  # Assuming you have 'right_column' defined from st.columns
    st.header("Player Status")
    player_id = "player123"  # Define player_id here
    player = Player(player_id)  # Now instantiate the Player
    st.write("Points:", player.points)
    st.write("Level:", player.level)
st.markdown('</div>', unsafe_allow_html=True)

# Load CSS from file
try:
    with open('./CSS/style.css') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("CSS file not found. Please check the path.")