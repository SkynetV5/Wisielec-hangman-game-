from random import randint
def play():
    napisy = open("Files/napisy.txt")
    lista_wyrazow = []
    choice = False
    ktore_wyrazy_byly_uzyte = []
    for line in napisy:
        temp = line[:-1]
        lista_wyrazow.append(temp)
    napisy.close()
    ilosc_wyrazow = len(lista_wyrazow)
    ilosc_wybranych_slow = 0
    while choice != True or ilosc_wybranych_slow != len(ktore_wyrazy_byly_uzyte):
        los = randint(0,ilosc_wyrazow)
        flaga = False
        while flaga != True:
            for i in ktore_wyrazy_byly_uzyte:
                if i == los:
                    los = randint(0, ilosc_wyrazow)
                    break
            flaga = True
        ktore_wyrazy_byly_uzyte.append(los)
        ilosc_wybranych_slow += 1
        wyraz = lista_wyrazow[los]
        print("Wyraz został wybrany:\n")
        for i in range(0,len(wyraz)):
            print("_", end = " ")
        print("\n")
        flaga = False
        while flaga != True:
            litera = input("Wpisz daną litere z alfabetu:")
            if len(litera) == 1:
                print(litera)
                flaga = True
            else:
                print("Podałeś więcej niż jedną literę!!!")
                continue
        choice = True
