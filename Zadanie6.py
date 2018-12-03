dystans=int(input ("Podaj ilość przejechanych kilometrów:\n"))
while (dystans<0):
    dystans=int(input ("Podaj ilość przejechanych kilometrów:\n"))

paliwo=int(input ("Podaj ilość zatankowanych litrów paliwa:\n"))
while(paliwo<0):
    paliwo=int(input ("Podaj ilość zatankowanych litrów paliwa:\n"))

spalanie=float(100*paliwo)/dystans

print("Średnie spalanie samochodu wynosi: ", spalanie)

#w tym zadaniu wykorzystałem pętle while, po podaniu liczy ujemnej program będzie prosił nas o powtórne podanie liczbt ( dodatniej )
