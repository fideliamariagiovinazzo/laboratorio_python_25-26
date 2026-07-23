#
# File: classe_json.py
#
# Author: F.M. Giovinazzo
#
# Date: 20/06/2026
#
# Version: 1.0
#
# Description: Classe Rubrica per la gestione di una collezione di contatti; definizione mediante file json
#   
import json  # Modulo per leggere e scrivere file in formato JSON


class Rubrica:
    """Classe che gestisce una collezione di contatti."""

    def __init__(self, dizionario=None):
       
        """Inizializza la rubrica con un dizionario, oppure a None se non è ancora stata aperta."""
        # Se viene passato esplicitamente None, la rubrica è considerata "non aperta"
        self.contatti = dizionario

    @classmethod
    def da_json(cls, nome_file):
       
        """Metodo di classe per creare una rubrica leggendo i dati da un file JSON."""
        with open(nome_file, 'r') as f:  
         # context manager per la lettura di un file json
            data = json.load(f)         
        # carica il contenuto del file JSON in un dizionario Python
        return cls(data)                 
         # costruisce e restituisce una nuova Rubrica con quei dati

    @classmethod
    def da_testo(cls, nome_file):
        """
        Metodo di classe per creare una rubrica leggendo i dati da un file di testo
        (una riga per contatto, campi separati da virgola).
        """
        data = {}  # dizionario che conterrà tutti i contatti letti dal file
        with open(nome_file, 'r') as f:   
        # context manager per la lettura del file di testo
            for riga in f:               
         # scorre il file riga per riga
                riga = riga.strip()     
         # rimuove spazi/ritorni a capo iniziali e finali
                if not riga:
                    continue              # salta le righe vuote

            
                parti = [p.strip() for p in riga.split(',')] 
         
        # spezza la riga usando come separatore , e rimuove gli spazi
                if len(parti) >= 7:  
        # verifica che ci siano tutti e 7 i campi attesi (indici da 0 a 6)
                    nome = parti[0]  # il primo campo è il nome e cognome, usato come chiave
                    data[nome] = {
                        'giorno': int(parti[1]),  # converte il giorno in intero
                        'mese': parti[2],          # il mese resta una stringa
                        'anno': int(parti[3]),     # converte l'anno in intero
                        'età': int(parti[4]),      # converte l'età in intero
                        'sesso': parti[5],         # sesso resta una stringa (M/F)
                        'mail': parti[6]           # email resta una stringa
                    }
        return cls(data)  # costruisce e restituisce una nuova Rubrica con i dati letti

    def aggiungi(self, nome, info):
        """
        Aggiunge un contatto alla rubrica; richiede che la rubrica sia già stata aperta.

        Args:
            nome (str): nome del contatto da aggiungere.
            info (dict): dizionario con le informazioni del contatto.
        """
        if self.contatti is None:  # controlla che la rubrica sia stata aperta/inizializzata
            print("Prima apri una rubrica")
            return  # esce subito dal metodo senza fare nulla
        self.contatti[nome] = info  # inserisce (o sovrascrive) il contatto nel dizionario
        print(f"Contatto '{nome}' aggiunto con successo!")

    def rimuovi(self, nome):
        """
        Rimuove un contatto dalla rubrica, se presente.

        Args:
            nome (str): nome del contatto da rimuovere.
        """
        if self.contatti is None or not self.contatti:  # rubrica non aperta oppure vuota
            print("La rubrica è vuota")
        elif nome not in self.contatti:  # il contatto cercato non esiste
            print(f"Il contatto {nome} non esiste in rubrica")
        else:
            del self.contatti[nome]  # elimina la voce dal dizionario
            print(f"Contatto '{nome}' rimosso con successo!")

    def stampa_contatto(self, nome):
        """
        Stampa a video tutte le informazioni di un contatto specifico.

        Args:
            nome (str): nome del contatto da stampare.
        """
        if self.contatti is None or not self.contatti:  # rubrica non aperta oppure vuota
            print("La rubrica è vuota")
        elif nome not in self.contatti:  # il contatto cercato non esiste
            print(f"Il contatto {nome} non esiste in rubrica")
        else:
            dati = self.contatti[nome]  # recupera il dizionario di informazioni del contatto
            # Formattazione come nell'esercizio 3
            stringa_out = f"'{nome}', "  # inizia la stringa di output con il nome tra apici
            for chiave in dati:  # scorre ogni campo del contatto
                if chiave in ['mese', 'sesso', 'mail']:
                    # campi testuali: valore stampato tra apici
                    stringa_out += f"'{chiave}' '{dati[chiave]}', "
                else:
                    # campi numerici: valore stampato senza apici
                    stringa_out += f"'{chiave}' {dati[chiave]}, "
            print(stringa_out[:-2])  # rimuove l'ultima ", " in eccesso e stampa il risultato

    def salva(self, nome_file):
        """
        Salva la rubrica su file, in formato JSON o testo a seconda dell'estensione.

        Args:
            nome_file (str): percorso del file di destinazione (.json oppure altra estensione per il testo).
        """
        if self.contatti is None or not self.contatti:  # rubrica non aperta oppure vuota
            print("La rubrica è vuota")
            return  # non c'è nulla da salvare

        if nome_file.endswith('.json'):        # se il nome del file termina con .json
            with open(nome_file, 'w') as f:    # context manager per la scrittura di un file json
                json.dump(self.contatti, f)    # serializza l'intero dizionario contatti su file
        else:
            with open(nome_file, 'w') as f:    # context manager per la scrittura di un file di testo
                for nome, d in self.contatti.items():  # scorre ogni contatto (nome, dati)
                    # ricostruisce la riga in formato CSV nello stesso ordine dei campi in lettura
                    riga = f"{nome}, {d['giorno']}, {d['mese']}, {d['anno']}, {d['età']}, {d['sesso']}, {d['mail']}\n"
                    f.write(riga)  # scrive la riga sul file

        print(f"Rubrica salvata con successo in '{nome_file}'!")  # conferma finale (corretto: un solo print)