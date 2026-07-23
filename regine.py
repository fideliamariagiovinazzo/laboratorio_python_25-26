#
# File: Regine.py
#
# Author: F. M. Giovinazzo
#
# Date: 18/06/2026
#
# Version: 3.0
#
# Description: Progetto che risolve con approccio brute force il problema delle 8 regine.
#
import random 
 # Modulo per la generazione di permutazioni casuali
import time    
# Modulo per il monitoraggio del timeout di 15 secondi e il calcolo dei tempi


def stessa_diagonale(x0, y0, x1, y1):
    """
    Verifica se due regine si trovano sulla stessa diagonale.
    Sfrutta la proprietà geometrica per cui la distanza sulle X 
    è uguale alla distanza sulle Y (inclinazione a 45°).    
    Returns:
        bool: True se sono sulla stessa diagonale, False altrimenti.
    """
    return abs(y1 - y0) == abs(x1 - x0)                     
    # se dx == dy , dx/dy == 1 e sono sulla stessa diagonale, boolean expression

def incrocia_colonne(posizioni, col):
    """
    Controlla se la regina posizionata alla colonna corrente ('col')
    incontra ostacoli sulle diagonali rispetto a tutte le regine precedenti.    
    Returns:
        bool: True se c'è un'intersezione diagonale, False se è sicura.
    """
    for c in range(col):                         
    # scorre tutte le colonne con un ciclo for
    # Se rileva una collisione diagonale con una regina precedente, la posizione non è valida
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True  
    # Collisione diagonale trovata: la posizione della regina corrente non è valida
    return False 
     # La posizione è sicura rispetto alle regine precedenti

def soluzione_ok(soluzione_posizioni):
    """
    Scansiona l'intera scacchiera per verificare la validità globale della soluzione.
    Essendo basata su permutazioni, i controlli su righe e colonne sono impliciti.    
    Returns:
        bool: True se la soluzione è valida, False altrimenti.
    """
    for col in range(1, len(soluzione_posizioni)):                              
        # Itera ciclicamente su tutte le colonne della scacchiera a partire dall'indice 1.

        if incrocia_colonne(soluzione_posizioni, col):                          
            # Richiama la funzione di controllo per verificare se la regina nella colonna 
            # corrente interseca le diagonali o le posizioni delle regine precedenti.
                             
            return False                                                         
            # Se la funzione restituisce True (cioè rileva un'intersezione/collisione), 
            # interrompe subito il controllo e restituisce False: la configurazione non è valida.
                             
    return True                                                                  
    # Se il ciclo termina senza aver trovato alcuna collisione, significa che nessuna 
    # regina minaccia le altre. Restituisce True: la configurazione è una soluzione valida.

def ruota_90(soluzione):
    """
    Esegue una rotazione di 90 gradi in senso orario della scacchiera delle regine.
    Returns:
        list: Nuova lista con le posizioni ruotate di 90 gradi.
    """
  
    nuova_soluzione = []
    N = len(soluzione)  # Memorizza la dimensione N della scacchiera (numero di regine)
    
    # Costruisce il nuovo vettore di stato sequenzialmente usando il metodo append().
    # Itera sulle nuove colonne (da 0 a N-1) per generare le coordinate ruotate.
    for nuv_col in range(N):
        # Individua la riga in cui si trovava la regina nella disposizione originale.
        # Usa .index() (per cercare l'indice di corrispondenza )per mappare la vecchia coordinata y associata alla colonna corrente.
        vecchia_riga = soluzione.index(nuv_col)
        
        # Calcola la rotazione: inverte l'asse e aggiunge il valore calcolato in coda alla lista.
        nuova_riga = N - 1 - vecchia_riga  # Inversione dell'asse per ottenere la rotazione di 90°
        nuova_soluzione.append(nuova_riga)  # Aggiunge la nuova posizione calcolata alla lista risultato
        
    return nuova_soluzione  # Restituisce la configurazione ruotata di 90°

def ruota_180(soluzione):
   
    """Esegue una rotazione di 180 gradi della scacchiera delle regine."""
    
    
    # Inizializza una lista vuota per contenere lo stato ruotato
    nuova_soluzione = []
    N = len(soluzione)  # Memorizza la dimensione N della scacchiera
    
    # Itera la lista originale al contrario (inversione delle righe) usando reversed()
    for col in reversed(soluzione):
        # Specchia le coordinate (inversione delle colonne) e aggiunge in coda
        nuova_soluzione.append(N - 1 - col)  # Calcola e inserisce la coordinata specchiata
        
    return nuova_soluzione  # Restituisce la configurazione ruotata di 180°

