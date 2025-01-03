import streamlit as st
import pandas as pd
from utils.fonctions import load_css, load_movies, nettoyer_donnees_films
import datetime

st.set_page_config(page_title="NetflixClone", page_icon="🎬", layout="wide")

# Style CSS
st.markdown("""
<style>
.stApp {
    background-color: #141414;
}

.movie-title {
    color: white;
    font-size: 48px;
    font-weight: bold;
    margin: 20px 0;
}

.movie-info {
    color: #999;
    font-size: 18px;
}

.movie-description {
    color: white;
    font-size: 16px;
    margin: 20px 0;
}

.category-title {
    color: white;
    font-size: 24px;
    font-weight: bold;
    margin: 20px 10px;
}

.movie-card {
    position: relative;
    transition: transform 0.3s;
    margin-bottom: 20px;
}

.movie-card:hover {
    transform: scale(1.05);
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

if "selected_film" in st.session_state and st.session_state["selected_film"]:
    film = st.session_state["selected_film"]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f'<h1 class="movie-title">{film["title"]}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p class="movie-description">{film["overview"]}</p>', unsafe_allow_html=True)
        st.markdown("")
        
        st.markdown(f"""
        <div class="movie-info">
        ⭐ Note: {film.get('note_moyenne', 0) if pd.notna(film.get('note_moyenne')) else 0}/10<br>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.write("")
        
        col_btn1, col_btn2 = st.columns([1, 2])
        with col_btn2:
            if st.button("▶️ Voir plus de détails", use_container_width=True):
                st.switch_page("pages/page_4.py")
        with col_btn1:
            st.button("+ Ma Liste", use_container_width=True, icon="❤️")
    
    with col2:
        st.image(film["lien_photos"], use_container_width=True)

    st.markdown('<p class="category-title">Films recommendés</p>', unsafe_allow_html=True)
    recommendations = eval(film.get("recommendations", "[]"))
    movies = load_movies()
    recommended_movies = movies[movies["title"].isin(recommendations)]
    
    cols = st.columns(5)
    for idx, (_, movie) in enumerate(recommended_movies.iterrows()):
        with cols[idx % 5]:
            with st.container():
                st.markdown(f"""
                    <div class="movie-card">
                        <img src="{movie['lien_photos']}" style="width: 100%; border-radius: 4px;">
                    </div>
                """, unsafe_allow_html=True)
                
                if st.button(
                    movie["title"],
                    key=f"rec_{idx}",
                    use_container_width=True
                ):
                    st.session_state["selected_film"] = movie.to_dict()
                    st.rerun()