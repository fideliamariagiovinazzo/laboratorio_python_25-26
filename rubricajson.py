#
# File: Rubricajson.py
#
# Author: F. M. Giovinazzo
#
# Date: 3/07/2026
#
# Version: 2.0
#
# Description: Programma che crea e legge un file json contenente la rubrica, è presente il codice utilizzato nell'opzione dell'es3.
#

import json

# Dizionario annidato contenente i dati dei contatti della rubrica
rubrica = {
    'Paolino Paperino': {
        'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 93, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'
    },
    'Ron Weasley': {
        'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 46, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'
    },
    'Ramona Flowers': {
        'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'
    },
    'Madoka Ayukawa': {
        'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'
    }
}

# 1. Funzione per generare il file di testo rubrica.txt
def scrivi_txt(rubrica_input):
    """
    Esporta i dati della rubrica all'interno di un file di testo in formato.
    
    """
    # Apre il file in modalità scrittura ('w'); se non esiste, viene creato automaticamente
    file_rubrica = open('rubrica.txt', 'w')
    
    # Itera attraverso ogni contatto estraendo chiave (nome) e valore (dizionario dei dati)
    for nome, d in rubrica_input.items():
        # Compone una stringa formattata separando i vari campi con una virgola
        riga = f"{nome}, {d['giorno']}, {d['mese']}, {d['anno']}, {d['età']}, {d['sesso']}, {d['mail']}\n"
        # Scrive la riga all'interno del file di testo
        file_rubrica.write(riga)
        
    # Chiude il file per salvare le modifiche e rilasciare le risorse di sistema
    file_rubrica.close()
    print("File 'rubrica.txt' generato con successo!")

# 2. Funzione per creare il file JSON con la stessa struttura del dizionario
def scrivi_json(rubrica_input):
    """
    Serializza il dizionario della rubrica salvandolo in un file in formato JSON.
    
    Args:
        rubrica_input (dict): Il dizionario della rubrica da serializzare.
    """
    # Utilizza il context manager 'with' per aprire il file JSON in scrittura ('w'), 
    # garantendo la chiusura automatica del file alla fine dell'operazione
    with open('rubrica.json', 'w') as write_file:
         # Converte il dizionario Python in formato JSON e lo scrive nel file con una indentazione di 4 spazi per la leggibilità
         json.dump(rubrica_input, write_file, indent=4)
         
    print("File 'rubrica.json' generato con successo!")

# 3. Funzione per leggere la rubrica dal file JSON e visualizzarla
def leggi_json():
    """
    Legge i dati da un file JSON esistente e li carica nuovamente in un dizionario Python.
    """
    # Apre il file JSON in modalità lettura ('r') usando il context manager 'with'
    with open('rubrica.json', 'r') as in_file:
         # Carica il contenuto del file JSON convertendolo in un oggetto Python (dizionario)
         data = json.load(in_file)
         
    print("Contenuto letto dal file JSON:")
    print(data)

# Eseguiamo le funzioni per testarle
scrivi_txt(rubrica)
scrivi_json(rubrica)
leggi_json()