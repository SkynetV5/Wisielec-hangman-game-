from Functions.show_words import show_words
print('Witaj w grze "Wisielec".')
print("MENU:")
print("1.Graj!")
print("2.Wyswietl plik z napisami.")
print("3.Zobacz ostatnie wyniki.")
print("4.Zakończ.")
print("Wybierz opcje (1-4)")
choice = int(input())
if choice < 1 or choice > 4:
    while choice < 1 or choice > 4:
        print("Wybierz odpowiednią liczbe z menu!")
        choice = int(input())
while(choice != 4):
    if choice == 2:
        show_words();
        print("MENU:")
        print("1.Graj!")
        print("2.Wyswietl plik z napisami.")
        print("3.Zobacz ostatnie wyniki.")
        print("4.Zakończ.")
        print("Wybierz opcje (1-4)")
    choice = int(input())