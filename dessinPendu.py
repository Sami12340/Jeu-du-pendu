def dessinPendu(num_image):
    """
    IN: num_image (type int) doit être compris entre 1 et 9
    OUT: une string correspondant à l'image demandé du dessin du pendu    

    """
    
    # On définit une liste de String où chacun des éléments est une chaine
    # de caractères représentant une étape du dessin complet du pendu
    
    tableau_images=[
    """
    
    
    
    
    
    ==============
    """,
    """
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    
    if num_image<1 or num_image>len(tableau_images) :
        return "Numéro d'image incorrect"
    
    else:
        return tableau_images[num_image-1]

