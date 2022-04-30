# @author Acca Emme
# github: https://github.com/AccaEmme/DTLabCiscoBootcampAcademy

# Traccia: contare tutte le (occorrenze) vocali in una parola
# svolgimento non ottimizzato, creato per uso puramente didattico per testare le varie modalità: range, in, .lower, regexp, split

import re; #importo la libreria per le regex

vocali = ['a', 'e', 'i', 'o', 'u']
numeri = range(48,58); # Il range da 0 a 10-1 non va bene perché sono cifre, ma in input ho stringhe/chr
numeri_s = [chr(x) for x in range(48,58)];
simboli = { *range(0,48), *range(58,65), *range(91,97), *range(123,128)} #da python 3.5 creo un set (elimina i duplicati) dei caratteri ASCII esclusi numeri e lettere maiuscole e minuscole
simboli.remove(32); # rimuovo lo spazio dai simboli.

frase = input("inserisci una parola o una frase: ");

contaVocali = 0; contaCaratteri = 0; contaSpazi = 0; contaSimboli = 0; contaCifre = 0; contaParole = 0; # una parola escludendo simboli e numeri, è tra uno spazio o un segno di punteggiatura : (), ; .

for carattere in frase.lower():
    if carattere in vocali:
        contaVocali+=1;
    if carattere == " ":
        contaSpazi+=1;
    if ord(carattere) in simboli: # ord() è il reciproco di chr()
        contaSimboli+=1;
    #if ord(carattere) in numeri: #funziona ma cerco una soluzione bizzarra
    #    contaCifre+=1;
    if carattere in numeri_s:
        contaCifre+=1;
    contaCaratteri+=1;
#x = "ciao,mondo".split("."); print( len(x) )
#parole = re.split('\W+', frase) # Mediante le regexp splitto eliminando any non-word character per ottenere il testo.
# La funzione split non va bene, "ciao come stai?" restituisce 4 parole. Adopero la funzione findall (find e match restituiscono solo la prima occorrenza).
parole = re.findall("[a-zA-Z]+", frase); # purtroppo \w+ include anche i digits. Imperfetto con l33t words: "Hello World 2 Everyb0dy! HELLO!!!"

print("""In \"%s\" ci sono:
      %d vocali
      %d lettere
      %d simboli
      %d cifre
      %d spazi
      %d parole: %s""" %(frase, contaVocali, contaCaratteri, contaSimboli, contaCifre, contaSpazi, len(parole), parole));