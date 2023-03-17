from methodes import charger_fichier, charger_source

chemin_fichier = "test.csv"
fichier_non="non_csv.txt"
separateur = ','

#Erreurs
df, layout, l1, l2 = charger_fichier(12, separateur)
df, layout, l1, l2 = charger_fichier(chemin_fichier, 12)
df, layout, l1, l2 = charger_fichier(-1, 12)
df, layout, l1, l2 = charger_fichier(fichier_non, separateur)
df_input = charger_source(df, 43)
df_input = charger_source(21, separateur)
df_input = charger_source(21, -1)
    
#Bonne utilisation
df, layout, l1, l2 = charger_fichier(chemin_fichier, separateur)
df_input = charger_source(df, separateur) 