import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Système de Recommandation", layout="wide")
st.title("🎥 Système de Recommandation de Films")

# Barre de recherche pour entrer un titre de film
search_query = st.text_input("🔍 Entrez le titre d'un film pour commencer :", "")

# Bouton pour naviguer vers la Page 2
if search_query:
    st.session_state['search_query'] = search_query
    st.write(f"**Film recherché** : {search_query}")
    # Bouton pour changer de page
    if st.button("Voir les recommandations 🚀"):
        st.switch_page("pages\page_2_recommendation.py")
