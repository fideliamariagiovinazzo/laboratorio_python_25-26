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
import json   
 # Modulo per leggere/scrivere il file con l'elenco delle parole
import random  
# Modulo per scegliere casualmente la parola da indovinare

# 1. Definiamo la funzione per caricare le parole e restituire direttamente la lista
def carica_parole(percorso_file):
    """
    Carica l'elenco delle parole disponibili da un file JSON.

    Args:
        percorso_file (str): percorso del file JSON da leggere.

    Returns:
        list: lista delle parole contenuta nella chiave "parole" del file.
    """
    with open(percorso_file, 'r') as in_file:  
    # apre il file in lettura (si chiude automaticamente)
        data = json.load(in_file)             n'
    return data["parole"]

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
    """
    Costruisce la rappresentazione testuale della parola, mostrando le lettere
    già indovinate e un trattino basso per quelle ancora nascoste.
    Usa un approccio EAFP: tenta di leggere la chiave dal dizionario e gestisce
    l'assenza tramite KeyError, invece di controllare prima con 'in'.

    Args:
        parola (str): la parola da indovinare.
        lettere_indovinate (dict): dizionario {lettera: True} con le lettere indovinate finora.

    Returns:
        str: stringa con lettere e trattini separati da spazio (es. "_ a _ a").
    """
    stato = ''
    for lettera in parola:  
    # scorre ogni carattere della parola segreta
        try:
    # Tenta di accedere alla chiave; se non esiste, solleva KeyError-> sto cercando di accedere a una chiave inesistente
            lettere_indovinate[lettera]
            stato += lettera + ' '  
    # la lettera è nota: la mostra
        except KeyError:
            stato += '_ '  
    # la lettera non è ancora stata indovinata: la nasconde con "_"
    return stato.strip()  
    # rimuove lo spazio finale in eccesso


def gioca_eafp():
    """
    Avvia una partita interattiva al gioco dell'impiccato, gestendo gli errori
    con approccio EAFP (Easier to Ask Forgiveness than Permission): ogni
    operazione viene tentata direttamente e l'eventuale eccezione (KeyError,
    ValueError, IndexError...) viene intercettata invece di essere prevenuta
    con controlli 'if' preventivi.
    """
    print("\n GIOCO DELL'IMPICCATO")
    try:
        parole = carica_parole('parole.json')  
    # tenta di caricare le parole disponibili
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
    parola_indovinata = False   # flag che diventa True quando la parola è stata completata

    while tentativi_rimasti > 0 and not parola_indovinata: 
    # continua finché ci sono tentativi e non si è vinto
        print(f"\nTentativi rimasti: {tentativi_rimasti}")
        print("Parola: ", mostra_stato_eafp(parola, lettere_indovinate)) 
    # mostra lo stato attuale della parola
        tentativo = input("Inserisci lettera o parola: ").lower() 
    # legge l'input e lo normalizza in minuscolo

        # EAFP per la validazione dell'input
        try:
            if not tentativo or not tentativo.isalpha():
                raise ValueError  
    # input vuoto o non alfabetico: solleva un'eccezione volontariamente
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
                    # EAFP: se la lettera non è nella parola, index() solleva ValueError
                    parola.index(tentativo)
                    lettere_indovinate[tentativo] = True  
                    # registra la lettera come indovinata
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
        else:  #
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
import json    # Modulo per leggere/scrivere il file con l'elenco delle parole
import random  # Modulo per scegliere casualmente la parola da indovinare

# 1. Definiamo la funzione di caricamento usando il blocco 'with open'
def carica_parole(percorso_file):
    """
    Carica l'elenco delle parole disponibili da un file JSON
    Returns:
        list: lista delle parole contenute nella chiave "parole" del file.
    """
    with open(percorso_file, 'r') as in_file:  # apre il file in lettura (context manager: si chiude da solo)
        data = json.load(in_file)              # carica il contenuto JSON in un dizionario Python
    return data["parole"]                       # restituisce solo la lista delle parole

# 2. Creiamo il file JSON iniziale per assicurarci che esista
dati_iniziali = {
    "parole": ["lollipop", "impiccato", "penitente", "lilla", "fiorellino", "ecclesiastico", "parigi", "portinaia"]
}  # dizionario con la lista di parole di default usate dal gioco
with open('parole.json', 'w') as file:  # apre (o crea) il file parole.json in scrittura
    json.dump(dati_iniziali, file)       # scrive il dizionario nel file in formato JSON

# 3. Testiamo il caricamento e stampiamo il risultato fuori dalla funzione
parole_caricate = carica_parole('parole.json')  # richiama la funzione per verificare che il file sia leggibile
print("Parole caricate correttamente:", parole_caricate)  # stampa la lista caricata come controllo

