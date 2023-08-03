from Functions.show_words import show_words
from Functions.scores import scores
from Functions.play import play
print('Witaj w grze "Wisielec".')
print("MENU:")
print("1.Graj!")
print("2.Wyswietl plik z napisami.")
print("3.Zobacz ostatnie wyniki.")
print("4.Zakończ.")
print("Wybierz opcje (1-4)")
choice = int(input())
while(choice != 4):
    if choice < 1 or choice > 4:
        print("Zła wartość!!!")
    if choice == 1:
        play()
    if choice == 2:
        show_words()
    if choice == 3:
        scores()
    print("MENU:")
    print("1.Graj!")
    print("2.Wyswietl plik z napisami.")
    print("3.Zobacz ostatnie wyniki.")
    print("4.Zakończ.")
    print("Wybierz opcje (1-4)")
    choice = int(input())