def ruota_270(soluzione):
    """
    Esegue una rotazione di 270 gradi in senso orario (o 90 in senso antiorario).
    Returns:
        list: Nuova lista con le posizioni ruotate di 270 gradi.
    """
    # Questa funzione sfrutta la composizione funzionale applicando 90° e 180°.
    return ruota_90(ruota_180(soluzione))  # Compone le rotazioni: 180° seguita da 90° = 270° totali


def main_regine(n, s):
    """
    Risolve il problema delle N-Regine tramite approccio Brute-Force statistico.
    Cerca 's' soluzioni uniche, monitora i duplicati e gestisce il timeout di 15 secondi.
    
    Args:
        n (int): Dimensione della scacchiera (N x N).
        s (int): Numero di soluzioni uniche richieste.
        
    Returns:
        list or None: Lista delle soluzioni uniche trovate sotto forma di tuple, oppure None se scatta il timeout.
    """
    random_generator = random.Random()                              # Inizializzazione dell'oggetto Random per la generazione casuale
                                       
    tempi_soluzioni = []      # Memorizza il tempo impiegato per ogni soluzione unica
    tentativi_soluzioni = []  # Memorizza il numero di tentativi per ogni soluzione unica
    registro_soluzioni = {}   # Dizionario per il tracking delle soluzioni uniche e conteggio duplicati
    
    soluzioni_trovate = 0     # Contatore delle soluzioni uniche validate
    tentativi = 0             # Contatore dei tentativi per la soluzione corrente
    start_time = time.time()  # Registrazione del timestamp iniziale della ricerca
    
    while soluzioni_trovate < s:  # Il ciclo prosegue fino al raggiungimento del numero richiesto di soluzioni uniche
        
        # APPLICAZIONE DELLE PERMUTAZIONI CASUALI VIA SHUFFLE
        lista_soluzione = list(range(n))          # Genera la lista iniziale ordinata (es: [0, 1, 2, ..., n-1])
        random_generator.shuffle(lista_soluzione) # Genera una permutazione casuale (mescolamento)
        
        tentativi += 1  # Incrementa il contatore dei tentativi effettuati
        
        # controllo che la ricerca delle soluzioni non duri più di 15 secondi -> timeout
        if time.time() - start_time > 15.0:
            print(f"TIMEOUT RAGGIUNTO PER N={n}")  # Segnala a video il superamento del limite di tempo
            return None  # Interruzione forzata dell'algoritmo
            
        # Verifica geometrica della permutazione casuale generata
        if soluzione_ok(lista_soluzione):
            scacchiera_tupla = tuple(lista_soluzione)  # Converte in tupla per renderla chiave immutabile del dizionario
            tempo_impiegato = time.time() - start_time   # Calcola il delta temporale
            
            # GESTIONE DEI DUPLICATI 
            if scacchiera_tupla in registro_soluzioni:
                registro_soluzioni[scacchiera_tupla] += 1  # Incrementa il contatore dei duplicati
                start_time = time.time()  # Resetta il timer per il prossimo tentativo
                tentativi = 0             # Resetta il contatore dei tentativi
                continue                  # Salta al tentativo successivo per cercare una nuova soluzione
                
            # GESTIONE DI UNA SOLUZIONE UNICA
            registro_soluzioni[scacchiera_tupla] = 1  # Registra la nuova soluzione nel dizionario
            tempi_soluzioni.append(tempo_impiegato)   # Salva il tempo impiegato
            tentativi_soluzioni.append(tentativi)     # Salva i tentativi accumulati
            soluzioni_trovate += 1                    # Avanza nel contatore delle soluzioni uniche
            
            # Output in tempo reale della soluzione individuata
            print(f"Sol{soluzioni_trovate}(N={n}): {lista_soluzione} in {tempo_impiegato:.5f}s con {tentativi} tentativi")
            
            # Reset delle metriche di sessione per la ricerca della soluzione successiva
            start_time = time.time()  # Riavvia il cronometro per la prossima ricerca
            tentativi = 0  # Azzera il conteggio dei tentativi per la prossima ricerca
            
    # COMPILAZIONE E STAMPA DEL REPORT STATISTICO FINALE
    if tempi_soluzioni:  # Esegue il report solo se è stata trovata almeno una soluzione
        tempo_medio = sum(tempi_soluzioni) / len(tempi_soluzioni)  # Calcola il tempo medio impiegato per soluzione unica
        totale_duplicati = sum(valore - 1 for valore in registro_soluzioni.values())  # Somma tutte le occorrenze duplicate scartate
        print(f"\nSTATISTICHE FINALI (N={n})")  # Intestazione del report statistico
        print(f"Tempo medio per soluzione unica: {tempo_medio:.5f}s")  # Stampa il tempo medio calcolato
        print(f"Lista tentativi per soluzione: {tentativi_soluzioni}")  # Stampa il dettaglio dei tentativi per ogni soluzione
        print(f"Totale duplicati scartati: {totale_duplicati}")  # Stampa il totale dei duplicati incontrati
        print("Dettaglio occorrenze soluzioni uniche:")  # Intestazione del dettaglio per singola soluzione
        for sol, cont in registro_soluzioni.items():  # Scorre ogni soluzione unica registrata insieme al suo conteggio
            print(f" > Soluzione {sol} riprodotta complessivamente {cont} volte")  # Stampa quante volte è stata ritrovata la soluzione
            
    return list(registro_soluzioni.keys())  # Restituisce l'insieme delle soluzioni uniche

