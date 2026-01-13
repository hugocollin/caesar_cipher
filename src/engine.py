"""
Module comportant le moteur de chiffrement et de déchiffrement.
"""

class Engine:
    """
    Moteur de chiffrement et de déchiffrement selon des règles spécifiques.
    """

    # Paramètres de chiffrement des voyelles
    VOWEL_MAP = {
        'A': 'O',
        'E': 'Y',
        'I': 'A',
        'O': 'E',
        'U': 'I',
        'Y': 'U'
    }

    # Paramètres de chiffrement des consonnes
    CONSONANT_MAP = {
        'B': 'G',
        'C': 'F',
        'D': 'R',
        'F': 'P',
        'G': 'T',
        'H': 'M',
        'J': 'N',
        'K': 'Q',
        'L': 'S',
        'M': 'L',
        'N': 'B',
        'P': 'C',
        'Q': 'K',
        'R': 'D',
        'S': 'V',
        'T': 'J',
        'V': 'H',
        'W': 'X', 
        'X': 'Z',
         'Z': 'W'
    }


    def __init__(self) -> None:
        """
        Initialise les tables de chiffrement et de déchiffrement.
        """
        # Combinaison des règles de chiffrement des voyelles et des consonnes
        _encode_upper = {**self.VOWEL_MAP, **self.CONSONANT_MAP}

        # Création des tables de chiffrement et de déchiffrement avec gestion de la casse
        self._encode_map = {}
        self._decode_map = {}
        for k, v in _encode_upper.items():
            self._encode_map[k] = v
            self._encode_map[k.lower()] = v.lower()
            self._decode_map[v] = k
            self._decode_map[v.lower()] = k.lower()


    def _is_consonant_letter(self, letter: str) -> bool:
        """
        Vérifie si la lettre est une consonne selon la table de chiffrement.

        Args:
            letter (str): Lettre à vérifier.

        Returns:
            bool: True si la lettre est une consonne, False sinon.
        """
        if not letter or not letter.isalpha():
            return False
        return letter.upper() in self.CONSONANT_MAP


    def encode_text(self, text: str) -> str:
        """
        Encode le texte selon les règles définies dans la table de chiffrement.

        Args:
            text (str): Texte à encoder.
        
        Returns:
            str: Texte encodé.
        """
        # Liste pour stocker les caractères encodés
        out = []

        # Stockage de la dernière lettre conservée pour détecter les consonnes doublées
        prev_kept_input = None

        # Parcours du texte à encoder
        for letter in text:
            # Traitement des lettres alphabétiques
            if letter.isalpha():
                # Vérification et suppression des consonnes doublées
                if (
                    prev_kept_input is not None
                    and letter.lower() == prev_kept_input.lower()
                    and self._is_consonant_letter(letter)
                    and self._is_consonant_letter(prev_kept_input)
                ):
                    continue

                # Encodage de la lettre
                out.append(self._encode_map.get(letter, letter))
                prev_kept_input = letter
            else:
                out.append(letter)
                prev_kept_input = None

        return ''.join(out)


    def decode_text(self, text: str) -> str:
        """
        Décode le texte selon les règles définies dans la table de chiffrement.

        Args:
            text (str): Texte à décoder.
        
        Returns:
            str: Texte décodé.
        """
        # Liste pour stocker les caractères décodés
        out = []

        # Parcours du texte à décoder
        for letter in text:
            # Traitement des lettres alphabétiques
            if letter.isalpha():
                # Décodage de la lettre
                out.append(self._decode_map.get(letter, letter))
            else:
                out.append(letter)
        return ''.join(out)
