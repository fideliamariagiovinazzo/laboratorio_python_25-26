# File: rubrica_opzioni.py
# Author: F. M. Giovinazzo
# Date: 17/06/2026
# Version: 3.0
# Description: Programma che visualizza il dizionario, crea liste ordinate 
# e messaggi di auguri personalizzati per le chiavi del dizionario (nomi).

import sys
import argparse

# Dizionario annidato contenente i dati dei contatti della rubrica
rubrica = {
    'Paolino Paperino': {
        'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 93, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'
    },
    'Ron Weasley': {
        'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 46, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'
    },
    'Ramona Flowers': {
        'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'
    },
    'Madoka Ayukawa': {
        'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'
    }
}


def visualizza_contenuto():
    """
    Visualizza il contenuto completo della rubrica formattando ogni record 
    con le relative chiavi e valori, distinguendo tra stringhe e valori numerici.
    """
    # Utilizza il comando .items() per scorrere sia sulle chiavi principali (i nomi) che sui valori
    for nome, dati in rubrica.items():
        stringa_out = f"'{nome}', "
        
        for chiave, valore in dati.items():
            # Controlla se il tipo del valore è una stringa
            if type(valore) == str:
                stringa_out += f"'{chiave}' '{valore}', "
            else:
                stringa_out += f"'{chiave}' {valore}, "
                
        # Rimuove l'ultima virgola e lo spazio extra dalla fine della stringa e stampa a schermo
        print(stringa_out.rstrip(", "))


def costruisci_lista_età():
    """
    Costruisce e restituisce una lista di tuple contenenti l'età e il nome 
    di ogni contatto, ordinata in base all'età crescente.
    """
    lista_età = []
    for nome, dati in rubrica.items():
        # Aggiunge una tupla (età, nome) alla lista
        lista_età.append((dati['età'], nome))
    
    # Ordina la lista in base al primo elemento della tupla (l'età) in ordine crescente
    lista_età.sort()
    return lista_età
 
def stampa_nomi_ordinati():
    """
    Stampa i nomi dei contatti ordinati in base all'età (dal più giovane al più anziano).
    """
    lista_età = costruisci_lista_età()
    
    # Estrae il nome dalla tupla ordinata e lo stampa
    for età, nome in lista_età:
        print(nome)


def lista_invertita():
    """
    Costruisce la lista ordinata per età e la inverte, stampando il risultato 
    sotto forma di lista di tuple (età, nome).
    """
    lista_età = costruisci_lista_età()
    
    # Inverte l'ordine della lista (dal più anziano al più giovane)
    lista_età.reverse()
    print(lista_età)


def messaggio_auguri(nome_specifico):
    """
    Genera e stampa un messaggio di auguri personalizzato per il contatto specificato,
    adattando il genere grammaticale in base al sesso registrato.
    """
    # Verifica l'effettiva presenza del nome all'interno della rubrica
    if nome_specifico in rubrica:
        dati = rubrica[nome_specifico]
        # Determina il suffisso di genere in base al sesso ('o' per M, 'a' per F)
        suffisso = 'o' if dati['sesso'] == 'M' else 'a'
        print(f"Car{suffisso} {nome_specifico}, sei nat{suffisso} il {dati['giorno']} di {dati['mese']} del {dati['anno']} e quindi a breve compirai {dati['età']} anni. Ti manderemo gli auguri a {dati['mail']}")
    else:
        print("Nome non trovato nella rubrica!")


def estrai_valori_per_chiave(chiave_scelta):
    """
    Estrae e stampa una lista di tutti i valori associati a una specifica chiave 
    (es. 'mail', 'età') per ogni contatto presente nella rubrica.
    
    Args:
        chiave_scelta (str): La chiave del dizionario interno da estrarre.
    """
    valori = []
    
    # Raccoglie il valore corrispondente alla chiave scelta per ciascun contatto
    for nome in rubrica:
        if chiave_scelta in rubrica[nome]:
            valori.append(rubrica[nome][chiave_scelta])
            #aggiungo alla lista dei valori il valore specifico richiesto
            
    print(f"Valori per la chiave '{chiave_scelta}': {valori}")


# CONFIGURAZIONE ARGPARSE 
parser = argparse.ArgumentParser(description="Gestione Rubrica")

parser.add_argument('-v', '--visualizza', action='store_true', help="Esegue il punto 1")
parser.add_argument('-o', '--lista_ordinata', action='store_true', help="Esegue il punto 2")
parser.add_argument('-i', '--lista_invertita', action='store_true', help="Esegue il punto 3")
parser.add_argument('-n', '--nome', type=str, help="Esegue il punto 4 per il nome specificato")

# Analizza gli argomenti noti separatamente per evitare conflitti con il sys.argv del punto 5
args_parser, unknown = parser.parse_known_args()

# ESECUZIONE DEI COMANDI 
if args_parser.visualizza:
    visualizza_contenuto()
elif args_parser.lista_ordinata:
    stampa_nomi_ordinati()
elif args_parser.lista_invertita:
    lista_invertita()
elif args_parser.nome:
    messaggio_auguri(args_parser.nome)
else:
    # PUNTO 5 CON sys.argv, inserire nel terminale python3 rubrica_opzioni.py chiave
    args = sys.argv
    if len(args) > 1:
        #l'utente ha inserito una chiave dopo il nome del file
        chiave_inserita = args[1]
        #chiave = primo argomento utile digitato dall'utente.
        chavi_valide = ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']
        
        # Valida se il parametro inserito corrisponde a una chiave ammessa della rubrica
        if chiave_inserita in chavi_valide:
            estrai_valori_per_chiave(chiave_inserita)
        else:
            print("Argomento non valido o chiave non riconosciuta. Usa --help per le opzioni.")         
    else:
        print("Nessun argomento inserito. Usa --help per la guida")
        #python3 rubrica_opzioni.py --help, notazione corretta da inserire nel terminale