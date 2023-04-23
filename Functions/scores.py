import os
def scores():
    if os.stat("Files/scores.txt").st_size == 0:
        print("Nie tutaj żadnych wyników. Zagraj aby coś tutaj się pojawiło")
    else:
        print("Tabela wyników:")
        file = open("scores.txt")
        print(file.read())
        file.close()