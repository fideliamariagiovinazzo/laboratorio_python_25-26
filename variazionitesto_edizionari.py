# File: variazionitesto_e_dizionari,py
# Author: F.M. Giovinazzo
# Date: 23/06/2026
# Version: 4.0
# Description: Programma che analizza e modifica in modi diveri (scritura a specchio, testo sostituito) un testo dato e crea due dizionari.

# Assegno il testo alla variabile
testo = '''Day after day, day after day
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.'''


lista_righe = testo.split('\n') 
# Divide il testo in una lista usando il carattere di a capo ('\n')
lista_righe_pulite = []          
# Inizializza una lista vuota per contenere solo le righe non vuote


for riga in lista_righe:                
# Itera su tutte le righe della lista_righe
    if riga != '':                      
# Controlla se la riga NON è una stringa vuota
        lista_righe_pulite.append(riga) 
# Aggiunge la riga valida (non vuota) alla nuova lista

print(lista_righe_pulite)                                       
# Stampa la lista delle righe ripulite
print(f"Numero di righe non vuote: {len(lista_righe_pulite)}") 
 # Stampa il conteggio totale delle righe valide, formattazione f-strings



parole = testo.split()          
# Divide il testo in base agli spazi bianchi, restituendo tutte le parole
print(f"Numero di parole: {len(parole)}")  
# Stampa il numero complessivo di parole trovate nel testo

# Crea una lista con tutti i caratteri del testo che sono lettere o numeri (esclude spazi e punteggiatura)-> usa la list comprehension
lista_caratteri_alfanume = [lettera for lettera in testo if lettera.isalnum()]
print(f"Numero di caratteri alfanumerici: {len(lista_caratteri_alfanume)}")  
# Stampa il conteggio totale alfanumerico

lettera = input("Inserisci una lettera: ")  
# Chiede all'utente di digitare una lettera 
# Converte tutto in minuscolo per rendere la ricerca case-insensitive e conta le occorrenze della lettera inserita.
conteggio_lettera = testo.lower().count(lettera.lower())
print(f"La lettera {lettera} compare {conteggio_lettera} volte nel testo.\n")       
#Stampa il conteggio delle volte in cui appare la lettera.



testo_sostituito = testo                   
# Copia il testo originale in una nuova variabile per non modificarlo
# Definisce una tupla con le varianti maiuscole/minuscole delle parole da cercare
lista_parole_da_sostituire = ("Water", "Day", "day", "water", "about", "About")

for parola in lista_parole_da_sostituire:       
 # Itera su ciascuna parola da rimpiazzare
    testo_sostituito = testo_sostituito.replace(parola, "PYTHON")  
# Sostituisce la parola con "PYTHON"

print(testo_sostituito)                    
# Stampa il testo con le modifiche applicate


parole_testo = testo.split()                
 # Divide il testo in una lista di singole parole
# Crea una lista in cui la parola viene messa in maiuscolo (.upper()) se l'indice è pari (0, 2, 4...), 
# altrimenti rimane invariata. 
parole_modificate = [parole_testo[i].upper() if i % 2 == 0 else parole_testo[i] for i in range(len(parole_testo))]
#list comprehension
print(" ".join(parole_modificate)) 
# Riunisce la lista di parole in un'unica stringa separata da spazi e la stampa


# Divide il testo in righe, eliminando gli spazi bianchi superflui (.strip()) e ignorando le righe vuote
righe_testo = [r for r in testo.split('\n') if r.strip() != '']         
#list comprehension

print("\n".join(righe_testo[::-1])) 
# Inverte l'ordine della lista tramite slicing ([::-1]) e le unisce con un a capo
print("\n")


strofe = testo.split('\n\n')     
# Divide il testo in strofe usando il doppio a capo come separatore
strofe_modificate = []           
# Lista d'appoggio per le strofe elaborate

for strofa in strofe:                   
# Itera su ogni singola strofa
    righe_strofa = strofa.split('\n')   
# Divide la strofa nelle sue righe costitutive
    if len (righe_strofa) >= 2:        
# Controlla se la strofa ha almeno 2 righe
        righe_strofa[1] = righe_strofa[1][::-1]  
# Inverte i caratteri della seconda riga (scrittura a specchio)
    strofe_modificate.append("\n".join(righe_strofa))  
# Ricompone la strofa e la aggiunge alla lista

print("\n\n".join(strofe_modificate))  
# Unisce tutte le strofe con un doppio a capo e stampa il risultato
print("\n")


# Converte ogni strofa in un insieme (set) di parole uniche per facilitare il confronto logico
set_per_strofa = [set(s.split()) for s in strofe]
# Trova l'intersezione tra tutti i set: restituisce solo le parole presenti contemporaneamente in ogni strofa dopo aver effettuato il set unpacking
parole_comuni = set.intersection(*set_per_strofa) if set_per_strofa else set()

print(f"Parole in tutte le strofe: {parole_comuni}\n")


# Trasforma la lista di parole in un set (rimuovendo i duplicati), poi in lista e la ordina usando la lunghezza (key=len)
parole_uniche = sorted(list(set(parole)), key=len)

for p in parole_uniche:          # Itera su ogni parola unica ordinata
    print(f"{p} ({len(p)} caratteri)")  # Stampa la parola insieme al numero dei suoi caratteri
print("\n")


diz_tutti_caratteri = {}        
 # Inizializza un dizionario vuoto per le frequenze dei caratteri
diz_tutti_caratteri = {c: testo.count(c) for c in testo}     
 # Conta la frequenza di ogni carattere nel testo in modo compatto-> dictionary comprehension
print("Dizionario tutti i caratteri:")
print(diz_tutti_caratteri)      
 # Stampa il dizionario 
print("\n")


diz_alfa = {}                  
# Converte tutto il testo in minuscolo per un conteggio case-insensitive
testo_minuscolo = testo.lower()

# Crea il dizionario contando solo i caratteri alfanumerici (esclude spazi e punteggiatura)
diz_alfa = {c: testo_minuscolo.count(c) for c in testo_minuscolo if c.isalnum()}

print("Dizionario caratteri alfanumerici (case-insensitive):")
print(diz_alfa)                 
 # Stampa il dizionario pulito con le frequenze alfanumeriche