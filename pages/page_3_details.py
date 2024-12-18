import streamlit as st

st.title("🎬 Détails du Film Sélectionné")

# Afficher les détails du film sélectionné
if 'selected_film' in st.session_state:
    film = st.session_state['selected_film']
    st.image(film['lien_photos'], caption=film['title'], use_container_width=True)
    st.subheader(film['title'])
    st.write(f"**Description :** {film['overview'] if film['overview'] else 'Aucune description disponible.'}")
else:
    st.warning("Aucun film sélectionné. Retournez à la Page 2.")
