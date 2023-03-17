def function2(texte) :
    assert type(texte) == str, "Ce n'est pas une chaine de caractere"
    assert len(texte) < 10, "Le texte n'est pas assez long"
    print("Voici le texte mis en parametre :")
    print(texte)
    print("Premier caractere :", texte[0])
    print("Deuxieme caractere :", texte[1])
    print("Troisieme caractere :", texte[2])
    print("Quatrieme caractere :", texte[3])
    print("Cinquieme caractere :", texte[4])
    print("Sixieme caractere :", texte[5])
    print("Premier caractere :", texte[6])
    print("Premier caractere :", texte[7])
    print("Premier caractere :", texte[8])
    print("Premier caractere :", texte[9])
    print("Premier caractere :", texte[10])