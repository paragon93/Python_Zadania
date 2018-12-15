print("Napisz komunikat")
komunikat = input()
dlugosc = len(komunikat)

for i in range(dlugosc, 0, -1):
    print("Twoj komunikat w odwrotnej kolejności to: " + komunikat[::-1])
