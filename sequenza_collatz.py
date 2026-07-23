
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
        print("Riprova, il numero non è del tipo cercato")       
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
        
    lista_numeri.append(m)                                     

    if len(lista_numeri) >= 100 or lista_numeri[-1] == 1:             
        return lista_numeri                                       
    else:
        return genera_collatz(m, lista_numeri)                  

def analizza_sequenza(lista):   
    
    """Calcola massimo, lunghezza, somma su una sequenza di numeri."""
                                             
    massimo = max(lista)                                               
    somma = sum(lista)                                             
    lunghezza = len(lista)                                             
    return massimo, lunghezza, somma                                      

def ricerca(lista):                     
    """
    Cerca e stampa tutti i multipli di 5 presenti in una lista.
    Se non ne trova nessuno, stampa un messaggio informativo.
    """                                 
    trovato = False                                                   
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

    quanti = int(input("Quanti numeri vuoi testare? "))

    for i in range(quanti):
        numero_iniziale = chiedi_numero_positivo()    
        lista_numeri = [numero_iniziale]               
        genera_collatz(numero_iniziale, lista_numeri)   
        
        print(f"Sequenza per {numero_iniziale}: {lista_numeri}")         
        
        massimo, lunghezza, somma = analizza_sequenza(lista_numeri)                  
        print(f"Massimo: {massimo}, Lunghezza: {lunghezza}, Somma: {somma}")
        
        ricerca(lista_numeri)
        
        # CORRETTO: Spostato dentro il ciclo for per confrontare ogni sequenza
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