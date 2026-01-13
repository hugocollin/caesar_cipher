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

def handle_encode():
    """
    Gère l'encodage du texte clair en texte encodé.
    """
    st.session_state['encoded'] = engine.encode_text(st.session_state['plain'])

def handle_decode():
    """
    Gère le décodage du texte encodé en texte clair.
    """
    st.session_state['plain'] = engine.decode_text(st.session_state['encoded'])

@st.dialog(title="Règles de chiffrement")
def display_encryption_rules():
    """
    Affiche les règles de chiffrement.
    """
    # Affichage des règles de chiffrement des voyelles
    st.subheader("Voyelles :")

    vowel_container = st.container(horizontal=True)

    # Parcours de la liste des voyelles pour créer un conteneur par règle
    for original, change in engine.VOWEL_MAP.items():
        with vowel_container.container(border=True):
            st.subheader(
                body=f"{original} :material/arrow_forward: {change}",
                text_alignment ="center"
            )

    # Affichage des règles de chiffrement des consonnes
    st.subheader("Consonnes :")

    consonant_container = st.container(horizontal=True)

    # Parcours de la liste des consonnes pour créer un conteneur par règle
    for original, change in engine.CONSONANT_MAP.items():
        with consonant_container.container(border=True):
            st.subheader(
                body=f"{original} :material/arrow_forward: {change}",
                text_alignment ="center"
            )

    # Affichage de la règle spéciale pour les consonnes doublées
    st.subheader("Règle spéciale :")
    st.info(
        body=(
            "Lorsque deux consonnes identiques se suivent, "
            "la seconde est supprimée lors de l'encodage."
        ),
        icon=":material/info:"
    )

# Titre de l'application
st.title(
    body=":material/encrypted: Caesar Cipher App",
    text_alignment ="center"
)

# Bouton pour afficher les règles de chiffrement
with st.container(horizontal=True, horizontal_alignment="right"):
    st.button(
        label="Règles de chiffrement",
        icon=":material/policy:",
        on_click=display_encryption_rules,
        help="Affiche les règles de chiffrement"
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
        key='plain',
        label_visibility="hidden"
    )

# Boutons d'encodage et de décodage
with container.container(width="content"):
    st.space(size="large")
    st.button(
        label="Encoder",
        icon=":material/keyboard_double_arrow_right:",
        key='encode_btn',
        on_click=handle_encode,
        help="Transforme le texte clair en texte encodé"
    )
    st.button(
        label="Décoder",
        icon=":material/keyboard_double_arrow_left:",
        key='decode_btn',
        on_click=handle_decode,
        help="Transforme le texte encodé en texte clair"
    )

# Zone de texte encodé
with container.container(border=True):
    st.subheader(
        "Texte encodé",
        text_alignment ="center"
    )
    st.text_area(
        label="",
        key='encoded',
        label_visibility="hidden"
)
