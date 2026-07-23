#
# File: Regine.py
#
# Author: F. M. Giovinazzo
#
# Date: 18/06/2026
#
# Version: 3.4
#
# Description: Progetto che risolve con approccio brute force il problema delle regine.
#
import random 
import time    


def stessa_diagonale(x0, y0, x1, y1):
    return abs(y1 - y0) == abs(x1 - x0)                     

def incrocia_colonne(posizioni, col):
    for c in range(col):                         
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True  
    return False 

def soluzione_corretta(soluzione_posizioni):
    for col in range(1, len(soluzione_posizioni)):                              
        if incrocia_colonne(soluzione_posizioni, col):                          
            return False                                                         
    return True                                                                  

def ruota_90(soluzione):
    nuova_soluzione = []
    N = len(soluzione)  
    for nuv_col in range(N):
        vecchia_riga = soluzione.index(nuv_col)
        nuova_riga = N - 1 - vecchia_riga  
        nuova_soluzione.append(nuova_riga)  
    return tuple(nuova_soluzione)  

def ruota_180(soluzione):
    nuova_soluzione = []
    N = len(soluzione) 
    for col in reversed(soluzione):
        nuova_soluzione.append(N - 1 - col)  
    return tuple(nuova_soluzione)  

def ruota_270(soluzione):
    return ruota_90(ruota_180(soluzione))  

def main_regine(n, s):
    random_generator = random.Random()                           
    tempi_soluzioni = []     
    tentativi_soluzioni = []  
    registro_soluzioni = {}  
    
    soluzioni_trovate = 0    
    tentativi = 0            
    start_time = time.time() 
    
    while soluzioni_trovate < s:  
        lista_soluzione = list(range(n))     
        random_generator.shuffle(lista_soluzione) 
        tentativi += 1 
        
        if time.time() - start_time > 15.0:
            print(f"TIMEOUT RAGGIUNTO PER N={n}")  
            return None  
            
        if soluzione_corretta(lista_soluzione):
            scacchiera_tupla = tuple(lista_soluzione)  
            tempo_impiegato = time.time() - start_time  
            
            if scacchiera_tupla in registro_soluzioni:
                registro_soluzioni[scacchiera_tupla] += 1  
                start_time = time.time()  
                tentativi = 0             
                continue                  
                
            registro_soluzioni[scacchiera_tupla] = 1  
            tempi_soluzioni.append(tempo_impiegato)  
            tentativi_soluzioni.append(tentativi)     
            soluzioni_trovate += 1                  
            
            print(f"Sol{soluzioni_trovate}(N={n}): {lista_soluzione} in {tempo_impiegato:.5f}s con {tentativi} tentativi")
            
            start_time = time.time() 
            tentativi = 0 

    if tempi_soluzioni: 
        tempo_medio = sum(tempi_soluzioni) / len(tempi_soluzioni)  
        totale_duplicati = sum(valore - 1 for valore in registro_soluzioni.values())  
        print(f"\nSTATISTICHE FINALI (N={n})") 
        print(f"Tempo medio per soluzione unica: {tempo_medio:.5f}s")  
        print(f"Lista tentativi per soluzione: {tentativi_soluzioni}")  
        print(f"Totale duplicati scartati: {totale_duplicati}")  
        
        # LISTA 1: OCCORRENZE UNICHE (trovate esattamente 1 volta)
        print("\n--- LISTA 1: OCCORRENZE UNICHE (Trovate 1 sola volta) ---")
        uniche_trovate = False
        for sol, cont in registro_soluzioni.items():  
            if cont == 1:
                print(f" > Soluzione {sol}")
                uniche_trovate = True
        if not uniche_trovate:
            print(" > Nessuna soluzione è rimasta unica (tutte ripetute).")

    
        print("\n 2: LISTA OCCORRENZE DUPLICATE (Trovate più di 1 volta) ")
        duplicati_trovati = False
        for sol, cont in registro_soluzioni.items():  
            if cont > 1:
                print(f" > Soluzione {sol} riprodotta {cont} volte")
                duplicati_trovati = True
        if not duplicati_trovati:
            print(" > Nessun duplicato riscontrato in questa esecuzione.")
            
    return list(registro_soluzioni.keys())  

def trova_una_soluzione(n, timeout=15.0):
    start_time = time.time()
    lista_soluzione = list(range(n))
    while True:
        if time.time() - start_time > timeout:
            return False
        random.shuffle(lista_soluzione)
        if soluzione_corretta(lista_soluzione):
            return True


if __name__ == "__main__":
    # 1, 2, 3, 4) Test di funzionamento e ricerca 10 soluzioni (N=8)
    print("[PHASE 1] TEST DI FUNZIONAMENTO (N=8, TARGET=10)")  
    soluzioni_base = main_regine(8, 10) 
    
    # 5) Test di velocità e limiti (timeout 15s)
    print("\n TEST DI VELOCITÀ E LIMITI (TIMEOUT 15s)")  
    lato_n = 8  
    ultimo_lato_valido = 8  
    while True:  
        print(f"Test in corso per N = {lato_n}...", end=" ", flush=True)
        trovato = trova_una_soluzione(lato_n, timeout=15.0)
        
        if trovato:
            print("OK (< 15s)")
            ultimo_lato_valido = lato_n  
            lato_n += 1  
        else:
            print("TIMEOUT (> 15s)")
            break  
            
    print(f"\n Dimensione massima calcolata in 15s: N={ultimo_lato_valido}")  
    
    # 6, 7) Test delle rotazioni geometriche per 5 soluzioni uniche su scacchiera 8x8
    print("\n TEST DELLE ROTAZIONI (5 SOLUZIONI UNICHE 8x8) ")  
    soluzioni_simmetria = main_regine(8, 5)  
    if soluzioni_simmetria:  
        print("\nCalcolo delle 4 rotazioni per ogni soluzione:")  
        for idx, sol in enumerate(soluzioni_simmetria):                     
            print(f"\n[Soluzione Unica {idx+1}]")  
            print(f"           Originale (0°) : {sol}")  
            print(f"           Ruotata 90°    : {ruota_90(sol)}")  
            print(f"           Ruotata 180°   : {ruota_180(sol)}")  
            print(f"           Ruotata 270°   : {ruota_270(sol)}")