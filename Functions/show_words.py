def show_words():
    file = open("Files/napisy.txt", "r")
    print("W grze występują napisy:")
    print(file.read())
    file.close()