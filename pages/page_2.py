import re
import streamlit as st
from utils.fonctions import (
    load_css,
    load_movies,
    fuzzy_search,
    load_movies
)

st.set_page_config(
    page_title="Netflix Clone",
    page_icon="🎬",
    layout="wide"
)

# Style CSS
st.markdown("""
<style>
.stApp {
    background-color: #141414;
}

#MainMenu {
    background-color: #181818;
}

.stSidebar {
    background-color: #181818;
}

section[data-testid="stSidebar"] > div {
    background-color: #181818;
}

.movie-card {
    position: relative;
    transition: transform 0.3s;
    margin-bottom: 20px;
}

.movie-card:hover {
    transform: scale(1.05);
}

.movie-title {
    margin-top: 8px;
    color: white;
    text-align: center;
    font-size: 14px;
}

.stButton > button {
    background-color: #E50914;
    color: white;
    width: 100%;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    margin-top: 8px;
    margin-bottom: 16px;
    font-weight: 500;
}

.stButton > button:hover {
    background-color: #F40612;
}
</style>
""", unsafe_allow_html=True)

load_css("style.css")

if "selected_film" not in st.session_state:
    st.session_state["selected_film"] = None

movies = load_movies()

if "query" in st.session_state:
    query = st.session_state["query"]
    
    st.markdown("<h2>Résultats de recherche</h2>", unsafe_allow_html=True)
    st.markdown("<h4>Films correspondants à votre recherche</h4>", unsafe_allow_html=True)
    
    titles = movies["title"].tolist()
    results = fuzzy_search(query, titles)
    
    if results:
        matched_titles = [res[0] for res in results]
        matched_movies = movies[movies["title"].isin(matched_titles)]
        
        cols = st.columns(5)
        
        for idx, (_, film) in enumerate(matched_movies.iterrows()):
            col = cols[idx % 5]
            with col:
                with st.container():
                    st.markdown(f"""
                        <div class="movie-card">
                            <img src="{film['lien_photos']}" style="width: 100%; border-radius: 4px;">
                        </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(
                        film['title'],
                        key=f"btn_{idx}",
                        use_container_width=True,
                    ):
                        st.session_state["selected_film"] = film.to_dict()
                        st.switch_page("pages/page_3.py")
    else:
        st.warning("Aucun résultat trouvé pour votre recherche.")
        if st.button("Retour à la page principale"):
            st.switch_page("pages/page_1.py")
else:
    st.error("Aucune recherche détectée. Veuillez effectuer une recherche depuis la page principale.")
    if st.button("Retour à la page principale"):
        st.switch_page("pages/page_1.py")