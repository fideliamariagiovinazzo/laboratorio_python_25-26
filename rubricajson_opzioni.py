#
# File: rubrica.json_opzioni.py
#
# Author: F. M. Giovinazzo
#
# Date: 23/06/2026
#
# Version: 3.0
#
# Description: Programma interattivo che usa la classe Rubrica per gestire
#              una rubrica di contatti (apertura, aggiunta, rimozione, stampa, salvataggio).
#
from classe_json import Rubrica  # importa la classe Rubrica definita in classe_json.py


def esegui():
    """Programma interattivo per gestire la rubrica tramite un menu testuale a comandi."""
    mia_rubrica = Rubrica(dizionario=None)  # crea una rubrica non ancora aperta (dizionario=None)

    while True:  # ciclo principale del menu, continua finché l'utente non digita EXIT
        comando = input(
            "\nInserisci operazione (APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA) o EXIT: "
        ).upper()  # legge il comando dell'utente e lo normalizza in maiuscolo

        if comando == "EXIT":
            print("Uscita dal programma. Arrivederci!")
            break  # esce dal ciclo e termina il programma

        elif comando == "APRI":
            file = input("Nome file da aprire (.json o .txt): ")
            try:
                if file.endswith('.json'):
                    mia_rubrica = Rubrica.da_json(file)   # apre la rubrica da un file JSON
                else:
                    mia_rubrica = Rubrica.da_testo(file)  # apre la rubrica da un file di testo
                print("Rubrica aperta con successo!")
            except FileNotFoundError:
                print("File non trovato. Riprova.")  # gestisce il caso(EAFP) in cui il file non esista

        elif comando == "AGGIUNGI":
            nome = input("Nome e Cognome del contatto: ")
            try:
                giorno = int(input("Giorno di nascita: "))   # richiede e converte il giorno in intero
                mese = input("Mese di nascita: ")             # il mese resta una stringa
                anno = int(input("Anno di nascita: "))        # richiede e converte l'anno in intero
                eta = int(input("Età: "))                     # richiede e converte l'età in intero
                sesso = input("Sesso (M/F): ").upper()        # normalizza il sesso in maiuscolo
                mail = input("Email: ")                       # email resta una stringa
                info = {
                    'giorno': giorno,
                    'mese': mese,
                    'anno': anno,
                    'età': eta,
                    'sesso': sesso,
                    'mail': mail
                }
                mia_rubrica.aggiungi(nome, info)  # delega alla classe l'inserimento del contatto
            except ValueError:
                # scatta se giorno, anno o età non sono numeri validi (EAFP)
                print("Errore nell'inserimento dei dati numerici. Contatto non aggiunto.")

        elif comando == "RIMUOVI":
            nome = input("Nome del contatto da rimuovere: ")
            mia_rubrica.rimuovi(nome)  # delega alla classe la rimozione del contatto

        elif comando == "STAMPA":
            nome = input("Nome del contatto da stampare: ")
            mia_rubrica.stampa_contatto(nome)  # delega alla classe la stampa del contatto

        elif comando == "SALVA":
            file = input("Nome file di destinazione (es. rubrica.json o rubrica.txt): ")
            mia_rubrica.salva(file)  # delega alla classe il salvataggio su file

        else:
            print("Comando non riconosciuto.")  # gestisce qualsiasi comando non previsto


if __name__ == "__main__":
    esegui()  # avvia il programma interattivo