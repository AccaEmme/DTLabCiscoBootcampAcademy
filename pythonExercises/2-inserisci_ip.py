# Acquisiamo come input da tastiera un indirizzo IPv4 in notazione dotted decimal
# a = inpunt("Dammi un indirizzo IPv4 (A.B.C.D): ")
# Assumiamo che le quattro parti dell'indirizzo siano formate esattamente da TRE cifre decimali e non ci preoccupiamo di gestire eventuali errori di digitazione
# Spezziamo l'indirizzo in quattro numeri interi:
# a0 = int(a[0:3]); a1 = int(a[4:7]); a2 = int(a[8:11]); a3=int(a[12:])
# Usando la funzione format(), produciamo come output la stringa che rappresenta l'indirizzo in binario (32 bit)

menu="";
#while menu.upper()!="ESC":
while True:
    while( len(menu)<15 ):
        menu = input("Dammi un indirizzo IPv4 (AAA.BBB.CCC.DDD) o digita ESC per uscire: ")
        if menu.upper()=="ESC": break;
        a  = menu;    a0 = int(a[0:3]);    a1 = int(a[4:7]);    a2 = int(a[8:11]);    a3 = int(a[12:]);
        binary = "{0:08b}".format(a0) + "." + "{0:08b}".format(a1) + "." + "{0:08b}".format(a2) + "." + "{0:08b}".format(a3);
        integerNotation = a0*(2**24) + a1*(2**16) + a2*(2**8) + a3*(2**0);
        print("l'indirizzo inserito: %s.%s.%s.%s è convertibile in binario come %s ed equivale al valore intero %d" %(a0, a1, a2, a3, binary, integerNotation))
    if menu.upper()=="ESC": break;
print("Uno è lieto di servire. Arrivederci.");