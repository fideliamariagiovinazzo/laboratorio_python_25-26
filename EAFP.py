#
# File: impiccato_eafp.py
# Author: F. M. Giovinazzo
#
# Date: 3/07/2026
#
# Version: 3.0 
#
# Description: Progetto che fa giocare interattivamente all'impiccato gestendo gli errori in maniera EAFP.
#
import json    # Modulo per leggere/scrivere il file con l'elenco delle parole
import random  # Modulo per scegliere casualmente la parola da indovinare


# 1. Definiamo la funzione per caricare le parole e restituire direttamente la lista
def carica_parole(percorso_file):
    """Carica l'elenco delle parole disponibili da un file JSON."""
    with open(percorso_file, 'r') as in_file: 
# apre il file in lettura (si chiude automaticamente)
        data = json.load(in_file)              
# carica il contenuto JSON in un dizionario Python
    return data["parole"]                      
# restituisce solo la lista delle parole


# 2. Creiamo il file JSON con i dati iniziali
dati_iniziali = {
    "parole": ["lollipop", "impiccato", "penitente", "lilla", "fiorellino", "ecclesiastico", "parigi", "portinaia"]
}  # dizionario con la lista di parole di default usate dal gioco

with open('parole.json', 'w') as file:  
# apre (o crea/sovrascrive) il file parole.json in scrittura
    json.dump(dati_iniziali, file)      
# scrive il dizionario nel file in formato JSON


# 3. Testiamo il caricamento
parole_caricate = carica_parole('parole.json')
print("Parole caricate con successo:", parole_caricate)


def mostra_stato_eafp(parola, lettere_indovinate):
    """Costruisce la rappresentazione della parola, mostrando le lettere
       già indovinate e un trattino basso per quelle ancora nascoste."""
    stato = ''
    for lettera in parola: 
 # scorre ogni carattere della parola segreta
        try:
# Tenta di accedere alla chiave; se non esiste, solleva KeyError
            lettere_indovinate[lettera]
            stato += lettera + ' ' 
 # la lettera è nota: la mostra
        except KeyError:
            stato += '_ ' 
 # la lettera non è ancora stata indovinata: la nasconde con "_"
    return stato.strip()  
# rimuove lo spazio finale in eccesso


def gioca_eafp():
    """Avvia una partita interattiva al gioco dell'impiccato"""

    print("\nGIOCO DELL'IMPICCATO")
    try:
        parole = carica_parole('parole.json')  # tenta di caricare le parole disponibili
    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore nel caricamento del file parole.json.")
        return  
# esce dalla funzione senza avviare la partita

    try:
        parola = random.choice(parole).lower()  
# tenta di scegliere una parola casuale
    except IndexError:
# random.choice solleva IndexError se la sequenza passata è vuota
        print("La lista delle parole è vuota.")
        return  
# esce dalla funzione: non c'è nulla da far indovinare

    lettere_indovinate = {}
    tentativi_rimasti = 6
    parola_indovinata = False  
# flag che diventa True quando la parola è stata completata

    while tentativi_rimasti > 0 and not parola_indovinata:
        # continua finché ci sono tentativi e non si è vinto
        print(f"\nTentativi rimasti: {tentativi_rimasti}")
        print("Parola: ", mostra_stato_eafp(parola, lettere_indovinate))
        tentativo = input("Inserisci lettera o parola: ").lower()  # normalizza in minuscolo

       
        try:
            if not tentativo or not tentativo.isalpha():
                raise ValueError  # input vuoto o non alfabetico
        except ValueError:
            print("Inserimento non valido. Inserisci solo lettere.")
            continue  
# richiede un nuovo input senza consumare un tentativo

        if len(tentativo) == 1:
            # caso: l'utente ha inserito una singola lettera
            try:
                lettere_indovinate[tentativo]
                print("Hai già inserito questa lettera!")
            except KeyError:
                try:
                    # EAFP: se la lettera non è nella parola, index() rileva ValueError
                    parola.index(tentativo)
                    lettere_indovinate[tentativo] = True  # registra la lettera come indovinata
                    print(f"Ottimo! La lettera '{tentativo}' è presente.")
                    # Controllo se la parola è stata interamente indovinata
                    try:
                        for lettera in parola:
                            lettere_indovinate[lettera]  
# tenta di leggere ogni lettera della parola
                        parola_indovinata = True  
# se il ciclo finisce senza KeyError, sono tutte note
                    except KeyError:
                        pass  
# almeno una lettera manca ancora: la partita continua
                except ValueError:
                    tentativi_rimasti -= 1  
# lettera sbagliata: consuma un tentativo
                    print(f"La lettera '{tentativo}' non è presente.")
        else:
            # caso: l'utente ha inserito una parola intera (tentativo di più caratteri)
            try:
                if tentativo != parola:
                    raise ValueError  # parola sbagliata: solleva un'eccezione volontariamente
                lettere_indovinate = {l: True for l in parola}  # segna tutte le lettere come indovinate
                parola_indovinata = True  # la partita è vinta
            except ValueError:
                tentativi_rimasti -= 1
                print("Parola errata.")

    # Messaggio finale in base all'esito della partita
    if parola_indovinata:
        print(f"\nComplimenti! Hai indovinato la parola: {parola}")
    else:
        print(f"\nHai terminato i tentativi! La parola era: {parola}")


if __name__ == "__main__":
    gioca_eafp() 
 # avvia la partita quando lo script viene eseguito direttamente
