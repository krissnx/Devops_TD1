import PySimpleGUI as sg
import pandas as pd

def charger_source(df, separateur):
    assert isinstance(df,pd.DataFrame()), "Erreur, un dataframe est requis"
    layout = [[sg.Text('Sélectionnez un fichier')],[sg.Input(key='_FILEBROWSE_'), sg.FileBrowse()],[sg.OK(), sg.Cancel('Annuler')]]
    file_window = sg.Window('File Browse', layout)
    while True:
        event, values = file_window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == 'OK':
            filepath = values['_FILEBROWSE_']
            df_input = pd.read_csv(filepath, separateur)
            if(len(df_input.columns)!=len(df.columns)):
                sg.popup('Fichier source non valide (mauvais nombre de parametres)')
                df_input = []
            file_window.close()
    return df_input

def charger_fichier(chemin_fichier, separateur):
    df = pd.read_csv(chemin_fichier, separateur)
    df = df.fillna(" ")
    events = []
    events_entrer = []
    column_names = df.columns.tolist()
    layout = [[sg.Text(column_names[i]), sg.InputText(key=i)] for i in range(len(column_names))]
    layout.append([sg.Button('Entrer', key="enter_"+chemin_fichier), sg.Button('Choisir fichier source', key= 'key_' + chemin_fichier)])
    events.append('key_'+chemin_fichier)
    events_entrer.append("enter_"+chemin_fichier)
    
    layout = [[sg.Column(layout, scrollable=True, vertical_scroll_only=True)]]
    return df, layout, events, events_entrer