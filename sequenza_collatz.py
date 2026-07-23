
# File: sequenza_collatz.py
#
# Author: F.M. Giovinazzo
#
# Date: 15/06/2026
#
# Version: 4.1
#
# Description: Programma che genera, analizza e effettua ricerca dei multipli di 5 in una lista collatz.
#

def is_pari(n):             
    """
    Verifica se un numero è pari. Parametri: n,(int): il numero da controllare.
    """                             
    if n % 2 == 0:         
    #se il numero è pari ritorna True, altrimenti False              
        return True
    else:
        return False   

def chiedi_numero_positivo():         
    """
    Chiede all'utente un numero intero positivo.
    Continua a chiedere finché non viene inserito un valore > 0.
    """                                     
    n = int(input("Scrivi un numero positivo: "))             
    while n <= 0:                                 
    #while loop, condizione n minore o uguale di 0                
        print("Riprova, il numero non è del tipo cercato")  
        #messaggio dedicato se l'input non è quello specificato     
        n = int(input("Scrivi un numero positivo: "))                               
    return n                                                      

def genera_collatz(n, lista_numeri):                         
    """
    Genera ricorsivamente la sequenza di Collatz a partire da n,
    aggiungendo ogni nuovo valore a lista_numeri.
    """                                 
    if is_pari(n):                                             
        m = n // 2
    else:
        m = n * 3 + 1
    #svolgo delle operazioni diverse in base all'eventuale parità o disparità del valore        
    lista_numeri.append(m)  
    #aggiungo m alla lista numeri                                   

    if len(lista_numeri) >= 100 or lista_numeri[-1] == 1:    
    # se la lista ha più di 100 elementi o il suo ultimo elemento è pari a 1 interrompo la generazione della lista.         
        return lista_numeri                                       
    else:
        return genera_collatz(m, lista_numeri)       #altrimenti continuo a generarla           

def analizza_sequenza(lista):   
    
    """Calcola massimo, lunghezza, somma su una sequenza di numeri."""
                                             
    massimo = max(lista)                                               
    somma = sum(lista)                                             
    lunghezza = len(lista)                                             
    return massimo, lunghezza, somma        
    #stampo le statistiche richieste                              

def ricerca(lista):                     
    """
    Cerca e stampa tutti i multipli di 5 presenti in una lista.
    Se non ne trova nessuno, stampa un messaggio informativo.
    """                                 
    trovato = False              
    #inizializzo il valore 'trovato' che utilizzerò come "flag"                                     
    for numero in lista:                                              
        if numero % 5 == 0:                                           
            print(numero)
            trovato = True
            
    if not trovato:                                                   
        print("Non sono presenti multipli di 5")

def main():
    
    """Funzione principale del programma."""
    
    lunghezza_massima = 0
    numero_migliore = None
    # inizializzo le variabili che serviranno per il riepilogo finale

    quanti = int(input("Quanti numeri vuoi testare? "))

    for i in range(quanti):
        #ripeto questo procedimento tante volte quante scrive l'utente
        numero_iniziale = chiedi_numero_positivo()    
        lista_numeri = [numero_iniziale]               
        genera_collatz(numero_iniziale, lista_numeri)   
        #genero la lista utilizzando come n il numero che chiedo all'utente
        
        print(f"Sequenza per {numero_iniziale}: {lista_numeri}")         
        
        massimo, lunghezza, somma = analizza_sequenza(lista_numeri)                  
        print(f"Massimo: {massimo}, Lunghezza: {lunghezza}, Somma: {somma}")
        
        ricerca(lista_numeri)
        
        
        if lunghezza > lunghezza_massima:  
            lunghezza_massima = lunghezza  
            numero_migliore = numero_iniziale  

    # Riepilogo finale
    print("\n--- Riepilogo Finale ---")
    print("Il numero che ha generato la sequenza più lunga è: %s" % (numero_migliore))      
     #uso della formattazione a stringhe old-style        
    print("Lunghezza della sequenza: %i" % (lunghezza_massima))

if __name__ == "__main__":                  
    main()
    #eseguo automaticamente la sezione  main se sono all'interno del file e(non in caso di import)