def mostra_stato_lbyl(parola, lettere_indovinate):
    """
    Costruisce la rappresentazione testuale della parola, mostrando le lettere
    già indovinate e un trattino basso per quelle ancora nascoste.

    Args:
        parola (str): la parola da indovinare.
        lettere_indovinate (set): insieme delle lettere correttamente indovinate finora.

    Returns:
        str: stringa con lettere e trattini separati da spazio (es. "_ a _ a").
    """
    stato = ''
    for lettera in parola:  # scorre ogni carattere della parola segreta
        # LBYL: controlla prima se la condizione è vera
        if lettera in lettere_indovinate:
            stato += lettera + ' '  # la lettera è nota: la mostra
        else:
            stato += '_ '  # la lettera non è ancora stata indovinata: la nasconde con "_"
    return stato.strip()  # rimuove lo spazio finale in eccesso

def gioca_lbyl():
    """
    Avvia una partita interattiva al gioco dell'impiccato, gestendo gli errori
    con approccio LBYL (Look Before You Leap): ogni condizione a rischio viene
    verificata con un 'if' prima di agire, evitando di affidarsi a try/except
    per la logica di gioco.
    """
    print("\n--- GIOCO DELL'IMPICCATO (LBYL) ---")
    try:
        parole = carica_parole('parole.json')  # tenta di caricare le parole disponibili
    except (FileNotFoundError, json.JSONDecodeError):
        # unico punto EAFP del programma: qui si tenta l'apertura/lettura del file
        # e si gestisce l'eccezione solo se il file manca o è JSON non valido
        print("Errore nel caricamento del file parole.json.")
        return  # esce dalla funzione senza avviare la partita

    parola = random.choice(parole).lower()  # sceglie una parola casuale e la normalizza in minuscolo
    lettere_indovinate = set()  # insieme delle SOLE lettere indovinate correttamente finora
    tentativi_rimasti = 6       # numero di errori consentiti prima di perdere
    parola_indovinata = False   # flag che diventa True quando la parola è stata completata

    while tentativi_rimasti > 0 and not parola_indovinata:  # il gioco continua finché ci sono tentativi e non si è vinto
        print(f"\nTentativi rimasti: {tentativi_rimasti}")
        print("Parola: ", mostra_stato_lbyl(parola, lettere_indovinate))  # mostra lo stato attuale della parola
        tentativo = input("Inserisci lettera o parola: ").lower()  # legge l'input e lo normalizza in minuscolo

        # LBYL: controlla prima se l'input è valido
        if len(tentativo) == 0 or not tentativo.isalpha():
            print("Inserimento non valido. Inserisci solo lettere.")
            continue  # richiede un nuovo input senza consumare un tentativo

        if len(tentativo) == 1:  # caso: l'utente ha inserito una singola lettera
            # LBYL: controlla prima se la lettera è già stata inserita
            # NB: questo controllo verifica solo le lettere già indovinate CORRETTAMENTE.
            #     Una lettera già provata ma SBAGLIATA non è tracciata da nessuna parte,
            #     quindi può essere reinserita più volte, consumando un tentativo ogni volta
            #     senza ricevere l'avviso "Hai già inserito questa lettera!".
            if tentativo in lettere_indovinate:
                print("Hai già inserito questa lettera!")
                continue  # richiede un nuovo input senza consumare un tentativo

            # LBYL: controlla prima se la lettera è nella parola
            if tentativo in parola:
                lettere_indovinate.add(tentativo)  # registra la lettera come indovinata
                print(f"Ottimo! La lettera '{tentativo}' è presente.")
                if all(l in lettere_indovinate for l in parola):  # verifica se tutte le lettere sono state trovate
                    parola_indovinata = True  # la parola è stata completamente indovinata
            else:
                tentativi_rimasti -= 1  # lettera sbagliata: consuma un tentativo
                print(f"La lettera '{tentativo}' non è presente.")
        else:  # caso: l'utente ha inserito una parola intera (tentativo di più caratteri)
            # LBYL: controlla prima se la parola è corretta
            if tentativo == parola:
                lettere_indovinate = set(parola)  # segna tutte le lettere della parola come indovinate
                parola_indovinata = True           # la partita è vinta
            else:
                tentativi_rimasti -= 1  # parola sbagliata: consuma un tentativo
                print("Parola errata.")

    # Messaggio finale in base all'esito della partita
    if parola_indovinata:
        print(f"\nComplimenti! Hai indovinato la parola: {parola}")
    else:
        print(f"\nHai terminato i tentativi! La parola era: {parola}")

if __name__ == "__main__":
    gioca_lbyl()  # avvia la partita quando lo script viene eseguito direttamente

        # caso: l'utente ha inserito una parola intera (tentativo di più caratteri)
            try:
                if tentativo != parola:
                    raise ValueError 
         # parola sbagliata: solleva un'eccezione volontariamente
                lettere_indovinate = {l: True for l in parola}  
        # segna tutte le lettere come indovinate
                parola_indovinata = True 
         # la partita è vinta
            except ValueError:
                tentativi_rimasti -= 1  
                print("Parola errata.")

    # Messaggio finale in base all'esito della partita
    if parola_indovinata:
        print(f"\nComplimenti! Hai indovinato la parola: {parola}")
    else:
        print(f"\nHai terminato i tentativi! La parola era: {parola}")


if __name__ == "__main__":
    gioca_eafp()  # avvia la partita quando lo script viene eseguito direttamente
