def saisir_valeur(n: int) -> list:
    """Saisit n valeurs à partir de l'entrée standard et les retourne sous forme de liste de chaînes."""

    valeurs = []

    for i in range(n):
        valeur = input(f"Valeur {i+1}: ")

        try:
            float(valeur)
        except ValueError:
            raise ValueError("La valeur doit être un nombre.")

        valeurs.append(valeur)

    return valeurs


def afficher_csv(csv_data: list):
    """Affiche les données CSV sous forme de tableau avec des bordures."""

    # Calculer la largeur de chaque colonne
    column_widths = [max(len(str(data_item)) for data_item in column) for column in zip(*csv_data)]

    # Afficher les en-têtes de colonne
    headers = [str(header).ljust(column_widths[i]) for i, header in enumerate(csv_data[0])]
    print("|".join(headers))

    # Afficher les bordures de la table
    border = "|".join(['-' * width for width in column_widths])
    print(border)

    # Afficher les données
    for row in csv_data[1:]:
        row_data = [str(data_item).ljust(column_widths[i]) for i, data_item in enumerate(row)]
        print("|".join(row_data))