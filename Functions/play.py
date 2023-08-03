from random import randint
from datetime import date
def play():
    napisy = open("Files/napisy.txt")
    lista_wyrazow = []
    ilosc_odgadnietych_slow = 0
    ilosc_nieodgadnietych_slow = 0
    choice = False
    for line in napisy:
        temp = line[:-1]
        lista_wyrazow.append(temp)
    napisy.close()
    ilosc_wyrazow = len(lista_wyrazow)
    ilosc_wybranych_slow = 0
    while choice != True and ilosc_wybranych_slow != ilosc_wyrazow:
        los = randint(0,len(lista_wyrazow))
        ilosc_wybranych_slow += 1
        wyraz = lista_wyrazow[los]
        lista_wyrazow.pop(los)
        print("Wyraz został wybrany:\n")
        for i in range(0,len(wyraz)):
            print("_", end = "")
        print("\n")

        flaga = False
        ilosc_prob = 11
        litera = ''
        wyraz_do_odgadniecia = ''
        for i in range(0,len(wyraz)):
            if wyraz[i] == ' ':
                wyraz_do_odgadniecia += ' '
            else:
                wyraz_do_odgadniecia += '_'
        lista_liter_uzytych = set()
        while flaga != True and ilosc_prob != 0:
            litera = input("Wpisz daną litere z alfabetu:")
            if len(litera) == 1:
                flaga = True
            else:
                print("Podałeś więcej niż jedną literę!!!")
                continue
            swap = False
            if litera not in lista_liter_uzytych:
                for i in range(0,len(wyraz)):
                    if wyraz[i] == litera:
                        char_list = list(wyraz_do_odgadniecia)
                        char_list[i] = litera
                        wyraz_do_odgadniecia = "".join(char_list)
                        swap = True
                if swap == False:
                    ilosc_prob -= 1
                lista_liter_uzytych.add(litera)
            else:
                print("Ta litera już była!!!")
                ilosc_prob -= 1
            print(wyraz_do_odgadniecia)
            print("Ilość prób: ",ilosc_prob)
            print("Użyte litery: ")
            for litery in lista_liter_uzytych:
                print(litery, end = " ")
            print()
            flaga = False
            if wyraz == wyraz_do_odgadniecia:
                ilosc_odgadnietych_slow += 1
                print("Brawo zgadłeś wyraz :D ")
                continue_game = int(input("Czy chcesz grać dalej? 1. TAK, 2. NIE"))
                print()
                flaga = True
                if continue_game == 1:
                    choice = False
                elif continue_game == 2:
                    choice = True
                else:
                    print("Podałeś złą instrukcje")
                    continue_game = input("Czy chcesz grać dalej? 1. TAK, 2. NIE")
                    print()
            elif ilosc_prob == 0:
                ilosc_nieodgadnietych_slow += 1
                print()
                print("Koniec prób!")
                print("Wyrazem był: ",wyraz)
                continue_game = int(input("Czy chcesz grać dalej? 1. TAK, 2. NIE"))
                print()
                flaga = True
                if continue_game == 1:
                    choice = False
                elif continue_game == 2:
                    choice = True
                else:
                    print("Podałeś złą instrukcje")
                    continue_game = input("Czy chcesz grać dalej? 1. TAK, 2. NIE")
                    print()

    wyniki = open("Files/scores.txt", 'a')
    wyniki.write(str(date.today()))
    wyniki.write(" ")
    wyniki.write(str(ilosc_odgadnietych_slow))
    wyniki.write(" ")
    wyniki.write(str(ilosc_nieodgadnietych_slow))
    wyniki.write("\n")
    wyniki.close()