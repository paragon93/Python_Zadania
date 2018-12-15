import random
words = ("Volvo", "Seat", "Audi", "Renault", "Porsche", "Mercedes", "Alfa Romeo")
word = random.choice(words)
correct = word
tries = 0

print("\nProgram wylosuje marke samochodu, a Ty musisz ja odgadnac w 5 probach")
print("\nJako podpowiedz mozesz zapytac czy jakas litera znajduje sie w tym slowie")
print("\nSzukane slowo zawiera", len(word), "znakow")

litera = input("Podaj litere ")
if litera in correct:
    print("Podana litera znajduje sie w tym slowie\n")
    guess = input("Teraz podaj swoja odpowiedz: ")
    tries += 1
if litera == correct:
    print("Brawo! Zgadles, szukane slowo to: ", correct)
    print("Nie udalo sie, sprobuj jeszcze raz")
if tries > 5:
    print("Wykorzystales juz 5 prob")

elif litera not in correct:
    print:( litera, "nie ma w tym slowie, sprobuj jeszcze raz")
