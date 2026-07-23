#
# File: Impiccato_lbyl.py
#
# Author: F. M. Giovinazzo
#
# Date: 19/06/2026
#
# Version: 5.0
#
# Description: Progetto che fa giocare interattivamente all'impiccato gestendo gli errori in maniera lbyl
#
import json    
# Modulo per leggere/scrivere il file con l'elenco delle parole
import random  
# Modulo per scegliere casualmente la parola da indovinare


def carica_parole(percorso_file):
    
    """Carica l'elenco delle parole disponibili da un file JSON"""
    
    with open(percorso_file, 'r') as in_file:  
    # apre il file in lettura (context manager: si chiude da solo)
        data = json.load(in_file)              
    return data["parole"]                     
    # restituisce solo la lista delle parole
    #utilizzo percorso_file inmodo da poter riutilizzare la funzione con file diversi

dati_iniziali = {
    "parole": ["lollipop", "impiccato", "penitente", "lilla", "fiorellino", "ecclesiastico", "parigi", "portinaia"]
}  # dizionario con la lista di parole di default usate dal gioco
with open('parole.json', 'w') as file:  
    # apre (o crea se non esistente) il file parole.json in scrittura
    json.dump(dati_iniziali, file)     
    #scrive il dizionario nel file in formato JSON

# 3. Testiamo il caricamento e stampiamo il risultato fuori dalla funzione
parole_caricate = carica_parole('parole.json')  
print("Parole caricate correttamente:", parole_caricate)  
# stampa la lista caricata come controllo

def mostra_stato_lbyl(parola, lettere_indovinate):
    """
    Costruisce la rappresentazione della parola, mostrando le lettere
    già indovinate e un trattino basso per quelle ancora nascoste.
    Returns:
        str: stringa con lettere e trattini separati da spazio (es. "_ a _ a").
    """
    stato = ''
    for lettera in parola:
    # scorre ogni carattere della parola segreta
    # LBYL: controlla prima se la condizione è vera
        if lettera in lettere_indovinate:
            stato += lettera + ' '  
    # la lettera è nota: la mostra
        else:
            stato += '_ '  
    # la lettera non è ancora stata indovinata: la nasconde con "_"
    return stato.strip() 
     # rimuove lo spazio finale in eccesso

def gioca_lbyl():
    
    """Avvia una partita interattiva al gioco dell'impiccato"""
    print("\n-GIOCO DELL'IMPICCATO ")
    try:
        parole = carica_parole('parole.json')  
    # tenta di caricare le parole disponibili
    except (FileNotFoundError, json.JSONDecodeError):
        # unico punto EAFP del programma: qui si tenta l'apertura/lettura del file
        # e si gestisce l'eccezione solo se il file manca o è JSON non valido
        print("Errore nel caricamento del file parole.json.")
        return  
    # esce dalla funzione senza avviare la partita

    parola = random.choice(parole).lower()  
    # sceglie una parola casuale e la normalizza in minuscolo
    lettere_indovinate = set()  
    # insieme delle lettere indovinate correttamente finora
    tentativi_rimasti = 6      
     # numero di errori consentiti prima di perdere
    parola_indovinata = False   
    # flag che diventa True quando la parola è stata completata

    while tentativi_rimasti > 0 and not parola_indovinata:  
    # il gioco continua finché ci sono tentativi e non si è vinto
        print(f"\nTentativi rimasti: {tentativi_rimasti}")
        print("Parola: ", mostra_stato_lbyl(parola, lettere_indovinate)) 
    # mostra lo stato attuale della parola
        tentativo = input("Inserisci lettera o parola: ").lower()  
    # legge l'input e lo normalizza in minuscolo

        # LBYL: controlla prima se l'input è valido
        if len(tentativo) == 0 or not tentativo.isalpha():
            print("Inserimento non valido. Inserisci solo lettere.")
            continue  
            # richiede un nuovo input senza consumare un tentativo

        if len(tentativo) == 1:  
            # caso: l'utente ha inserito una singola lettera
            # controlla prima se la lettera è già stata inserita
            if tentativo in lettere_indovinate:
                print("Hai già inserito questa lettera!")
                continue 
             # richiede un nuovo input senza consumare un tentativo

            # controlla prima se la lettera è nella parola
            if tentativo in parola:
                lettere_indovinate.add(tentativo)  
            # registra la lettera come indovinata
                print(f"Ottimo! La lettera '{tentativo}' è presente.")
                if all(l in lettere_indovinate for l in parola): 
            # verifica se tutte le lettere sono state trovate
                    parola_indovinata = True  
            # la parola è stata indovinata
            else:
                tentativi_rimasti -= 1  
            # lettera sbagliata: consuma un tentativo
                print(f"La lettera '{tentativo}' non è presente.")
        else:  
            # caso: l'utente ha inserito una parola intera (tentativo di più caratteri)
            # controlla prima se la parola è corretta
            if tentativo == parola:
                lettere_indovinate = set(parola)  
            # segna tutte le lettere della parola come indovinate
                parola_indovinata = True      
            else:
                tentativi_rimasti -= 1  
                print("Parola errata.")

    # Messaggio finale in base all'esito della partita
    if parola_indovinata:
        print(f"\nComplimenti! Hai indovinato la parola: {parola}")
    else:
        print(f"\nHai terminato i tentativi! La parola era: {parola}")

if __name__ == "__main__":
    gioca_lbyl()  
# avvia la partita quando lo script viene eseguito direttamente
