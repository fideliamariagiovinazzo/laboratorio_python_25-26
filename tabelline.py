
#
# File: tabelline.py
#
# Author: F. M. Giovinazzo
#
# Date: 28/06/2026
#
# Version: 2.0
#
# Description: Mini-gioco interattivo per allenarsi con le tabelline matematiche, 
#              implementato utilizzando i generatori di Python e la gestione degli input.
#
import random

# 1. Generatore della tabellina
def tabellina(n):
    """
    Generatore infinito che produce i multipli di un numero intero n 
    partendo da n * 0, n * 1, n * 2 e così via.    
    Yields:
        int: Il valore corrente della tabellina.
    """
    i = 0
    while True:
        yield n * i
        i += 1

# 2. Funzione principale del gioco
def gioca():
    """
    Gestisce la logica principale del gioco interattivo delle tabelline,
    validando l'input dell'utente e gestendo l'avanzamento tramite il generatore.
    """
    numero = random.randint(1, 10)  # numero casuale della tabellina
    g = tabellina(numero)          # Creazione dell'istanza del generatore
    valore_corrente = next(g)
    turno = 0
    
    print("Indovina i valori della tabellina! Scrivi 'esci' per terminare.")
    
    while True:
        risposta = input(f"Turno {turno}: qual è il valore corrente? ")
        
        # Chiusura del gioco personalizzata
        if risposta.lower() == "esci":
            print("Grazie per aver giocato! Alla prossima.")
            break
            
        # Gestione di lettere, caratteri speciali, decimali
        try:
            tentativo = int(risposta)
        except ValueError:
            print("Input non valido: inserisci un numero intero, per favore.")
            continue
            
        # Confronto e avanzamento
        if tentativo == valore_corrente:
            print("Corretto!")
        else:
            print(f"Sbagliato, il valore corretto era {valore_corrente}")
            
        valore_corrente = next(g)
        turno += 1

# 3. Avvio del programma
if __name__ == "__main__":
    gioca()