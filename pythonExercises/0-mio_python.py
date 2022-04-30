# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#from six.moves import input as raw_input
#import 0s

print("Hello world")

while True:
    menu=input("Fai la tua scelta! \n\t1) Esempio scemo \n\t2) Crea N switches \n\t3) esporta su devices.txt \n\t4) leggi da devices.txt \n\tq) esci \n> ")
    if menu=="1":
        x=int(input("inserisci un numero a caso: "))
        if x>5:
            print("blablabla")
        elif x<0:
            print("non essere così negativo")
        else:
            print("boh")
    elif menu=="2":
        N=int(input("Quanti switches vuoi creare? "))
        switches = {}
        i=1
        while i<=N:
            print("="*6 + "Switch "+str(i)+"="*6)
            #print("\t")
            switchName = input("\tInserisci il nome dello switch "+str(i)+": ")
            #switchName = raw_input("Inserisci il nome dello switch "+str(i)+": ")
            #print("Hello, {0}, how do you do?".format(raw_input("Enter name here: ")))
            #print("\t")
            switchVendor = input("\tInserisci vendor switch "+str(i)+": ")
            #switches = switches.append({switchName : switchVendor})
            switches[switchName] = switchVendor
            #print("\n")
            i=i+1
        print(switches)
    elif menu=="3":
        file = fopen("devices.txt", "r")
        if switches[0] != "":
            for item in switches:
                print(switches[item])
        file.close
    elif menu=="q":
        break
    else:
        print("Forse non hai capito come funziono?!?")