if __name__ == "__main__":
    # Verifica di base (N=8)
    # Controlliamo che il programma trovi le soluzioni su una scacchiera classica.
    print("[PHASE 1] TEST DI FUNZIONAMENTO (N=8, TARGET=10)")  # Messaggio introduttivo della fase 1
    soluzioni_base = main_regine(8, 10)  # Esegue la ricerca di 10 soluzioni uniche per N=8
    
    # Fase 2: Test di velocità (limite 15 secondi)
    # Proviamo a risolvere scacchiere sempre più grandi finché il computer ci mette troppo tempo.
    print("\n TEST DI VELOCITÀ E LIMITI =")  # Messaggio introduttivo della fase 2
    lato_n = 8  # Dimensione di partenza della scacchiera da testare
    ultimo_lato_valido = 8  # Memorizza l'ultima dimensione N risolta con successo entro il timeout
    while True:  # Ciclo infinito interrotto manualmente al raggiungimento del timeout
        # Tentiamo di trovare almeno una soluzione per la dimensione N corrente
        risultato = main_regine(lato_n, 1)  # Cerca una singola soluzione per la dimensione corrente
        if risultato is not None:
            # Se la trova, ricordiamo il valore e proviamo con una più grande
            ultimo_lato_valido = lato_n  # Aggiorna l'ultima dimensione risolta con successo
            lato_n += 1  # Incrementa la dimensione della scacchiera per il prossimo tentativo
        else:
            # Se si ferma, abbiamo raggiunto il limite
            break  # Esce dal ciclo perché è scattato il timeout
    print(f"\n[!] Dimensione massima calcolata in 15s: N={ultimo_lato_valido}")  # Stampa il risultato finale della fase 2
    
    #  Test delle rotazioni geometriche
    # Verifichiamo che le funzioni per ruotare la scacchiera funzionino correttamente.
    # Costruiamo le 4 soluzioni simmetriche (0°, 90°, 180°, 270°) per ogni caso.
    print("\nTEST DELLE ROTAZIONI")  # Messaggio introduttivo della fase 3
    soluzioni_simmetria = main_regine(8, 5)  # Cerca 5 soluzioni uniche da usare come base per i test di rotazione
    if soluzioni_simmetria:  # Prosegue solo se sono state effettivamente trovate delle soluzioni
        print("\nCalcolo delle 4 rotazioni per ogni soluzione:")  # Intestazione del blocco di stampa delle rotazioni
        for idx, sol in enumerate(soluzioni_simmetria):                     # scorro gli indici e le soluzioni e individuo elemento della lista e indice grazie alla funzione enumerate
            print(f"\n[Soluzione {idx+1}]")  # Stampa il numero progressivo della soluzione analizzata
            print(f"           Originale (0°) : {sol}")  # Stampa la configurazione originale senza rotazione
            print(f"           Ruotata 90°    : {ruota_90(sol)}")  # Calcola e stampa la rotazione di 90°
            print(f"           Ruotata 180°   : {ruota_180(sol)}")  # Calcola e stampa la rotazione di 180°
            print(f"           Ruotata 270°   : {ruota_270(sol)}")  # Calcola e stampa la rotazione di 270°