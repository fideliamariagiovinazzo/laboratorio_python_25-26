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
    """
    Carica l'elenco delle parole disponibili da un file JSON.

    Args:
        percorso_file (str): percorso del file JSON da leggere.

    Returns:
        list: lista delle parole contenuta nella chiave "parole" del file.
    """
    with open(percorso_file, 'r') as in_file:  # apre il file in lettura (si chiude automaticamente)
        data = json.load(in_file)              # carica il contenuto JSON in un dizionario Python
    # Restituiamo direttamente la lista delle parole contenuta nella chiave 'parole'
    return data["parole"]

# 2. Creiamo il file JSON con i dati iniziali
dati_iniziali = {
    "parole": ["lollipop", "impiccato", "penitente", "lilla", "fiorellino", "ecclesiastico", "parigi", "portinaia"]
}  # dizionario con la lista di parole di default usate dal gioco

with open('parole.json', 'w') as file:  # apre (o crea/sovrascrive) il file parole.json in scrittura
    json.dump(dati_iniziali, file)       # scrive il dizionario nel file in formato JSON

# 3. Testiamo il caricamento
parole_caricate = carica_parole('parole.json')  # richiama la funzione per verificare che il file sia leggibile
print("Parole caricate con successo:", parole_caricate)  # stampa la lista caricata come controllo


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
    for lettera in parola:  # scorre ogni carattere della parola segreta
        try:
            # Tenta di accedere alla chiave; se non esiste, solleva KeyError
            lettere_indovinate[lettera]
            stato += lettera + ' '  # la lettera è nota: la mostra
        except KeyError:
            stato += '_ '  # la lettera non è ancora stata indovinata: la nasconde con "_"
    return stato.strip()  # rimuove lo spazio finale in eccesso


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
        parole = carica_parole('parole.json')  # tenta di caricare le parole disponibili
    except (FileNotFoundError, json.JSONDecodeError):
        print("Errore nel caricamento del file parole.json.")
        return  # esce dalla funzione senza avviare la partita

    try:
        parola = random.choice(parole).lower()  # tenta di scegliere una parola casuale
    except IndexError:
        # random.choice solleva IndexError se la sequenza passata è vuota
        print("La lista delle parole è vuota.")
        return  # esce dalla funzione: non c'è nulla da far indovinare

    lettere_indovinate = {}     # dizionario delle SOLE lettere indovinate correttamente finora
    tentativi_rimasti = 6       # numero di errori consentiti prima di perdere
    parola_indovinata = False   # flag che diventa True quando la parola è stata completata

    while tentativi_rimasti > 0 and not parola_indovinata:  # continua finché ci sono tentativi e non si è vinto
        print(f"\nTentativi rimasti: {tentativi_rimasti}")
        print("Parola: ", mostra_stato_eafp(parola, lettere_indovinate))  # mostra lo stato attuale della parola
        tentativo = input("Inserisci lettera o parola: ").lower()  # legge l'input e lo normalizza in minuscolo

        # EAFP per la validazione dell'input
        try:
            if not tentativo or not tentativo.isalpha():
                raise ValueError  # input vuoto o non alfabetico: solleva un'eccezione volontariamente
        except ValueError:
            print("Inserimento non valido. Inserisci solo lettere.")
            continue  # richiede un nuovo input senza consumare un tentativo

        if len(tentativo) == 1:  # caso: l'utente ha inserito una singola lettera
            try:
                # EAFP: se la lettera è già nel dizionario, l'accesso riesce e NON solleva eccezioni
                lettere_indovinate[tentativo]
                print("Hai già inserito questa lettera!")
                # NB: questo blocco intercetta solo le lettere già presenti in lettere_indovinate,
                #     che contiene SOLO le lettere indovinate CORRETTAMENTE (vedi sotto, il ramo
                #     "lettera non presente" non aggiunge mai nulla al dizionario). Di conseguenza
                #     una lettera già provata ma SBAGLIATA può essere reinserita più volte,
                #     consumando un tentativo ogni volta senza ricevere questo avviso.
            except KeyError:
                try:
                    # EAFP: se la lettera non è nella parola, index() solleva ValueError
                    parola.index(tentativo)
                    lettere_indovinate[tentativo] = True  # registra la lettera come indovinata
                    print(f"Ottimo! La lettera '{tentativo}' è presente.")
                    # Controllo se la parola è stata interamente indovinata
                    try:
                        for lettera in parola:
                            lettere_indovinate[lettera]  # tenta di leggere ogni lettera della parola
                        parola_indovinata = True  # se il ciclo finisce senza KeyError, sono tutte note
                    except KeyError:
                        pass  # almeno una lettera manca ancora: la partita continua
                except ValueError:
                    tentativi_rimasti -= 1  # lettera sbagliata: consuma un tentativo
                    print(f"La lettera '{tentativo}' non è presente.")
        else:  # caso: l'utente ha inserito una parola intera (tentativo di più caratteri)
            try:
                if tentativo != parola:
                    raise ValueError  # parola sbagliata: solleva un'eccezione volontariamente
                lettere_indovinate = {l: True for l in parola}  # segna tutte le lettere come indovinate
                parola_indovinata = True  # la partita è vinta
            except ValueError:
                tentativi_rimasti -= 1  # parola sbagliata: consuma un tentativo
                print("Parola errata.")

    # Messaggio finale in base all'esito della partita
    if parola_indovinata:
        print(f"\nComplimenti! Hai indovinato la parola: {parola}")
    else:
        print(f"\nHai terminato i tentativi! La parola era: {parola}")


if __name__ == "__main__":
    gioca_eafp()  # avvia la partita quando lo script viene eseguito direttamente
