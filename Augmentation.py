import pandas as pd 
import numpy as np 

def augmentation(df_data, target): 
    assert isinstance(df_data, pd.DataFrame), "Le dataframe n'est pas au bon format"
    assert isinstance(target, str), "La target n'est pas un String"
    assert target in df_data.columns
    liste_valeur = df_data.pivot_table(index = [target], aggfunc ='size')
    max_valeur = max(liste_valeur)
    
    groupes = df_data.groupby(target)
    dataframes = [groupe[1] for groupe in groupes] 
    
    df = pd.DataFrame() 
    
    for i in dataframes : 
        while i.shape[0] <= max_valeur : 
            ligne = i.sample() 
            n_ligne = ligne.copy() 
            n_ligne.index = np.arange(len(i), len(i)+1)
            i = i.append(n_ligne)
            
        df = pd.concat([df, i])
        
    df_data = df 
    
    return df_data 