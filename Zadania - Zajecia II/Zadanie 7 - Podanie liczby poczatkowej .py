
start = int(input("Podaj swoja liczbe poczatkowa: "))
finish = int(input("Podaj swoja liczbe koncowa: "))
jump = int(input("Podaj wielkosc odstepu miedzy kolejnymi liczbami: "))

for digit in range(start, finish, jump):
   print(digit, end=" ")

input("\n\nAby zakonczyc program, nacisnij klawisz Enter.")
