import os
def scores():
    if os.stat("Files/scores.txt").st_size == 0:
        print("Nie ma tutaj żadnych wyników. Zagraj aby coś tutaj się pojawiło")
    else:
        print("Tabela wyników:")
        print("Data - Zgadniete slowa - Niezgadniete slowa")
        file = open("Files/scores.txt")
        print(file.read())
        file.close()