import streamlit as st
import pandas as pd
import os
from fuzzywuzzy import process

import streamlit as st

def afficher_films_sans_boutons(df_films, nb_colonnes=5):
    """
    Affiche les films en plusieurs lignes, nb_colonnes par ligne,
    SANS bouton (uniquement image + titre). Cette version utilise
    un conteneur HTML + classe CSS pour un rendu plus stylé.
    """
    for i in range(0, len(df_films), nb_colonnes):
        subset = df_films.iloc[i : i + nb_colonnes]
        
        # Toujours nb_colonnes (ex: 5)
        cols = st.columns(nb_colonnes)

        for j, (index, film) in enumerate(subset.iterrows()):
            with cols[j]:
                lien_photo = film.get("lien_photos", None)
                titre = film.get("title", None)

                if lien_photo:
                    # On injecte directement du HTML + classe CSS
                    st.markdown( f"""
                        <div class="custom-image">
                            <img src="{lien_photo}" alt="{titre}" />
                            <p>{titre}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.warning("Image indisponible.")


def afficher_films_avec_boutons(df_films, nb_colonnes=5, prefix="reco"):
    """
    Affiche les films en plusieurs lignes, nb_colonnes par ligne,
    AVEC un bouton. En cliquant, on stocke le film sélectionné
    dans la session et on passe en page 2.
    """
    for i in range(0, len(df_films), nb_colonnes):
        subset = df_films.iloc[i : i + nb_colonnes]
        
        cols = st.columns(nb_colonnes)
        for j, (index, film) in enumerate(subset.iterrows()):
            with cols[j]:
                lien_photo = film.get("lien_photos", None)
                titre = film.get("title", None)
                if lien_photo:
                    st.image(lien_photo, caption=titre, use_container_width=True)
                else:
                    st.warning("Image indisponible.")

                # Bouton pour aller sur la page 2
                btn_key = f"{prefix}_{i}_{j}"
                if st.button(f"Voir '{titre}'", key=btn_key):
                    st.session_state["selected_film"] = film.to_dict()
                    # Redirection vers la page 2
                    st.switch_page("pages\page_3.py")


def get_random_movies(df, count=10):
    """Retourne un échantillon aléatoire de films."""
    return df.sample(count)


def fuzzy_search(query, titles):
    """
    Recherche floue via fuzzywuzzy.process.extract.
    On ne garde que ceux dont le score >= 70.
    """
    matches = process.extract(query, titles, limit=10)
    return [m for m in matches if m[1] >= 70]


def load_css(file_name):
    """
    Charge un fichier CSS (dans un dossier 'styles' à côté).
    """
    css_path = os.path.join("styles", file_name)
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.error(f"Le fichier CSS '{file_name}' est introuvable.")

def load_movies():
    try:
        return pd.read_csv("data/recommendation_dataset.csv")  
    except FileNotFoundError:
        st.error("Le fichier de données est introuvable. Vérifiez le chemin.")
        return pd.DataFrame()
    

