import streamlit as st
import pandas as pd
from utils.fonctions import load_css

st.set_page_config(
    page_title="Netflix Clone - Connexion",
    page_icon="🎬",
    layout="wide"
)

# Style pour la page de connexion
st.markdown("""
<style>
.stApp {
    background-color: #141414;
    background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), url('https://assets.nflxext.com/ffe/siteui/vlv3/fc164b4b-f085-44ee-bb7f-ec7df8539eff/d23a1608-7d90-4da1-93d6-bae2fe60a69b/FR-fr-20230814-popsignuptwoweeks-perspective_alpha_website_large.jpg');
    background-size: cover;
    background-position: center;
}

.login-container {
    max-width: 450px;
    margin: 40px auto;
    padding: 60px 68px 40px;
    background-color: rgba(0, 0, 0, 0.75);
    border-radius: 4px;
    box-sizing: border-box;
}

.login-title {
    color: white;
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 28px;
}

.stTextInput > div > div {
    background-color: #333;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 16px 20px;
    margin-bottom: 16px;
}

.stTextInput > div > div:focus {
    outline: none;
    background-color: #454545;
}

.stButton > button {
    background-color: #E50914;
    color: white;
    padding: 16px;
    font-size: 16px;
    font-weight: 500;
    border: none;
    border-radius: 4px;
    width: 100%;
    margin-top: 24px;
    cursor: pointer;
}

.stButton > button:hover {
    background-color: #F40612;
}

.login-text {
    color: #737373;
    font-size: 16px;
    margin-top: 16px;
}

.login-link {
    color: white;
    text-decoration: none;
}

.login-link:hover {
    text-decoration: underline;
}

.error-message {
    color: #E50914;
    padding: 10px;
    margin-bottom: 16px;
    font-size: 14px;
}

.divider {
    border-top: 1px solid #737373;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# Initialisation des variables de session
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login(username, password):

    if username == "admin" and password == "admin":
        st.session_state['logged_in'] = True
        st.session_state['username'] = username
        return True
    return False

def main():
    # Container principal
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        

        
        st.markdown('<h1 class="login-title">Connexion</h1>', unsafe_allow_html=True)
        
        # Formulaire de connexion
        with st.form("login_form"):
            email = st.text_input("Email", placeholder="Email ou numéro de téléphone")
            password = st.text_input("Mot de passe", type="password", placeholder="Mot de passe")
            
            if st.form_submit_button("Se connecter"):
                if login(email, password):
                    st.success("Connexion réussie!")
                    st.switch_page("pages/main.py")
                else:
                    st.markdown("""
                        <div class="error-message">
                            Désolé, nous ne trouvons pas de compte avec cette adresse email. 
                            Veuillez réessayer ou créer un nouveau compte.
                        </div>
                    """, unsafe_allow_html=True)
        
        # Liens supplémentaires
        st.markdown("""
            <div class="login-text">
                Première visite sur MovieMind ? 
                <a href="#" class="login-link">Inscrivez-vous</a>
            </div>
            
            <div class="divider"></div>
            
            <div class="login-text">
                Cette page est protégée par Google reCAPTCHA pour nous assurer que vous n'êtes pas un robot.
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    if not st.session_state['logged_in']:
        main()
    else:
        st.switch_page("login.py")