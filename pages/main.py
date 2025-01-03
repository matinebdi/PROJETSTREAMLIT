import streamlit as st
from utils.fonctions import (
    load_css,
    load_movies,
    get_random_movies,
    afficher_films_sans_boutons,
    nettoyer_donnees_films
    
)

st.set_page_config(
    page_title="MovieMind",
    page_icon="🎬",
    layout="wide"
)

# Style 
st.markdown("""
<style>
.stApp {
    background-color: #141414;
}
.main-title {
    color: #E50914;
    font-size: 3.5em;
    font-weight: bold;
    text-align: center;
    margin-bottom: 0.5em;
}
.subtitle {
    color: #999;
    font-size: 1.8em;
    margin-bottom: 2em;
}
.search-container {
    max-width: 800px;
    margin: 2em auto;
}
.stTextInput > div > div {
    background-color: rgba(255,255,255,0.1);
    border: 1px solid #333;
    border-radius: 4px;
    color: white;
    font-size: 1.2em;
}
.stTextInput > div > div:focus-within {
    border-color: #E50914;
}
.movie-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1em;
    padding: 2em 0;
}
</style>
""", unsafe_allow_html=True)

load_css("style.css")

# Initialisation
if "selected_film" not in st.session_state:
    st.session_state["selected_film"] = None

# Chargement des films
movies = load_movies()


# En-tête
st.markdown('<h1 class="main-title">MovieMind</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="subtitle">Explorez vos films préférés</h3>', unsafe_allow_html=True)

# Barre de recherche
with st.container():
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    query = st.text_input("", placeholder="Rechercher un film...", key="search_input")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if query:
        st.session_state["query"] = query
        st.switch_page("pages/page_2.py")

# Films suggérés
if not query and not movies.empty:
    st.markdown('<h2 style="color: #999; margin: 1em 0;">Apercu des films disponible</h2>', unsafe_allow_html=True)
    random_movies = get_random_movies(movies, count=20)
    afficher_films_sans_boutons(random_movies)
elif movies.empty:
    st.error("Aucune donnée disponible. Vérifiez la base de données.")