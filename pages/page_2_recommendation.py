import streamlit as st
import pandas as pd
import os
import ast

# Fonction pour charger les recommandations
@st.cache_data
def load_recommendations():
    path = os.path.join("data", "recommendation_dataset.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        st.error("Le fichier 'recommendation_dataset.csv' est introuvable.")
        return None

# Titre de la Page 2
st.title("🎯 Résultats des Recommandations")

# Vérification de la recherche
if 'search_query' in st.session_state:
    search_query = st.session_state['search_query']
    st.write(f"**Film recherché** : {search_query}")

    # Charger les recommandations
    recommendations_df = load_recommendations()
    if recommendations_df is not None:
        # Filtrer les recommandations
        film_selected = recommendations_df[recommendations_df['title'].str.contains(search_query, case=False, na=False)]
        
        if not film_selected.empty:
            st.write("### Films Recommandés :")

            # Extraire les recommandations
            try:
                recommended_titles = ast.literal_eval(film_selected.iloc[0]['recommendations'])
            except (ValueError, SyntaxError):
                st.error("Erreur dans le format des recommandations.")
                recommended_titles = []

            # Afficher les recommandations
            for recommended_title in recommended_titles:
                recommended_film = recommendations_df[recommendations_df['title'] == recommended_title]
                if not recommended_film.empty:
                    row = recommended_film.iloc[0]
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.image(row['lien_photos'], use_container_width=True)
                    with col2:
                        st.subheader(row['title'])
                        st.write(row['overview'] if pd.notnull(row['overview']) else "Aucune description disponible.")
                        # Bouton pour aller à la Page 3
                        if st.button(f"Voir {row['title']}", key=row['title']):
                            st.session_state['selected_film'] = row.to_dict()  # Sauvegarder les détails
                            st.switch_page("pages\page_3_details.py")

  # Rediriger vers Page 3
        else:
            st.warning("Aucune recommandation trouvée.")
else:
    st.error("Aucun film recherché. Retournez à la page principale.")
