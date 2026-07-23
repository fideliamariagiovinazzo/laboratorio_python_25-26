#
#File: rock_paper.py
#Author: F.M. Giovinazzo
#Date: 24/06/2026
#Version: 2.3 
#Description: Gioco Rock, Paper, Scissors, Lizard, Spock (RPSLS) che tiene traccia del punteggio e assegna premi



import random           # modulo random: usato per far scegliere una mossa casuale al computer
import sys              # modulo sys: usato per uscire dal programma in modo pulito (sys.exit())


class Giocatore:
    """Classe che modella un giocatore (Utente o Computer) con stato e metodi dedicati."""

    def __init__(self, nome):
        """Inizializza una nuova istanza di Giocatore."""
        self.nome = nome                    # attributi dell'istanza
        self.punteggio = 0                  # punteggio accumulato durante la partita, inizialmente 0
        self.mossa_corrente = None          # mossa scelta nel round in corso (None finché non gioca)

    def aggiorna_punteggio(self, punti):
        """Incrementa il punteggio del giocatore, usando come parametri self e i punti ottenuti."""
        self.punteggio += punti  # somma i punti passati al punteggio già accumulato

    def reset_punteggio(self):
        """Resetta il punteggio del giocatore a zero."""
        self.punteggio = 0  # azzera il contatore dei punti


# Funzione lambda per verificare velocemente se un punteggio sblocca un premio.
# Dopo l'assegnazione della variabile valida_premio quivalente a: def valida_premio(punti, soglia): return punti >= soglia
valida_premio = lambda punti, soglia: punti >= soglia  # restituisce True se punti raggiunge/supera la soglia


def generatore_partite(max_partite):
    
    """Generatore che tiene traccia del numero di partite giocate."""
  
    corrente = 1  # contatore che parte dalla prima partita
    while corrente <= max_partite:  # continua finché non si raggiunge il numero massimo richiesto
        yield corrente               # restituisce il numero di partita corrente e sospende l'esecuzione
        corrente += 1                # alla ripresa, incrementa il contatore per la prossima iterazione


def mostra_regole():
    """Stampa a video le regole estese del gioco RPSLS (chi batte chi)."""
    print("\n REGOLE DI ROCK, PAPER, SCISSORS, LIZARD, SPOCK")
    print("Le forbici tagliano la carta")
    print(" La carta avvolge il sasso")
    print(" Il sasso schiaccia lizard")
    print(" Lizard avvelena Spock")
    print(" Spock smussa le forbici")
    print(" Le forbici decapitano lizard")
    print(" Lizard mangia la carta")
    print("La carta sbugiarda Spock")
    print("Spock vaporizza il sasso")
    print(" Il sasso rompe le forbici\n")


def calcola_vincitore(mossa1, mossa2):
  
    """Stabilisce il vincitore tra due mosse secondo le regole di RPSLS."""
    
    if mossa1 == mossa2:
        return 0  # stessa mossa per entrambi: pareggio

    # Dizionario che delinea la "gerarchia" delle mosse: la chiave batte le mosse contenuta nella lista associata.
    regole_gioco = {
        "rock": ["scissor", "lizard"],    # il sasso rompe le forbici e schiaccia lizard
        "paper": ["rock", "spock"],       # la carta avvolge il sasso e sbugiarda Spock
        "scissor": ["paper", "lizard"],   # le forbici tagliano la carta e decapitano lizard
        "lizard": ["spock", "paper"],     # lizard avvelena Spock e mangia la carta
        "spock": ["scissor", "rock"]      # Spock smussa le forbici e vaporizza il sasso
    }

    if mossa2 in regole_gioco[mossa1]:  # verifica se mossa1 batte mossa2 secondo il dizionario
        return 1  # vince il primo giocatore
    else:
        return 2  # altrimenti vince il secondo giocatore (essendo già escluso il pareggio sopra)
  

def assegna_premio(punti):
    """Verifica e assegna un premio in base ai punti accumulati, usando la funzione lambda 'valida_premio'."""
 
    premio = "Nessun premio sbloccato"  # valore di default se nessuna soglia viene raggiunta

    if valida_premio(punti, 10):  # controlla per prima la soglia più alta (10+ punti)
        premio = "Primo classificato (10+ punti): Set completo della serie The Big Bang Theory e maglia"
    elif valida_premio(punti, 4):  # soglia intermedia (4-9 punti)
        premio = "Secondo classificato (4-9 punti): Buono da 30 euro da Gino il gelataio"
    elif valida_premio(punti, 1):  # soglia minima (1-3 punti)
        premio = "Terzo classificato (1-3 punti): Peluche a forma di armadillo"

    return premio  # restituisce la stringa del premio corrispondente 

