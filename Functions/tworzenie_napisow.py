def tworz_napisy():
    file = open("Files/napisy.txt", 'a')
    print("Podaj slowa. Aby zakonczyc wczytywanie wpisz STOP")
    napis = input()
    while napis != 'STOP':
        file.write(napis)
        file.write('\n')
        napis = input()
    file.close()