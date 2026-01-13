"""
Module principal de l'application, permettant l'affichage de l'interface utilisateur.
"""

import streamlit as st

from src.engine import Engine

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Caesar Cipher App",
    page_icon=":material/encrypted:",
    layout="wide"
)

# Initialisation du moteur de chiffrement
engine = Engine()

# Intialisation des sessions state pour stocker les textes
if 'plain' not in st.session_state:
    st.session_state['plain'] = ''
if 'encoded' not in st.session_state:
    st.session_state['encoded'] = ''

# Titre de l'application
st.title(
    body=":material/encrypted: Caesar Cipher App",
    text_alignment ="center"
)

# Bouton pour afficher les règles de chiffrement
with st.container(horizontal=True, horizontal_alignment="right"):
    st.button(
        label="Règles de chiffrement",
        icon=":material/policy:"
    )

# Mise en page
container = st.container(horizontal=True)

# Zone de texte clair
with container.container(border=True):
    st.subheader(
        "Texte clair",
        text_alignment ="center"
    )
    st.text_area(
        label="",
        value=st.session_state['plain'],
        key='plain',
        label_visibility="hidden"
    )

# Boutons d'encodage et de décodage
with container.container(width="content"):
    st.space(size="large")
    if st.button(
        label="Encoder",
        icon=":material/keyboard_double_arrow_right:",
        key='encode_btn'
    ):
        st.session_state['encoded'] = engine.encode_text(st.session_state.get('plain', ''))
    if st.button(
        label="Décoder",
        icon=":material/keyboard_double_arrow_left:",
        key='decode_btn'
    ):
        st.session_state['plain'] = engine.decode_text(st.session_state.get('encoded', ''))

# Zone de texte encodé
with container.container(border=True):
    st.subheader(
        "Texte encodé",
        text_alignment ="center"
    )
    st.text_area(
        label="",
        value=st.session_state['encoded'],
        key='encoded',
        label_visibility="hidden"
)