def chiedi_scelta_utente(mosse_consentite):
   
    """Chiede ripetutamente l'input all'utente, in caso di inserimento di stringa non valida (non appartenente alle mosse consentite o non del tipo corretto)"""
 
    while True:  # continua a chiedere finché non riceve un input valido o l'utente esce
        try:
            scelta = input("Seleziona [Rock, Paper, Scissor, Lizard, Spock] (o 'esci'): ").strip().lower()
 
            if scelta == 'esci':
                print("Chiusura del gioco in corso. Arrivederci!")
                sys.exit()  # termina immediatamente il programma
 
            if scelta not in mosse_consentite:
                raise ValueError(f"Mossa '{scelta}' non riconosciuta!")  # solleva un errore di runtime e cerca il primo blocco except
 
            return scelta  # input valido: lo restituisce e interrompe il ciclo
 
        except (ValueError, TypeError) as e:            #indica in una tupla due tipi di errori: la mossa non è tra quelle consentite oppure inserissi un numero
            print(f"[Errore di input]: {e} Riprova.")
        except Exception as e:
            # blocco except per qualsiasi altro errore imprevisto 
            print(f"[Errore inatteso]: {e}. Riprova.")




def main():
    """
    Funzione principale: gestisce l'intero flusso di gioco, dalla configurazione iniziale
    (numero di round) fino alla stampa del punteggio finale e all'assegnazione del premio.
    """
    mosse_consentite = ("rock", "paper", "scissor", "lizard", "spock")  # Tupla immutabile delle mosse valide

    # Istanziamo gli oggetti della classe Giocatore (OOP)
    utente = Giocatore("Utente")      # crea il giocatore umano
    computer = Giocatore("Computer")  # crea il giocatore automatico

    mostra_regole()  # stampa le regole del gioco prima di iniziare

    # Acquisizione sicura del numero di round desiderati con gestione errori
    while True:
        try:
            num_round = int(input("Quante partite vuoi giocare in totale? "))  # casting a intero
            if num_round <= 0:
                print("Inserisci un numero maggiore di zero.")
                continue  # richiede un nuovo input senza uscire dal ciclo
            break  # numero valido e positivo: esce dal ciclo di acquisizione
        except ValueError:
            print("[Errore]: Devi inserire un numero intero valido!")  # input non numerico(es stringa)

    print(f"\nIniziamo! Si giocheranno {num_round} partite.\n")

    # Utilizzo del generatore per iterare le partite
    for partita in generatore_partite(num_round):  # ottiene il numero di partita ad ogni iterazione
        print(f" PARTITA N. {partita} ")

        # Input dell'utente
        mossa_utente = chiedi_scelta_utente(mosse_consentite)  # chiede e valida la mossa dell'utente
        utente.mossa_corrente = mossa_utente  # memorizza la mossa scelta nell'oggetto Giocatore

        # Scelta casuale del computer
        mossa_comp = random.choice(mosse_consentite)  # sceglie casualmente una mossa tra quelle valide
        computer.mossa_corrente = mossa_comp  # memorizza la mossa del computer

        # Formattazione delle stringhe con f-strings
        print(f"Hai scelto: {utente.mossa_corrente.capitalize()}")
        print(f"Il computer ha scelto: {computer.mossa_corrente.capitalize()}")

        # Valutazione del risultato della mano
        risultato = calcola_vincitore(utente.mossa_corrente, computer.mossa_corrente)

        if risultato == 0:
            print("Risultato: Pareggio in questa mano!\n")
        elif risultato == 1:
            print("Risultato: Hai vinto tu questa mano!\n")
            utente.aggiorna_punteggio(1)  # incrementa il punteggio dell'utente
        else:
            print("Risultato: Ha vinto il Computer questa mano!\n")
            computer.aggiorna_punteggio(1)  # incrementa il punteggio del computer

    print("                 FINE DEL GIOCO                    ")
    print(f"Punteggio finale - {utente.nome}: {utente.punteggio}")
    print(f"Punteggio finale - {computer.nome}: {computer.punteggio}")

    # Determinazione del vincitore assoluto e assegnazione premi basata sui punti
    if utente.punteggio > computer.punteggio:
        print(f"\nCongratulazioni {utente.nome}! Hai vinto la sfida!")
        premio_ottenuto = assegna_premio(utente.punteggio)  # calcola il premio in base ai punti dell'utente
        print(f"Premio sbloccato -> {premio_ottenuto}")
    elif utente.punteggio < computer.punteggio:
        print("\nIl Computer ha vinto la sfida. Andrà meglio la prossima volta!")
        premio_ottenuto = assegna_premio(utente.punteggio)  # premio di consolazione basato sui punti utente
        print(f"Premio di consolazione in base ai punti ({utente.punteggio}) -> {premio_ottenuto}")
    else:
        print("\nLa sfida si è conclusa in un pareggio complessivo!")
        premio_ottenuto = assegna_premio(utente.punteggio)  # premio comunque calcolato sui punti dell'utente
        print(f"Premio in base ai punti totalizzati ({utente.punteggio}) -> {premio_ottenuto}")


if __name__ == "__main__":
    main()  # avvia il gioco solo se lo script viene eseguito direttamente (non importato come modulo)